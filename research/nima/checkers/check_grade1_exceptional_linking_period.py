"""Exact small-meridian periods of the grade -1 q_g3 sewn component."""
import json
import sympy as sp
xi,k,p=sp.symbols('xi k p')
w=-1/(64*p**4*(k-xi)*(xi+1))
r_endpoint=sp.factor(sp.residue(w,xi,-1))
r_branch=sp.factor(sp.residue(w,xi,k))
period_endpoint=sp.factor(2*sp.pi*sp.I*r_endpoint)
period_branch=sp.factor(2*sp.pi*sp.I*r_branch)
assert r_endpoint==-1/(64*p**4*(k+1))
assert r_branch==1/(64*p**4*(k+1))
assert sp.factor(period_endpoint+period_branch)==0
assert period_endpoint!=0
print(json.dumps({'schema':'marici.nima.grade1-exceptional-linking-period.v1','status':'passed','counterclockwise_periods':{'meridian_xi=-1':str(period_endpoint),'meridian_xi=kappa':str(period_branch)},'sum_homology_relation':str(sp.factor(period_endpoint+period_branch)),'positive_sheet_period_nonzero':True,'sheet_reversal_multiplier':-1,'physical_positive_cut_identified':False,'claim_boundary':'small algebraic meridians on q_g3 only; no source-derived identification with physical positive-cut chain'},sort_keys=True))
