import os
import subprocess
from pathlib import Path

import pytest
from dotenv import load_dotenv

load_dotenv()
BLENDER_EXE_PATH = Path(os.getenv("BLENDER_EXE_PATH"))


@pytest.fixture
def run_blender_script():
    def _run_blender_script(path: Path):
        return subprocess.run(["powershell", "-Command", f".'{BLENDER_EXE_PATH}' -P '{path}'"])

    return _run_blender_script
