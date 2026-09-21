"""Exact weight, cutoff and split-response checks for the rigged comparison."""
from fractions import Fraction
from pathlib import Path
import json
import sympy as S

triangle_checks=0
for i in range(-32,33):
    u=Fraction(i,4)
    for j in range(17):
        a=Fraction(j,4)
        for sign in (-1,1):
            assert abs(u)+abs(u+sign*a)>=a
            triangle_checks+=1
# Sharpness: the weight ratio is constant for an input between the endpoints.
for j in range(1,17):
    a=Fraction(j,4)
    for numerator in range(11):
        v=a*Fraction(numerator,10)
        assert abs(v-a)+abs(v)==a

N,delta=S.symbols('N delta',positive=True)
tail=N**(-delta)*(S.log(N)/delta+1/delta**2)
assert S.simplify(S.diff(tail,N)+S.log(N)*N**(-1-delta))==0

k=S.symbols('k',integer=True,positive=True)
geometric_checks=0
for gamma in (S.Rational(1),S.Rational(3,2),S.Rational(2)):
    for p in (2,3,5,7,11,13,17,19):
        series=S.summation(S.Rational(1,p)**((1+2*gamma)*k),(k,1,S.oo))
        assert S.simplify(series-1/(S.Integer(p)**(1+2*gamma)-1))==0
        geometric_checks+=1

a,eps,L=S.symbols('a eps L',positive=True)
assert S.integrate(2/S.sqrt(a),(a,0,eps))==4*S.sqrt(eps)
assert S.simplify(S.integrate(2*S.exp(-a/2)+2*S.exp(-2*a),(a,L,S.oo))
                  -(4*S.exp(-L/2)+S.exp(-2*L)))==0

# Algebraic support decomposition with a non-real self-adjoint response.
A=S.Matrix([[2,1+S.I,3-S.I],[1-S.I,-1,2*S.I],[3+S.I,-2*S.I,4]])
assert A==A.conjugate().T
E=S.Matrix([[0,0],[1,0],[0,1]])
negative=S.diag(1,0,0)
f=S.Matrix([1+2*S.I,3-S.I])
B=-E.conjugate().T*A*E
leak=negative*A*E*f
assert A*E*f==-E*B*f+leak
# No change of metric was made in the pairing used by this decomposition.
g=S.Matrix([2-S.I,-1+S.I])
assert S.expand((E*g).conjugate().dot(A*E*f)+g.conjugate().dot(B*f))==0

result={'schema':'marici.grothendieck.rigged-all-prime-tate-comparison.v1','passed':True,
        'two_sided_translation_weight_checks':triangle_checks,
        'weighted_prime_tower_checks':geometric_checks,
        'checks':{'sharp_translation_weight':True,'prime_cutoff_integral_majorant':True,
                  'gamma_jump_and_large_shift_regulators':True,
                  'signed_compression_leakage_split':True},
        'scope':'Exact scalar weights, regulator integrals and an algebraic split-response fixture. Convergence of the actual prime series and its dual Fourier transport are proved in the companion note.'}
root=Path(__file__).resolve().parents[3]
out=root/'research/grothendieck/results/rigged-all-prime-tate-comparison.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
