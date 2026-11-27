"""Blue-edge requirements of constructed next rows; separate reading from coexistence."""
from itertools import combinations,permutations,product
from collections import Counter
from pathlib import Path
import json

V=set(range(1,11));path={(i,i+1) for i in range(1,10)};ind=lambda s:all(v+1 not in s for v in s)

def charts():
    rows={frozenset(s) for s in combinations(V,3) if ind(s)};squares=set()
    for c in rows:
        ops=[{i,i+1} for i in range(1,10) if len(c&{i,i+1})==1 and c^{i,i+1} in rows]
        for a,b in combinations(ops,2):
            if a&b or c^a^b not in rows:continue
            squares.add(tuple(sorted(tuple(sorted(s)) for s in (c,c^a,c^b,c^a^b))))
    for sq in sorted(squares):
        U=set().union(*sq);W=sorted(V-U);mov=U-set.intersection(*map(set,sq));qs={e:tuple(sorted((*e,min(z for z in mov if ind({*e,z}))))) for e in combinations(W,2) if e not in path};cycles=[]
        for tail in permutations(W[1:]):
            if tail[0]>tail[-1]:continue
            p=(W[0],)+tail;c={tuple(sorted((p[i-1],p[i]))) for i in range(5)}
            if any(set(e)<=set(W) and e not in c for e in path) or any(j-i==2 for i,j in c):continue
            cycles.append(c)
        if cycles:yield sq,qs,cycles

def coexists(sq,rows,cycle):
    # Enforce the edge probe's prescribed red links; vary links between probes.
    supports=list(map(set,(*sq,*rows)));m=len(supports);core=path|cycle
    base={ (i,j) for i in range(4) for j in range(4,m) if supports[i].isdisjoint(supports[j])};options=list(combinations(range(4,m),2));cv=[set(t) for n in range(1,8) for t in combinations(sorted(V),n) if all(e not in core for e in combinations(t,2))];cv.append(set())
    bad=[]
    for n in range(1,m+1):
        for q in combinations(range(m),n):
            if any(e in base for e in combinations(q,2)):continue
            u=set().union(*(supports[i] for i in q))
            if any(len(v)+n>=7 and v.isdisjoint(u) for v in cv):bad.append(set(q))
    for n in range(len(options)+1):
        for es in combinations(options,n):
            red=base|set(es)
            if any(not supports[i].isdisjoint(supports[j]) for i,j in es) or any(all(e in red for e in combinations(q,2)) for q in combinations(range(m),3)):continue
            if all(any(set(e)<=q for e in es) for q in bad):return True
    return False

def run():
    counts=Counter();packs=Counter();examples={};outcomes=Counter()
    for sq,qs,cycles in charts():
        # Only keep tests which can actually distinguish two completions.
        var=sorted(e for e in qs if 0<sum(e in c for c in cycles)<len(cycles));bins={}
        for n in range(len(var)+1):
            for cut in combinations(var,n):
                compatible=[i for i,c in enumerate(cycles) if set(cut).isdisjoint(c)];outcomes[len(compatible)]+=1
                if len(compatible)==1:bins.setdefault(compatible[0],[]).append(cut)
        for i,c in enumerate(cycles):
            opts=bins[i];n=len(opts[0]);counts[n]+=1;found=False
            for cut in (u for u in opts if len(u)==n):
                ok=coexists(sq,[qs[e] for e in cut],c);packs[n,ok]+=1;found|=ok
                if n>=2:examples.setdefault(str(ok),dict(square=sq,edges=cut,rows=[qs[e] for e in cut],cycle=sorted(c),alternatives=len(cycles)))
            if found:counts['jointly_realizable']+=1
            else:
                mov=set().union(*sq)-set.intersection(*map(set,sq));found=any(coexists(sq,rs,c) for cut in opts if len(cut)==n for rs in product(*[[tuple(sorted((*e,z))) for z in mov if ind({*e,z})] for e in cut]));counts['additional_with_alternate_site']+=int(found)
    assert sum(counts[n] for n in (0,1,2))==122
    res=dict(cycles_by_minimum={str(k):v for k,v in counts.items()},minimum_sets_by_size_and_joint={str(k):v for k,v in packs.items()},collections_by_number_of_cycles={str(k):v for k,v in outcomes.items()},examples=examples);print(res);(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_selector.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':run()
