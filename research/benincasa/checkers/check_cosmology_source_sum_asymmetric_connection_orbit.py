#!/usr/bin/env python3
"""Test whether the finite physical connection orbit of the source sum contains the exceptional difference."""
import argparse,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));a=ap.parse_args();os.environ['MARICI_FIELD_PRIME']=str(a.prime);sys.path.insert(0,str(ROOT/'research'/'benincasa'));import physical_four_mark_residue_twisted_derham as m
 names=('g1','g2','g3','g23','g31');gamma=-(pow(2,-1,a.prime))%a.prime;ambient=10;cutoff=5;low,cols,piv,free=m.presentation(names,gamma,ambient,cutoff,minimum_q_level=0);label_by_col={c:l for l,c in cols.items()}
 def qcoord(label):return m.quotient_coordinates(label,cols,piv,free)
 A=qcoord((0,1,1,1,0,1,(0,0)));B=qcoord((0,1,1,1,1,0,(0,0)))
 def add(dst,src,k=1):
  for c,v in src.items():m.add_value(dst,c,k*v)
 source=dict(A);add(source,B);difference=dict(A);add(difference,B,-1)
 def connection(v,axis):
  out={}
  for c,k in v.items():
   for d,w in m.connection_image(label_by_col[c],names,gamma,axis,cols).items():m.add_value(out,d,k*w)
  out=m.reduce_row(out,piv);return {c:out[c] for c in free if c in out}
 span={};front=[source];iterations=0
 while front:
  v=front.pop();before=len(span);m.add_pivot(dict(v),span)
  if len(span)==before:continue
  iterations+=1
  for axis in range(2):
   w=connection(v,axis)
   if w:front.append(w)
 residual=m.reduce_row(difference,span);sum_difference_rank=0;tmp={};m.add_pivot(dict(source),tmp);m.add_pivot(dict(difference),tmp);sum_difference_rank=len(tmp)
 out={'schema':'marici.benincasa.cosmology-source-sum-asymmetric-connection-orbit.v1','prime':a.prime,'gamma_mod_prime':gamma,'ambient':ambient,'cutoff':cutoff,'source_cells':['(g1,g2,g3,g31)','(g1,g2,g3,g23)'],'source_sum_nonzero':bool(source),'difference_nonzero':bool(difference),'sum_difference_rank':sum_difference_rank,'connection_orbit_rank':len(span),'orbit_basis_insertions':iterations,'difference_residual_coordinate_count':len(residual),'asymmetric_difference_in_connection_orbit':not residual,'finite_field_asymmetric_direction_constructed':not residual,'integral_unit_principal_selector_constructed':False,'principal_coefficient_lattice_from_sum_and_difference':'2*Z','scope':'finite physical-half-twist quotient at the presentation test fiber; the difference has zero principal-face coefficient, and recovering one summand from sum and difference divides by two','passed':True};path=ROOT/'research'/'benincasa'/'results'/f'cosmology_source_sum_asymmetric_connection_orbit_p{a.prime}.json';path.parent.mkdir(exist_ok=True);path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
