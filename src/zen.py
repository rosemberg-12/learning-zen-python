# Beautiful is better than ugly.

"""
This focus on the aesthetic Syntax of Python; Futhermore, Python allows the use of special characters for better
variable specification
"""
from math import cos, sin
from typing import Callable

tan: Callable = lambda θ: sin(θ) / cos(θ)
print(tan(θ=90))


# Explicit is better than implicit.

"""
Nothing should be assumpt. Therefore, it would be good the use of variable type specification and return type notation for ensuring everything is explicit
"""

from typing import TypeAlias

Angle: TypeAlias = float


def tan_func(θ: Angle) -> float:
    """
    Given an angle, calculate and return the tangent of the angle using a trigonometric function for this purpose
    """

    return sin(θ) / cos(θ)


print(tan_func(θ=90))


# Simple is better than complex.
# Complex is better than complicated.

"""
We should try to find the most simple approach as possible though not always it's possible
because the systems are complex, but complex is different to complicate or hard to understand

Picking comprenhention list, 
"""

WordToCheck: TypeAlias = str


def palindrome_check(word: WordToCheck) -> bool:
    upper_word = word.upper()
    return upper_word == upper_word[::-1]


print(palindrome_check(word="Ana"))
print(palindrome_check(word="BBWA"))
