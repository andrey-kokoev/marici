"""Unimodular incidence and residue orientation at E_T=q_G12=y12=0."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/total-energy-cut-corner-unimodular.json"

# (E,q)^T = J (E,y)^T with q=E+y.
J = [[1, 0], [1, 1]]
det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
assert det == 1

# dE wedge dq = dE wedge (dE+dy) = dE wedge dy.  Reversing the
# two residue orders supplies the ordinary Koszul sign -1.
packet = {
    "schema": "marici.benincasa.total_energy_cut_corner_unimodular.v1",
    "source_equation": "q_G12=E_T+y12",
    "coordinate_jacobian": J,
    "determinant": det,
    "regular_sequence": ["E_T", "q_G12"],
    "corner_equation": "E_T=q_G12=0 iff E_T=y12=0",
    "excess_tor": 0,
    "orientation_identity": "dE_T wedge dq_G12 = dE_T wedge dy12",
    "iterated_residue_swap_sign": -1,
    "mod2_carrier_defect": 0,
    "physical_chain_commutator_computed": False,
    "interpretation": "The base Cut-nearby square is transverse and unimodular. Any nonzero physical commutator or activation of the Legendre Z/2 coinvariant must come from the relative Cayley-Menger/signed-minor chain packet.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
