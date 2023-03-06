from random import random

import pytest

from helpers import roundf
from project import SCRIPTS


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
def test_move_cube(coordinates, run_blender_script, parse_stdout):
    run_blender_script(SCRIPTS / "move_cube.py", coordinates)
    parse_stdout()
