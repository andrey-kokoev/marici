"""Conditional on completeness of the 22-vertex catalogue and R(3,6)=18. Cover all possible new red neighborhoods by selected blue-six obstructions; verify every obstruction by three lifted Hall bundles."""
import runpy
from pathlib import Path
from collections import Counter
base=Path(__file__).resolve().parents[2]/'chatgpt/ramsey'
h=runpy.run_path(str(base/'ramsey_cyclic_quotient_constructor.py')); m=h['outputs'][0];bundles=[b for b in h['B'] if b<=m];pairs=h['P'];assert len(bundles)==3
hist=Counter();total=0
for row in (base/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines():
 adj=[0]*22;k=0
 for j in range(22):
  for i in range(j):
   if ((row[1+k//6]-63)>>(5-k%6))&1:adj[i]|=1<<j;adj[j]|=1<<i
   k+=1
 cand=[];six=[]
 def walk(a,c,n):
  if n>=5:cand.append(a)
  if n==6:six.append(a);return
  while c:
   t=c&-c;c-=t;walk(a|t,c&~adj[t.bit_length()-1],n+1)
 walk(0,(1<<22)-1,0);left=(1<<len(cand))-1;total+=len(cand)
 hit=[sum(1<<i for i,a in enumerate(cand) if a&s==0) for s in six];count=0
 while left:
  j=max(range(len(six)),key=lambda i:(hit[i]&left).bit_count());assert hit[j]&left
  v=[i for i in range(22) if six[j]>>i&1];assert all(not(adj[v[pairs[i][0]]]>>v[pairs[i][1]]&1) for b in bundles for i,_ in b)
  left &= ~hit[j];count+=1
 hist[count]+=1
print('parents',hist.total(),'candidate neighborhoods',total,'greedy cover sizes',sorted(hist.items()))
