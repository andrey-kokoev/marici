"""Fixed-test response certification; no numerical theta or inverse fitting."""
from pathlib import Path
import json
import sympy as s
I=s.I
# A Hermitian port form represented as a test/response evaluation.
Q=s.Matrix([[2,I],[-I,3]])
p=s.Matrix([1+I,2-I]);o=s.Matrix([2,I])
response=Q*p
assert s.simplify((p.H*Q*o)[0]-s.conjugate((o.H*response)[0]))==0
# Tensor noise expansion is exact before taking projective norms.
y1=s.Matrix([1,I]);y2=s.Matrix([2,1-I])
d1=s.Matrix([I,1]);d2=s.Matrix([1,-I])
assert (s.kronecker_product(y1+d1,y2+d2)-s.kronecker_product(y1,y2)
        -s.kronecker_product(d1,y2)-s.kronecker_product(y1,d2)
        -s.kronecker_product(d1,d2)).applyfunc(s.simplify)==s.zeros(4,1)
# Uniform effective-error threshold leaves half the positive margin.
w,g,y,C,X1,X2=s.symbols('w g y C X1 X2',positive=True)
Delta=w*s.sqrt(2)*g/(2*y)
eps=Delta/(2*w*C*(1/X1+1/X2))
assert s.simplify(w*C*eps*(1/X1+1/X2)-Delta/2)==0
# Strict window-gap lower bound: inner subwindows leave nonnegative slack.
p1,p2=s.symbols('p1 p2',positive=True)
h,dlo,dhi,a,b,c,d=s.symbols('h dlo dhi a b c d',real=True)
mu1=p1*(h-dlo-a)+(1-p1)*(h-b)
mu2=p2*(h+dhi+c)+(1-p2)*(h+d)
assert s.expand(mu2-mu1-p1*dlo-p2*dhi
                -(p1*a+(1-p1)*b+p2*c+(1-p2)*d))==0
result={'passed':True,'checks':{'fixed_observer_is_conjugate_output_evaluation':True,
 'two_factor_noise_telescoping':True,'half_margin_noise_threshold':True,
 'positive_inner_window_gap_bound':True},
 'scope':'Exact finite algebra and scalar margins. Actual balancing and nonzero attachment use the owning checker; response continuity and noise inequalities are proved in the companion note. No assertion that arbitrary noisy data are chain maps or have source preimages.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/noisy-attachment-certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
