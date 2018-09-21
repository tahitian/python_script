import json
import os
import re

path = os.path.dirname(os.path.abspath(__file__))
with open('%s/qz_data.json' % path, encoding='utf-8') as f:
    data = json.load(f)

server_list = []
server_lines = []
for server in data:
    s = {}
    s['server'] = server['servers']
    s['description'] = server['pname'] + server['sname'] + server['servername']
    s['mppe'] = 0
    if re.match('^.+188.link$', s['server']):
        s['mppe'] = 1
    avgdk = server['avgdk']
    if not avgdk:
        s['rate'] = 0
        s['enabled'] = 0
    else:
        s['rate'] = int(re.search('(\d+)(兆|$|-)', avgdk).group(1))
        s['enabled'] = 0 if int(server['isre']) else 1
    server_list.append(s)
    line_data = '{"server": "%s", "description": "%s", "mppe": %d, "rate": %d, "enabled": %d}\n' % (s['server'], s['description'], s['mppe'], s['rate'], s['enabled'])
    server_lines.append(line_data)

with open('%s/qz_servers.txt' % path, 'w', encoding='utf-8') as f:
    f.writelines(server_lines)

with open('%s/qz_servers.json' % path, 'w', encoding='utf-8') as f:
    json.dump(server_list, f, indent=4, ensure_ascii=False)