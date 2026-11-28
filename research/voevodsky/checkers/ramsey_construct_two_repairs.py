"""Build two-repair quartets from a missed blue edge and one movable pair."""
from itertools import combinations, permutations
from functools import lru_cache
from collections import Counter
from hashlib import sha256
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D
import json


def audit():
    keys=set();counts=Counter();example=None;edge_report=[]
    for sq,_,cycles in charts():
        U=set().union(*sq);fixed,=set.intersection(*map(set,sq));W=set(range(1,11))-U;mov=U-{fixed};axes=[e for e in combinations(sorted(mov),2) if all(not set(e)<=set(r) for r in sq)]
        for cyc in cycles:
            core=path|cyc;E=core|{(i,11+j) for j,r in enumerate(sq) for i in r}
            @lru_cache(None)
            def blue(s):return set(range(1,11))-set(s)|{11+j for j,r in enumerate(sq) if set(r)&set(s)}
            @lru_cache(None)
            def bad(t):return any(all(e not in E for e in combinations(q,2)) for q in combinations(sorted(set.intersection(*(blue(s) for s in t))),7-len(t)))
            def option(p):return set(p[0]).isdisjoint(p[1]) and all(set(r)&set(p[0]+p[1]) for r in sq)
            for edge in combinations(sorted(W),2):
                if edge in cyc:continue
                K=W-set(edge)
                edge_counts=[]
                for X in axes:
                    flank=(min(X)-1,max(X)+1)==edge;before=len(keys)
                    matches=[]
                    for pair in combinations(sorted(K),2):
                        if pair in cyc:continue
                        a,=K-set(pair)
                        for x,other in permutations(X):
                            s=tuple(sorted((*pair,x)))
                            for y in mov-set(X):
                                d=tuple(sorted((a,other,y)))
                                if any(e in core for r in (s,d) for e in combinations(r,2)) or not option((s,d)) or bad((s,)) or bad((d,)):continue
                                matches.append((s,d))
                    for (s,d),(t,h) in combinations(matches,2):
                        if s==t or d==h:continue
                        counts['proposals']+=1;rs=tuple(sorted((s,d,t,h)));pairs=list(combinations(rs,2))
                        if any(bad(p) for p in pairs):continue
                        # Each fixed repair must be necessary. Its triple uses the other single row.
                        triples=[(s,d,t),(t,h,s)]
                        def completes(tr):
                            sites=[v for v in U-set().union(*tr) if all(abs(v-i)!=1 for i in edge)]
                            ports=[r for r in sq if all(set(r)&set(z) for z in tr)]
                            return any(v!=fixed and (any(w!=v and abs(v-w)!=1 for w in sites) or any(v not in r for r in ports)) for v in sites)
                        if not all(completes(tr) for tr in triples) or option((s,t)):continue
                        key=(sq,tuple(sorted(cyc)),rs);assert key not in keys;keys.add(key)
                        if example is None:example=dict(square=sq,cycle=sorted(cyc),missed=edge,axis=X,matches=((s,d),(t,h)))
                    clear=all(abs(y-i)!=1 for y in mov-set(X) for i in edge)
                    assert (len(keys)>before)==(flank and clear)
                    if flank:edge_counts.append(dict(axis=X,other_axis_clear=clear,outputs=len(keys)-before))
                edge_report.append(dict(square=sq,cycle=sorted(cyc),missed=edge,flanks=edge_counts))
    packed=json.dumps(sorted(keys),separators=(',',':')).encode();out=dict(counts=dict(counts,constructed=len(keys)),digest=sha256(packed).hexdigest(),example=example,edge_report=edge_report);print(dict(counts=counts,constructed=len(keys)));(D/'ramsey_construct_two_repairs.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
