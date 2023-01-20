# pymolstyles_dir should be defined in .pymolrc file

import os

if pymolstyles_dir:
    #External Scripts
    cmd.run(os.path.join(f"{pymolstyles_dir}", 'external', 'cgo_arrow.py'))
    # PyMolStyles Scripts
    cmd.run(os.path.join(f"{pymolstyles_dir}", 'legacy', 'default.py'))
    cmd.run(os.path.join(f"{pymolstyles_dir}", 'legacy', 'plot_sterimol.py'))
    cmd.run(os.path.join(f"{pymolstyles_dir}", 'legacy', 'buried_volume.py'))
else:
    raise
