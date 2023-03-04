import subprocess
from pathlib import Path

import pytest

BLENDER_EXE_PATH = Path(r"C:\Program Files\Blender Foundation\Blender 3.3\Blender.exe")


@pytest.fixture
def run_blender_script():
    def _run_blender_script(path: Path):
        return subprocess.run(["powershell", "-Command", f".'{BLENDER_EXE_PATH}' -P '{path}'"])

    return _run_blender_script
