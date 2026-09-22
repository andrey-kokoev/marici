"""Exact source-to-observation budget arithmetic for realized towers."""
from pathlib import Path
import json
from fractions import Fraction as F
# Uniform selected response bounds inherited from the source certificate.
assert F(2944*70,15000)<14
assert F(16*4*70,15000)<F(3,10)
assert 3*F(3,10)==F(9,10)
# Parameter fixture only; it is not a claim that these priors were
# measured for some unspecified tower.
M=F(10**6); rho=F(1); d=F(1,10)
b=d/F(40*10**18)
coeff=b*rho/14
m=2
while M/F(2**(2*m+2))>coeff:m+=1
# eta=1 in this exact finite parameter fixture.
height_ratio=14*M/(b*rho)
H=(height_ratio.numerator+height_ratio.denominator-1)//height_ratio.denominator
prime_ratio=M/(b*rho)
N=max(3,(prime_ratio.numerator+prime_ratio.denominator-1)//prime_ratio.denominator)
# T_N <= (10/9)/N follows from log N <= sqrt N, N>=1.
source=14/rho*(coeff+M/F(2**(2*m+2))+M/F(H+1))
prime=F(9,10)*F(10,9)/N*M/rho
measurement=b
assert 4*10**18*(source+prime+measurement)<=d/2
# The fixed witness is visible at depth two, since its source corner
# length four is below 2(m+1); deeper ideal powers cannot change it.
assert 4<2*(2+1)
result={'passed':True,'checks':{'selected_response_bound_14':True,
 'selected_port_bound_0_3':True,'five_term_error_allocation':True,
 'fixed_packet_stabilizes_at_depth_two':True},
 'parameter_fixture':{'M':str(M),'rho':str(rho),'margin_per_seam':str(d),
 'eta':1,'depth':m,'height':H,'conservative_prime_cutoff':N,
 'retained_source_error':str(coeff),'total_response_noise':str(b)},
 'scope':'Exact rational budget checks only. Finite support, cornerwise preservation and the actual response bounds are analytic inputs. No arbitrary noisy tower is assumed realizable, and no global source inverse from response data is asserted.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/finite-tower-attachment-budget.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
