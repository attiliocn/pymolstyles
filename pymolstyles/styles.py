def houkmol(arg1='all'):
    ball_and_stick(arg1)
    default_env(arg1)
    
    cmd.color("gray70", f"elem C and {arg1}")
    cmd.color("red", f"elem O and {arg1}")
    cmd.color("tv_blue", f"elem N and {arg1}")
    
    cmd.set("stick_color",'black', arg1)
    cmd.set("stick_radius",0.1, arg1)
    cmd.set("stick_h_scale",1.0, arg1) 
    
    cmd.set('sphere_scale',0.20, arg1)
    cmd.set('sphere_scale',0.15, f'elem H and {arg1}')
    
    cmd.set("shininess", 100)
    cmd.set("ambient", 0.6)

def fatball(arg1='all'):
    default_colors(arg1)
    default_env(arg1)
    cmd.show("sticks", arg1)
    cmd.show("spheres", arg1)
    cmd.hide("nonbonded", arg1)
    cmd.hide("lines", arg1)
    cmd.hide("labels")

    cmd.set("stick_radius",0.2, arg1)
    cmd.set("stick_h_scale",1.0, arg1) 
    cmd.set("sphere_scale",0.25, arg1)
    cmd.set("sphere_scale",0.25, 'elem H')