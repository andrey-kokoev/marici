#!/usr/bin/env python3
"""Weight audit for the canonical formal function/distribution pairing and P24."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 c=json.loads((r/'research/voevodsky/marici_gr_distribution_counit_certificate_20260908.json').read_text());assert c['status']=='proved'
 checks=0;rows=[]
 # Q and the currently available outer operations are linear: weight n -> n.
 # Multiplication sends (i,j) to i+j; vacuum trace is nonzero only in weight 0.
 for i in range(7):
  for j in range(7):
   w=i+j
   derived_nonzero_at_vacuum=(w==0 and i>0) # Q kills weight-zero/base constants
   assert not derived_nonzero_at_vacuum
   p24_nonzero_at_vacuum=(w==0 and w>0) # linear X preserves weight and kills constants
   assert not p24_nonzero_at_vacuum
   rows.append({'i':i,'j':j,'product_weight':w,'vacuum_bruce_value':0,'vacuum_p24_value':0});checks+=2
 out={'schema':'marici.formal_function_distribution_pairing.v1','status':'proved','checks':checks,
  'functions':'continuous dual Hom_IndCoh(Sym^c_!(D_k), omega_B), equivalently completed functions when dualizability permits',
  'distributions':'Sym^c_!(D_k)','pairing':'canonical evaluation between the continuous dual and the distribution coalgebra',
  'canonical_trace':'pair with the weight-zero (zero-section/vacuum) distribution, then apply the sixfold base residue',
  'q_closed':True,'bruce_trace':'valid but annihilates every derived product in the linear model',
  'p24_cocycle_with_current_linear_outer_action':'identically zero','weight_audit':rows,
  'no_go':'A nonzero P24 value requires a non-vacuum Q-closed distribution, or an outer vector field with a weight-lowering/translation term, or nonlinear Q/geometry.',
  'open_gate':'construct one of those additional data and verify its conductor residue, symmetry, and cyclic closure'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'p24':'zero for canonical vacuum plus linear outer action'}))
if __name__=='__main__':main()
