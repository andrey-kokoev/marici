"""Test directional K polynomials against bounded polynomial spans of K and its integration-variable derivatives."""
from __future__ import annotations
import json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_K_derivative_template as kt
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_jacobian_span.json'; P=base.PRIME
def deriv(poly,axis):
 out={}
 for e,a in poly.items():
  if e[axis]:
   f=list(e); c=f[axis]; f[axis]-=1; out[tuple(f)]=a*c%P
 return out
def shift(poly,m):return {(e[0]+m[0],e[1]+m[1]):a for e,a in poly.items()}
def reduce_add(row,pivots,tag=None):
 row=dict(row); combo={} if tag is not None else None
 if tag is not None:combo[tag]=1
 while row:
  p=max(row)
  if p not in pivots:
   a=row[p]; inv=pow(a,P-2,P); nr={e:v*inv%P for e,v in row.items()}; nc={k:v*inv%P for k,v in combo.items()} if combo is not None else None; pivots[p]=(nr,nc); return False,None
  a=row[p]; pr,pc=pivots[p]
  for e,v in pr.items():base.add_value(row,e,-a*v)
  if combo is not None:
   for k,v in pc.items():base.add_value(combo,k,-a*v)
 return True,combo
def main():
 assert rees.AMBIENT==14 and P==32003
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); dirs={'nx':tuple(protocol['integral_unit_normals']['nx']),'ny':tuple(protocol['integral_unit_normals']['ny']),'p_tangent':tuple(protocol['integral_unit_normals']['p_tangent_difference'])}
 K=base.fiber_data(*point)[0]; gens={'K':K,'dK_du':deriv(K,0),'dK_dv':deriv(K,1)}; maxdeg=max(sum(e) for e in K); multipliers=[(i,d-i) for d in range(0,7) for i in range(d+1)]
 generator_rows=[]
 for name,g in gens.items():
  for m in multipliers:
   tag=f'{name}*u^{m[0]}v^{m[1]}'; generator_rows.append((shift(g,m),tag))
 tests={}
 for name,d in dirs.items():
  pivots={}
  for row,tag in generator_rows:reduce_add(row,pivots,tag)
  target=kt.derivative_K(point,d); member,certificate=reduce_add(target,pivots,'TARGET')
  if member:certificate.pop('TARGET',None)
  tests[name]={'member':member,'target_terms':len(target),'certificate_nonzero_terms':len(certificate or {}),'certificate':certificate}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-jacobian-span.v1','status':'directional_K_polynomial_membership_tested','field':P,'generators':['K','dK_du','dK_dv'],'multiplier_degree_bound':6,'tests':tests,'all_members':all(x['member'] for x in tests.values()),'decision':'Directional K derivatives lie in the bounded Jacobian span.' if all(x['member'] for x in tests.values()) else 'The bounded K/Jacobian span does not contain every directional K derivative; a marked-q or full source-complex mechanism is required.','limitations':['finite-field test','multiplier degree bounded by 6','polynomial membership alone does not verify source-row truncation compatibility'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
