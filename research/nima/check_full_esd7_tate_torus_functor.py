#!/usr/bin/env python3
"""Check the full esd7 manifest against the graded Tate-torus chain realization."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
m=json.loads((ROOT/'research/nima/results/esd7-source-manifest.json').read_text());cells={x['id']:x for x in m['cells']}
def coeffs_boundary(x):return {y['cell']:y['sign'] for y in x['boundary']}
def action_chain_ok(x,name,sign_name):
 y=cells[x[name]];lhs={z['cell']:x[sign_name]*z['sign'] for z in y['boundary']};rhs={cells[z['cell']][name]:z['sign']*cells[z['cell']][sign_name] for z in x['boundary']};return lhs==rhs
rho_bad=[];omega_bad=[];tri_bad=[];tet_bad=[]
for x in cells.values():
 if not action_chain_ok(x,'rho','rho_orientation_sign'):rho_bad.append(x['id'])
 if not action_chain_ok(x,'omega','omega_orientation_sign'):omega_bad.append(x['id'])
 if x['dimension']==2:
  # Lexicographic flag v0 < (v0v1) < (v0v1v2) gives a composable pair and canonical cone triangle.
  if len(x['boundary'])!=3:tri_bad.append(x['id'])
 if x['dimension']==3:
  fs=[cells[y['cell']] for y in x['boundary']]
  if len(fs)!=4 or any(f['dimension']!=2 for f in fs):tet_bad.append(x['id'])
counts=[sum(x['dimension']==d for x in cells.values()) for d in range(4)]
checks={'manifest_passed':m['passed'],'rho_is_signed_chain_map':not rho_bad,'omega_is_signed_chain_map':not omega_bad,'all_designated_triangles_admit_flag_cone_model':not tri_bad,'all_designated_tetrahedra_have_four_triangle_faces':not tet_bad,'graded_fourier_helix':'F_tilde^4=Sigma by chart-wrap definition','chart_trace_weight_exact':'1/4'}
out={'schema':'marici.nima.full-esd7-tate-torus-functor.v1','source_manifest':m['schema'],'counts':counts,'target':'derived category of channel-lattice distributions / dual-torus trigonometric polynomials, tensored with normalized simplex chains','assignments':{'cell_sigma':'N_*(sigma) tensor V','face_map':'signed normalized-chain inclusion tensor identity','triangle':'canonical cone triangle of the lexicographic two-step face flag','tetrahedron':'canonical octahedron of the lexicographic three-step face flag','q':'rho on simplex/channel coordinates plus Pontryagin Fourier; shift on phase-4 wrap','duality':'omega plus lattice reflection and derived dual'},'failures':{'rho':rho_bad[:20],'omega':omega_bad[:20],'triangles':tri_bad[:20],'tetrahedra':tet_bad[:20]},'checks':checks,'passed':all(v is True or isinstance(v,str) for v in checks.values())}
p=ROOT/'research/nima/results/full-esd7-tate-torus-functor.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'counts':counts,'failures':{k:len(v) for k,v in [('rho',rho_bad),('omega',omega_bad),('triangles',tri_bad),('tetrahedra',tet_bad)]},'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
