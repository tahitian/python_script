import json
import sys
import os
from openpyxl import Workbook
from openpyxl import load_workbook

path = os.path.dirname(os.path.abspath(__file__))
dir_name = 'ipduoduo'
file_name = 'ipduoduo_servers'
file_path = "%s/%s/%s.txt" % (path, dir_name, file_name)

def load_server_info():
    info = {}
    try:
        fd = open(file_path, encoding='utf-8')
        if fd:
            lines = fd.readlines()
        fd.close()
    except Exception as e:
        print("load_server_info: %r" % e)
    for line in lines:
        try:
            data = json.loads(line)
            name = data["server"]
            rate = data["rate"]
            enabled = data['enabled']
            info[name] = {"rate": rate, "enabled": enabled}
        except Exception as e:
            print("load_server_info: %r" % e)
    return info

def dump_to_xlsx(info):
    wb = Workbook()
    sheet = wb.active
    sheet['A1'] = 'server'
    sheet['B1'] = 'enabled'
    sheet['C1'] = 'rate'
    sheet['D1'] = 'ok'
    sheet['E1'] = 'error'
    sheet['F1'] = 'ok_rate'
    sheet['G1'] = 'average'
    row = 2
    for name in info:
        sheet['A%d'%row] = name
        sheet['B%d'%row] = info[name]['enabled']
        sheet['C%d'%row] = info[name]['rate']
        row += 1
    wb.save("%s/%s/%s.xlsx" % (path, dir_name, file_name))

if __name__ == '__main__':
    info = load_server_info()
    dump_to_xlsx(info)