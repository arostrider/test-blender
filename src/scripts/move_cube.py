import bpy

bpy.context.preferences.view.show_splash = False

bpy.context.active_object.location = (1, 2, 3)

assert tuple(bpy.context.active_object.location) == (0, 0, 0), f"Actual: {tuple(bpy.context.active_object.location)} "\
                                                               f"Expected: (0, 0, 0)"
