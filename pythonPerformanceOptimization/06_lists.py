import time

start_time = time.time()
# test 1
cube_numbers = []
for n in range(0, 10):
    if n % 2 == 1:
        cube_numbers.append(n ** 3)
        d_time = time.time()

# test 2
cube_numbers = [n ** 3 for n in range(1, 10) if n % 2 == 1]

end_time = time.time()
print(end_time - start_time)
