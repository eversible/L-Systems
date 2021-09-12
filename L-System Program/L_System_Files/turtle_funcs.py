# Callum Metzke

import turtle as t


def fwd(**kwargs) -> None:
    """Moves the turtle 1 unit forward, drawing a line."""

    t.pd()
    t.fd(1)


def fwd_nodraw(**kwargs) -> None:
    """Moves the turtle 1 units forward without drawing a line."""

    t.pu()
    t.fd(1)
    

def left(**kwargs) -> None:
    """Turns the turtle delta degrees to the left."""

    t.lt(kwargs["delta"])


def right(**kwargs) -> None:
    """Turns the turtle delta degrees to the right."""

    t.rt(kwargs["delta"])


def save(**kwargs) -> None:
    """Saves the turtle's position and heading to the top of the stack."""

    kwargs["stack"].append((t.pos(), t.heading()))


def load(**kwargs) -> None:
    """Recalls the turtle's position and heading from the top of the stack."""

    t.pu()

    try:
        t.setpos(kwargs["stack"][-1][0])
        t.seth(kwargs["stack"][-1][1])
        kwargs["stack"].pop()

    except IndexError:
        raise IndexError("The stack was exhausted")


def do_nothing(**kwargs) -> None:
    """Does nothing."""

    pass