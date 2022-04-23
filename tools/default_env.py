from pymol import cmd, util 

cmd.set("internal_gui_width", 400)
cmd.bg_color("white")

cmd.set("ray_trace_mode", 1)
cmd.set("ray_texture", 0)
cmd.set("ray_opaque_background", "off")

cmd.set('dash_color', 'gray')
cmd.set("dash_gap",0.15)
cmd.set("dash_radius",0.035)

cmd.space("cmyk")

cmd.set('label_color', 'yellow')
cmd.set('label_outline_color', 'black')
cmd.set('label_font_id', 7)
cmd.set('label_size', 30)

def set_enviroment_settings(arg1):
	cmd.set("ambient", 0.4) #amount of ambient light
	cmd.set("shininess", 25) #how much the object shines <the greater it becames opaque>
	cmd.set("reflect", 0.05) #amount of light reflection
	cmd.set("orthoscopic", 0)
	cmd.set("transparency", 0.5)
	cmd.set("antialias", 3)
	cmd.set("spec_count", 5)
	cmd.set("specular", 1.5)

def set_default_atom_colors(arg1):
    util.cbaw(arg1)
    cmd.color("gray35", f"elem C and {arg1}")
    cmd.color("gray95", f"elem H and {arg1}")
    cmd.color("br9", f"elem 0 and {arg1}")
    cmd.color("br0", f"elem N and {arg1}")

    cmd.set('stick_transparency', 0, arg1)
    cmd.set('stick_color', 'default', arg1)
    cmd.set('sphere_transparency', 0, arg1)