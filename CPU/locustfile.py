from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def calculate_fatorial(self):
        self.client.get("/data")