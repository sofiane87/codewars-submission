import numpy as np


def derivative(p):
    _range = np.arange(p.shape[0] - 1, 0, -1)
    return (p[:-1] * _range)


def divide(p, q):
    _prod, remaining = [], p
    while remaining.shape[0] >= q.shape[0]:
        deg = (remaining.shape[0] - q.shape[0])
        ratio = remaining[0] // q[0]
        _update = False
        if deg != 0:
            _prod.append(ratio)
            diff = ratio * np.insert(q, q.shape[0], [0] * deg)
            _update = True
        elif np.abs(remaining[0]) >= np.abs(q[0]):
            _prod.append(ratio)
            diff = ratio * np.insert(q, q.shape[0], [0] * deg)
            _update = True

        if _update:
            remaining -= diff
            remaining = remaining[1:]

    return _prod, remaining


def solve(p):
    b = np.array(p)
    d = derivative(p)

    
