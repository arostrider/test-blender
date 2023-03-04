import subprocess
from pathlib import Path

import pytest

BLENDER_EXE_PATH = Path(r"C:\Program Files\Blender Foundation\Blender 3.3\Blender.exe")


@pytest.fixture(scope="session", autouse=True)
def run_blender():
    subprocess.run(["powershell", "-Command", f".'{BLENDER_EXE_PATH}'"])
