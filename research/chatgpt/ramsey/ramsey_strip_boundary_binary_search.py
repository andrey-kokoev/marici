"""Target-independent matching decision tree from literal directed boundary. Propagate degree one, then branch at a minimum-degree position; vertex order is an explicit arbitrary tie breaker. Compare leaves against exhaustive matching census."""
from collections import Counter
from ramsey_strip_forced_local_propagation import adj
from ramsey_strip_minimal_shared_constraints import allms,ms
counts=Counter();leaves={}
def visit(chosen,history):
    remaining=set(adj)-{v for e in chosen for v in e}
    while remaining:
        options={v:adj[v]&remaining for v in remaining}
        v=min(options,key=lambda v:(len(options[v]),v));d=len(options[v])
        if d==0:counts['dead']+=1;return
        if d!=1:break
        w,=options[v];chosen=chosen|{tuple(sorted((v,w)))};remaining-={v,w}
    if not remaining:leaves[frozenset(chosen)]=history;return
    counts[d]+=1
    for w in sorted(options[v]):visit(chosen|{tuple(sorted((v,w)))},history+[(v,w)])
initial={(0,16),(7,29)};visit(initial,[]);expected={m for m in allms if initial<=m};assert set(leaves)==expected
print('branch arities and dead ends',dict(counts),'matching leaves',len(leaves),'decision depths',dict(Counter(map(len,leaves.values()))))
target,=[m for m in ms if initial<=m];print('target branch trace',leaves[target]);print('first branch', sorted({h[0] for h in leaves.values()}))
