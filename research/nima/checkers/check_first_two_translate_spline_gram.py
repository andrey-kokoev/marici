"""Certified first two-translate Gram determinant using arbitrary symmetric shift lists."""
from fractions import Fraction as F
import json
import preconditioned_spline_weil as w
BASE_C=[F(1),F(-5),F(33,4),F(-5),F(1)]; BASE_M=[2,1,0,-1,-2]
CROSS_C=[F(1,2),F(-5,2),F(37,8),F(-5),F(37,8),F(-5,2),F(1,2)]; CROSS_M=[3,2,1,0,-1,-2,-3]
def evaluate(coeff,index,wrong_sign=False):
    w.COEFF=list(coeff); w.SHIFT_INDEX=list(index); w._ARCH_FINITE.clear()
    a=w.scale(F(2),w.log_q(F(2)))
    return w.add(w.arch(a)[0],w.prime_term(a,wrong_sign))
def fl(iv): return [float(iv[0]),float(iv[1])]
baseline=evaluate(BASE_C,BASE_M); baseline_repeat=evaluate(BASE_C,BASE_M)
assert baseline==baseline_repeat and baseline[0]>0
cross=evaluate(CROSS_C,CROSS_M)
determinant=w.sub(w.mul(baseline,baseline),w.mul(cross,cross))
wrong_cross=evaluate(CROSS_C,CROSS_M,True)
wrong_determinant=w.sub(w.mul(baseline,baseline),w.mul(wrong_cross,wrong_cross))
assert cross[0]>0 and determinant[1]<0
print(json.dumps({'schema':'marici.nima.first-two-translate-spline-gram.v2','status':'passed','tail_prefix_N':3,'baseline':fl(baseline),'cross':fl(cross),'determinant':fl(determinant),'negative_direction':'disagreement','prime_sign_failure_cross':fl(wrong_cross),'prime_sign_failure_determinant':fl(wrong_determinant),'baseline_regression_preserved':True,'bounded_output':True},sort_keys=True))
