"""Canonical residual join key via ordered binary decision diagram (Bryant, 1986).
Build from clause diagrams by symbolic conjunction; enumerate full colorings only in the independent audit.
"""
from functools import cache
from collections import defaultdict
from pathlib import Path
import json
from ramsey_join_residual_key import constraints

def probe(n,k):
    edges,masks=constraints(n,k);m=len(edges);nodes=[(m,0,0),(m,1,1)];intern={}
    def node(i,l,h):
        if l==h:return l
        t=(i,l,h)
        if t not in intern:intern[t]=len(nodes);nodes.append(t)
        return intern[t]
    @cache
    def join(a,b):
        if min(a,b)==0:return 0
        if a==1:return b
        if b==1 or a==b:return a
        i=min(nodes[a][0],nodes[b][0]);al,ah=nodes[a][1:] if nodes[a][0]==i else (a,a);bl,bh=nodes[b][1:] if nodes[b][0]==i else (b,b)
        return node(i,join(al,bl),join(ah,bh))
    root=1
    for bad,sets in [(1,masks[3]),(0,masks[k])]:
        for s in sets:
            q=0
            for i in reversed(range(m)):
                if s>>i&1:q=node(i,1,q) if bad else node(i,q,1)
            root=join(root,q)
    reached=set();todo=[root]
    while todo:
        a=todo.pop()
        if a in reached:continue
        reached.add(a)
        if a>=2:todo.extend(nodes[a][1:])
    # Independent completeness and soundness comparison. Use all prefixes, even dead ones.
    models=[v for v in range(1<<m) if all(v&r!=r for r in masks[3]) and all(v&b for b in masks[k])];tot=0;summary={}
    for cut in range(m+1):
        groups=defaultdict(list);future=defaultdict(list)
        for v in models:future[v% (1<<cut)].append(v>>cut)
        bykey={};byfuture={}
        for x in range(1<<cut):
            a=root
            while nodes[a][0]<cut:
                i,l,h=nodes[a];a=h if x>>i&1 else l
            f=tuple(future.get(x,()));assert bykey.setdefault(a,f)==f and byfuture.setdefault(f,a)==a;groups[a].append(x);tot+=1
        # Provenance: the prefix list and common suffix list give exactly the full witnesses, once each.
        assert {x|(s<<cut) for a,xx in groups.items() for x in xx for s in bykey[a]}==set(models)
        if cut==m//2:summary={'cut':cut,'live_prefixes':sum(len(xx) for a,xx in groups.items() if bykey[a]),'live_keys':sum(bool(bykey[a]) for a in groups),'max_live_bucket':max((len(xx) for a,xx in groups.items() if bykey[a]),default=0)}
    return dict(n=n,k=k,models=len(models),reachable_decisions=len(reached-{0,1}),allocated_decisions=len(nodes)-2,verified_prefixes=tot,midpoint=summary)
if __name__=='__main__':
    results=[probe(n,k) for k in (3,4) for n in (5,6)];print(json.dumps(results,indent=2));(Path(__file__).resolve().parents[1]/'results/ramsey_join_diagram_key.json').write_text(json.dumps(results,indent=2)+'\n')
