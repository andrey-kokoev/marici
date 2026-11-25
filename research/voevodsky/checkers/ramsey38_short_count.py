"""Record 477142: lower-bound missed sevens by truncated inclusion-exclusion for each candidate. Count using only incidence counts for subsets up to the truncation degree."""
from pathlib import Path
import gzip,itertools,math,collections
base=Path(__file__).resolve().parents[2];b=gzip.decompress((base/'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines()[-1];adj=[0]*27
for j in range(27):
 for i in range(j):
  k=j*(j-1)//2+i
  if (b[1+k//6]-63)>>(5-k%6)&1:adj[i]|=1<<j;adj[j]|=1<<i
maximal=[];seven=[]
def walk(a,c):
 if not c and all(a>>i&1 or adj[i]&a for i in range(27)):
  maximal.append(a)
  if a.bit_count()==7:seven.append(a)
 while c:
  i=c&-c;c-=i;walk(a|i,c&~adj[i.bit_length()-1])
walk(0,(1<<27)-1)
# For odd k the lower bound equals exact misses minus sum_{hit>k} binom(hit-1,k).
def bounds(a):
 h=collections.Counter((a&s).bit_count() for s in seven)
 return [h[0]-sum(v*math.comb(t-1,k) for t,v in h.items() if t>k) for k in (1,3,5,7)]
v=list(map(bounds,maximal));print(len(v),len(seven),list(map(min,zip(*v))),[sum(t[i]<7 for t in v) for i in range(4)])
