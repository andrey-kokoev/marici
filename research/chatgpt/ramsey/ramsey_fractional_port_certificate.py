"""Exact integer verification of fractional six-port exclusion.

Compute a floating-point LP witness once, round every dual weight UP to
an integer numerator, then verify all inequalities with integer arithmetic.
The verifier itself uses no optimization assumptions.

Two 16-vertex residual examples are recorded in ramsey_fractional_port_certificates.json.
"""
from itertools import combinations
from pathlib import Path
import json


def independent_fives(A):
    return [sum(1<<v for v in C)
            for C in combinations(range(len(A)),5)
            if all(not ((A[u]>>v)&1) for u,v in combinations(C,2))]


def verify(A, weights, den):
    assert len(A)==16 and all(0<=a<(1<<16) for a in A)
    assert all(((A[u]>>v)&1)==((A[v]>>u)&1) for u in range(16) for v in range(16))
    assert all(not(A[u]&(1<<u)) for u in range(16))
    assert all(not(A[u]&A[v]) for u in range(16) for v in range(u+1,16) if A[u]>>v&1)
    assert sum(a.bit_count() for a in A)==66
    F=independent_fives(A)
    assert len(F)>0
    assert set(map(int,weights)) <= set(F)
    assert all(int(x)>=0 for x in weights.values())
    assert 0<sum(weights.values())<6*den
    for T in F:
        cover=sum(weight for I,weight in weights.items() if not (int(I)&T))
        assert cover >= den, ('uncovered',T,cover)
    # Verify alpha(H)<=5 without relying on the source catalogue.
    for C in combinations(range(16),6):
        assert any(A[u]>>v&1 for u,v in combinations(C,2)), ('independent6',C)
    return {'I5':len(F),'rational_total':str(sum(weights.values()))+'/'+str(den),
            'covered_neighborhoods':len(F), 'positive_weights':len([x for x in weights.values() if x])}


def calculate(A,den):
    import numpy as np
    from scipy.optimize import linprog
    F=independent_fives(A)
    M=np.array([[(f&g)==0 for f in F] for g in F],dtype=np.uint8)
    result=linprog(-np.ones(len(F)),A_ub=M,b_ub=np.ones(len(F)),bounds=(0,None),method='highs')
    assert result.success
    y=-result.ineqlin.marginals
    # A tiny positive bump guards against floating-point error when a value is
    # indistinguishable from an exact integer multiple of 1/den.
    ints=np.where(y > 1e-9, np.ceil(y*den + 1e-7), 0).astype(int)
    weights={str(F[i]):int(v) for i,v in enumerate(ints) if v}
    verify(A, weights, den)
    return {'A':A,'denominator':den,'weights':weights,'lp_numeric':float(-result.fun)}


def main():
    from ramsey_port_hall_witness import H
    p=Path('/mnt/data/ramsey_17parent_fast_probe_results.json')
    best=json.loads(p.read_text())['best'][1]
    records={'original_witness':calculate(H,100), 'harder_17parent_candidate':calculate(best,1000)}
    for label,rec in records.items():
        checks=verify(rec['A'],rec['weights'],rec['denominator'])
        print(label, checks, 'LP numerical',rec['lp_numeric'])
    out=Path('/mnt/data/ramsey_fractional_port_certificates.json')
    out.write_text(json.dumps(records,indent=2))
    print('wrote',out)


if __name__=='__main__':main()
