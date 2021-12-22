from locust import HttpUser, task, between

class User(HttpUser):

    host = 'https://reqres.in/api'
    time = between(1, 5)

    @task(3)
    def GetAll(self):
        self.client.get("/users")

    @task(3)
    def Get(self):
        self.client.get("/users/1")

    @task(1)
    def Create(self):
        self.client.post("/users", json={
            "name": "tom",
            "job": "junior"
        })

    @task(1)
    def Update(self):
        self.client.patch("/users", json={
            "name": "tom",
            "job": "ceo"
        })

    @task(1)
    def Delete(self):
        self.client.delete("/users/10")