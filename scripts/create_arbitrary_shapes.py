import bpy
from helpers.blender import blender_script_args, set_blender_render_settings, save_blend_file
from helpers.math_wrap import roundf

if __name__ == "__main__":
    args = blender_script_args()
    print(args)

    # init
    set_blender_render_settings(x_res=int(args['x']), y_res=int(args['y']), file_format='JPEG')
    bpy.context.preferences.view.show_splash = False

    # delete default cube
    object_to_delete = bpy.data.objects['Cube']
    bpy.data.objects.remove(object_to_delete, do_unlink=True)

    # create new cube
    x, y, z = tuple(float(coord) for coord in args['free_vals'])
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))

    # round coordinates of active object (should be new cube) to avoid assertion error due to high precision difference
    active_object_location = tuple(roundf(coord) for coord in bpy.context.active_object.location)

    assert active_object_location == (x, y, z), f"Actual: {active_object_location} Expected: {(x, y, z)}"

    print(bpy.data.scenes[0].render.resolution_x)
    print(bpy.data.scenes[0].render.resolution_y)
    print(bpy.data.scenes[0].render.image_settings.file_format)

    save_blend_file(path=args["out"])
