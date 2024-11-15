import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def smallangle_group():
    pass


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
    breaks the interval [0, 2pi] into a NUMBER steps and calculates the tangent for each one

    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    smallangle_group()
