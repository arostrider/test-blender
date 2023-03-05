import bpy
from helpers import blender_script_args


def move_cube(destination: tuple[float]):
    bpy.context.preferences.view.show_splash = False
    bpy.context.active_object.location = destination


if __name__ == "__main__":
    destination = tuple(float(coord) for coord in blender_script_args())
    move_cube(destination)

    assert tuple(bpy.context.active_object.location) == (1.0, 1.0, 1.0), \
        f"Actual: {tuple(bpy.context.active_object.location)} " \
        f"Expected: {(1.0, 1.0, 1.0)}"
