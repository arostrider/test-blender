import bpy
import helpers.blender_script_utils as bsu
from helpers.math_wrap import roundf, randec
from random import randint, choice

if __name__ == "__main__":
    args = bsu.blender_script_args()
    print(args)

    # init
    bsu.set_blender_render_settings(x_res=int(args['x']), y_res=int(args['y']), file_format='JPEG')
    bpy.context.preferences.view.show_splash = False

    # delete default cube
    object_to_delete = bpy.data.objects['Cube']
    bpy.data.objects.remove(object_to_delete, do_unlink=True)

    # generate arbitrary shapes at a random positions (number of shapes from script args)
    number_of_shapes = int(args['free_vals'][0])
    for i in range(number_of_shapes):
        x, y, z = (roundf(randint(-10, 11) + randec()),
                   roundf(randint(-10, 11) + randec()),
                   roundf(randint(-10, 11) + randec()))

        add_arbitrary_shape = choice([bsu.add_cube, bsu.add_cone, bsu.add_sphere])
        add_arbitrary_shape(location=[x, y, z])

        # round coordinates of active object (should be new cube)
        # to avoid assertion error due to high precision difference
        active_object_location = tuple(roundf(coord) for coord in bpy.context.active_object.location)

        assert active_object_location == (x, y, z), f"Shape No: {i} " \
                                                    f"Actual: {active_object_location} Expected: {(x, y, z)}"

    print(bpy.data.scenes[0].render.resolution_x)
    print(bpy.data.scenes[0].render.resolution_y)
    print(bpy.data.scenes[0].render.image_settings.file_format)

    bsu.save_blend_file(path=args["out"])
