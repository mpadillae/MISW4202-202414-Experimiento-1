from requests import post, get
from colored import fg, bg, attr
import threading
import time

url = "http://127.0.0.1:5000/status"
total_requests = 0
errors = 0


def do_monitor_request(requests):
    global total_requests, errors
    for _ in range(requests):
        ini = time.time()
        try:
            status_code = get(url).status_code
        except Exception as e:
            status_code = 500
        fin = time.time()
        total_time = round(fin - ini, 3)
        total_requests += 1
        response = f"Petición {total_requests}: {status_code}, {total_time}"
        if status_code != 200:
            errors += 1
            print(fg(196) + str(response))
        else:
            print(fg(46) + str(response))
        time.sleep(1)


if __name__ == '__main__':
    threads_count = 100
    thread_requests = 10
    threads = []
    for i in range(threads_count):
        thread = threading.Thread(target=lambda: do_monitor_request(thread_requests))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print(fg(27) + f"\nEl número de hilos fue: {threads_count}")
    print(f"El número de peticiones por hilo fue de: {thread_requests}")
    print(f"Número de peticiones totales: {threads_count * thread_requests}")
    print(f"Número de peticiones con éxito: {threads_count * thread_requests - errors}")
    print(f"Número de peticiones fallidas: {errors}")
    availability = round((1 - errors / (threads_count * thread_requests)) * 100, 2)
    print(f"Porcentaje de disponibilidad: {availability}%")
    expected_availability = 99
    if availability < expected_availability:
        print(fg(196) + "El sistema no cumple con la disponibilidad esperada")
    else:
        print(fg(46) + "El sistema cumple con la disponibilidad esperada")