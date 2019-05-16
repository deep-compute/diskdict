import os
import shutil

import numpy as np
import cmph
from diskarray import DiskVarArray
from deeputil import Dummy

DUMMY_LOG = Dummy()

class VarArray(DiskVarArray):
    def __init__(self, dpath, mode='r+',
            growby=DiskVarArray.GROWBY,
            log=DUMMY_LOG):
        super(VarArray, self).__init__(dpath,
                dtype=np.uint8,
                mode=mode, growby=growby,
                log=log)

    def __getitem__(self, idx):
        data = super(VarArray, self).__getitem__(idx)
        if not len(data):
            return None

        n = int(np.fromstring(data[:8].tostring(), dtype=np.uint64)[0])
        s = data[8:].tostring()
        return n, s

    def _convert(self, v):
        if v is None:
            return np.array([], dtype=np.uint8)

        n, s = v
        n = np.fromstring(np.uint64(n).tostring(), dtype=np.uint8)
        s = np.array(list(s), dtype=np.uint8)
        v = np.concatenate([n, s])
        return v

    def append(self, v):
        return super(VarArray, self).append(self._convert(v))

    def extend(self, v):
        v = [self._convert(x) for x in v]
        return super(VarArray, self).extend(v)

class StaticStringIndexDict:
    def __init__(self, path, keys=None, log=DUMMY_LOG):
        self._path = path
        self.log = log
        self._data = None
        self._mph = None
        self._mph_path = os.path.join(path, 'mph')

        if keys:
            self._data, self._mph = self._storedata(path, keys)
        else:
            self._data = VarArray(path)
            self._mph = cmph.load_hash(open(self._mph_path, 'rb'))

    def _storedata(self, path, keys):
        if os.path.exists(path):
            shutil.rmtree(path)

        os.makedirs(path)
        mph = cmph.generate_hash(keys)
        mph.save(self._mph_path)

        indices = [mph(k) for k in keys]
        _max = max(indices)

        keyindices = dict((k, i) for i, k in enumerate(keys))
        data = dict((zip(indices, keys)))
        d = VarArray(path)

        _data = []

        for i in range(_max+1):
            k = data.get(i, None)
            v = None if k is None else (keyindices[k], k)
            _data.append(v)

        d.extend(_data)

        d.flush()

        return d, mph

    def get(self, k, default=None):
        i = self._mph(k) # FIXME: what if i is out of range?
        n, _k = self._data[i]
        if _k != k:
            return None

        return n

    def __getitem__(self, k):
        n = self.get(k)
        if n is None:
            raise KeyError
        return n

    def items(self):
        for i in range(len(self._data)):
            v = self._data[i]
            if v is None: continue

            n, k = v
            yield k, n

    def values(self):
        for k, v in self.items():
            yield v

    def keys(self):
        for k, v in self.items():
            yield k

    def flush(self):
        self._data.flush()

    def close(self):
        self._data.close()
