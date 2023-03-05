import sys

import bpy


def move_cube(destination: tuple[float]):
    bpy.context.preferences.view.show_splash = False
    bpy.context.active_object.location = destination


if __name__ == "__main__":
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]

    destination = tuple(float(coord) for coord in argv)
    move_cube(destination)

    assert tuple(bpy.context.active_object.location) == (1.0, 1.0, 1.0), \
        f"Actual: {tuple(bpy.context.active_object.location)} " \
        f"Expected: {(1.0, 1.0, 1.0)}"
