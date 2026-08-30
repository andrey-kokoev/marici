import contextlib,io,json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
 from five_site_g5_source_residue import CI,L0,NN,HH,ivecadd,ivecscale,idot,sqrti,I

records=[]
for sheet in (-1,1):
 l=ivecadd(L0,ivecscale(sheet*HH,NN))
 units=[]
 for c in CI:
  d=tuple(a-b for a,b in zip(l,c));units.append(ivecscale(sqrti(idot(d,d)).inv(),d))
 grad_q=ivecscale(I(2),units[0])
 grad_g=ivecadd(units[3],units[4])
 cross=(grad_q[1]*grad_g[2]-grad_q[2]*grad_g[1],grad_q[2]*grad_g[0]-grad_q[0]*grad_g[2],grad_q[0]*grad_g[1]-grad_q[1]*grad_g[0])
 n2=idot(cross,cross);assert n2.l>0
 tang=ivecadd(grad_g,ivecscale(-idot(grad_g,units[0]),units[0]));tn2=idot(tang,tang);assert tn2.l>0
 records.append({'sheet':sheet,'cross_norm_squared_interval':[str(n2.l),str(n2.h)],
  'g5_tangent_gradient_norm_squared_interval':[str(tn2.l),str(tn2.h)],
  'physical_landau_gradient_dependence':False})
packet={'schema':'marici.five_site_g5_physical_gradient_obstruction.v1','records':records,
 'all_reflected_points_fail_physical_gradient_dependence':True,
 'distance_space_landau_candidate_survives':True,
 'physical_d3_loop_pinch':False,
 'classification':'Cayley-Menger/distance-space Landau candidate without critical pullback to the physical d3 loop current'}
Path('research/benincasa/results/five-site-g5-physical-gradient-obstruction.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
