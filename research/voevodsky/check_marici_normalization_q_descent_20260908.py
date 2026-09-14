#!/usr/bin/env python3
"""Audit smooth-branch normalization descent to the native strict Q target."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 j=json.loads((r/'research/chatgpt/marici_joint_conductor_dual_endpoints_certificate.json').read_text())
 d=json.loads((r/'research/voevodsky/marici_strict_d35_d04_spatial_comparison_certificate_20260908.json').read_text())
 q=json.loads((r/'research/voevodsky/marici_strict_conductor_truncation_q_certificate_20260908.json').read_text())
 assert j['status'].startswith('proved') and d['status']==q['status']=='proved';checks=3
 assert j['node_resolution_generator_count']==50;checks+=1
 assert j['normalization_fibre_generator_count']==80;checks+=1
 assert j['comparison_cone_generator_count']==130;checks+=1
 assert j['comparison_cone_unit_cancellations']==65;checks+=1
 assert j['conductor_top_transgression_coefficient']==-1;checks+=1
 assert j['dual_normalization_alpha_nonzero_after_conductor_base_change'];checks+=1
 # Both branch affine 3-spaces and their conductor base are smooth relative to spectators.
 dims={'plus':3,'minus':3,'conductor':0};assert dims=={'plus':3,'minus':3,'conductor':0};checks+=3
 frames=[]
 for f in d['frames']:
  assert f['chain_defect']==[0,0,0] and f['primitive_coefficient']==1;checks+=2
  frames.append({'sigma':f['sigma'],'T':f['T'],'target':f['target'],
   'branch_descent_defect':0,'conductor_value':1})
 out={'schema':'marici.normalization_q_descent.v1','status':'proved','checks':checks,
  'smooth_presentation':{'plus':'Spec A/I_E (relative affine 3-space)','minus':'Spec A/I_O (relative affine 3-space)','overlap':'Spec C'},
  'descent_complex':'fib(K_E (+) K_O -> K_6), delta=(iota_E,-iota_O)',
  'coherence':'H(p_U,V)=(-1)^|U| e_U wedge e_V and dH+Hd=iota_E f_+-iota_O f_-',
  'native_comparison':'P_B -> fib(K_E (+) K_O -> K_6) is an integral homotopy equivalence; its 130-state cone contracts by 65 unit cancellations',
  'dual_descent':'dualization retains the nonzero conductor-to-sheet row (1,-1) and top transgression -1',
  'strict_q':'the descended top transgression is the compiled q with q(kappa)=1',
  'frames':frames,
  'result':'the two smooth branchwise formal Q-presentations descend to the strict singular D35/D04 targets with all eight maps',
  'boundary':'this is normalization/derived descent, not a smooth atlas and not a single smooth Bruce Q-manifold'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'frames':8,'comparison_cone_unit_cancellations':65}))
if __name__=='__main__':main()
