"""Find every cycle of four permitted links before pair tests; check its blue seven."""
from itertools import combinations
from collections import Counter
import json
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import evaluate,D


def audit():
    counts=Counter()
    for sq,_,cycles in charts():
        U=set().union(*sq)
        for cyc in cycles:
            E=path|cyc|{(i,11+j) for j,r in enumerate(sq) for i in r};rows=sorted(s for s, in evaluate(10,sq,cyc,[(s,) for s in combinations(range(1,11),3) if s not in sq and all(e not in path for e in combinations(s,2))]));N={r:set() for r in rows}
            for a,b in combinations(rows,2):
                if set(a).isdisjoint(b) and all(set(r)&(set(a)|set(b)) for r in sq):N[a].add(b);N[b].add(a)
            for a,c in combinations(rows,2):
                for b,d in combinations(sorted(N[a]&N[c]),2):
                    if (a,c)>(b,d):continue
                    ring=[a,b,c,d];i=next((i for i,r in enumerate(ring) if len(set(r)&U)==1),None)
                    if i is not None:
                        s=ring[i];p=ring[i-1];q=ring[(i+1)%4];five=list(s)+[11+j for j,r in enumerate(sq) if set(s).isdisjoint(r)];kind='one movable'
                    else:
                        p,q=a,c;ports=[11+j for j,r in enumerate(sq) if set(p)&set(r) and set(q)&set(r)];miss=set(range(1,11))-U-set(p)-set(q);pair=next(e for e in combinations(sorted(miss),2) if e not in E);five=ports+list(pair);kind='two movable throughout'
                    assert len(five)==5 and all(e not in E for e in combinations(sorted(five),2))
                    assert all(i not in five for r in (p,q) for i in r) and all(11+j not in five or (set(r)&set(p) and set(r)&set(q)) for j,r in enumerate(sq));counts[kind]+=1
    print(counts);(D/'ramsey_pairing_cycle_obstruction.json').write_text(json.dumps(counts,indent=2)+'\n')
if __name__=='__main__':audit()
