# Callum Metzke

from dataclasses import dataclass, field

# In retrospect, I would have liked to define a number of class methods
# instead of defining a number of external functions to handle these
# L-Systems, but since everything is working fine, a drastic redesign
# would unfortunately be too time consuming. I might attempt this
# overhaul once I have more time on my hands, if anything, for practice.

@dataclass
class L_System:
    """A Lindenmayer-System (aka L-System).

    axiom: the starting string of characters
    productions: the transformation to be applied to each character
    order: how many iterations to be applied
    delta: the default angle for turns (degrees)
    heading: the initial heading of the turtle (0 is rightward)
    """

    axiom: str
    productions: dict
    order: int
    delta: int
    initial_heading: int = 0
    magnification: int = 1
    stack: list = field(default_factory=list)