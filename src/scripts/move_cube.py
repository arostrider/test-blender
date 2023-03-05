import bpy
from helpers import blender_script_args, roundf


def move_cube(destination: tuple[float]):
    bpy.context.preferences.view.show_splash = False
    bpy.context.active_object.location = destination


if __name__ == "__main__":
    destination = tuple(float(coord) for coord in blender_script_args())
    move_cube(destination)
    new_location = tuple(roundf(coord) for coord in bpy.context.active_object.location)

    assert new_location == destination, f"Actual: {new_location} Expected: {destination}"
