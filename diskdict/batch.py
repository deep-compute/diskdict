from multiprocessing import Pool

SIZE = 5000
JOBS = 1000

def _chunkify(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]

def _get(pindices):
    words = [xd.get(i, xdefault) for i in pindices]
    return words

# NOTE: This makes 3 times fast when the
# `k` is at the length of 100000 comparing
# with the normal list comprehension
def submit(ad, aindices, default=None):
    global xd
    global xi
    global xdefault

    xd = ad
    xi = aindices
    xdefault = default

    # NOTE: multiprocessing is fast when the
    # size of the input is more than 5K
    if len(xi) > SIZE:
        pool = Pool()
        tasks = []

        # NOTE: `n` decides the number of jobs
        n = int(len(xi)/JOBS)
        for pindices in _chunkify(xi, n):
            t = pool.apply_async(_get, (pindices,))
            tasks.append(t)

        result = []
        for t in tasks:
            result.extend(t.get())

    else:
        result = _get(aindices)

    return result
