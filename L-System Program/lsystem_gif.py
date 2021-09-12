# Callum Metzke

from imageio import imread, mimwrite
import turtle as t
from os import remove

from lsystem import main

import L_System_Files.arguments_gif as arguments_gif


def create_gif(args) -> None:
    """Creates a gif of an L-System progressing from a lower delta to an upper delta"""

    if args.values:
        main(args)

    else:

        framename = f"{args.name}.ps"
        images = []

        args.save = None
        args.no_pause = True

        for i in range(int( (args.upper_delta - args.lower_delta) / args.step_size) + 1):

            args.delta = args.lower_delta + i * args.step_size  # sequential deltas

            if args.delta > args.upper_delta:
                args.delta = args.upper_delta

            main(args)

            t.getscreen().getcanvas().postscript(file=framename)  # gets image as postscript
            t.clear()

            images.append(imread(framename))

            if args.delta in args.pause_deltas:  # pause in gif
                for _ in range(9):
                    images.append(imread(framename))

        remove(f"{framename}")  # removes temporary file

        if args.technical_information:
            args.name += f" {'C' if args.colour else 'B'} D({args.lower_delta}-{args.upper_delta}) O({args.system.order}) FR({args.frame_rate}) SS({args.step_size})"

        # converts postscript images to gif
        mimwrite(f"{args.name}.gif", images, fps=args.frame_rate)


if __name__ == "__main__":
    create_gif(arguments_gif.parser.parse_args())
