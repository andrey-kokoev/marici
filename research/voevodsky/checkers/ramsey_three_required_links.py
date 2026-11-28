"""Remove predecessor tests in stages; use explicit blue-five witnesses for each required link."""
from itertools import combinations
from collections import Counter
import json
from ramsey_pentagon_selector import charts
from ramsey_inherited_swap_selector import D


def audit():
    rows=[frozenset(s) for s in combinations(range(1,10),3) if min(s[1]-s[0],s[2]-s[1])>=2]
    parts=[p for p in combinations(rows,3) if len(set().union(*p))==9];counts=Counter();examples={}
    for sq,_,cycles in charts():
        if any(10 in s for s in sq):continue
        sq=list(map(frozenset,sq))
        for p in parts:
            if set(p)&set(sq) or any(sum(bool(r&t) for t in p)<2 for r in sq):continue
            for cyc in cycles:
                edges=cyc|{(i,i+1) for i in range(1,10)}|{(i,11+j) for j,r in enumerate(sq) for i in r}
                def blue(q):return all(e not in edges for e in combinations(sorted(q),2))
                def pool(rs):return sorted(set(range(1,11))-set().union(*rs))+[11+j for j,r in enumerate(sq) if all(r&t for t in rs)]
                if any(not blue(t) or any(blue(q) for q in combinations(pool([t]),6)) for t in p):continue
                cert=[next((q for q in combinations(pool(pair),5) if blue(q)),None) for pair in combinations(p,2)];n=sum(x is not None for x in cert);counts[n]+=1
                if n not in examples:examples[n]=dict(square=[sorted(s) for s in sq],cycle=sorted(cyc),rows=[sorted(s) for s in p],pair_witnesses=cert)
    assert not counts and len(parts)==29
    result=dict(partitions=len(parts),eligible_triples=sum(counts.values()),by_required_links=counts,examples=examples);print(result);(D/'ramsey_three_required_links.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':audit()
