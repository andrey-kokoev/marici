"""Exact Laplacian cut certificate for no independent five. Compare with a degree-only cut bound and direct five-subset checks. All counts are square occurrences, not distinct graphs."""
import sys,gzip,itertools,collections,json,subprocess
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';cat=P.parents[1]/'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz';freq=collections.Counter()
with gzip.open(cat,'rt') as f:
 while True:
  rows=list(itertools.islice(f,8192))
  if not rows:break
  freq.update(subprocess.check_output([sys.argv[1]],input=''.join(rows),text=True).splitlines())
def pd(M):
 # Fraction-free symmetric elimination: positive definite iff every pivot positive.
 M=[row.copy() for row in M];prev=1
 for i in range(len(M)):
  p=M[i][i]
  if p<=0:return False
  for j in range(i+1,len(M)):
   for k in range(i+1,len(M)):M[j][k]=(M[j][k]*p-M[j][i]*M[i][k])//prev
  prev=p
 return True
hist=collections.Counter();sizes=collections.Counter();examples={}
for s,f in freq.items():
 a=list(map(int,s.split()));n=len(a);d=[v.bit_count() for v in a];least=sum(sorted(d)[:5]);degree=2*least>sum(d);L=[[d[i] if j==i else -((a[i]>>j)&1) for j in range(n)] for i in range(n)];lap=pd([[int(i==j)*n*least-5*(n-5)*L[i][j] for j in range(n)] for i in range(n)]);ok=not any(all(not a[i]>>j&1 for i,j in itertools.combinations(q,2)) for q in itertools.combinations(range(n),5));assert ok or not(lap or degree);hist[ok,degree,lap]+=f;sizes[n]+=f;examples.setdefault(str((ok,degree,lap)),a)
print(sizes,hist);(P/'ramsey_laplacian_exterior.json').write_text(json.dumps(dict(sizes=sizes,counts={str(k):v for k,v in hist.items()},examples=examples))+'\n')
