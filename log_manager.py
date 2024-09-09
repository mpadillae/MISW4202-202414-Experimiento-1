from flask import Flask
from celery import Celery

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')


@celery.task(name="write_log", queue="logs")
def write_log(component, message, date):
    with open('logs.txt', 'a+') as f:
        f.write(f"[{date}] - {component} - {message}\n")

    status = message.split("-")[-1].strip()
    if status == "Disponible :)" or status == "No disponible :(":
        with open('call_center_status.txt', 'a+') as f:
            f.write(f"{status}\n")





if __name__ == '__main__':
    app.run(port=5000)
