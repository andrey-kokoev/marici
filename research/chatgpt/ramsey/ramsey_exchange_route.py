"""Can a fixed exchange component reach a disjoint block for every blue N?
It suffices to test inclusion-maximal independent sets N, not only maximum sets.
"""
from itertools import combinations
from collections import defaultdict,Counter
from pathlib import Path
from pauli_realization_audit import decode_graph6

def audit(a,k):
    full=(1<<len(a))-1; independent=[0]
    for i,row in enumerate(a):independent.extend([s|1<<i for s in independent if not row&s])
    blocks={s for s in independent if s.bit_count()==k}; assert max(s.bit_count() for s in independent)==k
    ns=[s for s in independent if all((s>>i&1) or row&s for i,row in enumerate(a))]
    faces=defaultdict(list)
    for s in blocks:
        for i in range(len(a)):
            if s>>i&1:faces[s^(1<<i)].append(s)
    adj=defaultdict(set)
    for v in faces.values():
        for s,t in combinations(v,2):adj[s].add(t);adj[t].add(s)
    todo=set(blocks);sizes=[];total=0
    while todo:
        s=todo.pop();stack=[s];comp=[s];total+=1
        while stack:
            for t in adj[stack.pop()] & todo:todo.remove(t);comp.append(t);stack.append(t)
        if all(any(not x&n for x in comp) for n in ns):sizes.append(len(comp))
    return total,sizes

if __name__=='__main__':
    for k,n in [(3,8),(4,13),(5,17),(6,22)]:
        path=Path(__file__).parent/'pauli-realization-catalogues'/f'r3{k+1}_{n}.g6';data=[audit(decode_graph6(l),k) for l in path.read_text().splitlines()];win=[min(s) for _,s in data if s];print(n,len(data),len(win),'min qualifying component range', (min(win),max(win)) if win else None, 'record 1',data[0],flush=True)
