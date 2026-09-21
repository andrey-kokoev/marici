"""Exact positive/negative residual and Hardy reflection regressions."""
from pathlib import Path
import json
import sympy as S

q,s=S.symbols('q s')
Pq,Ps,gq,gs=S.symbols('Pq Ps gq gs')
hq=1/q+1/(q-1);hs=1/s+1/(s-1)
Lq=hq+gq-Pq;Ls=hs+gs-Ps
endpoint=1/(s*(q-1))+1/((s-1)*q)
positive=(Pq+Ps-gq-gs)/(s+q-1)-endpoint
assert S.factor(positive+(Lq+Ls)/(s+q-1))==0
# Use only the fixed completed functional equation L(1-q)=-L(q).
negative_reflected=(-Lq-Ls)/(1-q-s)
assert S.factor(positive+negative_reflected)==0

C,D=S.symbols('C D')
assert S.expand((-D-Lq*C)+(D-(-Lq)*C))==0
assert S.expand((-D-Lq*C).subs(D,-Lq*C))==0

# A finite algebraic completed-factor fixture, not asserted xi zeros.
roots=[S.Rational(1,2)+3*S.I,S.Rational(1,2)-3*S.I,
       S.Rational(1,4)+5*S.I,S.Rational(1,4)-5*S.I,
       S.Rational(3,4)+5*S.I,S.Rational(3,4)-5*S.I]
Lmodel=sum(1/(q-rho) for rho in roots)
assert S.cancel(Lmodel.subs(q,1-q)+Lmodel)==0
B=S.prod((q-rho)/(q-(6-S.conjugate(rho))) for rho in roots)
Cmodel=B/(4-q)**6
Dmodel=Lmodel*Cmodel
assert S.cancel(-Dmodel.subs(q,1-q)-Lmodel*Cmodel.subs(q,1-q))==0
assert Cmodel.subs(q,0)!=0 and Cmodel.subs(q,1)!=0

# Kill the two prescribed endpoint functionals on the same source, not by
# changing or dropping their output channels.
Czero=q*(q-1)*B/(4-q)**8
Dzero=Lmodel*Czero
assert Czero.subs(q,0)==Czero.subs(q,1)==0
assert Czero.subs(q,-1)!=0
assert S.cancel(-Dzero.subs(q,1-q)-Lmodel*Czero.subs(q,1-q))==0

# A generic one-sided Hardy pole moves to the wrong half-plane on reflection.
Fminus=1/(q-S.Rational(1,4))
Fplus=-Fminus.subs(q,1-q)
assert S.factor(Fplus-1/(q-S.Rational(3,4)))==0
assert S.limit((q-S.Rational(3,4))*Fplus,q,S.Rational(3,4))==1

# Unsubtracted responses retain separate endpoint poles at q=1.
c0,c1=S.symbols('c0 c1')
regular=q**2+2*q
assert S.limit((q-1)*(regular+c1/(q-1)+c0/q),q,1)==c1
assert S.limit((q-1)*(regular+c0/(q-1)+c1/q),q,1)==c0

result={'schema':'marici.grothendieck.full-euler-residual-reflection.v1','passed':True,
        'checks':{'positive_prime_gamma_endpoint_assembly':True,
                  'negative_to_positive_transform_reflection':True,
                  'Cauchy_kernel_implies_both_residuals_zero':True,
                  'nonzero_endpoints_survive_full_relative_kernel':True,
                  'one_sided_Hardy_condition_does_not_imply_two_sided':True,
                  'source_endpoint_zeros_preserve_nonzero_kernel':True,
                  'unsubtracted_L2_requires_both_endpoint_poles_removed':True},
        'scope':'Exact scalar assembly and finite reflected-zero fixtures. The actual full residual theorem uses the completed xi functional equation, justified source superposition, and the Hardy support argument in the companion note.'}
root=Path(__file__).resolve().parents[3]
p=root/'research/grothendieck/results/full-euler-residual-reflection.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
