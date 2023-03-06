import os
import sys
from pathlib import Path

import bpy


def blender_script_args() -> dict:
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
