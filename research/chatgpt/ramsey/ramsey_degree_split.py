"""Construct regular two-address extensions from residual degrees and component flips."""
from collections import Counter
from itertools import combinations,product
from ramsey_37_pair_rotation_rule import build
from ramsey_difference_next_round import add,ids
from pauli_realization_audit import independent_witness,triangle_free


def split(rows):
    by={d:[i for i,r in enumerate(rows) if r.bit_count()==d] for d in (4,5,6)}
    assert sum(map(len,by.values()))==len(rows)
    common=sum(1<<i for i in by[4]);todo=set(by[5]);parts=[]
    while todo:
        start=min(todo);side={start:0};stack=[start];todo.remove(start)
        while stack:
            i=stack.pop()
            for j in by[5]:
                if not rows[i]>>j&1:continue
                if j in side:assert side[i]!=side[j]
                else:side[j]=1-side[i];stack.append(j);todo.remove(j)
        parts.append(tuple(sum(1<<i for i in side if side[i]==s) for s in (0,1)))
    candidates=set();wins=set()
    for signs in product((0,1),repeat=len(parts)):
        p=q=common
        for (x,y),s in zip(parts,signs):p|=(y if s else x);q|=(x if s else y)
        p,q=sorted((p,q));e=6-p.bit_count()
        if e not in (0,1) or q.bit_count()+e!=6:continue
        item=(p,q,e)
        if item in candidates:continue
        candidates.add(item);g=add(add(rows,p),q|(e<<len(rows)))
        if triangle_free(g) and independent_witness(g,7) is None:wins.add(item)
    return by,parts,candidates,wins

if __name__=='__main__':
    g=build();hist=Counter()
    for u,v in combinations(range(22),2):
        old=[i for i in range(22) if i not in (u,v)]
        proj=lambda r:sum((r>>i&1)<<j for j,i in enumerate(old))
        by,parts,candidates,wins=split([proj(g[i]) for i in old]);actual=(*sorted((proj(g[u]),proj(g[v]))),g[u]>>v&1)
        assert actual in wins;hist[len(wins)]+=1
        if (u,v)==(20,21):print('classes',by,'components',[(ids(x),ids(y)) for x,y in parts],'candidates',len(candidates),'wins',[(ids(x),ids(y),s) for x,y,s in wins])
    print('regular completions per deletion',dict(hist))
