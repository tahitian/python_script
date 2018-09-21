#!/usr/bin/python
import subprocess
import json
import fcntl
import os
import select

def call_ext_sync(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    errcode = process.returncode
    if errcode != 0:
        return False, err.strip()
    else:
        return True, out.strip()

def call_ext_async(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def get_public_ip():
    # called after connected to pptp
    ok, output = call_ext_sync('ip route add 176.58.123.25 dev ppp0')
    if not ok:
        # console.log.error('fail to set route for 176.58.123.25')
        print 'fail to set route for 176.58.123.25'
        # print output
        return
    ok, output = call_ext_sync('curl ident.me')
    if not ok:
        # console.log.error('fail to get public ip')
        print 'fail to get public ip'
    else:
        return output

def get_ips(num):
    ips = {}
    while num>0:
        num -= 1
        ok = start()
        if not ok:
            print 'fail to pon'
            break
        print 'success to pon'
        ip = get_public_ip()
        print 'success to get ip %s' % ip
        if not ip:
            break
        if ips.get(ip):
            print 'duplicate ip %s' % ip
        else:
            ips[ip] = 1
            print 'add ip %s' % ip
        # ok, output = call_ext_sync('poff p1')
        ok = stop()
        print 'success to poff'
        if not ok:
            print 'fail to poff'
            break
    return ips

def start():
    command = "pon p1 nodetach"
    process = call_ext_async(command)
    stdout_fd = process.stdout.fileno()
    fl = fcntl.fcntl(stdout_fd, fcntl.F_GETFL)
    fcntl.fcntl(stdout_fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    epoll = select.epoll()
    epoll.register(stdout_fd, select.EPOLLIN)
    timeout = 1
    retry = 0
    done = False
    ok = False
    while not done:
        events = epoll.poll(timeout)
        if not events:
            retry += 1
            if retry > 10:
                done = True
            continue
        for fd, event in events:
            if fd != stdout_fd:
                # console.log.warning("this should not happen")
                done = True
                continue
            if event == select.EPOLLHUP:
                done = True
                break
            elif event == select.EPOLLIN:
                line = process.stdout.readline()
                if not line:
                    # console.log.warning("nothing read")
                    continue
                line = line.strip()
                # console.log.debug(line)
                if line.find("MS-CHAP authentication failed") > -1:
                    done = True
                elif line.find("authentication failed") > -1:
                    done = True
                elif line.find("HOST NOT FOUND") > -1:
                    done = True
                elif line.find("Call manager exited with error") > -1:
                    done = True
                elif line.find("Modem hangup") > -1:
                    done = True
                elif line.find("Connection refused") > -1:
                    done = True
                elif line.find("CHAP authentication succeeded") > -1:
                    pass
                elif line.find("local  IP address ") > -1:
                    pass
                elif line.find("remote IP address ") > -1:
                    ok = True
                    done = True
    if not ok:
        stop()
    return ok

def stop():
    ok, output = call_ext_sync('poff -a p1')
    return ok

# with open('./ips.json', 'w') as f:
#     ips = get_ips(10)
#     json.dump(ips, f)
print get_public_ip()
