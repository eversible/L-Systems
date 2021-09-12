# Callum Metzke
# --------------------------------------------------------------------------- #
# INSTRUCTIONS


# To create a custom L-system, you need to provide, in order:
# 1. An axiom
# 2. A dictionary of definitions for symbols
# 3. The order
# 4. The value of delta
# 5 (optional). initial heading

# In the dictionary of definitions, each key is a symbol.
# The value of that key is a tuple containing:
# 1. The turtle function to be performed by that symbol
# 2. The production rule for that symbol

# Syntax:
#
# name = L_System(
#     axiom, {
#         symbol1: (function1, production1),
#         symbol2: (function2, production2),
#         ...
#     }, order, delta
# )


# --------------------------------------------------------------------------- #
# L-SYSTEMS


from .lsystem_class import L_System

from . import turtle_funcs as tf
from . import custom_funcs as cf


# For example (note this uses the example function from custom_funcs.py):
#
# aligned_terdragon = L_System(
#     "cF", {
#         "F": (tf.fwd, "F-F+F"),
#         "+": (tf.left, "+"),
#         "-": (tf.right, "-"),
#         "c": (tf.do_nothing, "dc"),
#         "d": (cf.custom_left, "d"),
#     }, 9, 120
# )
