import json
from pathlib import Path

from five_site_g5_cm_domain import landau

def norm(z):
    return z.a * z.a - 5 * z.b * z.b

constant_norm = norm(landau[0])
leading_norm = norm(landau[-1])
assert constant_norm != 0
assert leading_norm != 0

packet = {
    'schema': 'marici.five_site_g5_projective_slice_boundary.v1',
    'slice_coordinate': 'x=t^2',
    'total_energy_boundary': 'x=0',
    'degree': len(landau) - 1,
    'constant_coefficient_norm': str(constant_norm),
    'leading_coefficient_norm': str(leading_norm),
    'meets_total_energy_on_cyclic_slice': False,
    'meets_projective_infinity_on_cyclic_slice': False,
    'classification': 'all six projective slice intersections are finite and nonzero',
}
Path('research/benincasa/results/five-site-g5-projective-slice-boundary.json').write_text(
    json.dumps(packet, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(json.dumps(packet, sort_keys=True))
