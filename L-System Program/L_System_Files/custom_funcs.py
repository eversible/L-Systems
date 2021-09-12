# Callum Metzke
# --------------------------------------------------------------------------- #
# INSTRUCTIONS


# To write a custom function, use the turtle module (imported as "t").
# You can name this function anything you want, and use any turtle method 
# from the turtle module.
#
# You can write extra properties into custom_properties, and then access them
# by using the kwargs (keyword arguments).
# For example, by writing
#
# "constant": 30
#
# inside custom_properties, you can then use
#
# kwargs["constant"]
#
# inside your custom function, which has value 30 (or however you define it).


# --------------------------------------------------------------------------- #
# PROPERTIES


custom_properties = {
    # For example:
    # "constant": 30
}


# --------------------------------------------------------------------------- #
# FUNCTIONS


import turtle as t


# For example:
#
# def custom_left(**kwargs):
#     """Turns left by a constant amount."""

#     t.left(kwargs["constant"])


def custom_function(**kwargs):
    """A custom user function."""

    pass
