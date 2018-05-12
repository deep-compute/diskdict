import os
import pickle

from deeputil import Dummy
import plyvel

DUMMY_LOG = Dummy()

# export DISKDICT_DATADIR_PATH=='/home/usr/diskdict_dir_path'
DATA_FILE = os.environ.get('DISKDICT_DATADIR_PATH', '/tmp')


class DiskDict(object):
    # FIXME: using eval - dangerous

    def __init__(self, path, log=DUMMY_LOG):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> dd['deepcompute'] = 1
        '''

        self._path = path
        self.log = log
        self._f = plyvel.DB(path, create_if_missing=True)

    def _enckey(self, k):
        return repr(k).encode('utf8')

    def _deckey(self, k):
        return eval(k.decode('utf8'))

    def get(self, k, default=None):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(dd.get('deepcompute'))
        1
        '''

        k = self._enckey(k)
        v = self._f.get(k, None)
        if v is None: return default
        return pickle.loads(v)

    def __getitem__(self, k):
        return self.get(k)

    def __setitem__(self, k, v):
        k = self._enckey(k)
        v = pickle.dumps(v)
        self._f.put(k, v)

    def __delitem__(self, k):
        k = self._enckey(k)
        self._f.delete(k)

    def items(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(next(dd.items()))
        ('deepcompute', 1)
        '''

        for k, v in self._f:
            yield self._deckey(k), pickle.loads(v)

    def values(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(next(dd.values()))
        1
        '''

        for _, v in self.items():
            yield v

    def keys(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(next(dd.keys()))
        deepcompute
        '''

        for k, _ in self.items():
            yield k

    def flush(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> dd.flush()
        '''

        pass

    def close(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> dd.close()
        '''

        self._f.close()
        self._f = None
