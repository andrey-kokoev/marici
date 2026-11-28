"""Test a local obstruction: fixed ordered port pair A,D and alternative tips B."""
from itertools import combinations, permutations
from functools import lru_cache
from collections import Counter,defaultdict
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import evaluate,D
import json


def audit():
    hist=Counter();gates=Counter();ex={};overlap=Counter();extensions=Counter();free_ports=Counter();one_port_example=None;tip_shape=Counter()
    for sq,_,cycles in charts():
        for cyc in cycles:
            edges=path|cyc|{(i,11+j) for j,r in enumerate(sq) for i in r};queries=[(s,) for s in combinations(range(1,11),3) if s not in sq and all(e not in path for e in combinations(s,2))];rows=sorted(s for s, in evaluate(10,sq,cyc,queries));blue={s:set(range(1,11))-set(s)|{11+j for j,r in enumerate(sq) if set(s)&set(r)} for s in rows}
            @lru_cache(None)
            def bad(t):return any(all(e not in edges for e in combinations(q,2)) for q in combinations(sorted(set.intersection(*(blue[s] for s in t))),7-len(t)))
            def ok(a,b):return set(a).isdisjoint(b) and all(set(r)&(set(a)|set(b)) for r in sq)
            tips=defaultdict(list)
            for t in combinations(rows,3):
                if not bad(t) or any(bad(p) for p in combinations(t,2)):continue
                for a,b,d in permutations(t):
                    if ok(a,b):tips[a,d].append(b)
            for (a,d),bs in tips.items():
                hist[len(bs)]+=1;tip_shape[len([r for r in sq if set(a).isdisjoint(r)]),len(bs)]+=1
                if sum(set(a).isdisjoint(r) for r in sq)==1:
                    U=set().union(*sq);W=set(range(1,11))-U;out_a,=set(a)-U
                    for b in bs:
                        movable,=set(d)&U
                        # Recover its axis from the square: the partner is the only
                        # other movable site absent from every corner through it.
                        fixed=set.intersection(*map(set,sq));partner,=[x for x in U-fixed-{movable} if not any({x,movable}<=set(r) for r in sq)]
                        assert set(b)&U=={movable,partner}-set(a)
                        out_b=set(b)-U;other=W-{out_a}-out_b
                        assert len(other)==2 and tuple(sorted(other)) not in cyc
                        assert (set(d)-U)-{out_a} and (set(d)-U)-{out_a}<=out_b
                for b,c in combinations(bs,2):
                    if bad(tuple(sorted((b,c)))):reason='BC pair fails'
                    elif bad(tuple(sorted((b,c,d)))):reason='BCD survives both repairs'
                    elif ok(a,d) and not bad(tuple(sorted((a,b,c)))):reason='AD alone suffices'
                    else:raise AssertionError((a,b,c,d))
                    overlap[len(set(b)&set(c))]+=1
                    q=next(q for q in combinations(sorted(blue[b]&blue[c]),5) if all(e not in edges for e in combinations(q,2)))
                    free=[r for r in sq if set(a).isdisjoint(r)];free_ports[len(free)]+=1
                    if len(free)<2 and one_port_example is None:one_port_example=dict(square=sq,cycle=sorted(cyc),A=a,B=b,C=c,D=d,free=free)
                    extensions[any(all(e not in edges for e in combinations(sorted((*a,*extra)),2)) for extra in combinations(sorted((blue[b]&blue[c])-set(a)),2))]+=1
                    gates[reason]+=1;ex.setdefault(reason,dict(square=sq,cycle=sorted(cyc),A=a,B=b,C=c,D=d,blue_five=q))
    out=dict(tips_per_hinge=hist,exclusions=gates,tip_overlap=overlap,blue_five_extends_A=extensions,ports_disjoint_from_A=free_ports,one_port_example=one_port_example,local_tip_counts={str(k):v for k,v in tip_shape.items()},examples=ex);print(out);(D/'ramsey_repair_hinge.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
