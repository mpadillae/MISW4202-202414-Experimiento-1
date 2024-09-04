python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
instalar redis-server: https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-mac-os/

para ejecutar:

1. redis
. venv/bin/activate
redis-server

2. monitor
. venv/bin/activate
cd monitor
flask run --port=5000

3. celery del monitor
. venv/bin/activate
cd monitor
celery -A app.celery worker --loglevel=info -Q monitor

4. celery de la plataforma de mensajes
. venv/bin/activate
cd plataforma_de_mensajes
celery -A app.celery worker --loglevel=info -Q platform

5. celery del receptor de call center.
. venv/bin/activate
cd receptor_de_callcenter
celery -A app.celery worker --loglevel=info -Q callcenter


para probar:
http://172.0.0.1:5000/monitor