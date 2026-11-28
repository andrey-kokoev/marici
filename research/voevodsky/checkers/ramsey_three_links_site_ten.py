"""Disjoint legal rows using site 10 on every carried width-ten square."""
from itertools import combinations
from collections import Counter
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import evaluate,D
import json


def run():
    counts=Counter();blocked=Counter();example=None;repairs=Counter();two_example=None
    for sq,_,cycles in charts():
        if any(10 in s for s in sq):continue
        fixed,=set.intersection(*map(set,sq));U=set().union(*sq)
        triples=[s for s in combinations(range(1,11),3) if s not in sq and all(e not in path for e in combinations(s,2))]
        for cycle in cycles:
            counts['cycles']+=1
            legal={s for s, in evaluate(10,sq,cycle,[(s,) for s in triples])};assert all(fixed not in s for s in legal)
            graph=path|cycle|{(i,11+j) for j,r in enumerate(sq) for i in r}
            fives=[q for q in combinations(range(1,15),5) if not any(e in graph for e in combinations(q,2))]
            blue={s:set(range(1,11))-set(s)|{11+j for j,r in enumerate(sq) if set(s)&set(r)} for s in legal}
            for rows in combinations(sorted(legal),3):
                if len(set().union(*rows))!=9:continue
                counts['disjoint_triples']+=1
                repeated,=[s for s in rows if len(set(s)&U)==2];corner=tuple(sorted({fixed}|(set(repeated)&U)));assert corner in sq
                others=[s for s in rows if s!=repeated];assert all(set(corner).isdisjoint(s) for s in others)
                blocks=[p for p in combinations(rows,2) if any(set(r).isdisjoint(set().union(*p)) for r in sq)];blocked[len(blocks)]+=1
                witnesses={p:next((q for q in fives if set(q)<=blue[p[0]]&blue[p[1]]),None) for p in combinations(rows,2)}
                assert all(len((blue[a]&blue[b])-set(range(1,11)))==1 for a,b in combinations(rows,2))
                assert set.intersection(*(blue[s] for s in rows))=={fixed}
                need=[p for p,q in witnesses.items() if q];allowed=[p for p in need if p not in blocks];impossible=any(p in blocks for p in need);repairs[len(allowed),impossible]+=1
                if len(allowed)==2 and not impossible and two_example is None:
                    two_example=dict(square=sq,cycle=sorted(cycle),rows=rows,forced_red=[dict(pair=p,blue_five=witnesses[p]) for p in allowed],forced_blue=blocks)
                if example is None:example=dict(square=sq,cycle=sorted(cycle),rows=rows,corner=corner,blocked_pair=others)
    result=dict(counts=counts,blocked_pairs_per_triple=blocked,required_allowed_links_and_blocked_link_required={str(k):v for k,v in repairs.items()},example=example,two_example=two_example);print(result);(D/'ramsey_three_links_site_ten.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':run()
