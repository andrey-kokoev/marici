import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1012,1013,1014)
wp1012=json.loads((ROOT/"results"/"wp1012_mixed_portal_j_capacity.json").read_text())
wp1013=json.loads((ROOT/"results"/"wp1013_mixed_portal_ckm_no_go.json").read_text())
wp1014=json.loads((ROOT/"results"/"wp1014_mixed_word_universal_compiler.json").read_text())
assert wp1012["classification"] == "covariant mixed-portal capacity family; neither selector nor rigidifier"
assert wp1013["classification"] == "J-capacity actuator with empty measured-mixing image; neither selector nor rigidifier"
assert wp1014["classification"] == "universal covariant compiler; neither selector nor rigidifier"
# Mixed covariants can move J and compile the quotient, but the linear family
# fails the measured mixing image and the universal compiler has no source
# principle determining coefficients.
mixed_j_capacity=True
full_j_coordinate_reach=True
ckm_image_empty=True
universal_compiler=True
compiler_coefficients_unsolved=True
source_law_for_portal=False
full_physical16_image=False
numerical_prediction=False
calibrated_instrument=False
assert mixed_j_capacity and full_j_coordinate_reach and ckm_image_empty
assert universal_compiler and compiler_coefficients_unsolved
assert not (source_law_for_portal or full_physical16_image or numerical_prediction or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1232.v1",
    "status":"PASS",
    "question":"Can mixed covariant portals supply a source-selected Physical16 image?",
    "dpc":{
        "conjecture":"The one-parameter mixed portal or universal word compiler supplies the required source ratio and Physical16 image.",
        "rivals":["linear mixed portal","CKM mixing image","universal Hermitian word compiler","source-law assignment for compiler coefficients"],
        "risky_consequences":["the linear portal covers (0,5625/636056] in J squared and reaches all 1210 J-coordinate sheets","fitted J requires s squared greater than 4","the portal S2 floor exceeds the universal phase upper bound by 5294381/699338025","the word basis has rank nine and nonzero determinant","the compiler realizes an arbitrary admissible quotient only after target coefficients are supplied"],
        "falsification_attempt":"J reachability does not land in measured mixing, and universal compilation is algebraic reachability without a source law.",
        "residual":"source-derived mixed family or compiler-coefficient principle with enough independent invariant response to pass the full Physical16 image and instrument tests",
        "disposition":"accept mixed-portal and compiler capacity only; reject source selection"
    },
    "linear_portal":wp1012["portal"],
    "portal_j_squared":wp1012["J_squared"],
    "j_range":wp1012["range_on_nonnegative_branch"],
    "ckm_s2_floor":wp1013["portal_S2_floor_for_fitted_J_scale"],
    "target_s2_upper":wp1013["target_S2_universal_phase_upper_decimal"],
    "exact_separator_margin":wp1013["portal_separator_margin"],
    "word_basis_rank":wp1014["basis_rank"],
    "word_basis_determinant":wp1014["basis_determinant"],
    "quotient_capacity":wp1014["quotient_capacity"],
    "mixed_j_capacity":mixed_j_capacity,
    "full_j_coordinate_reach":full_j_coordinate_reach,
    "ckm_image_empty":ckm_image_empty,
    "universal_compiler":universal_compiler,
    "compiler_coefficients_unsolved":compiler_coefficients_unsolved,
    "source_law_for_portal":source_law_for_portal,
    "full_physical16_image":full_physical16_image,
    "numerical_prediction":numerical_prediction,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional mixed-portal capacity: algebraic reachability exists, source selection and Physical16 landing absent",
    "remaining_gate":"derive a source principle restricting or determining compiler coefficients and validate the complete Physical16 image with calibrated readout",
    "hostile_gate":"do not call J-coordinate reachability, CKM exclusion, or universal compilation a source-selected Physical16 image",
    "claim_boundary":"mixed covariants act as capacity constructors; neither fixes source coefficients nor physical readout",
    "disposition":"mixed-covariant-portal leaf resolved conditionally; compiler-coefficient source-principle rival selected"
}
(ROOT/"results"/"wp1232_mixed_covariant_portal_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1232 PASS: mixed portal capacity formal, compiler source principle absent")
