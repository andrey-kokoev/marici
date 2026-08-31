#!/usr/bin/env python3
"""Verify the source principal-three-wall identity for p=x+y+3z."""
import json,sys
from math import gcd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research'/'benincasa'))
import physical_four_mark_residue_twisted_derham as base
OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_principal_three_wall_p_identity.json';P=base.PRIME
def combine(terms):
 out={}
 for k,row in terms:
  for e,v in row.items():
   z=(out.get(e,0)+k*v)%P
   if z:out[e]=z
   else:out.pop(e,None)
 return out
def main():
 pts=[(2,3,-5),(3,6,-3),(7,-4,11),(-2,5,13)];checks=[]
 for x,y,z in pts:
  _,q=base.fiber_data(x,y,z);r=combine(((-1,q['g1']),(-1,q['g2']),(1,q['g3']),(-1,{(0,0):x+y+3*z})))
  checks.append({'point':[x,y,z],'p':x+y+3*z,'minus_q1_minus_q2_plus_q3_minus_p_zero':not r})
 assert all(c['minus_q1_minus_q2_plus_q3_minus_p_zero'] for c in checks)
 wall_coeff=(-1,-1,1);pair_coeff=(1,-1,-1);assert gcd(gcd(abs(pair_coeff[0]),abs(pair_coeff[1])),abs(pair_coeff[2]))==1
 out={'schema':'marici.benincasa.cosmology-principal-three-wall-p-identity.v1','source_identity':'p=-q_g1-q_g2+q_g3','normal_function':'p=x+y+3z','principal_wall_order':['g1','g2','g3'],'checks':checks,'wall_relation_coefficients_g1_g2_g3':list(wall_coeff),'primitive_pair_face_coefficients_order_12_13_23':list(pair_coeff),'primitive':True,'laurent_identity':'p/(q_g1 q_g2 q_g3)=-1/(q_g2 q_g3)-1/(q_g1 q_g3)+1/(q_g1 q_g2)','five_mark_extension':'p/(q_g1 q_g2 q_g3 q_g23 q_g31) is the same primitive three-term boundary tensored with 1/(q_g23 q_g31)','deletes_exceptional_marks':False,'depends_on_total_energy_identity':False,'principal_three_wall_coefficient_cell_constructed':True,'twisted_de_rham_horizontality_checked':False,'total_cech_d_squared_checked':False,'tau_p_column_computed':False,'physical_period_constructed':False,'interpretation':'p itself is the primitive ordered principal-three-wall affine dependence; this supplies a source coefficient cell and its five-mark extension without deleting g23 or g31, but not yet a total-complex chain map','next_gate':'test this coefficient cell with ordered Cech signs and the physical half-twist differential','passed':True};OUT.parent.mkdir(exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
