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


# Flat is better than nested.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class UserInput:
    name: Optional[str]
    last_name: Optional[str]
    cellphone: Optional[str]


def print_user_input_data_flat(user_input: UserInput) -> None:
    if user_input.name is None or len(user_input.name) < 3:
        print(f"The provided name {user_input.name} is not valid")
        return

    if user_input.last_name is None or len(user_input.last_name) < 4:
        print(f"The provided last_name {user_input.last_name} is not valid")
        return

    if user_input.cellphone is None or not user_input.cellphone.isnumeric():
        print(f"The provided last_name {user_input.last_name} is not valid")
        return

    print(
        f"The user input is {user_input.name} {user_input.last_name} {user_input.cellphone}"
    )


def print_user_input_data_nested(user_input: UserInput) -> None:
    if user_input.name is not None and len(user_input.name) >= 3:
        if user_input.last_name is not None and len(user_input.last_name) >= 4:
            if user_input.cellphone is not None and user_input.cellphone.isnumeric():
                print(
                    f"The user input is {user_input.name} {user_input.last_name} {user_input.cellphone}"
                )
            else:
                print(f"The provided last_name {user_input.last_name} is not valid")
                return
        else:
            print(f"The provided last_name {user_input.last_name} is not valid")
            return
    else:
        print(f"The provided name {user_input.name} is not valid")
        return


user_input: UserInput = UserInput(
    name="Rosemberg", last_name="Porras", cellphone="3215478569"
)
print_user_input_data_flat(user_input=user_input)
print_user_input_data_nested(user_input=user_input)

# Sparse is better than dense.

user_input: UserInput = UserInput(
    name="Rosemberg Sparse", last_name="Porras", cellphone="3215478569"
)
print_user_input_data_flat(user_input=user_input)

print_user_input_data_nested(
    user_input=UserInput(
        name="Rosemberg dense", last_name="Porras", cellphone="3215478569"
    )
)
