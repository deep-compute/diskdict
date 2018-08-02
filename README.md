# DiskDict

## Description
`DiskDict` is a file based module which stores data as key, value pairs like a python dictionary.

## Installation

> Prerequisites: Python

```
$ sudo pip install diskdict
```

## Quick Example

```python
>>> from diskdict import DiskDict

# Initiate the diskdict with the path
>>> dd = DiskDict('/tmp/diskdict')

# Storing the data into diskdict
>>> dd['deepcompute'] = 1
>>> dd['deeporg'] = 2
>>> dd[1] = 5

# Get the values regarding keys from diskdict
>>> print(dd.get('deepcompute'))
1

>>> print(dd['deepcompute'])
1

# Get key, value pairs in tuple format from diskdict
>>> next(dd.items())
('deeporg', 2)

>>> for item in dd.items():
...     print(item)
...
('deeporg', 2)
('deepcompute', 1)
(1, 5)

# Get the keys from diskdict
>>> next(dd.keys())
deeporg

>>> for key in dd.keys():
...     print(key)
...
deeporg
deepcompute
1

# Get the values from diskdict
>>> next(dd.values())
2

>>> for value in dd.values():
...     print(value)
...
2
1
5

# closing the file
>>> dd.close()

```

## Interactive console
```
$ diskdict interact <input_file>
```

#### QuickExample
```
$ diskdict interact /tmp/disk.dict
DiskDict Console
>>> dd['dc']=1
>>> dd.get('dc')
1
```

## DiskDict submit

When we need to get values for bunch of keys then the submit can be used

```python
from diskdict import DiskDict, submit

d = DiskDict('/tmp/diskdict')

keys = ['india', 'ap', 'bg', 'the', 'of']
result = submit(d, keys, default=None) # If key is not present then default is used
```

## Running Tests

```
$ python setup.py test
```
