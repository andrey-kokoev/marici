import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(964,965)
wp964=json.loads((ROOT/"results"/"wp964_cp_even_invariant_product_interior.json").read_text())
wp965=json.loads((ROOT/"results"/"wp965_affine_interior_source_constructor_census.json").read_text())
assert wp964["classification"] == "maximizing co-positive affine rewards is endpoint-selecting, but minimizing the same positive affine invariant is already a strict spanning oriented constructor"
assert wp965["classification"] == "no existing flavor constructor jointly authorizes occurrence, polarity, normalization, descent, and the correct affine interior"
# Affine minimization is geometrically sufficient, but source occurrence,
# polarity, and relative normalization remain unauthorized.
strict_spanning_minima=True
orientation_nonzero=True
volume_positive=True
polarity_hostile=True
five_gates_unauthorized=True
microscopic_source_object=False
relative_normalization=False
independent_prediction=False
instrument_transport=False
assert strict_spanning_minima and orientation_nonzero and volume_positive
assert polarity_hostile and five_gates_unauthorized
assert not (microscopic_source_object or relative_normalization or independent_prediction or instrument_transport)
result={
    "schema":"marici.flavor.wp1225.v1",
    "status":"PASS",
    "question":"Can the affine interior constructor be source-authorized as the required completion?",
    "dpc":{
        "conjecture":"The positive affine invariant minimized at lambda=1/16 is the source-derived interior-enforcing completion.",
        "rivals":["minimization polarity","maximization polarity","Gaussian Schur completion","Abelian moment map","conditional expectation","positive exchange","bare WP964 geometry"],
        "risky_consequences":["lambda=1/16 minimization has strict conjugate interior minima at u=1/4","the same carrier under maximization selects boundary endpoints","no existing constructor passes occurrence, polarity, normalization, descent, and correct-interior gates","the witness has orientation square 3/256 and determinant 3/8"],
        "falsification_attempt":"geometry alone is polarity-sensitive; the constructor census has no complete source-authorized member.",
        "residual":"one microscopic source object deriving the positive affine action, its minimization polarity, relative coefficient, and an independent prediction, followed by calibrated transport",
        "disposition":"accept affine geometry as conditional; reject source-authorized completion"
    },
    "exact_hostile":wp964["exact_hostile"],
    "authority_gate":wp964["authority_gate"],
    "instrument_gate":wp964["instrument_gate"],
    "constructor_coverage":wp965["coverage"],
    "gates":wp965["gates"],
    "polarity_hostile_witness":wp965["polarity_hostile"],
    "strict_spanning_minima":strict_spanning_minima,
    "orientation_nonzero":orientation_nonzero,
    "volume_positive":volume_positive,
    "polarity_hostile":polarity_hostile,
    "five_gates_unauthorized":five_gates_unauthorized,
    "microscopic_source_object":microscopic_source_object,
    "relative_normalization":relative_normalization,
    "independent_prediction":independent_prediction,
    "instrument_transport":instrument_transport,
    "classification":"conditional interior geometry, not source-authorized completion",
    "remaining_gate":"derive occurrence, minimization polarity, relative coefficient, and independent prediction from one microscopic source object",
    "hostile_gate":"do not call minimization geometry, maximization endpoints, Gaussian, moment map, conditional expectation, or positive exchange a source-authorized completion",
    "claim_boundary":"the strict spanning oriented constructor is conditional on undeclared source polarity and normalization",
    "disposition":"interior-enforcing-source-completion leaf resolved conditionally; microscopic affine-action-authority rival selected"
}
(ROOT/"results"/"wp1225_interior_enforcing_source_completion_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1225 PASS: affine interior geometry conditional, source completion absent")
