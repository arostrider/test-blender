from project import SCRIPTS


def test_move_cube(run_blender_script, parse_stdout):
    run_blender_script(SCRIPTS / "move_cube.py")
    parse_stdout()


def test_move_cube_clone(run_blender_script, parse_stdout):
    run_blender_script(SCRIPTS / "move_cube.py")
    parse_stdout()
