from pymol import cmd

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