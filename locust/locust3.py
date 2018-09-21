from locust import HttpLocust,TaskSet,task  
import json
  
# 定义用户行为，继承TaskSet类，用于描述用户行为  
# (这个类下面放各种请求，请求是基于requests的，每个方法请求和requests差不多，请求参数、方法、响应对象和requests一样的使用，url这里写的是路径)  
# client.get===>requests.get  
# client.post===>requests.post  
class test_scheduler(TaskSet):  
    # task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户执行概率越高，不设置默认是1，  
    @task()  
    def test_scheduler(self):  
        data = {
            'client_id': 'tahitian',
            'unit_id': "wukong_8ZZpS5Zc885XPbel0422"
        }
        response = self.client.post('/track', data=data).json()
        if response['status'] != 0:
            print(response['msg'])
            # time.sleep(1)
            return
  
# 这个类类似设置性能测试，继承HttpLocust  
class websitUser(HttpLocust):  
    # 指向一个上面定义的用户行为类  
    task_set = test_scheduler
    #执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time  
    min_wait = 0
    max_wait = 0  