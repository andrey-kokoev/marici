"""Exact integer seven-support search on the fractional survivor. Repeating supports allowed. Use six-cliques for pair compatibility, then five-cliques for triple compatibility."""
import json,itertools,collections,sys
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';h=sys.argv[1] if len(sys.argv)>1 else json.loads((P/'ramsey_38_fractional46.json').read_text())['core'];a=[0]*20
for k,(i,j) in enumerate((i,j) for j in range(20) for i in range(j)):
 if int(h,16)>>k&1:a[i]|=1<<j;a[j]|=1<<i
I=[0]
for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q={n:[q for q in I if q.bit_count()==n] for n in (5,6)};M={n:[sum(1<<j for j,q in enumerate(qs) if not s&q) for s in S] for n,qs in Q.items()};hist=collections.Counter();examples={}
adj=[sum(1<<j for j in range(i,len(S)) if not x&M[6][j]) for i,x in enumerate(M[6])];
def rec(p,c,one,two,test):
 hist[len(p)]+=1
 if len(p)==7:return p
 while c:
  b=c&-c;c^=b;j=b.bit_length()-1;m=M[5][j]
  if test and m&two:continue
  z=rec(p+[j],adj[j]&(c|b),one|m,two|(one&m),test)
  if z:return z
out=dict(core=h,maximal_supports=len(S),fives=len(Q[5]),sixes=len(Q[6]))
for test in (False,True):
 hist.clear();p=rec([],2**len(S)-1,0,0,test);out['joint' if test else 'sixes_only']=dict(example=None if p is None else [S[j] for j in p],visited=dict(hist));print(test,out['joint' if test else 'sixes_only'],flush=True)
(P/(f'ramsey_38_integer47_{h}.json' if len(sys.argv)>1 else 'ramsey_38_integer46.json')).write_text(json.dumps(out)+'\n')
