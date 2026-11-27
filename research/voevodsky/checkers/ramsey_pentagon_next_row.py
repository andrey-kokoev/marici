"""Labeled width-ten next-row languages of the 122 path-preserving square completions."""
from itertools import combinations,permutations
from collections import Counter
from functools import reduce
from pathlib import Path
import json

k=10;F=(1<<k)-1;D=Path(__file__).resolve().parents[1]/'results';fmt=lambda m:[i+1 for i in range(k) if m>>i&1]
def run():
    rows={sum(1<<i for i in s) for s in combinations(range(k),3) if min(s[1]-s[0],s[2]-s[1])>=2};sqs=set()
    for m in rows:
        moves=[3<<i for i in range(k-1) if (m&(3<<i)).bit_count()==1 and m^(3<<i) in rows]
        for a,b in combinations(moves,2):
            if not a&b and m^a^b in rows:sqs.add(tuple(sorted((m,m^a,m^b,m^a^b))))
    hist=Counter();examples={};total=0
    for sq in sorted(sqs):
        W=fmt(F^reduce(int.__or__,sq));path={(i,i+1) for i in range(1,10)};profiles=[]
        for tail in permutations(W[1:]):
            if tail[0]>tail[-1]:continue
            ring=(W[0],)+tail;cycle={tuple(sorted((ring[i-1],ring[i]))) for i in range(5)}
            if any(set(e)<=set(W) and e not in cycle for e in path) or any(j-i==2 for i,j in cycle):continue
            edges=[(1<<(i-1))|(1<<(j-1)) for i,j in path|cycle];cap=[0]*(F+1)
            for m in range(1,F+1):
                bit=m&-m;nb=reduce(int.__or__,(e for e in edges if e&bit),0);cap[m]=max(cap[m^bit],1+cap[m&~(nb|bit)])
            combos=[(ids,reduce(int.__or__,(sq[i] for i in ids),0)) for n in range(5) for ids in combinations(range(4),n)];plain=set();flex=set();triok=set()
            for s in rows-set(sq):
                if any(s&e==e for e in edges):continue
                triok.add(s);bad=[ids for ids,u in combos if len(ids)+1+cap[F&~(u|s)]>=7];red={i for i,r in enumerate(sq) if not r&s}
                if not bad:plain.add(s)
                if all(red.intersection(ids) for ids in bad):flex.add(s)
            assert not plain;hist['flex_row_cases']+=len(flex);hist['triangle_free_row_cases']+=len(triok)
            profiles.append((ring,plain,flex,triok));total+=1
        if profiles:
            hist['squares']+=1;hist['multiple']+=len(profiles)>1
            for j,key in [(1,'plain'),(2,'flex')]:
                classes=len({frozenset(p[j]) for p in profiles});hist[key+'_classes']+=classes;hist[key+'_splits']+=classes>1
            for l,r in combinations(profiles,2):
                for a,b in ((l,r),(r,l)):
                    for s in sorted(a[2]-b[2]):
                        reason='blue' if s in b[3] else 'triangle';examples.setdefault(reason,dict(square=list(map(fmt,sq)),accept=a[0],reject=b[0],next=fmt(s),red_to=[fmt(m) for m in sq if not m&s]))
                hist['pairs']+=1;hist['separated_even_if_individually_triangle_free']+=bool((l[2]^r[2])&l[3]&r[3])
    assert total==122 and hist['squares']==54;out=dict(completions=total,counts=hist,examples=examples);print(out);(D/'ramsey_pentagon_next_row.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
