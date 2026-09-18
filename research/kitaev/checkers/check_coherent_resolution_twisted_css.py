from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NIMA = ROOT / "research/nima/results"
OUT = ROOT / "research/kitaev/results/coherent_resolution_twisted_css.json"

a3 = json.loads((NIMA / "a3-coherent-resolution.json").read_text())
transport = json.loads((NIMA / "n8-boundary-completed-cluster-transport.json").read_text())
arbitrary = json.loads((NIMA / "arbitrary-n-boundary-cluster-completion.json").read_text())
no_go = json.loads((NIMA / "radiative-generator-map-no-go.json").read_text())

weights = {k: Fraction(v) for k, v in transport["negative_simple_weights"].items()}
defect = Fraction(transport["exchange_defect"])

# A vertex-coboundary twist has d_k^rho=G_{k-1} d_k G_k^{-1}; hence
# consecutive products and ranks are conjugate to the untwisted ones.
ranks = a3["ranks"]
dimensions = {"C0": a3["basis"]["C0_clusters"], "C1": a3["basis"]["C1_mutations"], "C2": a3["basis"]["C2_faces"], "C3": a3["basis"]["C3_polytope"]}
flat = all(Fraction(h) == 1 for h in transport["face_holonomies"])
q_square_zero = flat and a3["checks"]["d1_d2_zero"] and a3["checks"]["d2_d3_zero"]
h1 = dimensions["C1"] - ranks["d1"] - ranks["d2"]

# Reduction of a Q-valued local system mod 2 requires every gauge scalar to
# be a 2-adic unit. At least one supplied boundary coordinate is not.
def v2(q):
    n, d = abs(q.numerator), q.denominator
    vn = vd = 0
    while n and n % 2 == 0: vn += 1; n //= 2
    while d % 2 == 0: vd += 1; d //= 2
    return vn - vd
valuations = {k: v2(v) for k, v in weights.items()}
mod2_gauge_defined = all(v == 0 for v in valuations.values())

# Naive defect-as-syndrome assignment sends one scalar to every face; it
# contradicts the measured flat curvature (all face holonomies are one).
naive_defect_face_curvature = [defect for _ in transport["face_holonomies"]]
naive_assignment_falsified = defect != 0 and flat

checks = {
    "input_packets_pass": a3["passed"] and transport["passed"] and arbitrary["passed"] and no_go["passed"],
    "flat_q_twist_squares_zero": q_square_zero,
    "q_twist_rank_preserved": ranks == {"d1": 13, "d2": 8, "d3": 1},
    "q_twist_h1_zero": h1 == 0,
    "mod2_reduction_obstructed_by_nonunit": not mod2_gauge_defined,
    "negative_defect_nonzero": defect < 0,
    "naive_uniform_face_assignment_falsified": naive_assignment_falsified,
    "degree_zero_physical_map_no_go_preserved": no_go["checks"]["only_constant_zero_cocycles"]
}
result = {
    "schema": "marici.kitaev.coherent_resolution_twisted_css.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "q_weighted_boundary_theorem": "For nonzero diagonal gauges G_k, d_k^rho=G_(k-1)d_kG_k^-1, so d_(k-1)^rho d_k^rho=0 and ranks/homology are unchanged.",
    "a3_ranks": ranks,
    "a3_h1_dimension": h1,
    "negative_simple_2_adic_valuations": valuations,
    "mod2_local_system_gauge_defined": mod2_gauge_defined,
    "exchange_defect": str(defect),
    "flat_face_curvature": [str(Fraction(h) - 1) for h in transport["face_holonomies"]],
    "naive_defect_face_curvature": [str(x) for x in naive_defect_face_curvature],
    "disposition": {
        "q_flat_transport": "trivial_gauge_twist",
        "mod2_weighted_transport": "undefined_without_integral_unit_model",
        "negative_exchange_defect": "untyped_obstruction_not_face_curvature",
        "canonical_css_shadow": "code_with_zero_logical_dimension"
    },
    "claim_boundary": "Exact for supplied A3 packets; arbitrary finite A_m conjugacy is conditional on nonzero vertex-coboundary transport. No LDPC, distance, completion, or operational-noise claim."
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2) + "\n")
raise SystemExit(0 if result["passed"] else 1)
