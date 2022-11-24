import random
from collections import deque

messages = deque()
count = 0
while True:
    ran = random.randint(0, 100)
    messages.append(ran)

    if messages[0] != 67:
        print(messages)
        count +=1
        messages.pop()
    else:
        print(count)
        break