import bpy
import helpers.blender_script_utils as bsu
from helpers.math_wrap import roundf

if __name__ == "__main__":
    args = bsu.blender_script_args()
    print(args)

    # init
    bsu.set_blender_render_settings(x_res=int(args['x']), y_res=int(args['y']), file_format='JPEG')
    bpy.context.preferences.view.show_splash = False

    # delete default light
    object_to_delete = bpy.data.objects['Light']
    bpy.data.objects.remove(object_to_delete, do_unlink=True)

    bsu.new_light(args["li_name"], args["li_type"])

    light_data = bpy.data.lights.get(args["li_name"])
    assert light_data, f"The light object '{args['li_name']}' does not exist."
    assert light_data.type == args['li_type'], f"Actual: {light_data.type} Expected: {args['li_type']}"

    light_location = tuple(roundf(coord) for coord in bpy.data.objects.get(args["li_name"]).location)
    assert light_location == (0, 0, 0), f"Actual: {light_location} Expected: {(0, 0, 0)}"

    print(bpy.data.scenes[0].render.resolution_x)
    print(bpy.data.scenes[0].render.resolution_y)
    print(bpy.data.scenes[0].render.image_settings.file_format)

    bsu.render_image(path=args["rend_dest"])
    bsu.save_blend_file(path=args["out"])
