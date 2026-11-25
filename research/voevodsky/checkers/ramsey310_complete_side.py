"""Exhaust common supports for a fixed side, then its forced opposite degrees."""
from ramsey310_one_side_demands import possible,residual
from ramsey310_codegree7_test import sets,F
from ramsey310_cached_kernel import CachedKernel,bits
from itertools import combinations
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json

def complete(A,E,cache):
    count=Counter();samples=[];witness=[]
    @lru_cache(maxsize=8192)
    def extension(m,k):return next(sets(A,m,k),None)
    def defect(rows):
        # An independent outside set uses at most one side. With no roots,
        # its available outside pool is itself independent (the seven common and that side).
        for k in range(3,10):
            for J in combinations(rows,k):
                m=F
                for j in J:m &= ~j
                t=extension(m,10-k)
                if t is not None:return k,J,t
        return None
    def accept(C):
        count['common_choices']+=1
        fail=defect(C+tuple(E))
        if fail:
            k,J,t=fail;count[f'left_defect_{k}_outside']+=1
            if not samples:samples.append(dict(common=C,missed_by=J,residual_set=t))
            return False
        count['left_ok']+=1
        req=[9-a.bit_count()-sum(s>>i&1 for s in C+tuple(E)) for i,a in enumerate(A)]
        assert all(0<=x<=2 for x in req) and sum(req)==12
        forced=sum(1<<i for i,x in enumerate(req) if x==2); singles=sum(1<<i for i,x in enumerate(req) if x==1)
        for x in combinations(bits(singles),6-forced.bit_count()):
            part=sum(1<<i for i in x);a=forced|part;b=forced|(singles^part)
            if a>b or any(A[i]&s for s in (a,b) for i in bits(s)):continue
            if extension(F&~(a|b),7) is not None:continue
            count['right_candidates']+=1
            if defect(C+(a,b)) is None:
                witness.append(C+tuple(E)+(a,b));return True
        return False
    ok=possible(A,E,cache,accept);return dict(passes=ok,counts=dict(count),example_defect=samples,witness=witness)

if __name__=='__main__':
    d=Path(__file__).resolve().parents[1]/'results';cache={}
    for r in map(json.loads,(d/'ramsey310_side_frontier.jsonl').read_text().splitlines()):
        n=r['record']
        for s in r['sides']:
            if not s['passes']:continue
            if n not in cache:
                A=residual(n);cache[n]=(A,CachedKernel(A))
            A,c=cache[n];E=s['rows'];print(json.dumps(dict(record=n,side=E,**complete(A,E,c))),flush=True)
