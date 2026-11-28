"""Hold the four supports and the square fixed across cycles. Retain all-blue pair legality."""
from itertools import combinations
from functools import lru_cache
from collections import Counter
import json
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import evaluate,D


def audit():
    counts=Counter();ex=None;edge_tests=[];stable=[]
    for sq,_,cycles in charts():
        if len(cycles)<2:continue
        Q=[(r,) for r in combinations(range(1,11),3) if r not in sq and not any(e in path for e in combinations(r,2))]; groups={}
        for cyc in cycles:
            rows=sorted(r for r, in evaluate(10,sq,cyc,Q));E=path|cyc|{(i,11+j) for j,r in enumerate(sq) for i in r};blue={s:set(range(1,11))-set(s)|{11+j for j,r in enumerate(sq) if set(s)&set(r)} for s in rows}
            @lru_cache(None)
            def bad(rs):return any(all(e not in E for e in combinations(q,2)) for q in combinations(sorted(set.intersection(*(blue[s] for s in rs))),7-len(rs)))
            allowed={p for p in combinations(rows,2) if set(p[0]).isdisjoint(p[1]) and all(set(r)&set(p[0]+p[1]) for r in sq)}
            for rs in combinations(rows,4):
                ps=list(combinations(rs,2));opts=[p for p in ps if p in allowed]
                if not any((ps[i] in allowed and ps[5-i] in allowed) for i in range(3)) or any(bad(p) for p in ps):continue
                triples=[t for t in combinations(rs,3) if bad(t)]
                n= (int(bad(rs)) if not triples else 1 if any(all(set(p)<=set(t) for t in triples) for p in opts) else 2)
                groups.setdefault(rs,[]).append((n,sorted(cyc),triples))
        for rs,items in groups.items():
            if len(items)<2 or not any(i[0]==2 for i in items):continue
            counts['compared_supports_with_two']+=1
            if min(i[0] for i in items)<2:
                counts['mixed']+=1
                if ex is None:ex=dict(square=sq,rows=rs,verdicts=items)
                W=set(range(1,11))-set().union(*sq);miss=tuple(sorted(W-set().union(*rs)))
                singles=[]
                for e in combinations(sorted(W),2):
                    table={color:sorted({n for n,c,_ in items if (e in c)==color}) for color in (False,True)}
                    if all(len(ns)==1 for ns in table.values()):singles.append(dict(edge=e,blue=table[False][0],red=table[True][0]))
                assert len(miss)==2 and all(W-set().union(*t)==set(miss) for t in combinations(rs,3))
                assert dict(edge=miss,blue=2,red=0) in singles
                edge_tests.append(dict(square=sq,rows=rs,missed=miss,readouts=singles,verdicts=items))
            else:
                W=set(range(1,11))-set().union(*sq);miss=tuple(sorted(W-set().union(*rs)));same=all(W-set().union(*t)==set(miss) for t in combinations(rs,3));always_edges=set().union(*(set(c) for _,c,_ in items));known=path|{(i,11+j) for j,r in enumerate(sq) for i in r};families=[]
                for forbidden in (set(combinations(sorted(W),2)),always_edges):
                    found=[]
                    for t in combinations(rs,3):
                        pool=sorted(set(range(1,11))-set().union(*t))+[11+j for j,r in enumerate(sq) if all(set(s)&set(r) for s in t)]
                        q=next((q for q in combinations(pool,4) if all(e not in known|forbidden for e in combinations(q,2))),None)
                        if q:found.append(dict(triple=t,four=q))
                    families.append(found)
                assert len(miss)==2 and same and not families[0] and len(families[1])==2 and all(miss not in c for _,c,_ in items)
                red_candidates=[c for c in cycles if miss in c];single_pass=[c for c in red_candidates if len(evaluate(10,sq,c,[(r,) for r in rs]))==4]
                stable.append(dict(square=sq,rows=rs,missed=miss,same=same,red_candidates=len(red_candidates),red_after_singles=len(single_pass),miss_red=sorted({miss in c for _,c,_ in items}) if len(miss)==2 else None,independent=families[0],common=families[1],verdicts=items))
    print(counts,ex);(D/'ramsey_two_repairs_support_control.json').write_text(json.dumps(dict(counts=counts,example=ex,edge_tests=edge_tests,stable=stable),indent=2)+'\n')
if __name__=='__main__':audit()
