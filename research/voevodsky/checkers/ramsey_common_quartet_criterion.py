"""Check the two support certificates on every nonempty family, not just probe outputs."""
from itertools import combinations
from collections import Counter,defaultdict
import json
from ramsey_pentagon_selector import charts
from ramsey_inherited_swap_selector import D
from ramsey_two_repairs_opposite import run
from ramsey_readout_forced_quartet import from_forced_colors


def audit():
    index=defaultdict(set);hist=Counter();checked=0
    for sq,c,rows in run():index[sq,c].add(rows)
    for sq,_,cycles in charts():
        U=set().union(*sq);W=set(range(1,11))-U;fixed,=set.intersection(*map(set,sq))
        for n in range(1,len(cycles)+1):
            for cs in combinations(cycles,n):
                blue=lambda e:all(e not in c for c in cs);red=lambda e:all(e in c for c in cs)
                common=set.intersection(*(index[sq,tuple(sorted(c))] for c in cs));ans=from_forced_colors(sq,blue,red)
                assert bool(common)==bool(ans)
                if ans:assert tuple(sorted(tuple(sorted(s)) for s in ans[3])) in common
                hist[n,ans[0] if ans else 'none']+=1
                for rs in common:
                    missed=tuple(sorted(W-set().union(*rs)));assert len(missed)==2 and blue(missed)
                    singles=[set(s)&W for s in rs if len(set(s)&W)==2];A,B=singles
                    if A!=B:assert red(tuple(sorted(A^B)))
                    else:
                        h,=W-set(missed)-A;X=set(range(missed[0]+1,missed[1]));Y=U-X-{fixed}
                        assert blue(tuple(sorted(A))) and all(abs(h-y)!=1 for y in Y) and all(abs(fixed-i)!=1 for i in missed)
                    checked+=1
    out=dict(families=sum(hist.values()),by_size_and_first_certificate={str(k):v for k,v in hist.items()},quartet_family_instances=checked);print(out);(D/'ramsey_common_quartet_criterion.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
