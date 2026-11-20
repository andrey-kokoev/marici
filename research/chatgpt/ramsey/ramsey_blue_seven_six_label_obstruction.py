"""Reduce independent-set obstruction to graphs of candidate duads on six labels. Enumerate only the small extremal lemma, not Hall matchings or 22-vertex outputs."""
from itertools import combinations
from collections import Counter
P=list(combinations(range(6),2));T=[set(t) for t in combinations(P,3) if len(set(sum(t,())))==6];bad4=[]
for S in combinations(range(6),4):
 a,b,c,d=S;bad4.extend([set(map(tuple,z)) for z in [((a,b),(b,c),(c,d),(a,d)),((a,b),(b,d),(c,d),(a,c)),((a,c),(b,c),(b,d),(a,d))]])
hist=Counter();valid=[]
for mask in range(1<<15):
 F={P[i] for i in range(15) if mask>>i&1}
 if any(t<=F for t in T) or any(q<=F for q in bad4):continue
 valid.append(F)
 if len(F)>=6:
  deg=tuple(sorted(sum(v in e for e in F) for v in range(6)));hist[len(F),deg]+=1
  trapped=[e for e in F if all(bool((t-{e})&F) for t in T if e in t)];assert trapped
print('six-or-more duads with no C4 or three disjoint edges',dict(hist));assert max(map(len,valid))==6
# No root: k label vertices leave only 6-k available endpoints.
for k in range(1,7):
 available=set(range(6-k));threshold=7-k
 possible=[F for F in valid if all(set(e)<=available for e in F) and len(F)>=threshold]
 assert all(any(all(bool((t-{e})&F) for t in T if e in t) for e in F) for F in possible)
 print('selected label vertices',k,'remaining extremal duad candidates',len(possible))
