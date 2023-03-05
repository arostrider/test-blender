from project import SCRIPTS


def test_move_cube(run_blender_script, parse_stdout):
    run_blender_script(SCRIPTS / "move_cube.py", [1, "sss", 1])
    parse_stdout()
