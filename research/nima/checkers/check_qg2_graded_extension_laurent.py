"""Laurent extension test for the full unsplit q_g2 wall form."""
import json
import sympy as sp
x,p,k,xi=sp.symbols('x p k xi', nonzero=True)
y=p+x*k/2; z=p-x*k/2; e=x+y+z; b=e+x*xi; a=x+z
x2,y2,z2,e2=x**2,y**2,z**2,e**2; h=x2+y2-z2
f=x2*a**4-h*a**2*b**2+y2*b**4
ga=h*(x2+e2)-2*x2*(y2+e2)
gb=h*(y2+e2)-2*y2*(x2+e2)
h0=z2*((e2-y2)*(e2-x2)+e2*z2)
K=sp.expand(f+ga*a**2+gb*b**2+h0)
L=sp.cancel(K/x**2); L0=sp.factor(L.subs(x,0)); L1=sp.factor(sp.diff(L,x).subs(x,0))
root0=4*p**2*(k+xi)
assert sp.factor(root0**2-L0)==0
# Exact unsplit q_g2 rational wall factor; db=x dxi. After sqrt(K)=x sqrt(L), coefficient is r/sqrt(L).
N=b+z-y; O=(b-x)*(x+z-y); S=(b-y-z)*(x+b+2*z)
r=sp.factor(N/(O*S))
F=sp.cancel(x**2*r/root0*(1-x*L1/(2*L0)))
lead=sp.factor(F.subs(x,0)); sub=sp.factor(sp.diff(F,x).subs(x,0))
res_lead=sp.factor(sp.residue(lead,xi,-1)); res_sub=sp.factor(sp.residue(sub,xi,-1))
res_qg1=(3-k)/(64*p**4*(k-1)**2)
closure_sub=sp.factor(res_qg1+res_sub)
assert res_lead!=0
assert sub!=0
assert closure_sub!=0
print(json.dumps({'schema':'marici.nima.qg2-graded-extension-laurent.v1','status':'passed','bold_conjecture':'the full q_g2 subleading Laurent coefficient is the off-diagonal extension that closes the grade -1 sewn node','K_wall_leading':str(L0),'K_wall_linear':str(L1),'grade_minus_2_coefficient':str(lead),'grade_minus_1_subleading_coefficient':str(sub),'grade_minus_2_endpoint_residue':str(res_lead),'grade_minus_1_subleading_endpoint_residue':str(res_sub),'q_g1_node_residue':str(res_qg1),'grade_minus_1_closure_residual':str(closure_sub),'conjecture_disposition':'falsified generically','residual_conjecture':'the nonzero subleading coefficient defines a triangular deformation of q_g2 but not an extension boundary into the sewn q_g1/q_g3 class; the grades remain distinct absent a source differential'},sort_keys=True))
