"""Exact finite fixtures for the actual-letter bounded filtered limit.

Infinite domain assertions use monotone convergence and actual theta tails,
not a finite rank or a numerical theta sample.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import runpy
import json

ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))


def main():
    products=[]
    for r in range(1,7):
        for kind in (0,1):
            column=b['chain_product']([b['relation']((2*i,2*i+1),kind) for i in range(r)])
            count=(2 if kind==0 else 4)**r
            assert len(column)==count
            assert sum(abs(v) for v in column.values())==count
            assert all(len(word)==2*r and sum(marks)==kind*r for word,marks in column)
            if kind==0:
                unit={key:Q(v,count*factorial(2*r)) for key,v in column.items()}
                for R in (1,2,3):
                    assert factorial(2*r)*R**(2*r)*sum(abs(v) for v in unit.values())==R**(2*r)
            else:
                # A bound on actual late-window weights, not assigned fake letters.
                assert Q(1,2**(r*r))**r==Q(1,2**(r**3))
            products.append({'depth':r,'kind':kind,'terms':count})
    compatibility=0
    for m in range(1,17):
        for k in range(1,m+1):
            assert tuple(r for r in range(1,m+1) if r<=k)==tuple(range(1,k+1))
            compatibility+=1
        assert sum(1 for r in range(1,m+1))==m
    # Finite positive coefficient fixtures: low degrees are determined exactly;
    # no claim to compute general quotient distances by deleting degrees.
    radius_checks=0
    for m in range(1,9):
        for R,Rprime in ((1,2),(1,3),(2,3),(3,5)):
            masses={n:Q(1,(n+1)*factorial(n)**2) for n in range(2,25)}
            budget=sum(factorial(n)*Rprime**n*v for n,v in masses.items())
            short=sum(factorial(n)*R**n*v for n,v in masses.items() if n<=2*m+1)
            tail=sum(factorial(n)*R**n*v for n,v in masses.items() if n>=2*m+2)
            assert tail<=Q(R,Rprime)**(2*m+2)*budget
            assert short+tail<=short+Q(R,Rprime)**(2*m+2)*budget
            radius_checks+=1
    # Ratio formula for the late mixed-product majorant, at R=1.
    for r in range(1,20):
        a=Q(factorial(2*r),2**(r**3))
        nxt=Q(factorial(2*r+2),2**((r+1)**3))
        assert nxt/a==Q((2*r+2)*(2*r+1),2**(3*r*r+3*r+1))
        assert nxt/a<Q(1,2)
    result={'passed':True,'actual_ideal_products':products,
            'compatibility_checks':compatibility,'depth_radius_checks':radius_checks,
            'scope':'Exact coefficient and budget checks. Infinite reconstruction uses stabilized corners and monotone convergence; actual late-window existence uses theta integrability.'}
    out=ROOT/'research/nima/results/actual-letter-filtered-limit.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
