import json
from pathlib import Path

from five_site_g5_source_residue import CI,idot,sqrti,ivecadd,ivecscale

def unit_between(i,j):
    d=tuple(a-b for a,b in zip(CI[i],CI[j]))
    return ivecscale(sqrti(idot(d,d)).inv(),d)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

# Pair (g145,g23) shares boundary {e12,e34}; complement incidence plus
# q_e12 forces y34=0, hence l=C2. Test smooth Landau stationarity there.
n0=unit_between(2,0)
g5=ivecadd(unit_between(2,3),unit_between(2,4))
cr=cross(n0,g5);cross2=idot(cr,cr)
assert cross2.l>0

packet={
 'schema':'marici.five_site_g5_complement_pair_activation.v1',
 'pairs':[
  {'walls':['g_145','g_23'],'shared_boundary_edges':['e12','e34'],
   'forced_zero_distance':'y34=0','forced_loop_focus':'C2',
   'stationarity_cross_norm_squared_interval':[str(cross2.l),str(cross2.h)],
   'smooth_nonzero_multiplier_landau_solution':False,
   'classification':'excluded by exact nonparallel stationarity gradients'},
  {'walls':['g_15','g_234'],'shared_boundary_edges':['e12','e45'],
   'forced_zero_distance':'y45=0','forced_loop_focus':'C3',
   'zero_distance_is_defining_g5_boundary':True,
   'smooth_nonzero_multiplier_landau_solution':False,
   'classification':'existing defining-edge soft corner; ordinary gradient model invalid'}],
 'generic_higher_collision_survives':False,
 'remaining_supported_frontier':'resolved defining-edge soft corner for (g_15,g_234)',
}
Path('research/benincasa/results/five-site-g5-complement-pair-activation.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
