import os

from deeputil import Dummy
from sqlitedict import SqliteDict

DUMMY_LOG = Dummy()

# export DISKDICT_DATAFILE_PATH=='/home/usr/diskdict_file_path'
DATA_FILE = os.environ.get('DISKDICT_DATAFILE_PATH', '')


class DiskDict(object):
    # FIXME: using eval - dangerous

    def __init__(self, fpath, autocommit=True, log=DUMMY_LOG):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> dd['deepcompute'] = 1
        '''

        self._fpath = fpath
        self.log = log
        self._f = SqliteDict(fpath, autocommit=autocommit)

    def get(self, k, default=None):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(dd.get('deepcompute'))
        1
        '''

        k = repr(k)
        return self._f.get(k)

    def __getitem__(self, k):
        k = repr(k)
        return self._f[k]

    def __setitem__(self, k, v):
        k = repr(k)
        self._f[k] = v

    def items(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(next(dd.items()))
        ('deepcompute', 1)
        '''

        for k, v in self._f.iteritems():
            yield eval(k), v

    def values(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(next(dd.values()))
        1
        '''

        for v in self._f.itervalues():
            yield v

    def keys(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> print(next(dd.keys()))
        deepcompute
        '''

        for k in self._f.iterkeys():
            yield eval(k)

    def flush(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> dd.flush()
        '''

        self._f.commit()

    def close(self):
        '''
        >>> dd = DiskDict(DATA_FILE)
        >>> dd.close()
        '''

        self._f.close()
        self._f = None
