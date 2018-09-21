import fileinput
import os
import re

path = os.path.dirname(os.path.abspath(__file__))
f = path + '/accounts.txt'

i = 1
password = 'tahitian'
for line in fileinput.input(f, inplace=1):
        name = 'tahitian' + '%02d'%i
        i += 1
        line = re.sub('"username": ".{4}"', '"username": "%s"'%name, line)
        line = re.sub('"password": ".{4}"', '"password": "%s"'%password, line)
        print(line, end='')