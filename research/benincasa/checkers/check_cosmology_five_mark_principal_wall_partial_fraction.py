#!/usr/bin/env python3
"""Audit the tempting five-mark identity and reject it as total-energy, not p-normal."""
import json,sys
from math import gcd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research'/'benincasa'))
import physical_four_mark_residue_twisted_derham as base
OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_five_mark_principal_wall_partial_fraction.json'
P=base.PRIME

def sub(*terms):
 out={}
 for sign,row in terms:
  for e,v in row.items():
   z=(out.get(e,0)+sign*v)%P
   if z:out[e]=z
   else:out.pop(e,None)
 return out

def main():
 points=[(2,3,-5),(3,6,-3),(7,-4,11),(-2,5,13)];checks=[]
 for x,y,z in points:
  _,q=base.fiber_data(x,y,z);res=sub((1,q['g3']),(-1,q['g23']),(-1,q['g31']),(-1,{(0,0):x+y+z}))
  checks.append({'point':[x,y,z],'total_energy':x+y+z,'p_normal_function':x+y+3*z,'q3_minus_q23_minus_q31_minus_total_energy_zero':not res})
 assert all(c['q3_minus_q23_minus_q31_minus_total_energy_zero'] for c in checks)
 # Cross multiplication of
 # E/(q1 q2 q3 q23 q31) = 1/(q1 q2 q23 q31)
 #   -1/(q1 q2 q3 q31)-1/(q1 q2 q3 q23)
 # reduces exactly to p=q3-q23-q31.
 primitive=(1,-1,-1);assert gcd(gcd(abs(primitive[0]),abs(primitive[1])),abs(primitive[2]))==1
 out={'schema':'marici.benincasa.cosmology-five-mark-principal-wall-partial-fraction.v1','source_identity':'q_g3 - q_g23 - q_g31 = E, where E=x+y+z','checks':checks,'E_zero_specialization':'q_g3=q_g23+q_g31','laurent_identity':'E/(q_g1 q_g2 q_g3 q_g23 q_g31)=1/(q_g1 q_g2 q_g23 q_g31)-1/(q_g1 q_g2 q_g3 q_g31)-1/(q_g1 q_g2 q_g3 q_g23)','primitive_coefficient_vector':list(primitive),'primitive':True,'p_normal_derivative_of_E_for_nx':1,'p_normal_derivative_of_E_for_ny':1,'p_tangent_derivative_of_E':0,'routes_g23_and_g31_without_deletion':True,'p_normal_coefficient_ring_map_constructed':False,'twisted_de_rham_chain_map_constructed':False,'tau_p_column_computed':False,'physical_period_constructed':False,'interpretation':'the primitive partial fraction belongs to the total-energy divisor E=x+y+z, not the target p=x+y+3z; importing it into the p-normal problem would violate source typing','next_gate':'reject this total-energy bridge and require an identity whose coefficient is p=x+y+3z','passed':True};OUT.parent.mkdir(exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
