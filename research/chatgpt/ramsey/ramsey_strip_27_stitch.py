"""Is the unique mixed pattern an articulation under a one-half replacement? Compare exact sharing versus sharing a half's two ordered mark readings. Edges are defined before looking at outcomes."""
from ramsey_strip_37_order_control import bins,ps,words,combinations
from collections import defaultdict,Counter
mixed,=[k for k,c in bins.items() if len(c)==2]
def components(g,keep):
    todo=set(keep);out=[]
    while todo:
        root=todo.pop();c={root};stack=[root]
        while stack:
            new=g[stack.pop()]&todo;todo-=new;c|=new;stack.extend(new)
        out.append(c)
    return out
for mode in ('exact half','mark signature'):
    carriers=defaultdict(set);g={k:set() for k in bins}
    for p,q in combinations(ps,2):
        if not set(p).isdisjoint(q):continue
        key=tuple(sorted((words[p],words[q])))
        for h in (p,q):carriers[h if mode=='exact half' else words[h]].add(key)
    for s in carriers.values():
        for a,b in combinations(s,2):g[a].add(b);g[b].add(a)
    before=components(g,g);after=components(g,set(g)-{mixed});types=lambda c:dict(Counter('mixed' if len(bins[x])==2 else ('closes' if True in bins[x] else 'fails') for x in c));base=next(c for c in before if mixed in c);print(mode,'before',sorted(map(len,before)),'after',sorted(map(len,after)),'component',types(base),'neighbors',types(g[mixed]),'articulations',sum(len(components(g,set(g)-{k}))>len(before) for k in g));print('remainder of mixed component',[types(c) for c in after if c<=base]);print('direct pure opposite links',sum(1 for x in g if set(bins[x])=={True} for y in g[x] if set(bins[y])=={False}))
