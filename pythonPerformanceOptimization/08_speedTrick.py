import time
start = time.time()
import ctypes
fun = ctypes.CDLL("./libtest.so")  # compilamos el archivo C con gcc -fPIC -shared -o libtest.so function.c
fun.f()
end = time.time()
print(end - start)
