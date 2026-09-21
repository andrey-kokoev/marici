"""Factorial Fox-jet estimates and a source-family obstruction."""
from math import comb,factorial
from fractions import Fraction as F
from pathlib import Path
import runpy
import json
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))

checks=0
for n in range(41):
    for c in (F(2),F(3),F(7,2),F(10)):
        total=sum(comb(n,k)*c**k*factorial(k) for k in range(n+1))
        assert total<=factorial(n)*(1+c)**n
        # The k=n term alone requires factorial control.
        assert total>=factorial(n)*c**n
        checks+=1

# Highest jet of a forgotten diamond followed by a forgotten suffix:
# every edge is selected, so the two source paths remain distinct, each
# with unit coefficient and no feature or nontrivial memory norm.
witnesses=[]
for n in (2,3,4,8,16,32):
    column=b['multiply'](b['relation']((0,1),0),
                         {(tuple(range(2,n)),(0,)*(n-2)):1})
    top={}
    for (word,marks),coefficient in column.items():
        state=0;edges=[]
        for event,mark in zip(word,marks):
            end=state|(1<<event)
            edges.append(('e',state,end,mark));state=end
        top[tuple(edges),((),)*(n+1)]=coefficient
    assert len(top)==2 and sum(abs(v) for v in top.values())==2
    witnesses.append({'events':n,'top_jet_vacuum_mass':2,
                      'graph_weight_at_lambda_s_1':str(2**n*factorial(n))})

product_checks=0
for n in range(32):
    for m in range(32):
        assert factorial(n+m)<=2**(n+m)*factorial(n)*factorial(m)
        assert F(n,2**n)<=1
        product_checks+=1
result={'passed':True,'all_order_weight_checks':checks,
 'factorial_source_product_checks':product_checks,'top_jet_witnesses':witnesses,
 'scope':'Exact combinatorial bounds and actual forgotten source coefficients. Frechet convergence and the old-domain counterexample are proved in the companion note; no theta approximation or Green positivity claim.'}
out=ROOT/'research/voevodsky/results/all-order-fox-summability.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
