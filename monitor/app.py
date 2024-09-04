# monitor.py
from flask import Flask, jsonify
from celery import Celery

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')
celery.conf.task_routes = (
    [
        ('monitor', {'queue': 'monitor'}),
        ('platform', {'queue': 'platform'}),
    ],
)

@app.route("/monitor", methods=["GET"])
def monitor():
    platform.apply_async()
    return jsonify({"status": "Task initiated"})

@celery.task(name="monitor", queue="monitor")
def monitor():
    print("hola")

@celery.task(name="platform", queue="platform")
def platform():
    pass


if __name__ == '__main__':
    app.run(port=5000)
