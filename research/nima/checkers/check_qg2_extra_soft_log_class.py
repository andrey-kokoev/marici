"""Residue/exactness test for the q_g2 extra X1-soft leading one-form."""
import json
import sympy as sp
xi,k,p=sp.symbols('xi k p')
# Overall sign depends on the chosen square-root branch; nonvanishing does not.
f=-1/(16*p**3*(k-1)*(xi+1)*(k+xi))
r_endpoint=sp.factor(sp.residue(f,xi,-1))
r_conductor=sp.factor(sp.residue(f,xi,-k))
r_infinity=sp.factor(-r_endpoint-r_conductor)
assert r_endpoint!=0 and r_conductor!=0
assert sp.factor(r_endpoint+r_conductor)==0
assert r_infinity==0
# A derivative of a rational function has zero residues at every finite pole.
rational_exact=False
print(json.dumps({'schema':'marici.nima.qg2-extra-soft-log-class.v1','status':'passed','one_form_coefficient':str(f),'finite_residues':{'xi=-1':str(r_endpoint),'xi=-kappa':str(r_conductor)},'residue_at_infinity':str(r_infinity),'rationally_exact':rational_exact,'absolute_meromorphic_class_nonzero':True,'relative_class_zero_inferred':False,'support_typing':{'xi=-1':'soft endpoint divisor','xi=-kappa':'exceptional Cayley-Menger reduced-factor/conductor divisor'},'claim_boundary':'generic kappa != 1 and nonzero p; analytic epsilon normalization and physical cycle pairing excluded'},sort_keys=True))
