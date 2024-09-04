# monitor.py
from flask import Flask, jsonify
from celery import Celery

app = Flask(__name__)
celery = Celery(__name__, broker='redis://localhost:6379/0')


@app.route("/status", methods=["GET"])
def get_status():
    platform_request.apply_async()
    return jsonify({"status": "Solicitud de consulta de estado encolada exitosamente."})

@celery.task(name="monitor_callback", queue="monitor")
def monitor_callback(response):
    print("[Monitor] Respuesta recibida desde la plataforma de mensajes.")
    print(f"[Monitor] Status: {response}")

@celery.task(name="platform_request", queue="platform")
def platform_request():
    pass


if __name__ == '__main__':
    app.run(port=5000)
