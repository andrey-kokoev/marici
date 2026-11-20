"""Predict gains by adding one unlocked row to a surviving old optimal join.
Test on the first admissible induced 12-set of each catalogued 17-point graph.
Prediction is sufficient; more than one unlocked row can in principle be needed.
"""
from itertools import combinations,combinations_with_replacement
from pathlib import Path
from collections import Counter
from ramsey_join_fixed_order import solve
from pauli_realization_audit import decode_graph6

def cliques(edges):
    b=[0]
    for i in range(12):
        a=sum(1<<j for j in range(i) if (j,i) in edges);b += [x|1<<i for x in b if not a&x]
    return b

def audit(edges):
    ans=solve(edges)
    if not ans:return None
    d=ans[0];b=cliques(edges);rows=[s for s in b if not any(s!=t and s&t==s for t in b)]
    old=[]
    for rr in combinations_with_replacement(rows,d):
        tight=[]
        for c in b:
            load=c.bit_count()+sum(not r&c for r in rr)
            if load>5:break
            if load==5:tight.append(c)
        else:old.append((rr,tight))
    tally=Counter();gains=[]
    for e in sorted(edges):
        after=edges-{e};bb=cliques(after);new=set(bb)-set(b)
        if max(map(int.bit_count,bb))>4:tally['invalid']+=1;continue
        unlocked=[s for s in new if not any(s!=t and s&t==s for t in new)]
        pred=any(all(c.bit_count()+sum(not r&c for r in rr)<=5 for c in new) and any(all(u&c for c in tight) for u in unlocked) for rr,tight in old)
        actual=solve(after)[0]>d
        assert not pred or actual
        tally[pred,actual]+=1
        if actual:gains.append(tuple(i+1 for i in e))
    return d,dict(tally),gains

if __name__=='__main__':
    base={(i,j) for i,j in combinations(range(12),2) if j-i in (1,5,8)}
    print('original',audit(base),flush=True)
    for k,line in enumerate((Path(__file__).parent/'pauli-realization-catalogues/r36_17.g6').read_text().splitlines(),1):
        a=decode_graph6(line)
        for subset in combinations(range(17),12):
            edges={(i,j) for i,j in combinations(range(12),2) if a[subset[i]]>>subset[j]&1}
            if max(map(int.bit_count,cliques(edges)))<=4:
                print(k,subset,audit(edges),flush=True);break
        else:print(k,'no admissible subset',flush=True)
