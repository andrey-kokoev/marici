"""Exact rational Weyl/row-sum robustness comparison for the coherent c=1 rank-three cell."""
from fractions import Fraction as F
import json
scout_min=F('0.6204848787')
E4=F('0.06101538') # conservative decimal upper bound per Toeplitz cell
penalty4=3*E4
lower4=scout_min-penalty4
assert lower4>0
E3=F('0.477499157967168')
penalty3=3*E3
lower3=scout_min-penalty3
assert lower3<0
print(json.dumps({'schema':'marici.nima.c-one-rank-three-tail-margin.v1','status':'passed','rank':3,'scouted_min_eigenvalue':float(scout_min),'N4_entry_error_upper':float(E4),'N4_row_sum_penalty':float(penalty4),'N4_min_eigenvalue_lower':float(lower4),'N3_entry_error_upper':float(E3),'N3_row_sum_penalty':float(penalty3),'N3_min_eigenvalue_lower':float(lower3),'bold_conjecture':'coarse TV=5184 tails require signed-atom sharpening to certify the first three translates','disposition':'falsified at the robustness level','residual_conjecture':'one additional exact moment, N=4, leaves positive row-sum reserve; directed prefix intervals and a certified center eigenvalue bound remain required'},sort_keys=True))
