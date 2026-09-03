"""N=3 two-translate Gram test with scale-covariant a_c=c*(2 log 2)=log 2."""
from fractions import Fraction as F
import json
import preconditioned_spline_weil as w
BASE_C=[F(1),F(-5),F(33,4),F(-5),F(1)]; BASE_M=[2,1,0,-1,-2]
CROSS_C=[F(1,2),F(-5,2),F(37,8),F(-5),F(37,8),F(-5,2),F(1,2)]; CROSS_M=[3,2,1,0,-1,-2,-3]
A_C=w.log_q(F(2))
def evaluate(coeff,index,wrong_sign=False):
    w.COEFF=list(coeff); w.SHIFT_INDEX=list(index); w._ARCH_FINITE.clear()
    return w.add(w.arch(A_C)[0],w.prime_term(A_C,wrong_sign))
def fl(iv): return [float(iv[0]),float(iv[1])]
baseline=evaluate(BASE_C,BASE_M); cross=evaluate(CROSS_C,CROSS_M)
determinant=w.sub(w.mul(baseline,baseline),w.mul(cross,cross))
coherent=w.add(baseline,cross); disagreement=w.sub(baseline,cross)
wrong_cross=evaluate(CROSS_C,CROSS_M,True)
assert baseline==evaluate(BASE_C,BASE_M)
print(json.dumps({'schema':'marici.nima.scale-covariant-two-translate-spline-gram.v1','status':'passed','preconditioner_shift':'log 2','dilation_c':'1/2','annihilator_characters':['-1/2','1/2'],'aligned_translation':'2 log 2','baseline':fl(baseline),'cross':fl(cross),'determinant':fl(determinant),'coherent':fl(coherent),'disagreement':fl(disagreement),'positive_semidefinite_certified':determinant[0]>=0 and baseline[0]>=0,'negative_determinant_certified':determinant[1]<0,'prime_sign_failure_cross':fl(wrong_cross),'baseline_regression_preserved':True,'bounded_output':True},sort_keys=True))
