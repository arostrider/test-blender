import time
from random import random

import pytest

from helpers.math_wrap import roundf
from project import SCRIPTS
from environ import BLEND_OUT_DIR


def randec() -> float:
    return roundf(random())


@pytest.mark.parametrize("coordinates", [(0, 0, 0),
                                         (randec(), 0, 0),
                                         (0, randec(), 0),
                                         (0, 0, randec()),
                                         (randec(), randec(), 0),
                                         (randec(), 0, randec()),
                                         (0, randec(), randec()),
                                         (randec(), randec(), randec())
                                         ])
def test_create_arbitrary_shapes(coordinates, run_blender_script, parse_stdout):
    run_blender_script(SCRIPTS / "create_arbitrary_shapes.py",
                       script_args=['-x', 1922, '-y', 1081,
                                    '-out', BLEND_OUT_DIR / f'create_arbitrary_shapes_{time.time()}.blend',
                                    coordinates])
    parse_stdout()
