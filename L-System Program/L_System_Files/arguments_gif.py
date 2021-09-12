# Callum Metzke

from .arguments import parser

# Note, all of the following arguments become obsolete:
#
# args.save (set to None)
# args.no_pause (set to True)
# args.delta (calculated)

parser.description = "Generate L-System Fractal Gifs"

parser.add_argument("-n", "--name", action="store", type=str, default="L-System Gif",
                    help="save the gif at the given path")
parser.add_argument("-ti", "--technical_information", action="store_const", const=True, default=False,
                    help="append some technical information to the gif name")

parser.add_argument("-ld", "--lower_delta", action="store", type=float, default=0.,
                    help="the minimum value of delta to iterate over")
parser.add_argument("-ud", "--upper_delta", action="store", type=float, default=360.,
                    help="the maximum value of delta to iterate over")
parser.add_argument("-ss", "--step_size", action="store", type=float, default=1.,
                    help="the step size between deltas")
parser.add_argument("-pd", "--pause_deltas", nargs='*', action="store", type=float, default=[],
                    help="the values of delta to pause the gif at")

parser.add_argument("-fr", "--frame_rate", action="store", type=float, default=10.,
                    help="the amount of frames per second in the output gif")
