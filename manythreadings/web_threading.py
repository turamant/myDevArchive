import time
import requests
import threading


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)

"""
Этот пример многопоточности, конкуретное выполнение операций ввода-вывода с помощью потоков

ПАРАЛЛЕЛЬНОСТИ В ПАЙТОН НЕТ- только конкурентность!!!
"""

thread1 = threading.Thread(target=read_example)
thread2 = threading.Thread(target=read_example)
thread3 = threading.Thread(target=read_example)
thread4 = threading.Thread(target=read_example)
thread5 = threading.Thread(target=read_example)
thread6 = threading.Thread(target=read_example)

start_time = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
print("Выполняем два потока")
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
end_time = time.time()


print(f'Синхронное выполнение заняло: {end_time - start_time:.4f} с.')