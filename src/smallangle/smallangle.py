"""
This module contains functions that can calculate the sine or tangent of a list of numbers between 0 and 2pi.
Click is used so the functions can be summoned by commands in the terminal. The amount of numbers is given by NUMBER.
"""

import click
import numpy as np
import pandas as pd
from numpy import pi


# this code makes the group
@click.group()
def smallangle_group():
    pass


# this code makes the sin command
@smallangle_group.command
@click.option(
    "-n",
    "--number",
    default=10,
    help="The amount of steps the interval is divided in",
    type=int,
    show_default=True,  # shows the default in --help
)
def sin(number):
    """
    Breaks the interval [0, 2pi] into a NUMBER of steps and calculates the sine for each one.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


# this code makes the tan command
@smallangle_group.command
@click.option(
    "-n",
    "--number",
    default=10,
    help="The amount of steps the interval is divided in",
    type=int,
    show_default=True,  # shows the default in --help
)
def tan(number):
    """
    Breaks the interval [0, 2pi] into a NUMBER steps and calculates the tangent for each one.

    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


# this code ensures that the code above is only executed when the script is run directly, and not when it is imported as a module in another script.
if __name__ == "__main__":
    smallangle_group()
