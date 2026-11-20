"""Held-out tests: delete vertex 34 from the 35-circle; separately use cyclic 33 with distances 1,6,10,15. Keep previous pair classifier unchanged. Compare direct core size to inclusion-exclusion; look for same named degrees and pair counts but different outcome within host."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def inspect(n,edges):
    N=[set() for _ in range(n)];U=set(range(n))
    for i,j in edges:N[i].add(j);N[j].add(i)
    assert all(not N[i]&N[j] for i,j in edges)
    def independent(avail,k):
        if not k:return True
        while len(avail)>=k:
            x=avail.pop()
            if independent(avail-N[x],k-1):return True
        return False
    assert not independent(set(U),9)
    totals=Counter();example={};seen={};collision=None
    for q in combinations(range(n),4):
        pairs=list(combinations(q,2))
        if any(j in N[i] for i,j in pairs):continue
        d=tuple(len(N[i]) for i in q);p=tuple(len(N[i]&N[j]) for i,j in pairs);hi=[e for e,c in zip(pairs,p) if c==4];h=sorted(sum(i in e for e in hi) for i in q);pred=set(p)=={2,4} and h in ([1,1,2,2],[2,2,2,2]);triple=sum(len(set.intersection(*(N[i] for i in t))) for t in combinations(q,3));four=len(set.intersection(*(N[i] for i in q)));core=U-set(q)-set.union(*(N[i] for i in q));size=len(core);assert size==n-4-sum(d)+sum(p)-triple+four
        outcome=('true_' if pred==(size==13) else 'false_')+('positive' if pred else 'negative');totals[outcome]+=1
        row=dict(roots=q,degrees=d,pair_counts=p,triple_sum=triple,four=four,core_size=size);example.setdefault(outcome,row)
        key=(d,p);old=seen.setdefault(key,row)
        if collision is None and (old['core_size']==13)!=(size==13):collision=[old,row]
    return dict(counts=totals,examples=example,identical_degree_pair_collision=collision)
if __name__=='__main__':
    base=json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['plus_edges'];out={'deleted_34':inspect(34,[(i,j) for i,j in base if j<34]),'cyclic_33':inspect(33,[(i,j) for i,j in combinations(range(33),2) if min(j-i,33+i-j) in (1,6,10,15)])};print(json.dumps(out));(D/'ramsey_39_overlap_transfer.json').write_text(json.dumps(out,indent=2)+'\n')
