import os
import subprocess
import sys
from collections.abc import Iterable
from io import TextIOWrapper
from pathlib import Path

import bpy


def run_blender_script(blender_exe_path: str | Path,
                       script_path: str | Path,
                       script_args: Iterable = None,
                       *,
                       headless: bool) -> TextIOWrapper:
    """
    Run script and save its output to ScriptStdoutContainer.latest_stdout.

    :param blender_exe_path: path to Blender executable
    :param script_path: path to Blender python script
    :param script_args: arguments that should be passed to Blender python scrip
    :param headless: flag indicating if Blender should run in headless mode
    :return: iterator wrapping standard output of the executed Blender process
    """
    program: str = "powershell"

    program_args: str = f".'{blender_exe_path}' " \
                        f"{'-b' if headless else ''} " \
                        f"-P '{script_path}'" \
                        f"-- {' '.join(str(arg) for arg in script_args) if script_args else ''}"

    proc = subprocess.Popen([program, program_args], stdout=subprocess.PIPE)

    # saves process standard output at shared container defined in conftest, overwriting previous value
    return TextIOWrapper(proc.stdout, encoding="utf-8")


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
