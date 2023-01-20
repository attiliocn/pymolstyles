# pymolstyles_dir should be defined in .pymolrc file

if pymolstyles_dir:
    #External Scripts
    cmd.run(f"{pymolstyles_dir}/external/cgo_arrow.py")
    
    # PyMolStyles Scripts
    cmd.run(f"{pymolstyles_dir}/legacy/default.py")
    cmd.run(f"{pymolstyles_dir}/legacy/plot_sterimol.py")
    cmd.run(f"{pymolstyles_dir}/legacy/buried_volume.py")
else:
    raise
