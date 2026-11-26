"""Analyze exact rejection sets on the common 16-case corpus. Independently replay all eight verdicts by enumeration of maximal-support multisets (no SAT)."""
from pathlib import Path
from itertools import combinations_with_replacement
from collections import defaultdict
import json,numpy as np
P=Path(__file__).resolve().parents[1]/'results';rows=json.loads((P/'ramsey_test_coincidence.json').read_text())['rows'];cores=json.loads((P/'ramsey_core_capacity_36.json').read_text());names=list(rows[0]['reject']);R={name:set() for name in names};replay=0;case_key={};witness_counts={}
for i,row in enumerate(rows):
 t=row['vertices'];a=cores[row['parent']]['core'];n=len(t);g=[sum(1<<j for j,y in enumerate(t) if a[x]>>y&1) for x in t];I=[q for q in range(1,1<<n) if all(not(q>>j&1 and q&v) for j,v in enumerate(g))];S=[s for s in I if not any(s!=u and s&u==s for u in I)];M=np.array(list(combinations_with_replacement(range(len(S)),5)));ok={k:np.ones(len(M),dtype=bool) for k in range(1,5)}
 for q in I:
  k=q.bit_count();ok[k]&=np.array([bool(s&q) for s in S])[M].sum(axis=1)>=k
 for name in names:
  reject=not np.logical_and.reduce([ok[int(k)] for k in name]).any();assert reject==row['reject'][name];replay+=1
  if reject:R[name].add(i)
 witness_counts[i]={s:int(np.logical_and.reduce([ok[int(k)] for k in s]).sum()) for s in ('34','1234')}
 case_key[i]=dict(parent=row['parent'],vertices=t)
classes=defaultdict(list)
for name,c in R.items():classes[tuple(sorted(c))].append(name)
summary={}
for name,c in R.items():
 others=[v for j,v in R.items() if j!=name];strict=[v for v in others if v<c];summary[name]=dict(rejected=sorted(c),same_signature=[j for j in names if R[j]==c],unique_to_test=sorted(c-set().union(*others)),beyond_strictly_smaller_signatures=sorted(c-set().union(*strict)))
out=dict(scope='stored 11-vertex cores, d=5, target (3,6); equality on this corpus is not a theorem',case_key=case_key,maximal_support_multisets=witness_counts,independent_verdicts=replay,tests=summary,signature_classes=[dict(tests=v,rejected=list(k)) for k,v in classes.items()]);(P/'ramsey_rejection_signatures.json').write_text(json.dumps(out,indent=1)+'\n');print(replay,[(v,len(k)) for k,v in classes.items()])
