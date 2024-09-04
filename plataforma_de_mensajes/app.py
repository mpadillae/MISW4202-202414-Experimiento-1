# plataforma_de_mensajes.py
from flask import Flask, jsonify
from celery import Celery

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')
celery.conf.task_routes = (
    [
        ('platform', {'queue': 'platform'}),
        ('callcenter', {'queue': 'callcenter'}),
    ],
)

@celery.task(name="platform", queue="platform")
def platform():
    print("recibido por plataforma")
    callcenter.apply_async()

@celery.task(name="callcenter", queue="callcenter")
def callcenter():
    pass

if __name__ == '__main__':
    app.run(port=5001)
