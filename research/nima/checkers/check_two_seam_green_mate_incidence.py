"""Exact vacuum incidence transpose; no spectral or fitted metric data."""
from pathlib import Path
from itertools import product
from math import factorial
from fractions import Fraction as Q
import importlib.util
import json

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('descent',HERE/'check_seven_event_factorization_descent.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def main():
    witnesses=[];tested=0
    for n in range(2,7):
        full=(1<<n)-1;z=(1<<(n-1))-1
        edges=[(v,v|(1<<i)) for v in range(full+1) for i in range(n) if not v&(1<<i)]
        observer=((('v',0),('e',z,full,0)),((),(),()))
        mate={}
        for (x,y),(u,v) in product(edges,repeat=2):
            if y&u!=y:continue
            key=((('e',x,y,0),('e',u,v,0)),((),(),()))
            boundary=f.balanced_boundary({key:1})
            coefficient=boundary.get(observer,0)
            if coefficient:mate[key]=coefficient
            tested+=1
        expected={((('e',0,1<<i,0),('e',z,full,0)),((),(),())):-1 for i in range(n-1)}
        assert mate==expected
        witnesses.append({'length':n,'mate_terms':len(mate),'unweighted_norm':sum(abs(c) for c in mate.values())})
    bounds=0
    for n,lam,s,sp in product(range(2,21),(1,2),(1,2),(1,3)):
        input_norm=2*lam*sp
        output_norm=(n-1)*(2*lam*s)**2*factorial(2)
        assert Q(output_norm,input_norm)==Q(4*lam*s*s*(n-1),sp)
        for k in (0,1):
            local=2*n*(2-k)*lam*(2*lam*s*(k+1))
            assert local<=8*lam*lam*s*(1+n)
        bounds+=1
    # Divergence comparison: (n-1)/n^2 >= 1/(2n).
    assert all(Q(n-1,n*n)>=Q(1,2*n) for n in range(2,101))
    result={'passed':True,'actual_bottom_boundaries_tested':tested,
            'vacuum_mate_witnesses':witnesses,'graph_and_moment_bound_checks':bounds,
            'scope':'Finite exact incidence transpose checks. The proper-domain result and extension estimate are proved in the companion note.'}
    out=HERE.parent/'results/two-seam-green-mate-incidence.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
