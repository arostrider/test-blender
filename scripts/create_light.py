import bpy
import helpers.blender_script_utils as bsu

if __name__ == "__main__":
    args = bsu.blender_script_args()
    print(args)

    # init
    bsu.set_blender_render_settings(x_res=int(args['x']), y_res=int(args['y']), file_format='JPEG')
    bpy.context.preferences.view.show_splash = False

    # delete default light
    object_to_delete = bpy.data.objects['Light']
    bpy.data.objects.remove(object_to_delete, do_unlink=True)

    bsu.new_light("MyLight", "POINT")

    print(bpy.data.scenes[0].render.resolution_x)
    print(bpy.data.scenes[0].render.resolution_y)
    print(bpy.data.scenes[0].render.image_settings.file_format)

    bsu.render_image(path=args["rend_dest"])
    bsu.save_blend_file(path=args["out"])
