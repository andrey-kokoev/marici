"""Universal directional-polynomial template for all degree-14 K-multiplication derivative rows."""
from __future__ import annotations
import json,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_derivative_template.json'
def point_add(p,d,s):return tuple(a+s*b for a,b in zip(p,d))
def derivative_K(point,direction):
 samples=[base.fiber_data(*point_add(point,direction,o))[0] for o in rees.OFFSETS]; weights=rees.interpolation_weights(1); out={}
 for poly,w in zip(samples,weights):
  for exp,a in poly.items():
   v=(out.get(exp,0)+w*a)%base.PRIME
   if v:out[exp]=v
   else:out.pop(exp,None)
 return out
def poly_sub(a,b):
 out=dict(a)
 for e,v in b.items():
  x=(out.get(e,0)-v)%base.PRIME
  if x:out[e]=x
  else:out.pop(e,None)
 return out
def main():
 assert rees.AMBIENT==14 and base.PRIME==32003
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); dirs={'nx':tuple(protocol['integral_unit_normals']['nx']),'ny':tuple(protocol['integral_unit_normals']['ny']),'p_tangent':tuple(protocol['integral_unit_normals']['p_tangent_difference'])}
 low,columns=rees.column_packet(); derivatives={name:derivative_K(point,d) for name,d in dirs.items()}; assert poly_sub(derivatives['nx'],derivatives['ny'])==derivatives['p_tangent']
 template_checks={}
 for name,direction in dirs.items():
  rows,checked=adapter.derivative_rows(columns,point,direction); Krows=rows[480:4704]; cursor=0; failures=0
  for kp in range(rees.charts.K_DEPTH):
   for levels in product(range(1,rees.charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
    for exp in base.monomials_at_most(rees.AMBIENT-4):
     expected={}
     for term,a in derivatives[name].items():
      col=columns[(kp+1,*levels,base.shifted(exp,term))]; rees.add(expected,col,-a)
     if Krows[cursor]!=expected:failures+=1
     cursor+=1
  assert cursor==4224 and failures==0
  template_checks[name]={'rows_checked':cursor,'failures':failures,'directional_K_derivative':{str(e):a for e,a in sorted(derivatives[name].items())},'term_count':len(derivatives[name])}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-derivative-template.v1','status':'all_K_multiplication_derivatives_are_monomial_shifts_of_one_directional_polynomial','field':base.PRIME,'ambient_relation_degree':14,'template_checks':template_checks,'linearity':'D_nx K - D_ny K = D_(nx-ny) K','constructor':'D_v(e-K e_plus) = -(D_v K)e_plus; multiply by each retained monomial and copy across pole/level blocks','decision':'The 4224 nonzero K-family derivative rows per direction collapse to one exact directional K polynomial template. Absorption into S+T remains to be explained, but source generation is now uniform.','limitations':['single prime verification','degree-14 retained monomial range','does not construct the S+T homotopy'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
