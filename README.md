# DiskDict

## Description
`DiskDict` is a file based module which stores data as key, value pairs like a python dictionary. `DiskDict` stores the data on the disk unlike python dictionary which stores data in the RAM.

## Installation

> Prerequisites: Python

```bash
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
```bash
$ diskdict interact <input_file>
```

#### QuickExample
```bash
$ diskdict interact /tmp/disk.dict
DiskDict Console
>>> dd['dc']=1
>>> dd.get('dc')
1
```

## Static String to Int map
`diskdict` uses cmph and mmap to build static string to integer map. We have to provide the byte strings initially.
`diskdict` builds respective index for each key.

### Example

```python
from diskdict import StaticStringIndexDict

l = [b'india', b'usa', b'japan', b'china']
s = StaticStringIndexDict(path='/data/map', keys=l)

print(s[b'japan'])

s.close()
```

Above example builds the map in the location of `/data/map`. We don't have to provide the byte strings from second time onwards.

```python
from diskdict import StaticStringIndexDict

s = StaticStringIndexDict(path='/data/map')
print(s[b'japan'])

s.close()
```

## Running Tests

```bash
$ python setup.py test
```
