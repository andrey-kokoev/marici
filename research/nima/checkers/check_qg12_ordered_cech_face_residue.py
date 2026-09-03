"""Test whether an oriented iterated residue supplies the missing Cech-face coefficient."""
import json
import sympy as sp
k,p=sp.symbols('k p', nonzero=True)
qg1=(3-k)/(64*p**4*(k-1)**2)
iterated=1/(64*p**4*(k-1))
missing=-1/(32*p**4*(k-1)**2)
res_plus=sp.factor(qg1+iterated+iterated)
res_minus=sp.factor(qg1+iterated-iterated)
assert sp.simplify(iterated-missing)!=0
assert sp.simplify(-iterated-missing)!=0
assert res_plus!=0 and res_minus!=0
print(json.dumps({'schema':'marici.nima.qg12-ordered-cech-face-residue.v1','status':'passed','bold_conjecture':'the oppositely oriented ordered face is the source iterated residue and supplies the missing grade -1 coefficient','q_g1_residue':str(qg1),'q_g2_subleading_iterated_residue':str(iterated),'required_face_coefficient':str(missing),'closure_residual_face_plus':str(res_plus),'closure_residual_face_minus':str(res_minus),'conjecture_disposition':'falsified generically for either face orientation','exceptional_equalities':{'face_plus_matches_required_at':'kappa=-1','face_minus_matches_required_at':'kappa=3'},'residual_conjecture':'a Cech face generator may close the residue vector only if supplied as independent relative-chain data with a source coefficient; it is not the iterated residue of the existing bulk form'},sort_keys=True))
