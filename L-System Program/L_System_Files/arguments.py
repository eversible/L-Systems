# Callum Metzke

import argparse

from . import turtle_funcs as tf
from . import custom_funcs as cf

from . import custom_lsystems
from . import example_lsystems

from L_System_Files.lsystem_class import L_System


def L_System_Type(system: str) -> L_System:
    """Checks that the chosen system is a defined L-System and returns that L-System."""

    if system in (examples := [d for d in dir(example_lsystems) if "__" not in d and d not in ("L_System", "tf")]):
        return getattr(example_lsystems, system)

    elif system in (customs := [d for d in dir(custom_lsystems) if "__" not in d and d not in ("L_System", "tf", "cf")]):
        return getattr(custom_lsystems, system)

    else:
        raise argparse.ArgumentTypeError(f"No such L-System exists. Choose from {examples + customs}")


class DefineSymbol(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):

        if len(values[0]) != 1:
            raise ValueError("A symbol must be one character in length")

        cf_func_list = [d for d in dir(cf) if "__" not in d]
        cf_func_list.remove("t")
        cf_func_list.remove("custom_properties")

        tf_func_list = [d for d in dir(tf) if "__" not in d]
        tf_func_list.remove("t")

        if values[1] in cf_func_list:
            funcs = cf

        elif values[1] in tf_func_list:
            funcs = tf

        else:
            raise ValueError(
                f"{values[1]} is not a valid function; valid functions are:\n\n{tf_func_list + cf_func_list}\n")

        getattr(args, self.dest).append(
            [values[0], getattr(funcs, values[1]), values[2]])


parser = argparse.ArgumentParser(description="Generate L-System Fractals")

parser.add_argument("system", action="store", default=False, type=L_System_Type,
                    help="The L-system to be generated. Type \"blank\" to load a blank L-system.")

parser.add_argument("-a", "--axiom", action="store", type=str,
                    help="the axiom of the system")
parser.add_argument("-o", "--order", action="store", type=int,
                    help="order of the system (iterations + 1)")
parser.add_argument("-d", "--delta", action="store", type=float,
                    help="angle of each turn (degrees)")
parser.add_argument("-ih", "--initial_heading", action="store", type=float,
                    help="initial heading of the turtle (degrees)")
parser.add_argument("-def", "--definitions", nargs=3, action=DefineSymbol, default=[], type=list,
                    help="define or redefine a symbol with its function and production; \
                    format: -def [symbol] [function] [production]")
parser.add_argument("-v", "--values", action="store_const", const=True, default=False,
                    help="show all preset values of the system")

parser.add_argument("-i", "--intermediates", action="store_const", const=True, default=False,
                    help="show intermediate generations")
parser.add_argument("-t", "--time_delay", action="store", default=1, type=float,
                    help="time delay for loading next generation (for -i/--intermediates flag)")
parser.add_argument("-p", "--print_string", action="store_const", const=True, default=False,
                    help="print the final string (or the string after every iteration if -i/--intermediates is specified)")

parser.add_argument("-w", "--width", action="store", default=1, type=int,
                    help="set the line width of the turtle's path")
parser.add_argument("-c", "--colour", action="store_const", const=True, default=False,
                    help="add a colour gradient to the image (warning: takes significantly longer for large images, requires colour package)")

parser.add_argument("-s", "--save", nargs='?', action="store", type=str, const="L-System",
                    help="save the image as a png with the given name (requires imageio)")

parser.add_argument("-np", "--no_pause", action="store_const", const=True, default=False,
                    help="stop the program from pausing once the full image is generated")
