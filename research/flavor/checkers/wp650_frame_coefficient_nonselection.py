"""Exact WP650 coefficient nonselection after the faithful frame."""
import json
import runpy
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp649 = json.loads((ROOT / "results" / "wp649_two_triplet_faithful_frame.json").read_text())
wp646 = runpy.run_path(str(ROOT / "checkers" / "wp646_nonaligned_word_response_ladder.py"))
I3, J1, J2 = sp.eye(3), wp646["J"][0], wp646["J"][1]
response = wp646["response"]([I3, J1, J2])

# Two equally source-legal scalar coefficient packets in one sector.
Y0 = I3
Y1 = I3 + J1
norm0 = sp.trace(Y0*Y0.H)
norm1 = sp.trace(Y1*Y1.H)

checks = {
    "wp649_dependency_passed": wp649["status"] == "PASS",
    "coefficient_control_dimension_is_twelve_real": response.cols == 12,
    "intrinsic_response_rank_is_eight": response.rank() == 8,
    "local_control_kernel_dimension_is_four": len(response.nullspace()) == 4,
    "hostile_packets_are_literal_distinct": Y0 != Y1,
    "hostile_packets_are_physically_distinguished": sp.simplify(norm0-norm1) != 0,
    "hostile_norms_are_exact": norm0 == 3 and norm1 == 5,
}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP650", "status": "PASS", "checks": checks,
    "admitted_state_domain": "WP649 ordered orthonormal two-triplet vacuum with arbitrary complex scalar sector couplings",
    "faithful_quotient_coordinate": "ten-dimensional intrinsic quark quotient, recorded by physical16",
    "source_authorized_probe_family": "complex coefficients of {I,J_n,J_m} in each of the up and down sectors",
    "contextual_partition": "twelve-real control space has rank-eight physical tangent image and a four-dimensional local kernel at the exact hostile witness",
    "classification": "faithful frame rigidifier plus constrained carrier; neither coefficient selector nor source identifier",
    "hostile_pair": {"packet_0": "Y=I", "packet_1": "Y=I+J_n", "TrYYdagger": [3, 5]},
    "smallest_exact_falsifier": "an SO(3)-derived equation fixing any scalar sector coefficient without an added source invariant",
    "physical_instrument_gate": "derive messenger vertices and calibrated observables sensitive to the rank-eight image; scalar coefficient law remains prior",
}
(ROOT / "results" / "wp650_frame_coefficient_nonselection.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
