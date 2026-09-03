"""Show that changing the existing d parameter cannot implement the c=1 archimedean moments."""
from fractions import Fraction as F
import json
# Existing integral_shift uses exponential rate (4n+d)/2 = 2n+d/2 after x=2u.
# Direct c=1 profile needs rate n+1/4 with no x/2 substitution.
existing_n_slope=F(2); target_n_slope=F(1)
required_d_from_constant=F(1,2) # d/2=1/4
assert existing_n_slope!=target_n_slope
# Matching n=0 with d=1/2 fails already at n=1.
def existing(n,d): return 2*F(n)+F(d,2)
def target(n): return F(n)+F(1,4)
assert existing(0,required_d_from_constant)==target(0)
assert existing(1,required_d_from_constant)!=target(1)
print(json.dumps({'schema':'marici.nima.c-one-arch-parameter-no-go.v1','status':'passed','existing_rate':'2*n+d/2','target_rate':'n+1/4','constant_matching_d':'1/2','n1_existing':str(existing(1,required_d_from_constant)),'n1_target':str(target(1)),'bold_conjecture':'the existing integral_shift d parameter can implement the coherent c=1 repair','disposition':'falsified','residual_conjecture':'c=1 requires a new undilated moment kernel with rate n+1/4, not retuning d in the x=2u formula'},sort_keys=True))
