"""Read endpoint-extension obstructions on the old graph, then check actual extensions."""
from itertools import combinations,pairwise
from collections import Counter
import json
from ramsey_inherited_swap_selector import evaluate,run,D


def audit():
    counts=Counter();examples={};shapes=Counter()
    def inspect(sq,path,swaps,children):
        old={tuple(sorted(e)) for e in pairwise(path)};core=old|{(i,i+1) for i in range(1,9)}
        # Old ports use abstract labels 11..14, so that 10 is available for insertion.
        graph=core|{(i,11+j) for j,r in enumerate(sq) for i in r}
        ends={path[0],path[-1]};neighbors=ends|{9};U=set().union(*sq)
        candidate=old|{(i,10) for i in ends}
        independent=lambda q:all(e not in graph for e in combinations(sorted(q),2))
        pool=sorted((set(range(1,10))-neighbors)|set(range(11,15)))
        invalid=(9 not in U and 9 not in ends) or not independent(neighbors) or any(independent(q) for q in combinations(pool,6))
        interior_nine=9 in path[1:-1]
        boundary_triangle=9 in U and 8 in ends
        assert invalid==(interior_nine or boundary_triangle)
        if interior_nine:counts['nine_inside_outside_path']+=1
        if boundary_triangle:counts['covered_nine_endpoint_eight']+=1
        assert (not invalid)==any(c==candidate for c,v in children)
        if invalid:counts['invalid_core']+=1;return
        counts['valid_core']+=1
        queries=[(s,) for s in combinations(range(1,10),3) if s not in sq and min(s[1]-s[0],s[2]-s[1])>=2]
        rows=evaluate(9,sq,old,queries);actual=evaluate(10,sq,candidate,queries);assert actual<=rows
        fives=[q for q in combinations(pool,5) if independent(q)];lost=0
        fixed,=set.intersection(*map(set,sq));target=tuple(sorted({fixed}|ends))
        predicted={target} if all(b-a>1 for a,b in pairwise(target)) else set()
        for (s,) in rows:
            red=set(s)|{11+j for j,r in enumerate(sq) if set(r).isdisjoint(s)}
            witness=next((q for q in fives if red.isdisjoint(q)),None)
            direct=all(set(s)&set(r) for r in sq) and bool(set(path[1:-1])-set(s))
            assert bool(witness)==direct==((s,) not in actual)
            if witness:
                shapes[tuple(sorted({sum(v>10 for v in q) for q in fives if red.isdisjoint(q)}))]+=1
                lost+=1;examples.setdefault('loss',dict(square=sq,path=path,row=s,neighbors=sorted(neighbors),five=witness))
        assert predicted=={s for (s,) in rows-actual}
        if not lost:
            kept=next(v for c,v in children if c==candidate);missing=swaps-kept
            counts['all_rows_and_all_swaps']+=not missing;counts['all_rows_some_swaps_lost']+=bool(missing)
            counts['inherited_swaps_on_all_row_cases']+=len(swaps);counts['lost_swaps_on_all_row_cases']+=len(missing)
            counts['all_rows_no_old_swaps']+=not swaps
            # A missed old outside site h and new site 10 are the only outside
            # sites jointly omitted by a swap that changes its outside pair.
            mov=U-{fixed};expected=set()
            for s,t in swaps:
                A,B=set(s)-U,set(t)-U
                if A==B:continue
                h,=set(path)-A-B;z,=set(s)&U
                p,=[v for v in mov-{z} if not any({z,v}<=set(r) for r in sq)]
                if abs(p-h)!=1 and p!=9:
                    expected.add((s,t));examples.setdefault('joint_loss',dict(square=sq,path=path,rows=(s,t),partner=p,missed_old=h))
            assert expected==missing
        counts['lost_rows']+=lost;counts['old_rows']+=len(rows);counts['all_rows_survive']+=not lost
    run(inspect);result=dict(counts=counts,port_counts_in_witnesses={str(k):v for k,v in shapes.items()},examples=examples);print(result);(D/'ramsey_inherited_endpoint_shadow.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':audit()
