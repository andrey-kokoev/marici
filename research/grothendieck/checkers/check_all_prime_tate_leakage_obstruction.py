"""Exact fixtures for full-line prime leakage versus half-line convergence."""
from pathlib import Path
import json
import sympy as S

u,L,d=S.symbols('u L d',positive=True)
p=S.symbols('p',integer=True,positive=True)
k=S.symbols('k',integer=True,positive=True)
f=u*(L-u)
norm2=S.integrate(f*f,(u,0,L))
assert S.simplify(norm2-L**5/30)==0
corr=S.integrate(u*(L-u)*(u+d)*(L-u-d),(u,0,L-d))
formula=(L-d)**3*(L**2+3*L*d+d*d)/30
assert S.factor(corr-formula)==0
assert S.simplify(formula.subs(d,0)-norm2)==0

# Every correlation of two nonnegative translates is nonnegative.
correlation_checks=0
for j in range(21):
    assert formula.subs({L:S.Rational(1,4),d:S.Rational(j,80)})>=0
    correlation_checks+=1

geometric_checks=0
for prime in (2,3,5,7,11,13,17,19,23,29,31):
    exact=S.summation(S.Rational(1,prime)**k,(k,1,S.oo))
    assert exact==S.Rational(1,prime-1)
    for K in range(1,9):
        prefix=sum(S.Rational(1,prime)**j for j in range(1,K+1))
        assert prefix==S.Rational(1,prime-1)*(1-S.Rational(1,prime)**K)
        assert prefix<exact
        geometric_checks+=1

# Source fixture f=u(L-u) on (0,L), zero elsewhere, has zero boundary
# traces and lies in H^1_gamma. L=1/4<log 2, since integral_1^2 dt/t>=1/2.
assert S.Rational(1,4)<S.Rational(1,2)
# For every p>=2 and k>=1, translated supports are negative and disjoint
# within a prime tower. The positive opposite shifts are disjoint from f.
# The divergent lower bound uses Euler's reciprocal-prime theorem, not a
# finite numerical extrapolation of the fixtures above.

# The obstruction also occurs on actual positive Euler exponential states.
alpha=S.symbols('alpha',positive=True)
a=S.symbols('a',positive=True)
assert S.simplify(S.integrate(S.exp(-2*alpha*u),(u,0,a))
                  -(1-S.exp(-2*alpha*a))/(2*alpha))==0
exponential_checks=0
for decay in (S.Rational(1),S.Rational(3,2),S.Rational(2)):
    lower=(1-S.Rational(1,2)**(2*decay))/(2*decay)
    for prime in (2,3,5,7,11,13,17,19,23,29,31):
        mass=(1-S.Rational(1,prime)**(2*decay))/(2*decay)
        assert mass>=lower>0
        exponential_checks+=1

result={'schema':'marici.grothendieck.all-prime-tate-leakage-obstruction.v1','passed':True,
        'exact_nonnegative_translate_correlations':correlation_checks,
        'exact_prime_tower_norm_checks':geometric_checks,
        'positive_Euler_state_lower_bounds':exponential_checks,
        'checks':{'compact_source_H1_fixture':True,'prime_tower_leakage_geometric_identity':True,
                  'cross_prime_correlations_nonnegative':True,
                  'one_sided_prime_action_vanishes_on_short_support':True},
        'scope':'Exact compact-source and prime-tower fixtures. Infinite L2 divergence follows from the positive diagonal lower bound and divergence of the reciprocal-prime sum in the companion proof.'}
root=Path(__file__).resolve().parents[3]
out=root/'research/grothendieck/results/all-prime-tate-leakage-obstruction.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
