"""Count monochromatic subsets directly on a fixed-point-free half-turn quotient.
Python standard library. Pair i has copies 2*i and 2*i+1 in the test fixtures.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
from pauli_realization_audit import decode_graph6


def quotient(rows):
    n=len(rows); assert n%2==0
    assert all((rows[i]>>j&1)==(rows[i^1]>>(j^1)&1) for i,j in combinations(range(n),2))
    return ([rows[2*i]>>(2*i+1)&1 for i in range(n//2)],
            {(i,j):(rows[2*i]>>(2*j))&3 for i,j in combinations(range(n//2),2)})


def independent_counts(q,k):
    """Histogram by number of double selections. Red = set bit."""
    internal,edges=q; n=len(internal);counts=Counter()
    for d in range(k//2+1):
        for D in combinations([i for i in range(n) if not internal[i]],d):
            if any(edges[p] for p in combinations(D,2)):continue
            available=[i for i in range(n) if i not in D and all(not edges[min(i,j),max(i,j)] for j in D)]
            for S in combinations(available,k-2*d):
                adj={i:[] for i in S};ok=True
                for i,j in combinations(S,2):
                    m=edges[i,j]
                    if m==3:ok=False;break
                    if m: # avoid parallel (1) -> opposite bits; avoid crossed (2) -> equal bits
                        b=int(m==1);adj[i].append((j,b));adj[j].append((i,b))
                if not ok:continue
                value={}; components=0
                for i in S:
                    if i in value:continue
                    components+=1;value[i]=0;stack=[i]
                    while stack and ok:
                        v=stack.pop()
                        for w,b in adj[v]:
                            t=value[v]^b
                            if w not in value:value[w]=t;stack.append(w)
                            elif value[w]!=t:ok=False;break
                    if not ok:break
                if ok:counts[d]+=2**components
    return counts


def check(rows):
    q=quotient(rows);qc=([1-b for b in q[0]],{p:3^m for p,m in q[1].items()});out=[]
    for k,red,model in [(3,1,qc),(7,0,q)]:
        hist=independent_counts(model,k);direct=Counter()
        for t in combinations(range(len(rows)),k):
            if all((rows[i]>>j&1)==red for i,j in combinations(t,2)):
                direct[k-len({i//2 for i in t})]+=1
        assert hist==direct;out.append(dict(sorted(hist.items())))
    return out


def main():
    rows=decode_graph6((Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines()[173]);print('base',check(rows))
    for action,pairs in [('remove',[(6,14),(7,15)]),('add',[(0,4),(1,5)])]:
        a=rows[:]
        for i,j in pairs:
            assert bool(a[i]>>j&1)==(action=='remove');a[i]^=1<<j;a[j]^=1<<i
        print(action,pairs,check(a))

if __name__=='__main__':main()
