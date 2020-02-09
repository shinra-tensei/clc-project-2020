from locust import HttpLocust, TaskSet, task, between

def healthcheck(l):
    l.client.get("/calculate")

class UserTasks(TaskSet):
    tasks = [healthcheck]
    
class WebsiteUser(HttpLocust):
    host = "http://34.77.45.217:8080"
    wait_time = between(2, 5)
    task_set = UserTasks