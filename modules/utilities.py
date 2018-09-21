import pymysql
import os
import json
import time
import uuid
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac

def format_time(time_stamp):
    time_array = time.localtime(time_stamp)
    format_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return format_time

def do_sql(*, sql, database='ati', lock=False, table='',
            host='182.254.211.226', 
            port=3306, 
            user='root', 
            password='Zaq1xsw2110'):
    result = None
    connection = pymysql.connect(host=host,
                                port=port,
                                user=user,
                                password=password,
                                database=database,
                                charset='utf8')

    try:
        with connection.cursor() as cursor:
            if lock:
                cursor.execute('SET AUTOCOMMIT=0')
                cursor.execute('LOCK tables %s write' % table)
            try:
                if type(sql) == list:
                    for s in sql:
                        cursor.execute(s)
                else:
                    cursor.execute(sql)
                result = cursor.fetchall()
                connection.commit()
            except Exception as e:
                connection.rollback()
                raise
            finally:
                if lock:
                    cursor.execute('UNLOCK tables')
    except Exception as e:
        raise
    finally:
        connection.close()

    return result

def send_email(config, content):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = config['from_addr']
    password = config['password']
    to_addr = config['to_addr']
    smtp_server = config['smtp_server']

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr('%s <%s>' % (config['from_name'], from_addr))
    msg['To'] = _format_addr(to_addr)
    msg['Subject'] = Header(config['subject'], 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, config['smtp_port'])
    # server.ehlo()
    # server = smtplib.SMTP(smtp_server, config['smtp_port'])
    # server.set_debuglevel(1)
    # server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()