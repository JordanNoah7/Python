import time

# test 1
start_time = time.time()
x = "hello world this is an example text."
print(len(x))
ent_time = time.time()
print(ent_time - start_time)

# test 2
start_time = time.time()
x = "hello world this is an example text."
i = 0
while x[i] != '.':
    i = i + 1
print(i)
ent_time = time.time()
print(ent_time - start_time)
