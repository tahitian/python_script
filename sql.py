import sys
if not (sys.path[0] + "/modules") in sys.path:
    sys.path.append(sys.path[0] + "/modules")
import utilities
import threading
import json

do_sql = utilities.do_sql
# CONSTANT = utilities.get_constant()

database='ati'

# ali
# host='47.98.149.66'
# host = '172.16.47.208'

# tencent
# host='115.159.222.87'

# tahitian
host='182.254.211.226'

port=3306
user='root'
password='Zaq1xsw2110'

# sql = ("CREATE TABLE IF NOT EXISTS `tbl_task`("
#    "`name` VARCHAR(128) NOT NULL,"
#    "`task_type` INT UNSIGNED DEFAULT 0 NOT NULL,"
#    "`charge_type` INT UNSIGNED DEFAULT 0 NOT NULL,"
#    "`price` FLOAT DEFAULT 0 NOT NULL,"
#    "PRIMARY KEY (`name`)"
# ")ENGINE=InnoDB DEFAULT CHARSET=utf8;")
districts = json.dumps({
    'type': 0,
    'percentage_assigned': 1,
    'list': [{
        'district': '0101',
        'percentage': 0.4
    },{
        'district': '0102',
        'percentage': 0.6
    }]
})
sql1 = 'ALTER TABLE tbl_task add districts_region TINYINT DEFAULT 0 NOT NULL'
sql2 = 'ALTER TABLE tbl_task add districts TEXT NOT NULL'
# sql = 'SELECT * FROM tbl_task'
sql = "UPDATE tbl_task SET districts='%s'" % districts
sql = "UPDATE tbl_injections_IMPCLK SET imp=240, clk=60"

sqls = []
for i in range(15, 23):
    sql = 'INSERT INTO tbl_injections_IMPCLK VALUE("tahitian.pc", "20180920", %d, 240, 60)' % i
    sqls.append(sql)
for sql in sqls:
    do_sql(sql=sql, database=database, host=host)

# datas = do_sql(sql=sql, database=database, host=host)
# for data in datas:
#     print(data)