"""Exact kinematic and response-rank no-go for reciprocal protected widths."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
MA, MB, mn = sp.symbols("MA MB mn", positive=True)
margin_ab = MA-MB-mn
margin_ba = MB-MA-mn
y, z = sp.symbols("y z", positive=True)
total_width_coordinate = sp.Matrix([y**2+z**2])
chiral_coordinates = sp.Matrix([y**2, z**2])
total_jacobian = total_width_coordinate.jacobian([y, z])
chiral_jacobian = chiral_coordinates.jacobian([y, z])

pair_1 = {y: sp.Integer(1), z: sp.Integer(2)}
pair_2 = {y: sp.Rational(11, 5), z: sp.Rational(2, 5)}
W1 = (y**2+z**2).subs(pair_1)
W2 = (y**2+z**2).subs(pair_2)
Q1 = (y**4+z**4).subs(pair_1)
Q2 = (y**4+z**4).subs(pair_2)

checks = {
    "opposite_decay_margins_sum_to_negative_threshold": sp.simplify(margin_ab+margin_ba) == -2*mn,
    "both_directional_decays_cannot_be_open": bool(sp.ask(sp.Q.negative(margin_ab+margin_ba))),
    "unpolarized_massless_total_width_has_rank_one": total_jacobian.rank() == 1,
    "two_chiral_ports_would_have_rank_two": chiral_jacobian.rank() == 2,
    "hostile_pair_has_same_total_width": W1 == W2 == 5,
    "hostile_pair_has_different_loop_erosion": Q1 == 17 and Q2 == sp.Rational(14657, 625) and Q1 != Q2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP671", "status": "PASS", "checks": checks,
    "kinematic_identity": "Delta_AB+Delta_BA=-2m_n<0",
    "ordinary_port": "one open unpolarized massless-limit width proportional to y^2+z^2",
    "ordinary_response_rank": 1,
    "hostile_pair": {"vertices_1": ["1", "2"], "vertices_2": ["11/5", "2/5"], "common_width_coordinate": "5", "erosion_coordinates": ["17", "14657/625"]},
    "repair": "two source-derived chiral or polarization-resolved ports, not opposite directional decays",
    "classification": "the protected threshold width does not identify the loop-erosion coordinate",
    "smallest_exact_falsifier": "both strict directional threshold margins positive for m_n>0",
    "remaining_gate": "derive a polarization analyzer and its detector response from the same protected messenger source",
}
(ROOT / "results" / "wp671_protected_threshold_port_no_go.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
