"""
Source code is from: https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
"""

import time

def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', method.__name__.upper())
            kwargs['log_time'][name] = int((te - ts) * 1000)
            print('execute function: %r %2.2f s' % (method.__name__, (te - ts)))
        else:
            print('execute function: %r %2f s' % (method.__name__, (te - ts)))
        return result
    return timed