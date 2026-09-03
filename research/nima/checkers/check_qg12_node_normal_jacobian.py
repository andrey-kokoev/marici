"""Exact normal-bundle Jacobians at the q_g1--q_g2 soft node."""
import json
import sympy as sp
a,b,x,p,k,xi=sp.symbols('a b x p k xi')
y=p+x*k/2; z=p-x*k/2
q1=b-y-z
q2=a-x-z
q31=a-y
J_original=sp.factor(sp.det(sp.Matrix([[sp.diff(q1,a),sp.diff(q1,b)],[sp.diff(q2,a),sp.diff(q2,b)]])))
q1_exc=xi+1; q2_exc=a-p
J_exceptional=sp.factor(sp.det(sp.Matrix([[sp.diff(q1_exc,a),sp.diff(q1_exc,xi)],[sp.diff(q2_exc,a),sp.diff(q2_exc,xi)]])))
collision=sp.factor((q2-q31)/x)
required=-(k-3)/(4*p)
assert J_original==-1
assert J_exceptional==-1
assert collision==k-1
assert sp.simplify(J_original-required)!=0
assert sp.simplify(J_exceptional-required)!=0
print(json.dumps({'schema':'marici.nima.qg12-node-normal-jacobian.v1','status':'passed','bold_conjecture':'the q_g1-q_g2 normal/excess Jacobian supplies -(kappa-3)/(4p)','original_normal_jacobian':str(J_original),'exceptional_normal_jacobian':str(J_exceptional),'labeled_collision_coefficient':str(collision),'required_fitted_factor':str(required),'conjecture_disposition':'falsified generically','residual_conjecture':'the q_g2 grade -2 class is a separate excess-support summand; any map to grade -1 must use nonlocal denominator or lower-point source data, not the local wall normal bundle','claim_boundary':'first-order wall-normal and weighted exceptional coordinate maps only'},sort_keys=True))
