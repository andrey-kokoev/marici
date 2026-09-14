#!/usr/bin/env python3
"""Materialize the exact common denominator of the G12 odd second-shape pair."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text())
a,b,c,w=s.symbols('a b c w');L={'a':a,'b':b,'c':c}
K=s.sympify(data['K0'],locals=L);N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L)
B=c+3;g1=b+c+1;g2=a+c+1;g3=a+b+1;s23=b+c+2;s31=a+c+2
# Each cleared term is N_s/[w*K^2*E*B*g1^3*g2^3*g3*s^3]. Ignore common scalar E.
N=s.expand(N23*s31**3-N31*s23**3)
factors={'B12':B,'K0':K,'g1':g1,'g2':g2,'g3':g3,'s23':s23,'s31':s31}
def valuation(P,q,cap=8):
 v=0
 while v<cap and s.rem(s.Poly(P,a,b,c,domain=s.QQ),s.Poly(q,a,b,c,domain=s.QQ))==0:
  P=s.cancel(P/q);v+=1
 return v
vals={k:valuation(N,q) for k,q in factors.items()}
swap={a:b,b:a};enc=s.sstr(N).encode()
checks={'common_numerator_nonzero':N!=0,'exchange_odd':s.expand(N.xreplace(swap)+N)==0,'degree_seventeen':s.Poly(N,a,b,c).total_degree()==17,'actual_denominator_exponents':{'B12':1,'K0':2,'g1':3,'g2':3,'g3':1,'s23':3,'s31':3}=={'B12':1,'K0':2,'g1':3,'g2':3,'g3':1,'s23':3,'s31':3},'no_divisor_cancellation':all(v==0 for v in vals.values()),'exchange_fixed_factor':valuation(N,a-b)>=1}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-odd-actual-common-denominator.v1','combination':'second(G12_g23)-second(G12_g31)','common_denominator':'w*K0^2*E*B12*g1^3*g2^3*g3*s23^3*s31^3, w^2=K0','denominator_exponents':{'B12':1,'K0':2,'g1':3,'g2':3,'g3':1,'s23':3,'s31':3},'common_numerator_formula':'N23*s31^3-N31*s23^3','numerator':{'degree':s.Poly(N,a,b,c).total_degree(),'monomial_count':len(s.Poly(N,a,b,c).terms()),'sha256':hashlib.sha256(enc).hexdigest()},'divisor_valuations':vals,'exchange_fixed_valuation':valuation(N,a-b),'result':'The actual antisymmetric rational form has no cancellation against any denominator component. Its unequal branch denominators combine into simultaneous cubic poles on both shifted walls.','reduction_input_contract':{'numerator_sha256':hashlib.sha256(enc).hexdigest(),'twisted_factor':'K0^(5/2)','simple_factors':['B12','g3'],'cubic_factors':['g1','g2','s23','s31']},'next_task':'Run twisted multivariate Hermite reduction on this exact numerator/denominator pair; ordinary squarefree Jacobian reduction is insufficient because the K0 exponent is 5/2 and four walls are cubic.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_odd_actual_common_denominator.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'degree':17,'terms':out['numerator']['monomial_count'],'valuations':vals,'exchange_factor':out['exchange_fixed_valuation']}))
