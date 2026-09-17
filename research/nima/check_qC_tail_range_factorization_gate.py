#!/usr/bin/env python3
"""Exact finite hostile for the q-C tail range-factorization criterion."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def rank2(a):
 if not any(any(x for x in r) for r in a):return 0
 if len(a)>=2 and len(a[0])>=2:
  for i in range(len(a)):
   for j in range(i+1,len(a)):
    for k in range(len(a[0])):
     for l in range(k+1,len(a[0])):
      if a[i][k]*a[j][l]-a[i][l]*a[j][k]:return 2
 return 1
# Existing finite Fourier-cutoff leakage witness: image is span(1,-1).
A=[[1,1],[-1,-1]]
B=[[1,0],[0,1]]
Mgood=mm(A,B)
Mbad=[[1,0],[0,1]]
def augment(A,M):return [ra+rm for ra,rm in zip(A,M)]
good_range=rank2(augment(A,Mgood))==rank2(A)
bad_range=rank2(augment(A,Mbad))>rank2(A)
# y=(1,1) lies in ker A*; Douglas domination forces M* y=0.
y=[[1],[1]]
At_y=mm(tr(A),y);goodt_y=mm(tr(Mgood),y);badt_y=mm(tr(Mbad),y)
checks={'leakage_rank_one':rank2(A)==1,'factorable_defect_passes_range_test':good_range,'generic_two_channel_defect_fails_range_test':bad_range,'good_defect_annihilates_cokernel_witness':goodt_y==[[0],[0]],'bad_defect_hits_cokernel_witness':badt_y!=[[0],[0]],'actual_qC_completed_defect_operator_serialized':False}
out={'schema':'marici.nima.qC-tail-range-factorization-gate.v1','tail_boundary':A,'factorable_fixture':Mgood,'nonfactorable_fixture':Mbad,'checks':checks,'passed':all(v for k,v in checks.items() if k!='actual_qC_completed_defect_operator_serialized'),'criterion':'Ran(M2) subset Ran(A_X), equivalently M2 M2* <= lambda A_X A_X* in the bounded Hilbert setting','frontier':'serialize the actual completed bilinear q-C defect M2 with its visible graph target, then run the range and Douglas tests'}
p=ROOT/'research/nima/results/qC-tail-range-factorization-gate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
