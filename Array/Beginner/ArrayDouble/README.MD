# Dynamic Array Implementation in Python

This project implements a dynamic array in Python, which automatically resizes itself when it's full. The array doubles its capacity each time it's full and needs to resize.

## Files

- `Array/Beginner/ArrayDouble/ArrayDoubling.py`: This file contains the `DoubleArray` class, which implements the dynamic array.

- `Array/Beginner/ArrayDouble/DoubleArrayTest.py`: This file contains the `TestDoubleArray` class, which includes unit tests for the `DoubleArray` class.

## Usage

To use the `DoubleArray` class, create an instance and use the `append` method to add elements. The array will automatically resize itself when it's full.

```python
from Array.Beginner.ArrayDouble.ArrayDoubling import DoubleArray

arr = DoubleArray()
arr.append("test")

from Array.Beginner.ArrayDouble.ArrayDoubling import DoubleArray

arr = DoubleArray()
arr.input_until_quit()
```

## Testing

To run the tests, navigate to the Array/Beginner/ArrayDouble directory and run the DoubleArrayTest.py file with Python's unittest module:

```bash
from Array.Beginner.ArrayDouble.ArrayDoubling import DoubleArray

arr = DoubleArray()
arr.input_until_quit()
```
