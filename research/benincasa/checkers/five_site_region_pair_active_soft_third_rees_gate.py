import json
from fractions import Fraction
from pathlib import Path

# Verify the two polynomial-division identities at independent exact rational
# points.  They determine the logarithmic remainders universally.
for r,d,c in [(Fraction(2),Fraction(3),Fraction(5)),(Fraction(7,3),Fraction(2,5),Fraction(11,7)),(Fraction(5,2),Fraction(13,4),Fraction(3,2))]:
    lhs3=r**3/(d+c*r)
    rhs3=r*r/c-d*r/c**2+d*d/c**3-d**3/(c**3*(d+c*r))
    lhs2=r**2/(d+c*r)
    rhs2=r/c-d/c**2+d*d/(c**2*(d+c*r))
    assert lhs3==rhs3 and lhs2==rhs2

packet={
 'schema':'marici.five_site_region_pair_active_soft_third_rees_gate.v1',
 'local_integrand':'r^2*(A_0+A_1*r+A_delta*delta+...)/(delta+c*r+d*r^2+...)',
 'zero_ray_condition':'A_0=0',
 'division_identity_r3':'r^3/(delta+c*r)=r^2/c-delta*r/c^2+delta^2/c^3-delta^3/[c^3*(delta+c*r)]',
 'division_identity_r2':'r^2/(delta+c*r)=r/c-delta/c^2+delta^2/[c^2*(delta+c*r)]',
 'third_log_angular_density':'A_1/c^4-A_delta/c^3',
 'third_rees_coefficient':'integral_dOmega(A_1/c^4-A_delta/c^3)',
 'acceptance':'third Rees delta^3 log(delta) iff the source-normalized angular integral is nonzero',
 'currently_missing':['source-fixed normal deformation defining A_delta','radial derivative A_1 of the complete residual coefficient','physical angular-domain/orientation integral'],
 'carrier_change_required':False,
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-active-soft-third-rees-gate.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
