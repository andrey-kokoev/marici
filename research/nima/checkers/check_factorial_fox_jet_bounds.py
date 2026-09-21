"""Exact arithmetic regressions for the factorial full-jet bounds."""
from fractions import Fraction as Q
from math import factorial,comb
from pathlib import Path
import json


def main():
    sums=products=tails=0
    for n in range(41):
        for t in (Q(2),Q(3),Q(7,2),Q(8)):
            actual=sum(t**k*factorial(k)*comb(n,k) for k in range(n+1))
            series=sum(t**(-j)/factorial(j) for j in range(n+1))
            assert actual==factorial(n)*t**n*series
            # Finite exponential series is bounded by its geometric majorant.
            assert series<=sum(t**(-j) for j in range(n+1))<=1/(1-1/t)<=2
            assert actual<=2*factorial(n)*t**n
            sums+=1
            for N in (0,1,4,10,25):
                tail=sum(t**k*factorial(k)*comb(n,k) for k in range(N+1,n+1))
                for loss in (2,3):
                    assert tail<=2*Q(1,loss**(N+1))*factorial(n)*(loss*t)**n
                    tails+=1
    for n in range(41):
        for m in range(41):
            assert factorial(n+m)<=2**(n+m)*factorial(n)*factorial(m)
            products+=1
    result={'passed':True,'exact_jet_sum_and_majorant_checks':sums,
            'factorial_product_checks':products,'jet_order_tail_checks':tails,
            'scope':'Sufficient factorial source scale; no necessity, inverse stability, or new cross-degree pairing is asserted.'}
    out=Path(__file__).resolve().parents[1]/'results/factorial-fox-jet-bounds.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
