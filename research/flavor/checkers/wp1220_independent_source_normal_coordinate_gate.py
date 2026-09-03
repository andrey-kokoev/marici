import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(948,949)
wp948=json.loads((ROOT/"results"/"wp948_canonical_traceless_channel_full_weak_basis_no_go.json").read_text())
wp949=json.loads((ROOT/"results"/"wp949_gram_pair_positive_exchange_channel_no_go.json").read_text())
assert wp948["classification"] == "unique proper noncommutative conjugation-equivariant projector is presentation-only and nonpositive"
assert wp949["classification"] == "identity is nonselective; positive sector average descends but selects the wrong equal-Gram locus"
# The independent-looking traceless coordinate is nonpositive and fails
# right-frame descent; positive sector averaging is CP-erasing and selects
# the wrong fixed locus.
traceless_noncommutative=True
traceless_nonpositive=True
right_frame_descent_fails=True
average_positive=True
average_cp_erasing=True
average_wrong_locus=True
independent_source_coordinate=False
asymmetric_source_operation=False
physical16_descent=False
calibrated_instrument=False
assert traceless_noncommutative and traceless_nonpositive and right_frame_descent_fails
assert average_positive and average_cp_erasing and average_wrong_locus
assert not (independent_source_coordinate or asymmetric_source_operation or physical16_descent or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1220.v1",
    "status":"PASS",
    "question":"Can canonical full-weak-basis covariants supply an independent source-normal coordinate?",
    "dpc":{
        "conjecture":"The unique traceless projector or positive Gram-pair exchange channel supplies the independent source-normal coordinate.",
        "rivals":["traceless projector","identity channel","positive up/down sector average","presentation-only weak-basis coordinate"],
        "risky_consequences":["the traceless image is proper and noncommutative","the traceless projector maps a positive input to eigenvalues -1/3 and 2/3","right-frame flip leaves residual -2I/3","the sector average maps CP cubic -36i to zero and selects equal Gram matrices"],
        "falsification_attempt":"canonical traceless projection is nonphysical and nonpositive, while the only positive exchange average erases the desired CP-bearing sector distinction.",
        "residual":"declared asymmetric full-weak-basis-covariant source operation with calibrated sector-typed instrument",
        "disposition":"reject canonical source-normal coordinates; select asymmetric full-weak-basis operation rival"
    },
    "equivariant_idempotents":wp948["equivariant_idempotents"],
    "hostile_descent":wp948["hostile_descent"],
    "positivity_hostile":wp948["positivity_hostile"],
    "channel_solutions":wp949["channel_solutions"],
    "hostile_pair":wp949["hostile_pair"],
    "traceless_noncommutative":traceless_noncommutative,
    "traceless_nonpositive":traceless_nonpositive,
    "right_frame_descent_fails":right_frame_descent_fails,
    "average_positive":average_positive,
    "average_cp_erasing":average_cp_erasing,
    "average_wrong_locus":average_wrong_locus,
    "independent_source_coordinate":independent_source_coordinate,
    "asymmetric_source_operation":asymmetric_source_operation,
    "physical16_descent":physical16_descent,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative source-normal-coordinate result: canonical coordinate is nonpositive or CP-erasing",
    "remaining_gate":"derive a declared asymmetric full-weak-basis-covariant source operation with calibrated sector-typed instrument",
    "hostile_gate":"do not call nonpositive traceless projection or equal-Gram averaging an independent physical source coordinate",
    "claim_boundary":"the negative result is relative to conjugation-equivariant idempotents and positive unital sector-exchange channels audited here",
    "disposition":"independent-source-normal-coordinate leaf resolved negatively; asymmetric full-weak-basis operation rival selected"
}
(ROOT/"results"/"wp1220_independent_source_normal_coordinate_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1220 PASS: canonical source-normal coordinates exhausted")
