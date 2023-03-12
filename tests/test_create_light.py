import time
from random import choice

import pytest

from environ import BLEND_OUT_DIR
from helpers.math_wrap import randec
from project import SCRIPTS


@pytest.fixture(name="test_data_blend_file_path")
def generate_test_data(run_blender_script, parse_stdout) -> str:
    blend_file_path = BLEND_OUT_DIR / f'create_arbitrary_shapes_with_material_{time.time()}.blend'
    run_blender_script(SCRIPTS / "create_arbitrary_shapes.py",
                       script_args=['-x', 1922, '-y', 1081,
                                    '-n', 10,
                                    '-mat_name', 'Shader1',
                                    '-mat_type', choice(['diffuse', 'emission', 'glossy']),
                                    '-r', randec(),
                                    '-g', randec(),
                                    '-b', randec(),
                                    '-out', blend_file_path,
                                    '-rend_dest',
                                    BLEND_OUT_DIR / f'create_arbitrary_shapes_with_material_{time.time()}.jpeg'
                                    ])
    parse_stdout()
    return blend_file_path


def test_create_light(run_blender_script, parse_stdout, test_data_blend_file_path):
    timestamp = time.time()
    run_blender_script(SCRIPTS / "create_light.py",
                       blend_file_path=test_data_blend_file_path,
                       script_args=['-x', 1922, '-y', 1081,
                                    '-li_name', 'NewLight',
                                    '-li_type', 'SUN',
                                    '-out', BLEND_OUT_DIR / f'create_light_{timestamp}.blend',
                                    '-rend_dest', BLEND_OUT_DIR / f'create_light_{timestamp}.jpeg',
                                    ])
    parse_stdout()
