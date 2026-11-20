"""Propagate common core plus literal boundary, identify remaining graph and count its perfect matchings directly. Inspect whether connectivity follows from these constraints."""
from collections import Counter
from ramsey_strip_forced_local_propagation import adj,propagate
from ramsey_strip_connected_rotation_core import winners,leaves
core={(9,26),(14,15)};boundary={(0,16),(7,29)};chosen,left,rounds=propagate(core|boundary)
print('forced rounds',rounds,'unresolved vertices',sorted(left),'degree counts',dict(Counter(len(adj[v]&left) for v in left)))
todo=set(left);parts=[]
while todo:
    stack=[min(todo)];part=set()
    while stack:
        x=stack.pop()
        if x in part:continue
        part.add(x);stack.extend((adj[x]&left)-part)
    todo-=part;parts.append(part)
print('components',[(len(p),sum(len(adj[v]&p) for v in p)//2) for p in parts])
counts=Counter();solutions=set()
def grow(L,used):
    if not L:solutions.add(frozenset(used));return
    x=min(L,key=lambda v:(len(adj[v]&L),v));opts=adj[x]&L
    if not opts:counts['dead']+=1;return
    if len(opts)>1:counts[len(opts)]+=1
    for y in opts:grow(L-{x,y},used|{tuple(sorted((x,y)))})
grow(left,chosen);assert solutions==set(winners);print('local matching tree',dict(counts),'completions',len(solutions),'exactly the connected maximum-core candidates',True)
# Count core-only completions: oriented boundaries are additional constraints.
a,b,c=propagate(core);print('core alone forced rounds',c,'degree counts',dict(Counter(len(adj[v]&b) for v in b)))
