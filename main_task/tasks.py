from celery import Celery
from myutil_route import MainAPIRouteArray


BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL='redis://localhost'
app = Celery('tasks', backend=BACKEND_URL, broker=BROKER_URL)

@app.task
def add(x, y):
    return x + y

@app.task
def checkMainRoute():
    return len(MainAPIRouteArray)