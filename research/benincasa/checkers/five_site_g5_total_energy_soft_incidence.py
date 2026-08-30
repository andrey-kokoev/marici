import json
from pathlib import Path

# Source-labelled local linear forms in coordinates (E_T, y_e).
# The change (E_T,y_e) -> (E_T,q_e) has determinant 2.
matrix = [[1, 0], [1, 2]]
determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
assert determinant == 2

packet = {
    'schema': 'marici.five_site_g5_total_energy_soft_incidence.v1',
    'marked_wall': 'q_e=E_T+2*y_e',
    'intersection_ideal_identity': '(E_T,q_e)=(E_T,2*y_e)',
    'coordinate_change_determinant': determinant,
    'cartier_transverse_over_Q': True,
    'carrier_classification': 'existing total-energy/site-soft corner',
    'generic_total_energy_intersection_excluded': True,
}
Path('research/benincasa/results/five-site-g5-total-energy-soft-incidence.json').write_text(
    json.dumps(packet, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(json.dumps(packet, sort_keys=True))
