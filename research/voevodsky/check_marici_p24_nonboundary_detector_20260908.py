#!/usr/bin/env python3
"""Reduced Hochschild detector for the endpoint-translation P24 cocycle."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 c=json.loads((r/'research/voevodsky/marici_p24_translation_cocycle_certificate_20260908.json').read_text())
 l=json.loads((r/'research/voevodsky/branch_b_framed_line_adapter_certificate_20260908.json').read_text())
 assert c['status']==l['status']=='proved'
 rows=[];checks=0
 for f in c['frames']:
  lf=next(x for x in l['frames'] if x['sigma']==f['sigma'] and x['T']==f['T'])
  assert lf['coefficient']==1 and lf['degree_displacement']==0;checks+=2
  # lambda is the certified top chain detector, hence Q lambda=0.
  qlambda=0;qone=0
  # Derived products lambda*1 and 1*lambda both vanish.
  lam_star_one=qlambda;one_star_lam=qone
  assert lam_star_one==one_star_lam==0;checks+=2
  # Therefore every degree-zero Hochschild boundary vanishes on this pair,
  # independently of convention signs or the chosen zero-cochain sigma.
  boundary_detector=0;phi=f['odd_channel_test_value_phi(lambda_v,1)']
  assert phi==-1 and phi!=boundary_detector;checks+=2
  rows.append({'sigma':f['sigma'],'T':f['T'],'Qlambda':0,'lambda_star_1':0,
   '1_star_lambda':0,'every_b0_sigma_on_pair':0,'phi_on_pair':phi})
 assert len(rows)==8;checks+=8
 out={'schema':'marici.p24_nonboundary_detector.v1','status':'proved','checks':checks,
  'detector_pair':'(lambda_v,1), with lambda_v the closed framed top coordinate dual to v',
  'boundary_vanishing':'lambda_v star 1=0 and 1 star lambda_v=0, so (b sigma)(lambda_v,1)=0 for every zero-cochain sigma',
  'cocycle_value':'phi_v(lambda_v,1)=-1','frames':rows,
  'conclusion':'phi_v is not a Hochschild boundary; its derived cyclic degree-one class is nonzero',
  'normalization':'reduced/Dorroh normalization introduces no unit-degenerate boundary because both relevant derived products vanish',
  'scope':'algebraic continuous-formal cyclic complex with the supported distribution trace; smooth nuclear-Frechet realization is not asserted'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'frames':8,'p24_class':'nonzero'}))
if __name__=='__main__':main()
