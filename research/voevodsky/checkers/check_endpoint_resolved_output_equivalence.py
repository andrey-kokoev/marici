"""Output-only recovery on the prepared exponential sector, not arbitrary H1."""
from pathlib import Path
import json
import sympy as s
x=s.symbols('x',real=True)
y,delta=s.symbols('y delta',positive=True)
ss=s.Rational(1,2)+y-s.I*x
endpoint=1/ss
assert s.simplify(ss*endpoint)==1
# H1_gamma norm of exp(i z u), with Im z-gamma=delta.
norm_squared=(1+x*x+y*y)/(2*delta)
assert norm_squared.is_real is True

# One spectral fibre: source coordinates (a,v), with u=a*h. The output
# retains actual response, endpoints, and weak residual/even test values.
h=s.Matrix([1,s.I,2])
A=s.Matrix([[2,s.I,1],[-s.I,3,1-s.I],[1,1+s.I,4]])
assert A==A.H
S=s.Integer(2)
T=s.Integer(3)
den=T+S-s.Rational(1,2)
O=s.zeros(7,2)
O[:3,0]=A*h
O[3,0]=1/S;O[4,0]=1/(S-1)
O[5,1]=1/den;O[6,0]=1/den
R=s.zeros(2,7);R[0,3]=S;R[1,5]=den
assert R*O==s.eye(2)
assert (O*R)*(O*R)==O*R
# The independently specified source form can be transported without
# retaining u in the output. Its coefficients are not chosen by a fit.
q_ar=-(h.H*A*h)[0]+2/(S*(S-1))
Q=s.Matrix([[q_ar,1],[1,0]])
Qout=R.H*Q*R
assert (O.H*Qout*O-Q).applyfunc(s.simplify)==s.zeros(2)
OO=s.kronecker_product(O,O)
assert (OO.H*s.kronecker_product(Qout,Qout)*OO-s.kronecker_product(Q,Q)).applyfunc(s.simplify)==s.zeros(4)
# With all responses equal to zero, the endpoint gives a=0 and v=0.
assert O.rank()==2
result={'passed':True,'checks':{'endpoint_recovers_exponential_amplitude':True,
 'output_only_inverse_on_range':True,'output_range_projection':True,
 'paired_and_two_slot_transport':True,'zero_output_has_zero_prepared_port':True},
 'scope':'Prepared exponential sector with endpoint and weak window-residual outputs retained. Residual amplitude is recovered by a fixed decaying test, not a strong source-coordinate norm. Analytic bounds and completed descent are proved in the note. No inverse on arbitrary Sobolev inputs or unweighted L2 response is asserted.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/endpoint-resolved-output-equivalence.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
