# Callum Metzke

from . import turtle_funcs as tf
from .lsystem_class import L_System


# Syntax:
#
# name = L_System(
#     axiom, {
#         symbol1: (function1, production1),
#         symbol2: (function2, production2),
#         ...
#     }, order, delta, initial_heading
# )


# This is an L_System with no axiom, no productions, order = 1 and delta = 90.
blank = L_System(
    "", {

    }, 1, 90
)


koch_curve = L_System(
    "F", {
        "F": (tf.fwd, "F+F--F+F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 6, 60
)


koch_snowflake = L_System(
    "F++F++F", {
        "F": (tf.fwd, "F-F++F-F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 6, 60
)


koch_antisnowflake = L_System(
    "F++F++F++", {
        "F": (tf.fwd, "F+F--F+F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 6, 60
)


koch_island = L_System(
    "F+F+F+F", {
        "F": (tf.fwd, "F-F+F+FF-F-F+F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 4, 90
)


terdragon = L_System(
    "F", {
        "F": (tf.fwd, "F-F+F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 9, 120
)


dragon = L_System(
    "F", {
        "F": (tf.fwd, "F+G+"),
        "G": (tf.fwd, "-F-G"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 16, 90
)


sierpinski = L_System(
    "F", {
        "F": (tf.fwd, "G-F-G"),
        "G": (tf.fwd, "F+G+F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 10, 60
)


# An alternate version of the Sierpinski triangle that has only even iterations
#
# sierpinski_2 = L_System(
#     "F", {
#         "F": (tf.fwd, "F+G+F-G-F-G-F+G+F"),
#         "G": (tf.fwd, "G-F-G+F+G+F+G-F-G"),
#         "+": (tf.left, "+"),
#         "-": (tf.right, "-"),
#     }, 5, 60
# )


garden = L_System(
    "F+F+F+F", {
        "F": (tf.fwd, "F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF"),
        "f": (tf.fwd_nodraw, "ffffff"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 3, 90
)


bracelet = L_System(
    "F-F-F-F", {
        "F": (tf.fwd, "FF-F-F-F-F-F+F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 5, 90
)


manhattan = L_System(
    "F-F-F-F", {
        "F": (tf.fwd, "FF-F-F-F-FF"),
        "-": (tf.right, "-"),
    }, 5, 90
)


embroidery = L_System(
    "F-F-F-F", {
        "F": (tf.fwd, "FF-F+F-F-FF"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
    }, 4, 90
)


vine = L_System(
    "F", {
        "F": (tf.fwd, "F[+F]F[-F]F"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
        "[": (tf.save, "["),
        "]": (tf.load, "]"),
    }, 5, 25.7, 90
)


tall_tree = L_System(
    "F", {
        "F": (tf.fwd, "F[+F]F[-F][F]"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
        "[": (tf.save, "["),
        "]": (tf.load, "]"),
    }, 5, 20, 90
)


wide_tree = L_System(
    "F", {
        "F": (tf.fwd, "FF-[-F+F+F]+[+F-F-F]"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
        "[": (tf.save, "["),
        "]": (tf.load, "]"),
    }, 4, 22.5, 90
)


forked_tree = L_System(
    "F", {
        "F": (tf.fwd, "G[+F][-F]GF"),
        "G": (tf.fwd, "GG"),
        "+": (tf.left, "+"),
        "-": (tf.right, "-"),
        "[": (tf.save, "["),
        "]": (tf.load, "]"),
    }, 8, 25.7, 90
)