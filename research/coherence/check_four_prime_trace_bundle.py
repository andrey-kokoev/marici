#!/usr/bin/env python3
"""Verify trace pushforwards and Green metrics for varying broken-graph fibers."""

import json, math
from itertools import combinations
from pathlib import Path

LENGTHS=tuple(math.log(p) for p in (2,3,5,7)); TOL=1e-12
def key(x): return round(x,12)
def subsets(xs):
 for n in range(len(xs)+1): yield from combinations(xs,n)
def coords(B): return [('E',0.0)]+[(s,b) for b in B for s in ('L','R')]
def metric(B): return [-1]+[v for _ in B for v in (1,-1)]
def mat(rows,cols): return [[0]*cols for _ in range(rows)]
def gram_pull(M,j):
 return [[sum(j[r]*M[r][a]*M[r][b] for r in range(len(M))) for b in range(len(M[0]))] for a in range(len(M[0]))]

def main():
 B=tuple(sorted(key(sum(LENGTHS[i] for i in U)) for U in subsets(range(4)) if U))
 reports=[]
 for a0 in LENGTHS:
  a=key(a0); src=coords(B); si={c:i for i,c in enumerate(src)}
  # S_a trace pushforward
  BS=tuple(sorted({a}|{key(a+b) for b in B})); tgt=coords(BS); ti={c:i for i,c in enumerate(tgt)}; M=mat(len(tgt),len(src))
  M[ti[('R',a)]][si[('E',0.0)]]=1
  for b in B:
   for side in ('L','R'): M[ti[(side,key(a+b))]][si[(side,b)]]=1
  s_iso=gram_pull(M,metric(BS))==[[metric(B)[i] if i==j else 0 for j in range(len(src))] for i in range(len(src))]
  assert s_iso
  # R_a trace pushforward; a is a source break
  BR=tuple(b for b in (key(x-a) for x in B if x>a+TOL) if b>TOL); tgtR=coords(BR); tri={c:i for i,c in enumerate(tgtR)}; MR=mat(len(tgtR),len(src))
  MR[tri[('E',0.0)]][si[('R',a)]]=1
  for b in B:
   if b>a+TOL:
    for side in ('L','R'): MR[tri[(side,key(b-a))]][si[(side,b)]]=1
  pull=gram_pull(MR,metric(BR)); J=[[metric(B)[i] if i==j else 0 for j in range(len(src))] for i in range(len(src))]
  residual=[[pull[i][j]-J[i][j] for j in range(len(src))] for i in range(len(src))]
  residual_rank=sum(1 for i in range(len(src)) if residual[i][i])
  reports.append({'a':a,'S_green_isometry':s_iso,'R_relative_residual_diagonal_rank':residual_rank})
 result={'schema':'marici.coherence.four-prime-trace-bundle.v1','break_count':len(B),'trace_dimension':len(coords(B)),'S_pushforwards_preserve_green_form':all(r['S_green_isometry'] for r in reports),'R_pushforwards_have_declared_relative_defect':all(r['R_relative_residual_diagonal_rank']>0 for r in reports),'reports':reports}
 target=Path(__file__).with_name('four-prime-trace-bundle.v1.json');target.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
