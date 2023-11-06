# trapezoidalfuzzynumber 
[![Read the docs](https://img.shields.io/static/v1?label=&message=Read+the+docs&color=%23EC1C24&logo=readme&logoColor=%23FCFBFA)](https://github.com/zakrzewskij/trapezoidalfuzzynumber/wiki)
[![PyPI - trapezoidalfuzzynumber](https://img.shields.io/static/v1?label=PyPI&message=trapezoidalfuzzynumber&color=%23FF7328&logo=pypi&logoColor=%233775A9)](https://test.pypi.org/project/trapezoidalfuzzynumber/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/release)
[![QA - Python Tests & Coverage](https://github.com/zakrzewskij/trapezoidalfuzzynumber/actions/workflows/demo.yml/badge.svg)](https://github.com/zakrzewskij/trapezoidalfuzzynumber/actions/workflows/demo.yml)

A Python package implementing two-sample permutation tests for verifying the equality of ambiguities in fuzzy data. Additionally, it provides essential arithmetic operations performed on trapezoidal fuzzy numbers.

## Installation
Before installing trapezoidalfuzzynumber, make sure to have numpy installed. You can install it using pip:
```bash
pip install "numpy>=1.26.0"
```
You can install trapezoidalfuzzynumber using pip:
```bash
pip install -i https://test.pypi.org/simple/ trapezoidalfuzzynumber
```

# Overview
The trapezoidalfuzzynumber package is designed to handle fuzzy data, offering two-sample permutation tests and arithmetic operations on trapezoidal fuzzy numbers. Here's a quick guide to get you started.

## Usage
```python  
from ambiguity import *
from fuzzy_numbers import *
```

## Creating Trapezoidal Fuzzy Numbers
You can create trapezoidal fuzzy numbers with the TrapezoidalFuzzyNumber class:
```python  
# Create trapezoidal fuzzy numbers
from fuzzy_numbers import *
import numpy as np

tn = TrapezoidalFuzzyNumber(1, 2, 3, 4)
```

## Arithmetic Operations
You can perform arithmetic operations on trapezoidal fuzzy numbers:
### Addition
```python
from fuzzy_numbers import *
import numpy as np

tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
tn2 = TrapezoidalFuzzyNumber(2, 3, 4, 5)
tn3 = tn1 + tn2
print(tn3)
"""
Output:
TrapezoidalFuzzyNumber(a=3, b=5, c=7, d=9)
Support: (3, 9)
Core: (5, 7)
Ambiguity of the trapezoidal fuzzy number: 1.6667)
"""
```
### Subtraction
```python
from fuzzy_numbers import *
import numpy as np

tn1 = TrapezoidalFuzzyNumber(3, 4, 5, 6)
tn2 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
tn3 = TrapezoidalFuzzyNumber(-11, -4,-2, 0)
tn = tn1 - tn2
print(tn)
"""
Output:
TrapezoidalFuzzyNumber(a=-1, b=1, c=3, d=5)
Support: (-1, 5)
Core: (1, 3)
Ambiguity of the trapezoidal fuzzy number: 1.6667)
"""
```
### Multiplication
```python
from fuzzy_numbers import *
import numpy as np

tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
tn2 = TrapezoidalFuzzyNumber(-1, 0, 2, 3)

tn = tn1 * tn2
print(tn)
"""
Output tn1 * tn2:
TrapezoidalFuzzyNumber(a=-4, b=0, c=6, d=12)
Support: (-4, 12)
Core: (0, 6)
Ambiguity of the trapezoidal fuzzy number: 4.6667)
"""
```
### Division
```python
from fuzzy_numbers import *
import numpy as np

tn1 = TrapezoidalFuzzyNumber(1, 2, 3, 4)
tn2 = TrapezoidalFuzzyNumber(2, 3, 4, 5)
tn3 = tn1 / tn2
print(tn3)
"""
Output:
TrapezoidalFuzzyNumber(a=0.2, b=0.5, c=1, d=2)
Support: (0.2, 2)
Core: (0.5, 1)
Ambiguity of the trapezoidal fuzzy number: 0.4667)
"""
```

## Documentation
For detailed information on how to use `trapezoidalfuzzynumber`, check out the [documentation](https://github.com/zakrzewskij/trapezoidalfuzzynumber/wiki). Everything you need to know is described there, including examples and usage guidelines.

## License

This project is licensed under the MIT License. For more information, please see the [LICENSE](LICENSE) file.
