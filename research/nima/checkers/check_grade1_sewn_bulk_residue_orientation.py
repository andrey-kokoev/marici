"""Compare the grade -1 q_g1 wall form with the positive-sheet exceptional bulk residue."""
import json
import sympy as sp
a,k,p=sp.symbols('a k p')
root=a**2+(4*k-5)*p**2
bulk_xi_residue=(a+p)/(2*p*(a-p)**2*(a+3*p)*root)
# da wedge dxi/(xi+1) = -dlog(xi+1) wedge da, hence Poincare residue is -coefficient*da.
oriented_bulk_wall=-bulk_xi_residue
qg1=-(a+p)/(2*p*(a-p)**2*(a+3*p)*root)
assert sp.factor(oriented_bulk_wall-qg1)==0
node=sp.factor(sp.residue(qg1,a,-3*p))
assert sp.factor(node-1/(64*p**4*(k+1)))==0
print(json.dumps({'schema':'marici.nima.grade1-sewn-bulk-residue-orientation.v1','status':'passed','bulk_positive_sheet_measure_ratio':1,'poincare_orientation':'da wedge dxi = -dxi wedge da','oriented_q_g1_coefficient':str(qg1),'q_g1_q_g3_node_residue':str(node),'source_typed_comparison':'exact Poincare boundary residue','physical_period_nonzero_inferred':False,'claim_boundary':'cohomology and orientation comparison only; no explicit positive-cut chain or period integral'},sort_keys=True))
