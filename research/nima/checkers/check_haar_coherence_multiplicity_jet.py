"""Exact local-jet hostile for Xi-ideal membership of the Haar energy defect.

Coefficient ring Q[L]; variables Z,W are independent complexified coordinates.
Work modulo (Z^m,W^m). L denotes log(p), hence is a nonzero positive scalar
on every prime specialization. No zeta simplicity assumption is made.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]


def add(a,b):
    c=a.copy()
    for key,value in b.items():
        c[key]=c.get(key,F(0))+value
        if not c[key]: del c[key]
    return c


def scale(a,c):
    return {key:value*c for key,value in a.items() if value*c}


def mul(a,b,m):
    out={}
    for (i,j,k),x in a.items():
        for (u,v,w),y in b.items():
            if i+u < m and j+v < m:
                key=(i+u,j+v,k+w)
                out[key]=out.get(key,F(0))+x*y
    return {key:value for key,value in out.items() if value}


def power(a,n,m):
    result={(0,0,0):F(1)}
    for _ in range(n): result=mul(result,a,m)
    return result


def stringify(a):
    return [{'Z':i,'W':j,'L':k,'coefficient':str(c)}
            for (i,j,k),c in sorted(a.items())]


def main():
    one={(0,0,0):F(1)}
    cases=[]
    for m in range(1,9):
        q={(1,0,1):F(1),(0,1,1):F(1)} if m>1 else {}
        exponential={}
        for n in range(2*m-1):
            exponential=add(exponential,scale(power(q,n,m),F((-1)**n,factorial(n))))
        # E=1+Z*W is positive on W=conjugate(Z), with E(0)=1.
        energy=add(one,{(1,1,0):F(1)}) if m>1 else one
        delta=mul(add(one,scale(exponential,F(-1))),energy,m)
        assert bool(delta) == (m>1)
        assert not power(delta,2*m-1,m)
        penultimate=power(delta,2*m-2,m)
        coefficient=penultimate.get((m-1,m-1,2*m-2),F(0))
        assert coefficient==comb(2*m-2,m-1) and coefficient>0
        if m>1:
            assert delta[(1,0,1)]==1 and delta[(0,1,1)]==1
        # Deliberate hostile: evaluation at the reduced point always gives zero,
        # but nonreduced ideal membership fails whenever m>1.
        reduced_value=delta.get((0,0,0),F(0))
        assert reduced_value==0
        assert (not delta)==(m==1)
        cases.append({'multiplicity':m,'reduced_value':str(reduced_value),
                      'belongs_to_nonreduced_ideal':not bool(delta),
                      'nilpotency_index':2*m-1,
                      'last_nonzero_power_coefficient':str(coefficient),
                      'first_jet_nonzero':m>1})
    # Minimal double-root counterexample: tau=Z^2, all its zeros are on the seam.
    # Its zero-locus energy condition holds at Z=W=0, while the class is nonzero.
    assert cases[1]['belongs_to_nonreduced_ideal'] is False
    # For the BASELINE alone, a squared-divisor factor starts in degree 2m>=2
    # and cannot produce L*(Z+W), even at a simple zero. Mixed terms in the
    # full energy defect may cancel that jet when m=1.
    square_factor_orders=[2*m for m in range(1,9)]
    assert all(order>1 for order in square_factor_orders)
    report={
        'schema':'marici.nima.haar-coherence-multiplicity-jet.v1',
        'passed':True,
        'ring':'Q[L][Z,W]/(Z^m,W^m), L=log(p)>0 after specialization',
        'defect':'(1-exp(-L*(Z+W)))*(1+Z*W)',
        'cases':cases,
        'minimal_hostile':'tau=Z^2 is confined to the seam but its Haar energy defect is nonzero modulo (Z^2,W^2)',
        'baseline_squared_divisor_factor_has_wrong_first_jet':True,
        'claim_boundary':'Finite exact jet checks support the companion all-multiplicity local theorem. No assertion of a multiple Xi zero, no RH proof, and no prohibition of reduced-fiber energy conservation.',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'rh_proved':False,
    }
    target=ROOT/'research/nima/results/haar-coherence-multiplicity-jet.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__': main()
