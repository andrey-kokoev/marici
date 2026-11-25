"""Canonicalize requests by the maximal independent supports forbidden by at least one clause.
Compute them from the clauses with Bron-Kerbosch in the complement graph. Compare with exact enumeration.
"""
from itertools import combinations,product
from functools import cache
from pathlib import Path
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results'
def bits(m):return [i for i in range(8) if m>>i&1]
def maximal(L):return tuple(sorted(x for x in set(L) if not any(x!=y and x&y==x for y in L)))
def run(E,ref):
 F=255;A=[0]*8
 for a,b in E:A[a-1]|=1<<(b-1);A[b-1]|=1<<(a-1)
 G=[F&~(a|(1<<i)) for i,a in enumerate(A)]
 @cache
 def mis(m):
    out=[]
    def bk(R,P,X):
        if not(P|X):out.append(R);return
        while P:
            b=P&-P;i=b.bit_length()-1;bk(R|b,P&G[i],X&G[i]);P^=b;X|=b
    bk(0,m,0);return tuple(out)
 I=[x for x in range(256) if all(not x&A[i] for i in bits(x))];corners=list(product((1,2),(4,5),(7,8)));stats=Counter();results=[]
 for row in ref['rows']:
    T=row['T'];R=[];K=[];Sigs=[]
    for c in corners:
        s=sum(1<<(v-1) for v in c);b=[x for x in I if x.bit_count()==4 and not x&s];impossible=any(not x&T for x in b);r=b+[x for x in I if (x.bit_count()==4 and not x&T) or (x.bit_count()==3 and not x&(s|T))];raw=(0,) if impossible else tuple(sorted(x for x in set(r) if not any(y!=x and x&y==y for y in r)));key=maximal([u for x in raw for u in mis(F^x)]);sig=frozenset(u for u in I if all(u&x for x in raw));assert key==maximal([u for u in I if u not in sig]);R.append(raw);K.append(key);Sigs.append(sig)
    diffs=[]
    for i,j in combinations(range(8),2):
        assert (K[i]==K[j])==(Sigs[i]==Sigs[j]);stats['pair_comparisons']+=1
        if R[i]!=R[j] and K[i]==K[j]:
            diffs.append(dict(corners=[corners[i],corners[j]],requests=[R[i],R[j]],key=K[i],legal=len(Sigs[i])));stats['live' if Sigs[i] else 'dead']+=1
    assert bool(diffs)!=row['all8_profiles_exact']
    if diffs:results.append(dict(T=T,mergers=diffs))
 return dict(stats=stats,contexts=results)
if __name__=='__main__':
 r=json.loads((D/'ramsey_cube_conditional_folds.json').read_text());es=json.loads((D/'ramsey_cube_exterior_test.json').read_text());out={k:run(es[k]['edges'],ref) for k,ref in r.items()};(D/'ramsey_cube_relative_requests.json').write_text(json.dumps(out,indent=1));
 for k,v in out.items():print(k,v['stats'],[(r['T'],len(r['mergers'])) for r in v['contexts']]);print(v['contexts'][0]);
