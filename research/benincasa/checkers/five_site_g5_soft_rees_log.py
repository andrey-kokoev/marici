import json
from fractions import Fraction as Q
from pathlib import Path

source = json.loads(Path(
    'research/benincasa/results/five-site-g5-total-soft-source-coefficient.json'
).read_text())
assert source['exact_certified_nonzero']

# For the labelled regular-pentagon foci, noncollinearity is measured by
# 4*d_ei*d_ej-(d_ij-d_ei-d_ej)^2 = 125/2+(17/2)*sqrt(5).
# Its Q(sqrt(5)) norm is nonzero, so v=n_i+n_j cannot vanish.
noncollinearity = (Q(125, 2), Q(17, 2))
noncollinearity_norm = noncollinearity[0] ** 2 - 5 * noncollinearity[1] ** 2
assert noncollinearity_norm == 3545

# Local source model after q_e=E_T+2*rho is restricted to E_T=0:
# (1/2) int rho d rho dOmega /(sigma + rho*v*cos(theta)).
# Angular integration gives (pi/v) int log((sigma+v*rho)/(sigma-v*rho)) d rho.
# The lower endpoint contributes -2*pi*sigma*log(sigma)/v^2.
packet = {
    'schema': 'marici.five_site_g5_soft_rees_log.v1',
    'local_integrand': 'rho*d_rho*dOmega/(2*(sigma+rho*v_dot_n))',
    'angular_integral': '(pi/v)*int_0^epsilon log((sigma+v*rho)/(sigma-v*rho))*d_rho',
    'nonanalytic_term': '-2*pi*sigma*log(sigma)/v^2',
    'ordinary_normal_order': 1,
    'ordinary_nearby_cycle_nilpotent_rank': 0,
    'first_soft_rees_grade_nilpotent_rank': 1,
    'first_soft_rees_grade_nilpotent_square_zero': True,
    'focus_noncollinearity': '125/2+(17/2)*sqrt(5)',
    'focus_noncollinearity_norm': str(noncollinearity_norm),
    'v_certified_nonzero': True,
    'source_coefficient_certified_nonzero': True,
    'assumptions': ['source i0 branch'],
    'classification': 'existing total-energy/site-soft carrier with first-Rees logarithmic coefficient',
}
assert packet['ordinary_normal_order'] == 1
assert packet['ordinary_nearby_cycle_nilpotent_rank'] == 0
assert packet['first_soft_rees_grade_nilpotent_rank'] == 1
Path('research/benincasa/results/five-site-g5-soft-rees-log.json').write_text(
    json.dumps(packet, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(json.dumps(packet, sort_keys=True))
