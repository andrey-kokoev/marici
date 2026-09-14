#!/usr/bin/env python3
"""Derive the normal metric fixed by sign parity and channel reversal."""
import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def tr(A):return [list(x) for x in zip(*A)]
def invariant(T,G):return mm(mm(tr(T),G),T)==G

def main():
 S=[[1,0],[0,-1]]
 J=[[0,-1],[-1,0]]
 # Exhaustive rational-grid classification of positive symmetric candidates.
 candidates=[];both=[];only_j=[];only_s=[]
 vals=[Fraction(i) for i in range(-3,4)]
 for a in vals:
  for b in vals:
   for c in vals:
    if a>0 and a*c-b*b>0:
     G=[[a,b],[b,c]];candidates.append(G)
     si=invariant(S,G);ji=invariant(J,G)
     if si and ji:both.append(G)
     if ji and not si:only_j.append(G)
     if si and not ji:only_s.append(G)
 assert both and all(G[0][1]==0 and G[0][0]==G[1][1] for G in both)
 assert [[Fraction(2),Fraction(1)],[Fraction(1),Fraction(2)]] in only_j
 assert [[Fraction(2),Fraction(0)],[Fraction(0),Fraction(3)]] in only_s
 result={'schema':'marici.voevodsky.intrinsic-right-angle-from-channel-symmetries.v1','sign_parity':S,'channel_reversal':J,'positive_symmetric_metrics_checked':len(candidates),'metrics_invariant_under_both':len(both),'derived_metric_family':'lambda I, lambda>0','cross_pairing_forced_zero':True,'equal_norms_forced':True,'right_angle_forced':True,'reversal_only_counterexample':[[2,1],[1,2]],'sign_only_counterexample':[[2,0],[0,3]],'claim_boundary':'The metric is intrinsic relative to two declared isometric involutions; the involutions themselves remain model data.'}
 out=Path(__file__).parents[1]/'results'/'intrinsic_right_angle_from_channel_symmetries.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
