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
|  <img width="537" alt="Captura de pantalla 2024-09-04 a la(s) 12 13 37" src="https://github.com/user-attachments/assets/9ccd871b-b26e-458a-8e42-bae029db4cf4"> | 
|---| 
| Se realiza la solicitud para consultar el estado del receptor de CallCenter desde el API del Monitor. |

| <img width="1391" alt="Captura de pantalla 2024-09-04 a la(s) 12 14 08" src="https://github.com/user-attachments/assets/dc851a67-4bcc-45a1-b06f-24fc3c513002"> | 
|---| 
| La plataforma de mensajes recibe el mensaje y lo envia al receptor de CallCenter. |

| <img width="1388" alt="Captura de pantalla 2024-09-04 a la(s) 12 15 09" src="https://github.com/user-attachments/assets/d35a9139-c1f2-490a-9bb5-e3b11fd084d8"> | 
|---| 
| El receptor de CallCenter recibe el mensaje de la plataforma de mensajes y le responde con su estado actual: disponible/no disponible. |

| <img width="1379" alt="Captura de pantalla 2024-09-04 a la(s) 12 15 25" src="https://github.com/user-attachments/assets/0972a432-4839-4139-b065-ffa28ab62ae2"> | 
|---| 
| La plataforma de mensajes recibe la respuesta del receptor de CallCenter y la envia al Monitor.|

| <img width="1381" alt="Captura de pantalla 2024-09-04 a la(s) 12 15 38" src="https://github.com/user-attachments/assets/571efd44-6d7d-48e9-8125-818295d3f54f"> | 
|---| 
| El Monitor recibe la respuesta de la plataforma de mensajes sobre el estado del receptor de CallCenter. |

## License

Copyright © MISW4202 - Arquitecturas ágiles de software - 2024.


