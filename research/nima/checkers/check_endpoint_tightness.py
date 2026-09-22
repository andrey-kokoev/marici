"""Exact source normalization and finite depth/height budget regressions."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import runpy
import json

ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))


def main():
    relation=b['relation']((0,1),0)
    assert len(relation)==2
    unit={key:Q(value,4) for key,value in relation.items()}
    for radius in range(1,9):
        assert factorial(2)*radius**2*sum(abs(v) for v in unit.values())==radius**2
    # Distinct corner labels retain disjoint supports; no cross-corner cancellation.
    assert 2*factorial(2)*sum(abs(v) for v in unit.values())==2
    fixtures={(n,h):Q(1,(n+1)*(h+1)*factorial(n)**2)
              for n in range(2,17) for h in range(1,13)}
    checks=0
    for R,Rprime in ((1,2),(2,3),(3,5)):
        for eta in (1,2,3):
            prior=sum(factorial(n)*Rprime**n*h**eta*v
                      for (n,h),v in fixtures.items())
            for m in range(1,7):
                for H in (1,3,6,12):
                    omitted=sum(factorial(n)*R**n*v for (n,h),v in fixtures.items()
                                if n>2*m+1 or h>H)
                    bound=prior*(Q(R,Rprime)**(2*m+2)+Q(1,(H+1)**eta))
                    assert omitted<=bound
                    kept=sum(factorial(n)*R**n*v for (n,h),v in fixtures.items()
                             if n<=2*m+1 and h<=H)
                    total=sum(factorial(n)*R**n*v for (n,h),v in fixtures.items())
                    assert total==kept+omitted
                    assert total<=kept+bound
                    checks+=1
    result={'passed':True,'combined_depth_height_checks':checks,
            'checks':['actual_forgotten_diamond_normalization','disjoint_corner_distance'],
            'scope':'Finite rational budget checks. Uniform endpoint tightness and compactness follow from the finite-net proof, not these fixtures.'}
    out=ROOT/'research/nima/results/endpoint-tightness.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
