"""Generate and verify the WP405 no-refit precommitment."""

import hashlib
import json
from pathlib import Path


contract = {
    "grammar": "WP402 one mediator plus quadratic H/N terms, affine width, and at most one extra pole",
    "support": ["M2+c+Q2*c^2 nonzero at every context", "extra residue nonzero for extra-mass authority"],
    "fitted_packet": {
        "M2": "1", "J0": "1", "J1": "2", "J2": "0", "Q2": "0",
        "Gamma0": "1", "Gamma1": "1", "R2": "1", "MX2": "9",
    },
    "calibration_contexts": {
        "joint_static": ["c=0", "c=1", "c=2"],
        "absorptive": ["c=0,omega=2", "c=1,omega=2"],
        "extra_residual": ["omega=0", "omega=1"],
    },
    "withheld_contexts": {
        "static": "c=3",
        "dynamic": "c=2,omega=2",
        "extra_residual": "omega=2",
    },
    "predictions": {
        "static_H_A": ["4", "7/4"],
        "dynamic_A": "-5/37 + 30*I/37",
        "extra_residual": "1/5",
    },
    "decision_rule": "Any incompatible withheld record rejects the frozen packet; no parameter refit or added term is allowed.",
}

canonical = json.dumps(contract, sort_keys=True, separators=(",", ":"))
digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
expected_digest = "76735f9cc00c9829fd88f1c3cab85d91f9f0c502106eb7649eb9453cccfa89ef"

checks = {
    "contract_digest_is_frozen": digest == expected_digest,
    "calibration_and_withheld_contexts_disjoint": not (
        set(contract["calibration_contexts"]["joint_static"])
        & {contract["withheld_contexts"]["static"]}
    ),
    "all_nine_parameters_frozen": len(contract["fitted_packet"]) == 9,
    "three_predictions_reserved": len(contract["predictions"]) == 3,
    "decision_rule_forbids_refit": "no parameter refit" in contract["decision_rule"],
}

result = {
    "work_package": "WP405",
    "contract_sha256": digest,
    "contract": contract,
    "checks": checks,
    "passed": all(checks.values()),
    "status": "prospective precommitment only; no physical observations have been made",
}

out = Path(__file__).parents[1] / "results" / "wp405_no_refit_precommitment.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["passed"]:
    raise SystemExit(1)
