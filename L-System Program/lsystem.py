# Callum Metzke

import turtle as t
import time

import L_System_Files.arguments as arguments

import L_System_Files.auxiliary_funcs as af
import L_System_Files.custom_funcs as cf


def main(args) -> None:
    """Draws an L-System."""

    if args.values:
        print(f"Axiom\t\t{args.system.axiom}")
        print(f"Order\t\t{args.system.order}")
        print(f"Delta\t\t{args.system.delta}")
        print(f"Initial Heading\t{args.system.initial_heading}")

    else:

        if args.order is not None:
            args.system.order = args.order
        if args.delta is not None:
            args.system.delta = args.delta
        if args.delta is not None:
            args.system.delta = args.delta
        if args.initial_heading is not None:
            args.system.initial_heading = args.initial_heading

        for p in args.definitions:

            args.system.productions[p[0]] = p[1:]

        string = args.axiom if args.axiom is not None else args.system.axiom

        # Python 3.9+
        # properties = {"delta": args.system.delta, "stack": args.system.stack} | cf.custom_properties

        # Python 3.8
        properties = {"delta": args.system.delta, "stack": args.system.stack, **cf.custom_properties}

        t.Screen().getcanvas()._root().wm_attributes("-fullscreen", "True")

        t.setup(1., 1.)

        t.ht()

        t.tracer(0, 0)

        load_tur = t.Turtle(visible=False)
        load_tur.ht()

        t.speed(0)

        load_tur.speed(0)

        screen_ratio = (gs := t.getscreen()).window_width() / gs.window_height()

        af.reset_dimensions(screen_ratio, load_tur)

        af.send_to_origin(args.system.initial_heading)

        t.pensize(args.width)

        if args.intermediates:

            af.loading_text(load_tur, (-screen_ratio + 0.2, 0.8),
                            "left", ("Geneva", "40", "normal"))

            x_min, y_min, x_max, y_max = af.execute_string(
                string, args.system, af.label(args.print_string, 0), args.colour, **properties)

            load_tur.clear()

            dimensions = af.readjust_dimensions(
                x_min, y_min, x_max, y_max, screen_ratio)

            for o in range(args.system.order):

                time.sleep(args.time_delay)

                t.clear()

                af.reset_dimensions(screen_ratio, load_tur)

                af.loading_text(load_tur, (-screen_ratio + 0.2, 0.8),
                                "left", ("Geneva", "40", "normal"))

                af.send_to_origin(args.system.initial_heading)

                string = af.iterate_string(string, args.system.productions)

                args.system.stack.clear()

                x_min, y_min, x_max, y_max = af.execute_string(
                    string, args.system, af.label(args.print_string, o + 1), args.colour, **properties)

                load_tur.clear()

                dimensions = af.readjust_dimensions(
                    x_min, y_min, x_max, y_max, screen_ratio)

        else:

            af.loading_text(load_tur, (0, 0),
                "center", ("Geneva", "60", "normal"))

            string = af.iterate_string(string, args.system.productions, args.system.order)

            x_min, y_min, x_max, y_max = af.execute_string(
                string, args.system, af.label(args.print_string, args.system.order), args.colour, **properties)

            load_tur.clear()

            dimensions = af.readjust_dimensions(
                x_min, y_min, x_max, y_max, screen_ratio)


        if args.save:

            from imageio import imread, imwrite
            from os import remove

            t.getscreen().getcanvas().postscript(file=f"{args.save}.ps")

            imwrite(f"{args.save}.png", imread(f"{args.save}.ps"))

            remove(f"{args.save}.ps")


        if not args.no_pause:

            max_dimensions = tuple(dimensions)

            t.listen()

            t.onkeypress(exit, "Escape")
            t.onkeypress(exit, "q")
            t.onkeypress(exit, "Q")

            dimensions = af.zoom(args.system, dimensions, max_dimensions)

            t.done()


if __name__ == "__main__":
    main(arguments.parser.parse_args())