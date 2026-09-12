#!/usr/bin/env python3
"""Measure how orientation reversal enlarges the residual's context realization."""

import json, random
from fractions import Fraction
from pathlib import Path


def rank2(M):
 return 0 if all(x==0 for r in M for x in r) else (1 if M[0][0]*M[1][1]==M[0][1]*M[1][0] else 2)
def main():
 rng=random.Random(20260912);rows=[];rank_counts={1:0,2:0}
 for trial in range(200):
  qin=Fraction(rng.randrange(-9,10),rng.randrange(1,10));qout=Fraction(rng.randrange(-9,10),rng.randrange(1,10))
  if not qin and not qout:continue
  # Words in C2={1,R}; R swaps incoming and outgoing charges.
  H=[[qout,qin],[qin,qout]]
  r=rank2(H);rank_counts[r]+=1
  expected=1 if qout==qin or qout==-qin else 2
  assert r==expected
  rows.append({'qin':str(qin),'qout':str(qout),'hankel_rank':r,'self_dual':qout==qin,'anti_self_dual':qout==-qin})
 result={'schema':'marici.coherence.reversal-context-hankel-rank.v1','cases':len(rows),'rank_counts':rank_counts,'generic_rank':2,'rank_one_locus':'qout = qin or qout = -qin','conclusion':'a sewing-rank-one residual generically becomes a two-state realization when orientation reversal is an admitted continuation'}
 Path(__file__).with_name('reversal-context-hankel-rank.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','rank_counts','generic_rank','rank_one_locus','conclusion')},indent=2))
if __name__=='__main__':main()
