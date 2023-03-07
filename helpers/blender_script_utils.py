import os
import sys
from pathlib import Path

import bpy


def blender_script_args() -> dict:
    # TODO: remove ability to read 'free_vals' args
    argv = sys.argv
    args = iter(sys.argv[argv.index("--") + 1:])

    args_dict = {"free_vals": []}

    while True:
        try:
            arg = next(args)
        except StopIteration:
            break

        if arg.startswith("-"):
            arg = arg.replace("-", "")
            args_dict.update({arg: next(args)})
        else:
            args_dict['free_vals'].append(arg)

    return args_dict


def set_blender_render_settings(x_res: int, y_res: float, file_format: str):
    for scene in bpy.data.scenes:
        scene.render.resolution_x = x_res
        scene.render.resolution_y = y_res
        scene.render.image_settings.file_format = file_format


def save_blend_file(path: str | Path):
    if os.path.isfile(path):
        raise FileExistsError(str(path))

    bpy.ops.wm.save_as_mainfile(filepath=str(path))


def add_cube(
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
def add_sphere(
        subdivisions: int = 4,
        radius: float = 1.0,
        location: list[float] = (0.0, 0.0, 0.0),
        rotation: list[float] = (0.0, 0.0, 0.0),
        scale: list[float] = (1.0, 1.0, 1.0)
) -> None:
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
def add_cone(
        vertices: int = 4,
        radius1: float = 1.0,
        radius2: float = 0.0,
        depth: float = 2.0,
        location: list[float] = (0.0, 0.0, 0.0),
        rotation: list[float] = (0.0, 0.0, 0.0),
        scale: list[float] = (1.0, 1.0, 1.0)
) -> None:
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


def new_material(material_id: str):
    mat = bpy.data.materials.get(material_id)

    if mat is None:
        mat = bpy.data.materials.new(name=material_id)

    mat.use_nodes = True

    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()

    return mat


def new_shader(material_id: str, type: str, r: float, g: float, b: float):
    mat = new_material(material_id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if type == "diffuse":
        shader = nodes.new(type='ShaderNodeBsdfDiffuse')
        nodes["Diffuse BSDF"].inputs[0].default_value = (r, g, b, 1)

    elif type == "emission":
        shader = nodes.new(type='ShaderNodeEmission')
        nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
        nodes["Emission"].inputs[1].default_value = 1

    elif type == "glossy":
        shader = nodes.new(type='ShaderNodeBsdfGlossy')
        nodes["Glossy BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glossy BSDF"].inputs[1].default_value = 0

    links.new(shader.outputs[0], output.inputs[0])

    return mat
