import json
import sys
import time
if not (sys.path[0]+'/modules/dysms_python') in sys.path:
    sys.path.append(sys.path[0]+'/modules/dysms_python')
from demo_sms_send import send_sms

if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    params = {
        'time': time,
        'seconds': 55
    }
    params = json.dumps(params)
    print(send_sms("13052316968", sign_name='ATIsys', template_code='SMS_143712599', template_param=params))
   
    
    

