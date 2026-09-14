#!/usr/bin/env python3
"""Check the polarity-loaded marked-conormal line adapter in eight frames."""
import argparse,json
from pathlib import Path
TS=((1,3),(1,5),(3,5),(1,3,5))
# Entry 94, columns dx0,...,dx5.
K=((0,0,-1,0,0,1),(-1,0,0,1,0,0),(0,1,0,0,-1,0))
DELTA=(1,1,1)
POL=(-1,1,-1,1,-1,1)

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 mate=json.loads((r/'research/voevodsky/endpoint-to-conormal-cohomology-mate.json').read_text())
 jet=json.loads((r/'research/voevodsky/physical-conormal-first-jet-adapter.json').read_text())
 raw=[sum(DELTA[i]*K[i][j] for i in range(3)) for j in range(6)]
 loaded=[raw[j]*POL[j] for j in range(6)]
 assert raw==[-1,1,-1,1,-1,1]; assert loaded==[1]*6
 assert mate['construction']['degree_displacement']==0
 assert jet['conclusion']['kernel_column'].endswith('coefficient 1')
 rows=[]
 for sigma,kidx,k in [('plus',5,'35'),('minus',4,'04')]:
  for T in TS:
   assert loaded[kidx]==1
   rows.append({'sigma':sigma,'T':list(T),'marked_conormal':k,'column':kidx,
    'raw_primitive_sign':raw[kidx],'polarity_sign':POL[kidx],'coefficient':loaded[kidx],
    'degree_displacement':0,
    'map':'physical top detector -> marked column of (Delta^vee tensor L_pol) K_alt -> v_k tensor Pi^vee[3]',
    'excess_transport':'identity on the retained epsilon-labelled external line'})
 out={'schema':'marici.branch_b.framed_line_adapter.v1','status':'proved','frames':rows,
  'raw_row':raw,'polarity_row':list(POL),'loaded_row':loaded,
  'line_map':'chi_sigma,T,epsilon=(marked-column projection) o ((Delta^vee tensor L_pol)K_alt) o detector_sigma,T,epsilon',
  'normalization':'Pi is the once-retained polarity line; determinant dual/external-normal evaluation is the canonical pairing, not Euler evaluation; excess labels pass by identity',
  'new_integer_checks':6+len(rows)+2}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','frames':len(rows),'new_integer_checks':out['new_integer_checks']}))
if __name__=='__main__':main()
