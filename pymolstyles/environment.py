from pymol import util

def default_env(arg1):
	cmd.set("ambient", 0.4) #amount of ambient light
	cmd.set("shininess", 25) #how much the object shines <the greater it becames opaque>
	cmd.set("reflect", 0.05) #amount of light reflection
	cmd.set("orthoscopic", 0)
	cmd.set("transparency", 0.5)
	cmd.set("antialias", 3)
	cmd.set("spec_count", 5)
	cmd.set("specular", 1.5)

def default_colors(arg1):
    util.cbaw(arg1)
    cmd.color("gray35", f"elem C and {arg1}")
    cmd.color("gray95", f"elem H and {arg1}")
    cmd.color("br9", f"elem 0 and {arg1}")
    cmd.color("br0", f"elem N and {arg1}")

    cmd.set('stick_transparency', 0, arg1)
    cmd.set('stick_color', 'default', arg1)
    cmd.set('sphere_transparency', 0, arg1)