import time

import pytest

from environ import BLEND_OUT_DIR
from project import SCRIPTS


@pytest.mark.parametrize("number_of_shapes", [i for i in range(10)])
def test_create_arbitrary_shapes(number_of_shapes, run_blender_script, parse_stdout):
    run_blender_script(SCRIPTS / "create_arbitrary_shapes.py",
                       script_args=['-x', 1922, '-y', 1081,
                                    '-out', BLEND_OUT_DIR / f'create_arbitrary_shapes_{time.time()}.blend',
                                    number_of_shapes])
    parse_stdout()
