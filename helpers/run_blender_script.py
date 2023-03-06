import subprocess
from collections.abc import Iterable
from io import TextIOWrapper
from pathlib import Path


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
