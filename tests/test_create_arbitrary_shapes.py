import time

import pytest

from environ import BLEND_OUT_DIR
from project import SCRIPTS
from helpers.math_wrap import randec
from random import choice


@pytest.mark.parametrize("number_of_shapes", [i for i in range(10)])
def test_create_arbitrary_shapes(number_of_shapes, run_blender_script, parse_stdout):
    timestamp = time.time()
    run_blender_script(SCRIPTS / "create_arbitrary_shapes.py",
                       script_args=['-x', 1922, '-y', 1081,
                                    '-n', number_of_shapes,
                                    '-out', BLEND_OUT_DIR / f'create_arbitrary_shapes_{timestamp}.blend',
                                    '-rend_dest', BLEND_OUT_DIR / f'create_arbitrary_shapes_{timestamp}.jpeg'
                                    ])
    parse_stdout()


@pytest.mark.parametrize("number_of_shapes", [i for i in range(10)])
def test_create_arbitrary_shapes_with_material(number_of_shapes, run_blender_script, parse_stdout):
    timestamp = time.time()
    run_blender_script(SCRIPTS / "create_arbitrary_shapes.py",
                       script_args=['-x', 1922, '-y', 1081,
                                    '-n', number_of_shapes,
                                    '-mat_name', 'Shader1',
                                    '-mat_type', choice(['diffuse', 'emission', 'glossy']),
                                    '-r', randec(),
                                    '-g', randec(),
                                    '-b', randec(),
                                    '-out',
                                    BLEND_OUT_DIR / f'create_arbitrary_shapes_with_material_{timestamp}.blend',
                                    '-rend_dest',
                                    BLEND_OUT_DIR / f'create_arbitrary_shapes_with_material_{timestamp}.jpeg'
                                    ])
    parse_stdout()
