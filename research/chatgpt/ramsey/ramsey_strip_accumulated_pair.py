"""Resolve the two full matchings preserving all three shared residues. Inspect row-swap action and the symmetric-difference components."""
from ramsey_strip_accumulated_residue_extension import C,ids,N
from ramsey_strip_matching_restart import turn,r
fixed=set.union(*(set(C[i]) for i in ids));used={v for e in fixed for v in e}
def fill(L,R):
    if not L:yield frozenset(fixed);return
    i=min(L,key=lambda i:len(N[i]&R))
    for j in sorted(N[i]&R):
        for m in fill(L-{i},R-{j}):yield m|{(i,j)}
ms=list(fill(set(range(15))-used,set(range(15,30))-used));assert len(ms)==2
print('swap images indices',[ms.index(turn(m)) if turn(m) in ms else None for m in ms]);a,b=ms;common=a&b;diff=a^b;adj={}
for i,j in diff:adj.setdefault(i,set()).add(j);adj.setdefault(j,set()).add(i)
assert all(len(n)==2 for n in adj.values());todo=set(adj);cycles=[]
while todo:
 start=min(todo);cycle=[start];prev=None;cur=start
 while True:
    nxt=min(adj[cur]-({prev} if prev is not None else set()))
    if nxt==start:break
    cycle.append(nxt);prev,cur=cur,nxt
 todo-=set(cycle);cycles.append(cycle)
print('common links',sorted(common),'extra shared beyond input',sorted(common-fixed));print('alternating cycles',cycles,'row-fixed positions',[[v for v in c if r[v]==v] for c in cycles]);print('new matching pair', [sorted(m) for m in ms])
