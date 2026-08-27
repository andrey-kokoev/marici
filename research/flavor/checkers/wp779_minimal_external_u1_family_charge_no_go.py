"""Exact charge-lattice audit for the minimal external-U(1) flux window."""
import json
from math import gcd
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp778 = json.loads((ROOT / "results" / "wp778_flux_anomaly_tadpole_stability_gate.json").read_text(encoding="utf-8"))
x, y, z, m = sp.symbols("x y z m", integer=True)
mixed_su6_sq_u1 = 4*x + y + z
mixed_gravity_u1 = 15*x + 6*y + 6*z
cubic_u1 = 15*x**3 + 6*y**3 + 6*z**3
linear_solution = sp.solve(
    [sp.Eq(mixed_su6_sq_u1, 0), sp.Eq(mixed_gravity_u1, 0)], [x, z], dict=True
)[0]
cubic_on_solution = sp.expand(cubic_u1.subs(linear_solution))

solutions = []
for xv in range(-6, 7):
    for yv in range(-6, 7):
        for zv in range(-6, 7):
            if (mixed_su6_sq_u1.subs({x:xv,y:yv,z:zv}) == 0
                    and mixed_gravity_u1.subs({x:xv,y:yv,z:zv}) == 0
                    and cubic_u1.subs({x:xv,y:yv,z:zv}) == 0
                    and (xv,yv,zv) != (0,0,0)):
                if gcd(gcd(abs(xv), abs(yv)), abs(zv)) == 1:
                    solutions.append((xv,yv,zv))
solutions = sorted(set(solutions))

primitive = {x:0, y:1, z:-1}
indices = tuple((m*q).subs({**primitive,m:3}) for q in (x,y,z))
q = sp.symbols("q", integer=True)
common_solution = sp.solve(
    [sp.Eq(mixed_su6_sq_u1.subs({x:q,y:q,z:q}),0),
     sp.Eq(mixed_gravity_u1.subs({x:q,y:q,z:q}),0)], [q], dict=True
)
checks = {
    "wp778_dependency_passed": wp778["status"] == "PASS" and all(wp778["checks"].values()),
    "linear_anomalies_force_neutral_fifteen": linear_solution[x] == 0,
    "linear_anomalies_force_opposite_antifundamental_charges": linear_solution[z] == -y,
    "cubic_anomaly_then_cancels_identically": cubic_on_solution == 0,
    "bounded_primitive_lattice_is_only_two_orientations": solutions == [(0,-1,1),(0,1,-1)],
    "flux_three_indices_are_zero_plus_three_minus_three": indices == (0,3,-3),
    "complete_family_common_charge_is_only_zero": common_solution == [{q:0}],
    "minimal_packet_has_zero_net_linear_tadpole_charge": mixed_gravity_u1.subs(primitive) == 0,
    "opposite_charge_pair_is_vectorlike_in_four_dimensions": indices[1] == -indices[2],
}
checks = {name: bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package":"WP779", "status":"PASS", "checks":checks, "dependency":"WP778",
    "admitted_state_domain":"one four-dimensional chiral SU(6) family 15 plus two antifundamentals, with one external U(1)_F charge per representation and integer torus flux",
    "faithful_coordinate":"the integral charge triple (x,y,z), its mixed and cubic anomaly coefficients, and the three signed flux indices m(x,y,z)",
    "source_authorized_probe":"ordinary four-dimensional SU(6)^2-U(1)_F, gravitational-U(1)_F, and cubic-U(1)_F anomaly cancellation together with the flux index",
    "contextual_partition":"the anomaly-free charge lattice is the one-dimensional line (0,a,-a), with orientation a identified only if charge conjugation is admitted",
    "charge_result":"all anomaly-free assignments leave the 15 neutral and give the two antifundamentals opposite charges",
    "generation_result":"at flux three the indices are (0,3a,-3a), producing a vectorlike antifundamental pair rather than three complete chiral families",
    "tadpole_result":"the packet has zero dimension-weighted linear charge and does not supply the nonzero oriented localized charge required by WP778",
    "classification":"the minimal external U(1)_F is neither a complete-family selector nor a tadpole selector; it only rigidifies an oppositely oriented vectorlike pair",
    "smallest_exact_falsifier":"the primitive assignment (0,1,-1) gives indices (0,3,-3), so the 15 has no zero modes and the antifundamentals have opposite chirality",
    "deutschian_status":"a complete-family flux charge requires additional SU(6)-charged matter or a Green-Schwarz constructor, enlarging the source theory",
    "next_source_gate":"classify the smallest Green-Schwarz or additional-matter completion that makes common-sign family flux compulsory and also quantizes the oriented tadpole",
    "instrument_gate":"generation-resolved physical16 production and decay ports remain unconstructed",
    "primary_sources":["https://arxiv.org/abs/1604.07838","https://arxiv.org/abs/2007.08733"],
}
(ROOT/"results"/"wp779_minimal_external_u1_family_charge_no_go.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
