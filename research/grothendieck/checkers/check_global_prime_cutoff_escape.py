"""Exact profile/energy checks and PNT measure-mass regressions."""
from pathlib import Path
import json
import math
import sympy as S

t,L=S.symbols('t L',positive=True)
# h(t)=exp(-2t)1_(t>=0), an ordinary domain fixture, not a kernel source.
jm=S.Rational(2,3)*(S.exp(-t/2)-S.exp(-2*t))
jp_pos=S.Rational(2,5)*S.exp(-2*t)
jp_neg=S.Rational(2,5)*S.exp(t/2)
em=S.integrate(jm**2,(t,0,S.oo))
ep=S.integrate(jp_pos**2,(t,0,S.oo))+S.integrate(jp_neg**2,(t,-S.oo,0))
assert em==ep==S.Rational(1,5)
correlation=S.integrate(jm*jp_neg.subs(t,t-2*L),(t,0,2*L))+S.integrate(jm*jp_pos.subs(t,t-2*L),(t,2*L,S.oo))
assert S.limit(correlation,L,S.oo)==0
xi=S.symbols('xi',real=True)
# Unitary Fourier density of the zero-extended exponential.
coefficient=S.integrate(2/(2*S.pi*(4+xi**2)*(S.Rational(1,4)+xi**2)),(xi,-S.oo,S.oo))
assert coefficient==em+ep==S.Rational(2,5)

rows=[]
for cutoff in [1000,10000,100000]:
    primes=list(S.primerange(2,cutoff+1))
    for a in [0.,1.,2.]:
        mass=sum(math.log(p)/math.sqrt(p*cutoff) for p in primes if p<=cutoff*math.exp(-a))
        target=2*math.exp(-a/2)
        rows.append({'cutoff':cutoff,'a':a,'tail_mass':mass,'limit':target,'error':abs(mass-target)})
assert max(row['error'] for row in rows if row['cutoff']==100000)<.1
result={'schema':'marici.grothendieck.global-prime-cutoff-escape.v1','passed':True,
        'checks':{'equal_profile_energies':True,'separated_cross_term_vanishes':True,
                  'exact_Fourier_coefficient':True,'prime_measure_mass_regression':True},
        'fixture_exact_total_coefficient':str(coefficient),'numerical_rows':rows,
        'scope':'Exact exponential-domain fixture and numerical first-prime masses. Global strong convergence uses PNT, tightness and translation continuity, not finite numerics.'}
root=Path(__file__).resolve().parents[3]
p=root/'research/grothendieck/results/global-prime-cutoff-escape.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
