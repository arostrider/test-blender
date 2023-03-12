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
    number_of_shapes = int(args['n'])
    for i in range(number_of_shapes):
        x, y, z = (roundf(randint(-10, 11) + randec()),
                   roundf(randint(-10, 11) + randec()),
                   roundf(randint(-10, 11) + randec()))

        add_arbitrary_shape = choice([bsu.draw_cube, bsu.draw_cone, bsu.draw_sphere])
        add_arbitrary_shape(location=[x, y, z])

        # round coordinates of active object (should be new cube)
        # to avoid assertion error due to high precision difference
        active_object_location = tuple(roundf(coord) for coord in bpy.context.active_object.location)

        assert active_object_location == (x, y, z), f"Shape No: {i} " \
                                                    f"Actual: {active_object_location} Expected: {(x, y, z)}"

        # add material to shape if appropriate material arguments in cli are passed
        # else, skip the code below the except block
        try:
            material = bsu.new_material(material_id=args['mat_name'])
            bsu.add_shader_to_material(material,
                                       material_type=args['mat_type'],
                                       r=float(args['r']),
                                       g=float(args['g']),
                                       b=float(args['b']))
        except KeyError as ex:
            print(f"No or incorrect material argument passed from command line: {ex}")
            continue

        # add material
        bpy.context.active_object.data.materials.append(material)

        # extract actual and expected values for the assertion
        active_object_material = bpy.context.active_object.material_slots[0].material
        material_generated_from_cli_args = bpy.data.materials[args['mat_name']]

        # TODO: maybe better assertions (cmdline args values in expected) ?
        assert active_object_material.name == material_generated_from_cli_args.name, \
            f"Shape No: {i} " \
            f"Actual: {active_object_material.name} " \
            f"Expected: {material_generated_from_cli_args.name}"

        assert active_object_material.diffuse_color == material_generated_from_cli_args.diffuse_color, \
            f"Shape No: {i} " \
            f"Actual: {active_object_material.diffuse_color} " \
            f"Expected: {material_generated_from_cli_args.diffuse_color}"

    print(bpy.data.scenes[0].render.resolution_x)
    print(bpy.data.scenes[0].render.resolution_y)
    print(bpy.data.scenes[0].render.image_settings.file_format)

    bsu.render_image(path=args["rend_dest"])
    bsu.save_blend_file(path=args["out"])
