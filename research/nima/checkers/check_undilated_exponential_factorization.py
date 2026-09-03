"""Exact audit of the optimized dyadic factorization and knot-sign branches."""
from fractions import Fraction as F
import json
import preconditioned_spline_weil as w
A=w.scale(F(2),w.log_q(F(2)))
indices=set();unresolved=[]
for i in range(4):
 b=F(4*i+1,4)
 for m in range(-4,5):
  for j in range(9):
   # b*(m*2log2+4-j) = b*(4-j) + (2im+m/2)*log2
   lhs_log2_coefficient=2*b*m
   optimized_sqrt2_exponent=4*i*m+m
   assert lhs_log2_coefficient==F(optimized_sqrt2_exponent,2)
   s=w.add(w.scale(F(m),A),(F(4-j),F(4-j)))
   sign='positive' if s[0]>=0 else 'negative' if s[1]<=0 else 'unresolved'
   if sign=='unresolved':unresolved.append({'i':i,'m':m,'j':j})
   indices.add((i,j))
assert not unresolved and len(indices)==36
print(json.dumps({'schema':'marici.nima.undilated-exponential-factorization.v1','status':'passed','factorization':'exp((i+1/4)(ma+4-j)) = exp((i+1/4)(4-j))*sqrt(2)^(4im+m)','checked_i':[0,1,2,3],'checked_m':[-4,-3,-2,-1,0,1,2,3,4],'checked_j':[0,1,2,3,4,5,6,7,8],'cached_knot_keys':36,'all_knot_signs_resolved':True,'claim_boundary':'exact factorization and branch preflight only; no transcendental interval result'},sort_keys=True))
