
def show_buried_volume(bv_name, color='lightblue', radius=3.5):
    '''
    USAGE
        buriedvolume bv_name, color='lightblue', radius=3.5)
    '''
    cmd.pseudoatom(bv_name, selection='sele', vdw=radius)
    cmd.hide('wire', bv_name)
    cmd.show('spheres', bv_name)
    cmd.set('sphere_transparency', 0.5, bv_name, )
    cmd.color(color, bv_name)
cmd.extend('buriedvolume', show_buried_volume)