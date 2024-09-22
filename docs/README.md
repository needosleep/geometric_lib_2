# geometric\_lib\_2

## Introductory

This library provides modules with maths functions to work with different figures. 
It helps to calculate area and perimeter which can be very useful while solving geometric problems.
The library consists of python modules consisted formulas for different figures.

## Functions and possibilities

### Possibilities

The library can calculate area and perimeter of next figures:
- square
- circle
- triangle
- rectangle

All the functions can take int or float datatype. Output's type depends on input and function which you use.

## Examples

### Work with square

```python
from square import *
a = 12
print(f"The area of the square is {area(a)}")
printf(f"The perimeter of the square is {perimeter(a)}")
```

The output will be:

```
The area of the square is 144
The perimeter of the square is 48
```

### Work with circle

```python
from circle import *
r = 5
print(f"The area of the circle is {round(area(r), 2)}")
print(f"The perimeter of the circle is {round(perimeter(r), 3)}")
```

The output will be:

```
The area of the circle is 78.54
The perimeter of the circle is 31.416
```

### Work with rectangle

```python
from rectangle import *
a = 8
b = 5
printf(f"The area of the rectangle is {area(a, b)}")
print(f"The perimeter of the rectangle is {perimeter(a, b)}")
```

The output will be:

```
The area of the rectangle is 40
The perimeter of the rectangle is 26
```

### Work with triangle

```python
from triangle import *
a, b, c = 10, 6, 8
h = 4.8
print(f"The area of the triangle is {area(a, h)}")
print(f"The perimeter of the triangle is {perimeter(a, b, c)}")
```

The output will be:

```
The area of the triangle is 24.0
The perimeter of the triangle is 24
```

## Referential information

### Math formulas

#### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

#### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

### History of changes

#### March 4, 2021, 14:54:08

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
message: Circle and square added

In this commit some functions were added: circle and square. They take int or float type and return the same.

- Circle prototype:
```python
import math


def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

```

- Square prototype:
```python

def area(a):
    return a * a


def perimeter(a):
    return 4 * a

```

#### March 4, 2021, 14:55:29

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
message: Docs added

In this commit the directory docs was added and README.md file was added there and it had the next information:
```
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
```

#### September 22, 2024, 13:40:38

commit a268052a06defb13684d842271ff81470c194d67
message: File rectangle.py was added

In this commit the new file of library rectangle.py was added, operations with rectangles became possible. It had the next code:

```python
def area(a, b):
    return a * b

def perimeter(a, b):
    return a + b
```

#### September 22, 2024, 13:42:18

commit b026607cce6eced68c3f561d79402d4179ac2e1b
message: File rectangle.py: the function perimeter was corrected; file triangle.py was added

Bug fixed in rectangle.py:
```
 def perimeter(a, b):
-    return a + b
+    return 2 * (a + b)
```

The new file triangle.py was added, it consisted the next code:
```python
def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

```
#### September 22, 2024, 13:54:01

commit 39d870ea9f42edf474e508d6210bdf4c9976739d
message: The functions of the file rectangle.py were documented

In this commit one of the functions rectangle.py was documented (test mode)

#### September 22, 2024, 14:02:41

commit 59b2131bb6c9dd1a76d77ea48c08218862a97179
message: The functions of the file triangle.py were documented

Triangle.py was also documented in this commit (test mode)

#### September 22, 2024, 15:11:23

commit ca67fea87f751e56cad7fb23fdae5169342a002c
message: The functions from the first two files square.py and circle.py were also documented

In this commit all the function in all the files were documented, now it's easier to understand what each of them does
