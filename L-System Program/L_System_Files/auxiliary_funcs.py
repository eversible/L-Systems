# Callum Metzke

import turtle as t

from .lsystem_class import L_System


def iterate_string(string: str, productions: dict, n: int = 1) -> str:
    """Iterates over an L-System string according to the system productions."""

    for _ in range(n):

        new_string = ""

        for s in string:

            new_string += productions[s][1]

        string = new_string

    return string


def execute_string(string: str, system: L_System, print_label=False, colour=False, **kwargs) -> list:
    """Executes an L-System string.

    Returns the list of dimensions following:
    dimensions = [x_min, y_min, x_max, y_max]
    """

    dimensions = [0, 0, 0, 0]

    if colour:

        from colour import Color

        # a colour gradient from red to magenta
        gradient = list(
            map(str, Color("#ff0000").range_to(Color("#ff00ff"), len(string))))

        for i in range(len(string)):

            t.pencolor(gradient[i])

            system.productions[string[i]][0](**kwargs)

            dimensions[0] = min(dimensions[0], (p := t.pos())[0])
            dimensions[1] = min(dimensions[1], p[1])
            dimensions[2] = max(dimensions[2], p[0])
            dimensions[3] = max(dimensions[3], p[1])

    else:

        for s in string:

            system.productions[s][0](**kwargs)

            dimensions[0] = min(dimensions[0], (p := t.pos())[0])
            dimensions[1] = min(dimensions[1], p[1])
            dimensions[2] = max(dimensions[2], p[0])
            dimensions[3] = max(dimensions[3], p[1])

    if print_label:
        print()
        print(print_label)
        print(string)

    return dimensions


def reset_dimensions(screen_ratio: float, load_turtle: t.Turtle) -> None:
    """Resets world coordinates."""

    t.setworldcoordinates(-screen_ratio, -1, screen_ratio, 1)
    t.ht()
    load_turtle.ht()
    t.update()


def readjust_dimensions(x_min: float, y_min: float, x_max: float, y_max: float, screen_ratio: float) -> list:
    """Readjusts world coordinates to fit image."""

    border_quotient = 5

    # The corner case that the image is a point
    if x_min == x_max and y_min == y_max:
        dimensions = [x_min - 1, y_min - 1,
                      x_max + 1, y_max + 1]

    # The case that the image is wider than the screen ratio
    elif y_min == y_max or (x_max - x_min) / (y_max - y_min) >= screen_ratio:
        border = (dif := x_max - x_min) / border_quotient
        box = dif / screen_ratio / 2
        avg = (y_max + y_min) / 2
        dimensions = [x_min - border, avg - box - (border / screen_ratio),
                      x_max + border, avg + box + (border / screen_ratio)]

    # The case that the image is taller than the screen ratio
    else:
        border = (dif := y_max - y_min) / border_quotient
        box = dif * screen_ratio / 2
        avg = (x_max + x_min) / 2
        dimensions = [avg - box - (border * screen_ratio), y_min - border,
                      avg + box + (border * screen_ratio), y_max + border]

    t.setworldcoordinates(*dimensions)

    t.ht()
    t.update()

    return dimensions


def zoom(system: L_System, dimensions: list, max_dimensions: tuple) -> list:
    """Adjusts the world coordinates to zoom in or out the turtle drawing.

    Zooms in 2× at the mouse position when '+' (or '=') is pressed.
    Zooms out 2× at the mouse position when '-' (or '_') is pressed.
    """

    def zoom_in_or_out(zoom_in) -> None:
        "Handles the zooming functionality."

        if zoom_in:
            system.magnification *= 2
        elif system.magnification > 1:
            system.magnification //= 2

        gs = t.getscreen()

        max_x_span, max_y_span = max_dimensions[2] - \
            max_dimensions[0], max_dimensions[3] - max_dimensions[1]

        # the position of the mouse relative to the screen
        x_mouse_ratio = gs.cv.winfo_pointerx() / gs.window_width()
        y_mouse_ratio = 1 - gs.cv.winfo_pointery() / gs.window_height()

        # transforms the position of the mouse to terms of world coordinates
        x = dimensions[0] + (dimensions[2] - dimensions[0]) * x_mouse_ratio
        y = dimensions[1] + (dimensions[3] - dimensions[1]) * y_mouse_ratio

        x_diameter = max_x_span / system.magnification
        y_diameter = max_y_span / system.magnification

        left = x_diameter * x_mouse_ratio
        right = x_diameter - left

        down = y_diameter * y_mouse_ratio
        up = y_diameter - down

        # x-direction zoom
        if x - left <= max_dimensions[0]:
            dimensions[0] = max_dimensions[0]
            dimensions[2] = max_dimensions[0] + x_diameter

        elif x + right >= max_dimensions[2]:
            dimensions[0] = max_dimensions[2] - x_diameter
            dimensions[2] = max_dimensions[2]

        else:
            dimensions[0] = x - left
            dimensions[2] = x + right

        # y-direction zoom
        if y - down <= max_dimensions[1]:
            dimensions[1] = max_dimensions[1]
            dimensions[3] = max_dimensions[1] + y_diameter

        elif y + up >= max_dimensions[3]:
            dimensions[1] = max_dimensions[3] - y_diameter
            dimensions[3] = max_dimensions[3]

        else:
            dimensions[1] = y - down
            dimensions[3] = y + up

        t.setworldcoordinates(*dimensions)

    def zoom_in() -> None:
        zoom_in_or_out(True)

    def zoom_out() -> None:
        zoom_in_or_out(False)

    t.onkey(zoom_in, "=")
    t.onkey(zoom_in, "+")

    t.onkey(zoom_out, "-")
    t.onkey(zoom_out, "_")

    return dimensions


def send_to_origin(heading: float) -> None:
    """Sends the main turtle back to the origin and sets its heading."""

    t.pu()
    t.setpos(0, 0)
    t.seth(heading)


def loading_text(load_turtle: t.Turtle, coords: tuple, alignment: str, font: tuple) -> None:
    """Prints the loading text on the screen."""

    load_turtle.pu()
    load_turtle.setpos(coords)
    load_turtle.write("Loading...", align=alignment, font=font)


def label(print_string: bool, order: int) -> str:
    """A label for the -s flag."""

    if print_string:
        return f"Order: {order}"

    return ""
