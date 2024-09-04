# Experimento de disponibilidad
Este repositorio contiene la solución al experimento de disponibilidad del curso de Arquitecturas ágiles de software. El proyecto fue realizado utilizando [Python](https://www.python.org/downloads/) versión 3.12.4.


## Prerrequisitos

Para levantar este proyecto necesitarás:

* [Python](https://www.python.org/downloads/) (con virtualenv)
* [redis-server](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
* Copia local de este repositorio.

## Estructura

```
📦 Experimento
├─ monitor
│  └─ app.py
├─ plataforma_de_mensajes
│  └─ app.py
├─ receptor_de_callcenter
│  └─ app.py
└─ requirements.txt
```
Donde:
| Componente / archivo    | Descripción |
| -------- | ------- |
| monitor  | Microservicio encargado de consultar el estado del componente receptor a través de la `plataforma de mensajes`.    |
| plataforma_de_mensajes    | Microservicio encargado de gestionar los mensajes de solicitud y respuesta desde los microservicios `monitor` y `receptor de callcenter`.     |
| receptor_de_callcenter    | Microservicio que ejecutaría la lógica de negocio necesaria y que informa de su estado actual. Configurado para simular una disponibilidad del `90%`    |
| requirements.txt    | Archivo donde se detallan las dependencias necesarias para el proyecto.    |

## Instalación

En la raiz del proyecto ejecutar los siguientes comandos:
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
**Nota:** El comando `. venv/bin/activate` funciona para sistemas UNIX (Linux/MacOS). Si se encuentra en Windows deberá ejecutar su equivalente. Esto aplica también para los pasos siguientes.

## Ejecución

1. Abrir una terminal y ejecutar `redis-server` con el siguiente comando:

    ```
    redis-server
    ```

2. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para levantar el `monitor (api)`:

    ```
    . venv/bin/activate
    cd monitor
    flask run --port=5000
    ```

3. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para levantar el `monitor (celery)`:

    ```
    . venv/bin/activate
    cd monitor
    celery -A app.celery worker --loglevel=info -Q monitor
    ```

4. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para levantar la `plataforma de mensajes`:

    ```
    . venv/bin/activate
    cd plataforma_de_mensajes
    celery -A app.celery worker --loglevel=info -Q platform
    ```

5. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para levantar la `receptor de callcenter`:

    ```
    . venv/bin/activate
    cd receptor_de_callcenter
    celery -A app.celery worker --loglevel=info -Q callcenter
    ```

## Pruebas

Abrir un navegador o un cliente HTTP para ejecutar la siguiente petición GET:

```
http://172.0.0.1:5000/status
```
**Nota:** La respuesta asíncrona que contiene el estado del receptor de callcenter podrá verse en la consola del monitor (celery).


## Capturas
wip.

## License

Copyright © MISW4202 - Arquitecturas ágiles de software - 2024.


