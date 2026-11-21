"""Test the balanced-root and split-cycle conjectures independently."""
from pathlib import Path
import json
from itertools import permutations, combinations
from collections import Counter
from ramsey_six_point_reconstruction import pairs, graph, decode, independent
from ramsey_mutual_repair_conjecture import switches, apply

D=Path(__file__).parent
for row in json.loads((D/'ramsey_hall_center_conjecture.json').read_text())['regular']:
    A=decode(row['graph6'].encode()); roots=[]
    for r in range(22):
        traces=[A[r]&A[v] for v in range(22) if v!=r and not A[r]>>v&1]
        if all(t.bit_count()==2 for t in traces): roots.append((r,len(set(traces))))
    print(row['record'],roots)

def key(s,p):
    return tuple(tuple(sorted(tuple(sorted((p[u],p[v]))) for u,v in s[k])) for k in ('removed','added'))

for m in [0x42aa460550a,0x42c54a0550a]:
    A=graph(m);moves=list(switches(A));identity=list(range(22));todo={key(s,identity):s for s in moves}
    for q in permutations(range(6)):
        if q==tuple(range(6)):continue
        p=[0]+[1+i for i in q]+[7+pairs.index(tuple(sorted((q[i],q[j])))) for i,j in pairs]
        if all((A[i]>>j&1)==(A[p[i]]>>p[j]&1) for i,j in combinations(identity,2)):break
    else:raise AssertionError('no generator')
    stats=Counter()
    while todo:
        k=next(iter(todo));o=[]
        while k in todo:
            s=todo.pop(k);o.append(s);k=key(s,p)
        if len(o)!=5 or any(s['support']&t['support'] for s,t in combinations(o,2)):continue
        stats['disjoint']+=1;valid=[]
        for n in range(1,32):
            B=A[:]
            for i,s in enumerate(o):
                if n>>i&1:B=apply(B,s['removed'],s['added'])
            if not any(B[i]&B[j] for i,j in combinations(identity,2) if B[i]>>j&1) and not independent(B,(1<<22)-1,7):valid.append(n)
        if 31 in valid:stats['valid full']+=1
        if valid==[31]:stats['irreducible']+=1
    print(hex(m),len(moves),stats)
