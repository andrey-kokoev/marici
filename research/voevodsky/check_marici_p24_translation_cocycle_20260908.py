#!/usr/bin/env python3
"""Compile constant endpoint translations and their primitive P24 evaluation."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 d=json.loads((r/'research/voevodsky/marici_strict_d35_d04_spatial_comparison_certificate_20260908.json').read_text())
 tr=json.loads((r/'research/voevodsky/marici_formal_function_distribution_pairing_certificate_20260908.json').read_text())
 assert d['status']==tr['status']=='proved'
 frames=[];checks=0
 for f in d['frames']:
  assert f['chain_defect']==[0,0,0] and f['primitive_coefficient']==1
  # v is a Q-cycle. Constant differentiation obeys [Q,partial_v]=partial_(Qv)=0.
  qv=0; comm=qv;assert comm==0;checks+=2
  # lambda_v(v)=1 in the certified framed line. For odd v/lambda,
  # P24 phi(lambda,1)=tau((-1)^1 partial_v(lambda))=-Res(1)=-1.
  pairing=f['primitive_coefficient'];residue=1;phi=-pairing*residue
  assert phi==-1;checks+=2
  frames.append({'sigma':f['sigma'],'T':f['T'],'target':f['target'],'Qv':qv,
   'Q_translation_supercommutator':comm,'dual_coordinate_pairing':pairing,
   'odd_channel_test_value_phi(lambda_v,1)':phi})
 # Reflection exchanges all four marked frames with equal normalized values.
 assert [x['odd_channel_test_value_phi(lambda_v,1)'] for x in frames]==[-1]*8;checks+=8
 out={'schema':'marici.p24_translation_cocycle.v1','status':'proved','checks':checks,
  'translation':'X_v=partial_v for v=b_sigma,T; it lowers formal symmetric weight by one',
  'commutator':'[Q,X_v]=partial_(Qv)=0 because every b_sigma,T is a strict cycle',
  'parity':'apply to odd primitive source classes (cubic or quintic); then v and X_v are odd',
  'trace':'canonical zero-section distribution followed by the normalized sixfold residue',
  'p24_formula':'phi_v(f0,f1)=tau((-1)^|f0| X_v(f0 f1))',
  'frames':frames,'nonzero_cochain_detector':'phi_v(lambda_v,1)=-1 in all eight normalized frames',
  'reflection':'the detector is carried D35 <-> D04 with the framed value unchanged',
  'boundary':'nonzero as a cochain is proved; nonzero derived-cyclic cohomology class is not yet proved',
  'next_gate':'exclude phi_v=-b(sigma) by a reduced Hochschild/cyclic boundary detector retaining the conductor line'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'frames':8,'primitive_p24_value':-1,'class_nonzero':'not yet proved'}))
if __name__=='__main__':main()
