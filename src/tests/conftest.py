import subprocess
from pathlib import Path

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


@pytest.fixture
def run_blender_script(blender_exe_path: str):
    def _run_blender_script(path: Path):
        return subprocess.run(["powershell", "-Command",
                               f".'{blender_exe_path}' -b -P '{path}'"])

    return _run_blender_script
