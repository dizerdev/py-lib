from time import perf_counter


def cronometro(f):
    def envelope(args, **kwargs):
        t1 = perf_counter()
        # Desenpacota na f, os parametros
        r = f(*args, **kwargs)
        t2 = perf_counter()
        print(f'{f.__name__} executada em {t2-t1:.4e} segundos')
        return r
    return envelope
