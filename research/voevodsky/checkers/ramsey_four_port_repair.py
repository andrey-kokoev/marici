"""Find a labeled four-port attachment requiring two repairs. Verify all 64 link masks."""
from itertools import combinations
from functools import lru_cache
from collections import Counter
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import evaluate,D
import json


def find(shared=False):
    by_pairings=Counter();shape=Counter();representatives={};coverage=Counter();certs={};completion_types=Counter();per_triple=Counter();quartet_last=Counter();shared_shapes=Counter()
    from hashlib import sha256
    positive_keys=[]
    square_count=cycle_count=quartets=two=shared_min=unique_shared=0
    for sq,_,cycles in charts():
        if not shared and any(10 in s for s in sq):continue
        square_count+=1
        for cyc in cycles:
            cycle_count+=1
            queries=[(s,) for s in combinations(range(1,11),3) if s not in sq and not any(e in path for e in combinations(s,2))];rows=sorted(s for s, in evaluate(10,sq,cyc,queries));core=path|cyc|{(i,11+j) for j,r in enumerate(sq) for i in r};blue={s:set(range(1,11))-set(s)|{11+j for j,r in enumerate(sq) if set(r)&set(s)} for s in rows}
            @lru_cache(None)
            def witness(group):
                return next((q for q in combinations(sorted(set.intersection(*(blue[s] for s in group))),7-len(group)) if all(e not in core for e in combinations(q,2))),None)
            def allowed(p):
                a,b=p;return set(a).isdisjoint(b) and all(set(r)&(set(a)|set(b)) for r in sq)
            for rs in combinations(rows,4):
                if not shared and not any(10 in s for s in rs):continue
                quartets+=1
                pairs=list(combinations(rs,2))
                if any(witness(p) for p in pairs):continue
                bad=[t for t in combinations(rs,3) if witness(t)]
                if len(bad)<2:continue
                opts=[p for p in pairs if allowed(p)];hits=lambda es:all(any(set(p)<=set(t) for p in es) for t in bad)
                if any(hits([p]) for p in opts):continue
                repair=next((es for es in combinations(opts,2) if hits(es)),None)
                if repair is None:continue
                if shared:
                    minima=[es for es in combinations(opts,2) if hits(es)]
                    positive_keys.append((sq,tuple(sorted(cyc)),rs))
                    two+=1;adjacent=[es for es in minima if set(es[0])&set(es[1])];shared_min+=bool(adjacent);unique_shared+=len(minima)==1 and bool(adjacent)
                    W=set(range(1,11))-set().union(*sq);miss=W-set().union(*rs);triples=list(combinations(rs,3));same=all(W-set().union(*t)==miss for t in triples);color=tuple(sorted(miss)) in cyc if len(miss)==2 else None
                    # Flip only the missed edge as a diagnostic (not a successor).
                    # Once all pairs pass, adding red cannot create a blue seven.
                    killed=None
                    if len(miss)==2 and not color:
                        killed=all(not any(all(e not in core and e!=tuple(sorted(miss)) for e in combinations(q,2)) for q in combinations(sorted(set.intersection(*(blue[s] for s in t))),7-len(t))) for t in triples+[rs])
                    assert len(miss)==2 and same and not color and killed
                    U=set().union(*sq);fixed,=set.intersection(*map(set,sq));local=[]
                    for t in triples:
                        sites=[v for v in sorted(U-set().union(*t)) if all(abs(v-i)!=1 for i in miss)]
                        ports=[j for j,r in enumerate(sq) if all(set(r)&set(s) for s in t)]
                        choices=[('fixed+movable' if fixed in (a,b) else 'two movable') for a,b in combinations(sites,2) if b-a!=1]+['site+port' for a in sites for j in ports if a not in sq[j]]+['two ports' for _ in combinations(ports,2)]
                        if choices:
                            local.append(t);completion_types.update(choices);per_triple[tuple(sorted(choices))]+=1
                    common=set.intersection(*map(set,bad));co=sorted(common);os=[set(s)&W for s in co];ms=[set(s)-W for s in co];shared_shapes[tuple(sorted(map(len,os))),len(set.intersection(*os)),len(set.intersection(*ms))]+=1
                    assert local==bad
                    for q in combinations(sorted(set.intersection(*(blue[s] for s in rs))),3):
                        if all(e not in core for e in combinations(q,2)):
                            assert miss<=set(q);v,=set(q)-miss
                            quartet_last['square port' if v>10 else 'fixed' if v==fixed else 'movable']+=1
                    key=(len(miss),same,color,killed);coverage[key]+=1;certs.setdefault(key,dict(square=sq,rows=rs,cycle=sorted(cyc),missed=sorted(miss),bad=[(t,witness(t)) for t in bad]))
                    by_pairings[len(minima)]+=1;shape[len(bad),len(opts),len(minima)]+=1
                    representatives.setdefault(len(minima),dict(square=sq,cycle=sorted(cyc),rows=rs,options=opts,bad=bad,minima=minima))
                    continue
                # Independent replay: brute-force triangles and sevens on 18 vertices.
                base=core|{(i,15+j) for j,r in enumerate(rs) for i in r}|{(11+i,15+j) for i,r in enumerate(sq) for j,s in enumerate(rs) if set(r).isdisjoint(s)};solutions=[]
                for n in range(7):
                    for es in combinations(combinations(range(15,19),2),n):
                        g=base|set(es)
                        if any(all(e in g for e in combinations(q,2)) for q in combinations(range(1,19),3)):continue
                        if not any(all(e not in g for e in combinations(q,2)) for q in combinations(range(1,19),7)):solutions.append(es)
                assert min(map(len,solutions))==2
                return dict(square=sq,cycle=sorted(cyc),rows=rs,bad_triples=[dict(rows=t,other_vertices=witness(t)) for t in bad],options=opts,repair=repair,solutions=solutions)
    if shared:return dict(squares=square_count,cycles=cycle_count,quartets=quartets,minimum_two=two,positive_digest=sha256(json.dumps(sorted(positive_keys),separators=(',',':')).encode()).hexdigest(),has_shared_minimum=shared_min,has_unique_shared_minimum=unique_shared,by_number_of_minima=by_pairings,by_bad_triples_options_minima={str(k):v for k,v in shape.items()},representatives=representatives,missed_edge_coverage={str(k):v for k,v in coverage.items()},completion_types=completion_types,quartet_last=quartet_last,shared_shapes={str(k):v for k,v in shared_shapes.items()},per_obstructed_triple={str(k):v for k,v in per_triple.items()},coverage_examples={str(k):v for k,v in certs.items()})
    raise ValueError('no example')
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--shared',action='store_true');args=parser.parse_args()
    result=find(args.shared);print(result);(D/('ramsey_four_port_repair_shared.json' if args.shared else 'ramsey_four_port_repair.json')).write_text(json.dumps(result,indent=2)+'\n')
