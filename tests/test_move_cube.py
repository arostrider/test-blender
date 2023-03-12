import time

import pytest

from environ import BLEND_OUT_DIR
from helpers.math_wrap import randec
from project import SCRIPTS


@pytest.mark.parametrize("new_location", [(0, 0, 0),
                                          (randec(), 0, 0),
                                          (0, randec(), 0),
                                          (0, 0, randec()),
                                          (randec(), randec(), 0),
                                          (randec(), 0, randec()),
                                          (0, randec(), randec()),
                                          (randec(), randec(), randec())
                                          ])
def test_move_cube(new_location, run_blender_script, parse_stdout):
    timestamp = time.time()
    run_blender_script(SCRIPTS / "move_cube.py",
                       script_args=['-x', 1922, '-y', 1081,
                                    '-out', BLEND_OUT_DIR / f'move_cube_{timestamp}.blend',
                                    '-rend_dest', BLEND_OUT_DIR / f'move_cube_{timestamp}.jpeg',
                                    new_location
                                    ])
    parse_stdout()
