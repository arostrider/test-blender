import os
import sys
from pathlib import Path

import bpy


def blender_script_args() -> dict:
    # TODO: remove ability to read 'free_vals' args
    argv = sys.argv
    args = iter(sys.argv[argv.index("--") + 1:])

    args_dict = {}

    while True:
        try:
            arg = next(args)
        except StopIteration:
            break

        if arg.startswith("-"):
            arg = arg.replace("-", "")
            args_dict.update({arg: next(args)})
        else:
            try:
                args_dict['free_vals'].append(arg)
            except KeyError:
                args_dict.update({'free_vals': [arg]})

    return args_dict


def set_blender_render_settings(x_res: int, y_res: float, file_format: str) -> None:
    for scene in bpy.data.scenes:
        scene.render.resolution_x = x_res
        scene.render.resolution_y = y_res
        scene.render.image_settings.file_format = file_format


def save_blend_file(path: str | Path) -> None:
    if os.path.isfile(path):
        raise FileExistsError(str(path))

    bpy.ops.wm.save_as_mainfile(filepath=str(path))


def draw_cube(
        size: float = 1.0,
        location: list[float] = (0.0, 0.0, 0.0),
        rotation: list[float] = (0.0, 0.0, 0.0),
        scale: list[float] = (2.0, 2.0, 2.0)) -> None:
    bpy.ops.mesh.primitive_cube_add(
        size=size,
        calc_uvs=True,
        enter_editmode=False,
        align='WORLD',
        location=location,
        rotation=rotation,
        scale=scale,
    )


# docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_ico_sphere_add
def draw_sphere(
        subdivisions: int = 4,
        radius: float = 1.0,
        location: list[float] = (0.0, 0.0, 0.0),
        rotation: list[float] = (0.0, 0.0, 0.0),
        scale: list[float] = (1.0, 1.0, 1.0)) -> None:
    bpy.ops.mesh.primitive_ico_sphere_add(
        subdivisions=subdivisions,
        radius=radius,
        calc_uvs=True,
        enter_editmode=False,
        align='WORLD',
        location=location,
        rotation=rotation,
        scale=scale
    )


# docs: https://docs.blender.org/api/current/bpy.ops.mesh.html#bpy.ops.mesh.primitive_cone_add
def draw_cone(
        vertices: int = 4,
        radius1: float = 1.0,
        radius2: float = 0.0,
        depth: float = 2.0,
        location: list[float] = (0.0, 0.0, 0.0),
        rotation: list[float] = (0.0, 0.0, 0.0),
        scale: list[float] = (1.0, 1.0, 1.0)) -> None:
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius1,
        radius2=radius2,
        depth=depth,
        end_fill_type='NGON',
        calc_uvs=True,
        enter_editmode=False,
        align='WORLD',
        location=location,
        rotation=rotation,
        scale=scale
    )


def new_material(material_id: str) -> bpy.types.Material:
    material = bpy.data.materials.get(material_id)

    if material is None:
        material = bpy.data.materials.new(name=material_id)

    material.use_nodes = True

    if material.node_tree:
        material.node_tree.links.clear()
        material.node_tree.nodes.clear()

    return material


def add_shader_to_material(material: bpy.types.Material,
                           material_type: str,
                           r: float,
                           g: float,
                           b: float) -> None:
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if material_type == "diffuse":
        shader = nodes.new(type='ShaderNodeBsdfDiffuse')
        nodes["Diffuse BSDF"].inputs[0].default_value = (r, g, b, 1)

    elif material_type == "emission":
        shader = nodes.new(type='ShaderNodeEmission')
        nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
        nodes["Emission"].inputs[1].default_value = 1

    elif material_type == "glossy":
        shader = nodes.new(type='ShaderNodeBsdfGlossy')
        nodes["Glossy BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glossy BSDF"].inputs[1].default_value = 0

    else:
        raise ValueError(f"Invalid material_type arg value: '{material_type}'. "
                         f"Valid values: 'diffuse', 'emission', 'glossy'")

    links.new(shader.outputs[0], output.inputs[0])


def new_light(light_id: str, light_type: str) -> None:
    light_type = light_type.upper()
    data = bpy.data.lights.new(light_id, type=light_type)
    obj = bpy.data.objects.new(light_id, data)
    bpy.context.collection.objects.link(obj)


def render_image(path: Path) -> None:
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
