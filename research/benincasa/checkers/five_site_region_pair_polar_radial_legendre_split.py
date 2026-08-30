import json
from fractions import Fraction
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-region-pair-polar-normal-blowup.json').read_text())
assert src['exceptional_modulus']=='m=h_2*r/(h_2*r-h_1)'

# The branch polynomial is linear in the common radial normal rho.
def branch_polynomial(x,h1,h2,r,rho):
    return x*(1-x)*(x*h1+(1-x)*h2)*(x*rho*r+(1-x)*rho)

for vals in [(2,3,5,7),(3,5,7,11),(5,11,13,17)]:
    x,h1,h2,r=map(Fraction,vals)
    x=x/(x+1)
    for rho in map(Fraction,(2,7,19)):
        assert branch_polynomial(x,h1,h2,r,rho)==rho*branch_polynomial(x,h1,h2,r,Fraction(1))

packet={
 'schema':'marici.five_site_region_pair_polar_radial_legendre_split.v1',
 'normal_chart':['delta_2=rho','delta_1=rho*r'],
 'curve_rescaling':'w^2=rho*F_r(x); W=w/sqrt(rho) gives W^2=F_r(x)',
 'period_factorization':'Pi(rho,r)=rho^(-1/2)*Pi_Leg(r)',
 'connection':'nabla=d-(1/2)dlog(rho)*Id+A_Leg(r)dr',
 'mixed_curvature':'zero',
 'mixed_extension':'absent in the resolved local coefficient family',
 'chart_transition':'on delta_1=rho_prime, s=delta_2/delta_1: rho_prime=rho*r, s=1/r; the square-root transition is the existing Kummer/root-cover character',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-polar-radial-legendre-split.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
