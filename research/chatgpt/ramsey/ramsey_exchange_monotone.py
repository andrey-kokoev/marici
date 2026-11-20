"""All independent neighborhoods at once; reverse reachability by bit masks."""
from collections import defaultdict, deque
from pathlib import Path
from pauli_realization_audit import decode_graph6


def audit(rows,k):
    ns=[0]
    for i,r in enumerate(rows):ns += [s|1<<i for s in ns if not s&r]
    blocks=[s for s in ns if s.bit_count()==k];full=(1<<len(ns))-1
    contains=[sum(1<<j for j,s in enumerate(ns) if s>>i&1) for i in range(len(rows))]
    faces=defaultdict(list); initial=[]
    for j,s in enumerate(blocks):
        mask=full
        for i in range(len(rows)):
            if s>>i&1:faces[s^(1<<i)].append((j,i));mask &= ~contains[i]
        initial.append(mask)
    results=[]
    for strict in (True,False):
        back=[[] for s in blocks]
        for pair in faces.values():
            if len(pair)==1:continue
            (a,x),(b,y)=pair;assert rows[x]>>y&1
            # a -> b removes x and adds y. N cannot contain both.
            back[b].append((a,contains[x] if strict else full^contains[y]))
            back[a].append((b,contains[y] if strict else full^contains[x]))
        reach=initial.copy();todo=deque(range(len(blocks)));pending=set(todo)
        while todo:
            b=todo.popleft();pending.remove(b)
            for a,permit in back[b]:
                delta=(reach[b]&permit)&~reach[a]
                if delta:
                    reach[a]|=delta
                    if a not in pending:todo.append(a);pending.add(a)
        results.append(sum(r==full for r in reach))
    return len(blocks),*results

if __name__=='__main__':
    for k,n in [(3,8),(4,13),(5,17),(6,22)]:
        codes=(Path(__file__).parent/'pauli-realization-catalogues'/f'r3{k+1}_{n}.g6').read_text().splitlines()
        out=[audit(decode_graph6(c),k) for c in codes];print(n,len(out),'strict/weak graph counts',[sum(r[i]>0 for r in out) for i in (1,2)],'weak starter range',min(r[2] for r in out),max(r[2] for r in out),'record 1',out[0],flush=True)
