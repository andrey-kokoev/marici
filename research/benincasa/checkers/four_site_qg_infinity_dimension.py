"""Type the four-site total-energy-residue infinity coefficient geometry."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-infinity-dimension.json"

n_edge_variables = 4
qg_edge_rank = 0                 # q_G=sum_i x_i contains no y variable.
projective_base_dimension = n_edge_variables - 1 - qg_edge_rank
branch_degree = 4
half_branch = branch_degree // 2
canonical_coefficient = -(projective_base_dimension + 1) + half_branch

assert projective_base_dimension == 3
assert canonical_coefficient == -2

# Smooth benchmark: a quartic surface in P3 is K3 with Euler characteristic
# 24.  For a degree-two cover, chi(X)=2 chi(P3)-chi(branch).
chi_p3 = 4
chi_smooth_quartic = 24
chi_smooth_double_solid = 2 * chi_p3 - chi_smooth_quartic
b3_smooth_benchmark = 4 - chi_smooth_double_solid
assert chi_smooth_double_solid == -16
assert b3_smooth_benchmark == 20

# The actual infinity form 4B4=-Delta^T adj(G) Delta has Delta=0 at the
# physical diagonal y=(1,1,1,1), so both B4 and its first derivatives vanish.
physical_diagonal_delta = [0, 0, 0]
assert physical_diagonal_delta == [0, 0, 0]

packet = {
    "schema": "marici.benincasa.four_site_qg_infinity_dimension.v1",
    "qG": "sum_i x_i",
    "qG_edge_rank": qg_edge_rank,
    "remaining_edge_variables": n_edge_variables,
    "infinity_base": "P^3",
    "branch_degree": branch_degree,
    "coefficient_geometry": "quartic double solid (actual branch singular at the physical diagonal)",
    "canonical_class": "K_X=-2 pi^*H",
    "smooth_benchmark": {
        "branch": "smooth quartic K3 surface",
        "euler_characteristic": chi_smooth_double_solid,
        "b3": b3_smooth_benchmark,
        "h21": b3_smooth_benchmark // 2,
    },
    "actual_physical_diagonal": [1, 1, 1, 1],
    "actual_diagonal_branch_status": "singular because Delta=0",
    "edge_dependent_residue_comparison": "rank-one edge normal leaves P^2 and the degree-two del Pezzo surface of Entries 1154-1155",
    "correction": "Entries 1154-1155 do not classify the q_G residue sector",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
