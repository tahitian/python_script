from locust import HttpLocust,TaskSet,task  
import json
# from apscheduler.schedulers.background import BackgroundScheduler
import time
# import sys
# if not (sys.path[0] + "/../../modules") in sys.path:
#     sys.path.append(sys.path[0] + "/../../modules")
# import logger

# log = logger.logger(name='baidu', log_dir='/var/log/ati').log

# count = 0

class test_scheduler(TaskSet):  
    # task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户执行概率越高，不设置默认是1，  
    @task()  
    def test_scheduler(self):
        global count
        response = self.client.get("",timeout=30)
        # count += 1
  
# 这个类类似设置性能测试，继承HttpLocust  
class websitUser(HttpLocust):  
    # 指向一个上面定义的用户行为类  
    task_set = test_scheduler
    #执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time  
    min_wait = 0
    max_wait = 0  

# def do_print():
#     log.info(count)
#     count = 0

# scheduler = BackgroundScheduler()
# scheduler.add_job(do_print, 'cron', second='0-59')
# scheduler.start()