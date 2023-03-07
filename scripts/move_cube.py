import bpy
import helpers.blender_script_utils as bsu
from helpers.math_wrap import roundf

if __name__ == "__main__":
    args = bsu.blender_script_args()
    print(args)

    # init
    bsu.set_blender_render_settings(x_res=int(args['x']), y_res=int(args['y']), file_format='JPEG')
    bpy.context.preferences.view.show_splash = False

    # move default cube to destination provided in cmdline args
    destination = tuple(float(coord) for coord in args['coords'])
    bpy.context.active_object.location = destination

    # round coordinates of active object (should be default cube)
    # to avoid assertion error due to high precision difference
    new_location = tuple(roundf(coord) for coord in bpy.context.active_object.location)

    assert new_location == destination, f"Actual: {new_location} Expected: {destination}"

    print(bpy.data.scenes[0].render.resolution_x)
    print(bpy.data.scenes[0].render.resolution_y)
    print(bpy.data.scenes[0].render.image_settings.file_format)

    bsu.save_blend_file(path=args["out"])
