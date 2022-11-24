import threading
import time


def worker(num):
    time.sleep(5)
    print(f'{num} - done ')


threads = []
for i in range(7):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()