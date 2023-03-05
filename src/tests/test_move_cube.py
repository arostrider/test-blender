from project import SCRIPTS


def test_move_cube(run_blender_script):
    run_blender_script(SCRIPTS / "move_cube.py")


def test_move_cube_clone(run_blender_script):
    run_blender_script(SCRIPTS / "move_cube.py")
