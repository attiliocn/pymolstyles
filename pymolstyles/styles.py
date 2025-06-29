from pymol import cmd
from pymolstyles.environment import default_environment, default_atoms_preset
from pymolstyles.tools import get_visible_entries

# GLOBAL SETTINGS

# Dash settings
cmd.set('dash_color', 'gray')
cmd.set("dash_gap",0.15)
cmd.set("dash_radius",0.035)

# Label settings
cmd.set('label_color', 'yellow')
cmd.set('label_outline_color', 'black')
cmd.set('label_font_id', 7)
cmd.set('label_size', 10)

def ball_stick_preset(arg1):
    default_atoms_preset(arg1)
    default_environment(arg1)
    cmd.show("sticks", arg1)
    cmd.show("spheres", arg1)
    cmd.hide("nonbonded", arg1)
    cmd.hide("lines", arg1)
    cmd.hide("labels")

def houkmol():
    for entry in get_visible_entries():
        ball_stick_preset(entry)
        default_environment(entry)
        
        cmd.color("gray70", f"elem C and {entry}")
        cmd.color("red", f"elem O and {entry}")
        cmd.color("tv_blue", f"elem N and {entry}")
        
        cmd.set("stick_color",'black', entry)
        cmd.set("stick_radius",0.1, entry)
        cmd.set("stick_h_scale",1.0, entry) 
        
        cmd.set('sphere_scale',0.20, entry)
        cmd.set('sphere_scale',0.15, f'elem H and {entry}')
        
        cmd.set("shininess", 100)
        cmd.set("ambient", 0.6)
cmd.extend("houkmol", houkmol)

def fatball(arg1='all'):
    ball_stick_preset(arg1)
    cmd.set("stick_radius",0.2, arg1)
    cmd.set("stick_h_scale",1.0, arg1) 
    cmd.set("sphere_scale",0.25, arg1)
    cmd.set("sphere_scale",0.25, 'elem H')
cmd.extend("fatball", fatball)

def flat(arg1='all'):
    ball_stick_preset(arg1)
    default_environment(arg1)