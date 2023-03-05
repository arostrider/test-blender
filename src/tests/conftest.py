from collections.abc import Callable
from io import TextIOWrapper
from typing import Type

import pytest

from helpers import run_blender_script as __run_blender_script


def pytest_addoption(parser):
    parser.addoption("--blender-exe-path",
                     action="store",
                     help="Path to Blender executable.")

    parser.addoption("--no-headless",
                     action="store_true",
                     default=False,
                     help="Run Blender in no-headless mode. If not passed, Blender will run headless.")


@pytest.fixture
def blender_exe_path(request) -> str:
    return request.config.getoption("--blender-exe-path")


@pytest.fixture
def headless(request) -> bool:
    return not request.config.getoption("--no-headless")


class ScriptStdoutContainer:
    latest_stdout: TextIOWrapper = None


@pytest.fixture
def script_stdout_container() -> Type[ScriptStdoutContainer]:
    return ScriptStdoutContainer


@pytest.fixture
def run_blender_script(blender_exe_path: str,
                       headless: bool,
                       script_stdout_container: ScriptStdoutContainer) -> Callable:
    """
    Factory as fixture providing access to helpers.run_blender_script function.
    Overrides blender_exe_path and headless params according to pytest cmd line args.
    Stores Blender stdout at script_stdout_container.latest_stdout.
    """

    def _run_blender_script(*args, **kwargs):
        script_stdout_container.latest_stdout = __run_blender_script(blender_exe_path, *args,
                                                                     headless=headless, **kwargs)

    return _run_blender_script


@pytest.fixture
def parse_stdout(script_stdout_container):
    def _parse_stdout():
        print("\n")
        for line in script_stdout_container.latest_stdout:
            print(line, end="")
            if "AssertionError" in line:
                pytest.fail(line)

    return _parse_stdout
