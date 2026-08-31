#!/usr/bin/env python3
"""Audit the integral parity of a minimal correction to the p partial fraction."""
import json
from math import gcd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_partial_fraction_primitive_correction_gate.json'
def mv(A,v):return [sum(a*x for a,x in zip(r,v)) for r in A]
def main():
 A=[[-1,-1,0],[1,0,-1],[0,1,1]];c=[1,-1,-1];f=[1,-1,1];v=[0,1,-1]
 assert mv(A,c)==[2*x for x in v] and mv(A,f)==[0,0,0]
 solutions=[]
 for a in range(-4,5):
  for b in range(-4,5):
   for k in range(-8,9):
    if a==b==k==0:continue
    if 2*a+k==0:solutions.append((a,b,k))
 assert solutions and all(k==-2*a for a,b,k in solutions)
 unit_p=[s for s in solutions if abs(s[0])==1];assert unit_p and all(abs(s[2])==2 for s in unit_p)
 assert not any(abs(a)==abs(k)==1 for a,b,k in solutions)
 out={'schema':'marici.benincasa.cosmology-partial-fraction-primitive-correction-gate.v1','candidate_pair_vector':c,'cech_face_cycle':f,'candidate_boundary':[2*x for x in v],'primitive_obstruction_direction':v,'hypothetical_minimal_correction_boundary':v,'closure_equation':'2*a+k=0 for a*(partial fraction)+b*(Cech face)+k*(primitive correction)','unit_p_coefficient_forces_correction_coefficient':2,'unit_balanced_attachment_exists':False,'minimal_closed_examples':[[1,0,-2],[-1,0,2]],'gcd_of_minimal_example':gcd(1,2),'conditional_scope':'assumes one correction generator with primitive boundary (0,1,-1); additional independently sourced cells are not excluded','maps_to_universal_tau_with_unit_coefficient':False,'interpretation':'the partial-fraction obstruction is twice a primitive vertex direction, so a minimal integral correction enters with coefficient two; it cannot supply the unit (1,1) universal attachment','next_gate':'seek at least two source-derived correction cells or a different chain map whose primitive boundary matches the candidate with unit coefficient','passed':True};OUT.parent.mkdir(exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
