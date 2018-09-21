from locust import HttpLocust,TaskSet,task  
import json
import time
  
class test_scheduler(TaskSet):  
    # task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户执行概率越高，不设置默认是1，  
    @task()  
    def test_scheduler(self):   
        payload = {
            'task_type': 1,
            'client_id': 'tahitian'
        }
        response = self.client.get("/get_task/bidding",timeout=30,params=payload)
        response = json.loads(response.content)
        if response['status'] != 0:
            print(response['msg'])
            time.sleep(1)
            return
        if response['size'] == 0:
            print('no task right now')
            time.sleep(1)
            return
        task = response['task']
        unit_id = task['unit_id']
        data = {
            'client_id': 'tahitian',
            'unit_id': unit_id
        }
        response = self.client.post('/track', data=data).json()
        if response['status'] != 0:
            print(response['msg'])
            time.sleep(1)
            return
  
# 这个类类似设置性能测试，继承HttpLocust  
class websitUser(HttpLocust):  
    # 指向一个上面定义的用户行为类  
    task_set = test_scheduler
    #执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time  
    min_wait = 0
    max_wait = 0  