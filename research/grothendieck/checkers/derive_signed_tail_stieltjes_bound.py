"""Work ledger for the next certificate: Abel summation data, not a verdict.

For f=-K>=0 on an adverse interval [a,b], psi<=U gives
 sum f(log n)Lambda(n) <= f(a)U(exp(a))+integral_a^b U(exp(u))(-f'(u))du
when f is decreasing.  Nonmonotone cells must be split at certified critical
points or use their positive variation.  This replaces repeated U(exp(r))
charges in the transition scout.
"""
from pathlib import Path
import json
out={'status':'DERIVATION_RECORDED','formula':'f(a) U(exp(a)) + integral U(exp(u)) (-f_prime(u)) du',
 'U':'2 log(2) x + log(x) + log(2)','required_certificates':['kernel derivative sign or positive variation on every adverse transition cell','root-box absolute contribution','infinite adverse suffix Abel bound'],'not_a_tail_certificate':True}
(Path(__file__).parents[1]/'results'/'signed-tail-stieltjes-work-ledger.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
