"""Falsify naive marked-normal closure of the q_g2 extra soft grade."""
import json
import sympy as sp
k,p=sp.symbols('k p', nonzero=True)
r1=-(k-3)/(64*p**4*(k-1)**2)
r2_x=-1/(16*p**3*(k-1)**2)
r2_collision=sp.factor((k-1)*r2_x)
closure_x=sp.factor(r1+r2_x)
closure_collision=sp.factor(r1+r2_collision)
required_factor=sp.factor(-r1/r2_x)
assert closure_x!=0
assert closure_collision!=0
assert sp.simplify(required_factor+(k-3)/(4*p))==0
print(json.dumps({'schema':'marici.nima.qg2-marked-normal-grade-shift.v1','status':'passed','bold_conjecture':'multiplication by the source-marked soft normal x shifts q_g2 to grade -1 and closes the q_g1-q_g2 node','q_g1_node_residue':str(r1),'q_g2_after_x_node_residue':str(r2_x),'closure_residual_after_x':str(closure_x),'closure_residual_after_collision_section':str(closure_collision),'bold_conjecture_disposition':'falsified generically','exact_extra_factor_required_for_closure':str(required_factor),'residual_conjecture':'a valid excess-Gysin map must derive the marked normal shift together with the exact node Jacobian factor -(kappa-3)/(4p)','claim_boundary':'algebraic node residues only; no assertion that the required factor is source-authorized'},sort_keys=True))
