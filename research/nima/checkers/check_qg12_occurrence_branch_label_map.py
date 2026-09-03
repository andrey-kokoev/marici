"""Test whether q_g31 and q_g23 label the two split q_g2 conductor branches."""
import json
import sympy as sp
x,p,k,s=sp.symbols('x p k s', nonzero=True)
xi=-k+s
y=p+x*k/2; z=p-x*k/2; a=x+z; b=2*p+x*(1+xi)
q31=sp.factor(a-y)
q23=sp.factor(b-x)
q31_strict=sp.factor(q31/x)
q23_exceptional=sp.factor(q23.subs(x,0))
assert q31_strict==1-k
assert q23_exceptional==2*p
assert sp.diff(q31_strict,s)==0
assert sp.diff(q23_exceptional,s)==0
print(json.dumps({'schema':'marici.nima.qg12-occurrence-branch-label-map.v1','status':'passed','bold_conjecture':'q_g31 and q_g23 are the two denominator labels of the split conductor branch points','q_g31_on_q_g2':str(q31),'q_g31_strict_at_conductor':str(q31_strict),'q_g23_on_q_g2':str(q23),'q_g23_exceptional_at_conductor':str(q23_exceptional),'dependence_on_branch_coordinate_s':{'q_g31':False,'q_g23':False},'conjecture_disposition':'falsified generically','residual_conjecture':'occurrence-label parity and nearby-cycle branch parity are distinct; the two split branches are the two roots of the Cayley-Menger smoothing and require a source chain map independent of q_g31,q_g23 labels'},sort_keys=True))
