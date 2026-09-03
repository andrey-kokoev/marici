"""Exact rational robustness margin for the coherent c=1 rank-two Gram cell."""
from fractions import Fraction as F
import json
def dec(s): return F(s)
d=dec('2.12511463965217217'); c=dec('-0.846660221734685927')
zeta_tail=dec('0.000092110177077'); tv=F(5184); E=zeta_tail*tv
d_lo=d-E; c_abs_hi=abs(c)+E; det_lo=d_lo*d_lo-c_abs_hi*c_abs_hi
assert E==dec('0.477499157967168')
assert d_lo>0 and det_lo>0
# Deliberate failure: a unit independent error destroys this proof strategy.
E_bad=F(1); det_bad=(d-E_bad)**2-(abs(c)+E_bad)**2
assert det_bad<0
print(json.dumps({'schema':'marici.nima.c-one-coarse-tail-margin.v1','status':'passed','N':3,'tail_zeta_upper':float(zeta_tail),'total_variation':5184,'independent_error_upper':float(E),'diagonal_lower':float(d_lo),'cross_absolute_upper':float(c_abs_hi),'determinant_lower':float(det_lo),'deliberate_failure_error':1.0,'deliberate_failure_determinant':float(det_bad),'bold_conjecture':'the corrected undilated TV=5184 makes the N=3 coarse tail too weak to certify rank two','disposition':'falsified','claim_boundary':'conditional robustness calculation around independently reproduced c=1 centers; directed interval prefix translation remains required'},sort_keys=True))
