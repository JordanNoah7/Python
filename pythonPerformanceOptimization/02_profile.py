import profile  # se usa profile en vez de cProfile porque no esta disponible


def f():
    for i in range(0, 10000):
        for j in range(0, 10000):
            z = i * j


profile.run('f()')
