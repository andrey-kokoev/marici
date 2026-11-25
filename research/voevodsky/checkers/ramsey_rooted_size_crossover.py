"""Rooted crossover replay: independent one/two/three-port extension audit on the (3,5;13) catalogue."""
from itertools import combinations,combinations_with_replacement
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';C=D.parents[1]/'chatgpt/ramsey/pauli-realization-catalogues'
def decode(g):
 n=ord(g[0])-63;a=[0]*n;b=''.join(f'{ord(c)-63:06b}' for c in g[1:]);idx=0
 for j in range(n):
  for i in range(j):
   if b[idx]=='1':a[i]|=1<<j;a[j]|=1<<i
   idx+=1
 return a
def independent(a,t):return all(not a[v]&t for v in range(len(a)) if t>>v&1)
def main():
 out=[]
 for g in (C/'r35_13.g6').read_text().splitlines():
  a=decode(g);I=[t for t in range(1<<13) if independent(a,t)];assert max(t.bit_count() for t in I)==4
  rows=[s for s in I if not any(s!=t and s&t==s for t in I)];counts={};w=None
  for k in (2,3):
   ok=0
   for E in combinations_with_replacement(rows,k):
    # Independent sets avoiding root: choose T in core and all ports missing T.
    if all(t.bit_count()+sum(not t&s for s in E)<6 for t in I):
     ok+=1
     if k==2 and w is None:w=E
   counts[k]=ok
  assert w and counts[3]==0
  A=a.copy()+[0]*3
  for j,s in enumerate(w,13):
   A[j]=s|1<<15;A[15]|=1<<j
   for i in range(13):
    if s>>i&1:A[i]|=1<<j
  assert all(not A[i]&A[j] for i,j in combinations(range(16),2) if A[i]>>j&1) and not any(independent(A,sum(1<<v for v in vs)) for vs in combinations(range(16),6));out.append(dict(core=g,ports=len(rows),valid_multisets=counts,root=15,witness_ports=[[i for i in range(13) if s>>i&1] for s in w],adjacency_masks=A))
 degs=[min(v.bit_count() for v in decode(g)) for g in (C/'r36_17.g6').read_text().splitlines()];assert min(degs)==4
 result=dict(extensions=out,catalogue17_min_degrees=degs);print(result);(D/'ramsey_rooted_size_crossover.json').write_text(json.dumps(result,indent=2))
if __name__=='__main__':main()
