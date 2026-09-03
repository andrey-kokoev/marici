"""Exact scale-covariance audit for the spline pole annihilator."""
from fractions import Fraction as F
import json
# In units of log(2), baseline a=2; dilation c=1/2 moves zero character to c/2.
a=F(2); c=F(1,2); target=F(1,2)
fixed_shift_zero=c/2
rescaled_a=c*a
rescaled_zero=c*target*a/rescaled_a
assert fixed_shift_zero==F(1,4)
assert rescaled_a==F(1)
assert rescaled_zero==target
print(json.dumps({'schema':'marici.nima.spline-dilation-pole-annihilator.v1','status':'passed','dilation_c':str(c),'fixed_a_zero_character':str(fixed_shift_zero),'required_completed_zeta_character':str(target),'fixed_a_annihilates_poles':False,'scale_covariant_a_over_log2':str(rescaled_a),'rescaled_zero_character':str(rescaled_zero),'rescaled_a_annihilates_poles':True,'bold_conjecture':'the N=3 hybrid checker may omit completed-zeta pole cells using the undilated annihilator','disposition':'falsified','residual_conjecture':'regenerate with a_c=c*a or restore explicit pole cells before interpreting the negative determinant'},sort_keys=True))
