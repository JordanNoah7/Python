# Test 1
import time
"""
start_time = time.time()
movies = ["Superman", "Spiderman", "Hulk", "Xmen", "Batman"]
m = []
for i in range(0, len(movies)):
    m.append(movies[i].upper())
print(m)
end_time = time.time()
print(end_time - start_time)
"""

# Test 2
start_time = time.time()
movies = ["Superman", "Spiderman", "Hulk", "Xmen", "Batman"]
m = map(str.upper, movies)
print(m)
end_time = time.time()
print(end_time - start_time)

# Más built-in functions en https://docs.python.org/3/library/functions.html
