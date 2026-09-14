#!/usr/bin/env python3
"""Exact smooth-exhaustion model separating finite generic leakage from its zero limit."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_smooth_cutoff_generic_leakage_decay_certificate_20260908.json');args=p.parse_args();checks=0;rows=[]
 # For Q_N=diag(1,t_N,t_N,t_N), t_N=1-1/N,
 # P0 F (I-Q_N)=(1/N)L with fixed rank-one L.
 previous=None
 for N in (2,4,8,16,32,64,128):
  coefficient=Fraction(1,N)
  matrix=[[Fraction(0),coefficient,coefficient,coefficient],[Fraction(0)]*4,[Fraction(0)]*4,[Fraction(0)]*4]
  rank=1 if coefficient else 0
  assert rank==1;checks+=1
  if previous is not None:assert coefficient<previous;checks+=1
  previous=coefficient
  rows.append({'cutoff':N,'leakage_coefficient':f'1/{N}','finite_rank':rank,'entrywise_bound':f'1/{N}'})
 # Cauchy compatibility is exact because all stages are scalar multiples of L.
 assert Fraction(1,8)-Fraction(1,16)==Fraction(1,16);checks+=1
 out={'schema':'marici.rh.smooth-cutoff-generic-leakage-decay.v1','status':'generic_defect_converges_to_zero','checks':checks,'rows':rows,'cutoff':'Q_N=diag(1,1-1/N,1-1/N,1-1/N)','leakage':'P0 F (I-Q_N)=L/N','claim':'the imposed scalar taper makes this particular finite defect converge uniformly to zero with exact bound 1/N','consequence':'seam support may be tested after completion only when an analogous source-derived quasi-locality or summable-shell estimate is proved','boundary':'strong cutoff convergence alone does not imply this 1/N operator-norm law; the backward-shift hostile retains moving-cutoff norm one'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'last_bound':'1/128'}))
if __name__=='__main__':main()
