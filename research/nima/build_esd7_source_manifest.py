#!/usr/bin/env python3
"""Build a fully incident, rho/omega-equivariant esd_7(Delta^3) source manifest."""
import json
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'research/voevodsky/results/esd7_explicit_analytical_census.json'
if not src.exists():raise SystemExit(f'run check_esd7_explicit_analytical_census.py first: {src}')
data=json.loads(src.read_text())
def tup(x):return tuple(x)
def bary(z):return (z[0],z[1]-z[0],z[2]-z[1],7-z[2])
def cumulative(a):return (a[0],a[0]+a[1],a[0]+a[1]+a[2])
def rho(z):
 a=bary(z);return cumulative((a[3],a[0],a[1],a[2]))
def omega(z):return cumulative(tuple(reversed(bary(z))))
def parity(xs):
 inv=sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)));return -1 if inv%2 else 1
bydim=[]
for key in ('vertices','edges','triangles','tetrahedra'):
 rows=data[key]; cells=[]
 for r in rows:
  if key=='vertices':vs=(tup(r['cumulative']),)
  else:
   lookup={x['id']:tup(x['cumulative']) for x in data['vertices']}
   vs=tuple(sorted(lookup[x] for x in r['vertices']))
  cells.append((r['id'],vs))
 bydim.append(cells)
lookup=[{vs:i for i,vs in cells} for cells in bydim]
idlookup=[{vs:id for id,vs in cells} for cells in bydim]
def action(vs,f):return tuple(sorted(f(v) for v in vs))
def action_sign(vs,f):
 raw=[f(v) for v in vs];ordered=sorted(raw);return parity([ordered.index(x) for x in raw])
manifest=[]
for dim,cells in enumerate(bydim):
 for id,vs in cells:
  boundaries=[]
  if dim:
   for i in range(dim+1):
    face=vs[:i]+vs[i+1:];boundaries.append({'cell':idlookup[dim-1][face],'sign':-1 if i%2 else 1})
  manifest.append({'id':id,'dimension':dim,'vertices':[list(v) for v in vs],'barycentric_vertices':[list(bary(v)) for v in vs],'boundary':boundaries,'rho':idlookup[dim][action(vs,rho)],'rho_orientation_sign':action_sign(vs,rho),'omega':idlookup[dim][action(vs,omega)],'omega_orientation_sign':action_sign(vs,omega)})
# Closure and action checks.
cellby={x['id']:x for x in manifest};checks={
'f_vector':[sum(x['dimension']==d for x in manifest) for d in range(4)]==[120,560,784,343],
'all_boundaries_resolve':all(all(y['cell'] in cellby for y in x['boundary']) for x in manifest),
'rho_fourth_power_identity':all(cellby[cellby[cellby[cellby[x['rho']]['rho']]['rho']]['rho']]['id']==x['id'] for x in manifest),
'omega_square_identity':all(cellby[cellby[x['omega']]['omega']]['id']==x['id'] for x in manifest),
'boundary_squared_zero':True,
}
for x in manifest:
 if x['dimension']>=2:
  coeff={}
  for f in x['boundary']:
   for g in cellby[f['cell']]['boundary']:coeff[g['cell']]=coeff.get(g['cell'],0)+f['sign']*g['sign']
  if any(coeff.values()):checks['boundary_squared_zero']=False
out={'schema':'marici.nima.esd7-source-manifest.v1','complex':'esd_7(Delta^3)','orientation':'lexicographic cumulative-coordinate vertex order; simplicial boundary sign (-1)^i','rho':'barycentric cyclic rotation (a1,a2,a3,a4)->(a4,a1,a2,a3)','omega':'barycentric reversal','designation_profile':{'quotient_triangles':'all 784 oriented 2-simplices','octahedral_tetrahedra':'all 343 oriented 3-simplices','zero_vertices':[],'warning':'All-cells designation and empty zero set are an explicit realization profile; replace if the universal source intends a smaller named subset.'},'checks':checks,'passed':all(checks.values()),'cells':manifest}
p=ROOT/'research/nima/results/esd7-source-manifest.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'cells':len(manifest),'counts':[sum(x['dimension']==d for x in manifest) for d in range(4)],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
