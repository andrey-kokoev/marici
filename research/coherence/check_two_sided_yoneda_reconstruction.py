#!/usr/bin/env python3
"""Test reconstruction of bicharged primitives from all pairwise contexts."""

import json, random
from fractions import Fraction
from pathlib import Path


def reconstruct(B):
 n=len(B);pivot=next(((i,j) for i in range(n) for j in range(n) if B[i][j]),None)
 if pivot is None:return None
 i0,j0=pivot
 # Gauge choice: outgoing[i0] = 1.
 incoming=B[i0][:]
 outgoing=[B[i][j0]/B[i0][j0] for i in range(n)]
 return incoming,outgoing

def main():
 rng=random.Random(20260912);rows=[]
 for n in range(1,10):
  for trial in range(20):
   incoming=[Fraction(rng.randrange(1,12),rng.randrange(1,12)) for _ in range(n)]
   outgoing=[Fraction(rng.randrange(1,12),rng.randrange(1,12)) for _ in range(n)]
   B=[[outgoing[i]*incoming[j] for j in range(n)] for i in range(n)]
   ri,ro=reconstruct(B);assert all(B[i][j]==ro[i]*ri[j] for i in range(n) for j in range(n))
   gauge=Fraction(1,outgoing[0]);assert ro==[gauge*x for x in outgoing] and ri==[x/gauge for x in incoming]
   rows.append({'objects':n,'trial':trial,'reconstructed_up_to_gauge':True})
 hostile=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]
 hi,ho=reconstruct(hostile);hostile_rejected=any(hostile[i][j]!=ho[i]*hi[j] for i in range(2) for j in range(2))
 assert hostile_rejected
 result={'schema':'marici.coherence.two-sided-yoneda-reconstruction.v1','cases':len(rows),'all_rank_one_behaviors_reconstructed_up_to_gauge':True,'gauge':'out -> lambda out; in -> lambda^(-1) in','rank_two_hostile_rejected':True,'zero_behavior_caveat':'if every pairing is zero, the two charge factors are not recoverable'}
 Path(__file__).with_name('two-sided-yoneda-reconstruction.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
