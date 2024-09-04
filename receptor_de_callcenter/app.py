# receptor_de_callcenter.py
from flask import Flask, jsonify
from celery import Celery

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')
celery.conf.task_routes = (
    [
        ('callcenter', {'queue': 'callcenter'}),
        ('monitor', {'queue': 'monitor'}),
    ],
)

@celery.task(name="callcenter", queue="callcenter")
def callcenter():
    print("recibido por callcenter")
    monitor.apply_async()

@celery.task(name="monitor", queue="monitor")
def monitor():
    pass


if __name__ == '__main__':
    app.run(port=5002)
