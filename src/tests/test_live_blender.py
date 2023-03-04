from src.blender_services.client import send_commands
from src.project import ROOT, SCRIPTS
from time import sleep


def test_live_blender(run_blender_script):
    run_blender_script(ROOT / "blender_services" / "server.py")
    sleep(5)
    send_commands([SCRIPTS / "move_cube.py"])
