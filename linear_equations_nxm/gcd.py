import numpy as np


def astrip(p):
    idx = 0
    while p[idx] == 0:
        idx += 1
        if idx == p.shape[0]:
            break
    if idx == 0:
        return p
    else:
        return p[idx:]


def gcd(p, q, _strip=True):
    p, q = np.array(p), np.array(q)
    if _strip:
        p, q = astrip(p), astrip(q)
    if p.shape[0] < q.shape[0]:
        p = np.insert(p, 0, np.zeros(q.shape[0] - p.shape[0]))
    else:
        q = np.insert(q, 0, np.zeros(p.shape[0] - q.shape[0]))

    high, low = max(p, q, key=lambda x: tuple(np.abs(x))), min(p, q, key=lambda x: tuple(np.abs(x)))
    if (low == 0).all():
        max_gcd = high[0]
        for c in high[1:]:
            max_gcd = np.gcd(max_gcd, c)
        return (high / max_gcd).astype(int)

    max_low = max(np.arange(low.shape[0]), key=lambda x: (low[x] != 0, -x))

    # Update Low Value
    new_low = low[max_low:]
    new_low = np.insert(new_low, new_low.shape[0], [0] * max_low)
    new_high = high * new_low[0]
    new_low *= high[0]
    diff = new_high - new_low
    return gcd(low, diff)
