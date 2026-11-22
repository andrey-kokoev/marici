"""Test descent of an orientation choice on the fixed 14 support under the actual arrow-reversing row action. Contrast invariant exposure, row-conditioned choices, and shared-token versus per-arrow consumption."""
from itertools import combinations,product
from ramsey_exit_consumption_units import run as trails,D,json

def run():
    out=[];fiber={'AB','BA'};subsets=[frozenset(s) for i in range(3) for s in combinations(sorted(fiber),i)]
    for ctrl in trails():
        p=ctrl['binding'];rho=dict(zip(p,(p[0],p[2],p[1],p[3])));move=lambda e:rho[e[1]]+rho[e[0]];assert frozenset((p[0],p[3]))==fiber_support==frozenset(rho[x] for x in fiber_support)
        lift=lambda s:frozenset(map(move,s));assert all(lift(s)!=s for s in subsets if len(s)==1);fixed=[sorted(s) for s in subsets if lift(s)==s];pairs=[(next(iter(s)),next(iter(t))) for s,t in product(subsets,repeat=2) if len(s)==len(t)==1 and lift(s)==t];assert len(pairs)==2
        def admits(w,shared):
            used=set()
            for e in w:
                if e not in fiber:continue
                key='14' if shared else e
                if key in used:return False
                used.add(key)
            return True
        policies={str(shared):[[len(h['word']) for h in rows if admits(h['word'],shared)] for rows in ctrl['rows']] for shared in (True,False)};assert policies=={'True':[[2],[2]],'False':[[2,4],[2,4]]};out.append(dict(binding=p,fixed_exposures=fixed,covariant_row_specific_singletons=pairs,admitted_lengths_by_shared_token=policies))
    return out
fiber_support=frozenset('AB')
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_exit_orientation_descent.json').write_text(json.dumps(out)+'\n')
