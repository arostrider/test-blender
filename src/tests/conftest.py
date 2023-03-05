import io
import subprocess
from pathlib import Path
from typing import Type

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--blender-exe-path",
        action="store",
        help="Path to Blender executable."
    )


@pytest.fixture
def blender_exe_path(request) -> str:
    return request.config.getoption("--blender-exe-path")


class ScriptStdoutContainer:
    latest_stdout: io.TextIOWrapper = None


@pytest.fixture
def script_stdout_container() -> Type[ScriptStdoutContainer]:
    return ScriptStdoutContainer


@pytest.fixture
def run_blender_script(blender_exe_path: str, script_stdout_container):

    def _run_blender_script(path: str | Path, headless: bool = True):
        """
        Run script and save its output to ScriptStdoutContainer.latest_stdout
        The equivalent of running the script without saving stdout would be:
        return subprocess.run(["powershell", "-Command",
                                [f".'{blender_exe_path}' "
                                f"{'-b' if headless else ''} "
                                f"-P '{path}'"]
                                "])

        :param path: path to blender python script
        :param headless: flag indicating if Blender should run in headless mode
        :return: None
        """
        program: str = "powershell"

        program_args: list[str] = [f".'{blender_exe_path}' "
                                   f"{'-b' if headless else ''} "
                                   f"-P '{path}'"]

        program_args: str = " ".join(program_args)

        proc = subprocess.Popen([program, program_args], stdout=subprocess.PIPE)

        script_stdout_container.latest_stdout = io.TextIOWrapper(proc.stdout, encoding="utf-8")

    return _run_blender_script


@pytest.fixture(autouse=True)
def parse_stdout(script_stdout_container):
    yield
    print("\n")
    for line in script_stdout_container.latest_stdout:
        print(line, end="")
        if "AssertionError" in line:
            pytest.fail(line)
