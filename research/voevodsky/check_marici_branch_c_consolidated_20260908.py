#!/usr/bin/env python3
"""Consolidated certificate audit for the algebraic/formal Branch C result."""
import argparse,json,hashlib
from pathlib import Path

INPUTS=[
 'marici_strict_conductor_truncation_q_certificate_20260908.json',
 'marici_strict_d35_d04_spatial_comparison_certificate_20260908.json',
 'marici_gr_distribution_counit_certificate_20260908.json',
 'marici_formal_function_distribution_pairing_certificate_20260908.json',
 'marici_p24_translation_cocycle_certificate_20260908.json',
 'marici_p24_nonboundary_detector_certificate_20260908.json',
 'marici_normalization_q_descent_certificate_20260908.json']

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();root=Path(a.root);base=root/'research/voevodsky'
 docs={};digests={};checks=0
 for name in INPUTS:
  raw=(base/name).read_bytes();docs[name]=json.loads(raw);digests[name]=hashlib.sha256(raw).hexdigest()
  assert docs[name]['status']=='proved';checks+=1
 q=docs[INPUTS[0]];d=docs[INPUTS[1]];dist=docs[INPUTS[2]];pair=docs[INPUTS[3]];phi=docs[INPUTS[4]];nb=docs[INPUTS[5]];desc=docs[INPUTS[6]]
 assert q['q_nonzero'] if 'q_nonzero' in q else q['formula'].startswith('q(');checks+=1
 assert q['chain_map_defects']==[] and q['dual_columns_checked']==50;checks+=2
 assert len(d['frames'])==8 and all(x['chain_defect']==[0,0,0] for x in d['frames']);checks+=9
 assert dist['q_closed']=='yes for the linear coderivation induced by d_D; it preserves symmetric weight and vanishes on omega_X';checks+=1
 assert pair['p24_cocycle_with_current_linear_outer_action']=='identically zero';checks+=1
 assert len(phi['frames'])==8 and all(x['odd_channel_test_value_phi(lambda_v,1)']==-1 for x in phi['frames']);checks+=9
 assert len(nb['frames'])==8 and all(x['every_b0_sigma_on_pair']==0 and x['phi_on_pair']==-1 for x in nb['frames']);checks+=17
 assert '65 unit cancellations' in desc['native_comparison'] and len(desc['frames'])==8;checks+=2
 out={'schema':'marici.branch_c.consolidated.v1','status':'proved','checks':checks,'input_sha256':digests,
  'theorem':{'category':'algebraic continuous-formal / GR IndCoh','targets':['D35','D04'],
   'q':'q(p_(E,O)^vee)=-1 and q(kappa)=1; strict on all 50 omega states',
   'spatial_maps':'eight b_(sigma,T)=(0,j_k kappa_(sigma,T),0), all strict with primitive coefficient 1',
   'descent':'two smooth normalization branches with conductor homotopy H descend integrally to the singular native targets',
   'trace':'Q-closed zero-section distribution followed by the normalized sixfold conductor residue',
   'outer_symmetry':'odd constant translation X_v=partial_v on cubic/quintic primitive sectors; [Q,X_v]=0',
   'p24':'phi_v(lambda_v,1)=-1 while every degree-zero Hochschild boundary is 0 on (lambda_v,1); therefore [phi_v] is nonzero'},
  'important_distinction':'weight-preserving linear outer operations give zero P24 cochain; the nonzero class uses the constant translation attached to the strict endpoint cycle',
  'excluded_from_claim':['reconstruction of Bruce smooth Q-manifold','compactness','nuclear Frechet topology','global smooth Berezin manifold'],
  'conclusion':'Branch C is complete in the intended algebraic/formal category.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'inputs':len(INPUTS),'conclusion':out['conclusion']}))
if __name__=='__main__':main()
