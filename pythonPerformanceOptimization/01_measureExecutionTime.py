import time


def long_time():
    total = 0
    for i in range(1, 10000):
        for j in range(1, 10000):
            total += i
            total += j


start_time = time.time()
long_time()
ent_time = time.time()
print(ent_time - start_time)
