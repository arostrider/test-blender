import bpy
from helpers import blender_script_args, roundf, set_blender_render_settings, save_blend_file


def move_cube(location: tuple[float]):
    bpy.context.preferences.view.show_splash = False
    bpy.context.active_object.location = location


if __name__ == "__main__":
    args = blender_script_args()
    print(args)

    set_blender_render_settings(x_res=int(args['x']), y_res=int(args['y']), file_format='JPEG')

    destination = tuple(float(coord) for coord in args['free_vals'])
    move_cube(destination)

    new_location = tuple(roundf(coord) for coord in bpy.context.active_object.location)

    assert new_location == destination, f"Actual: {new_location} Expected: {destination}"

    print(bpy.data.scenes[0].render.resolution_x)
    print(bpy.data.scenes[0].render.resolution_y)
    print(bpy.data.scenes[0].render.image_settings.file_format)

    save_blend_file(path=args["out"])
