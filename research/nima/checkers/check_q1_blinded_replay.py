#!/usr/bin/env python3
"""Typed blinded replay for the Q-1 apparency decision."""

UNKNOWN = "unknown"
NEGATIVE = "negative"
POSITIVE = "positive"


def classify(evidence):
    required = ("carrier", "transport", "physical_readout")
    positives = [k for k in required if evidence.get(k) == POSITIVE]
    if positives:
        return {"verdict": "live_intrinsic_candidate", "witnesses": positives}

    missing = [k for k in required if evidence.get(k, UNKNOWN) == UNKNOWN]
    if missing:
        return {
            "verdict": "underdetermined",
            "required_next": [
                "derive_source_normalized_cycle_monodromy_and_variation"
                if k == "physical_readout" else f"derive_{k}_test"
                for k in missing
            ],
        }

    assert all(evidence[k] == NEGATIVE for k in required)
    return {
        "verdict": "apparent_in_declared_scope",
        "coefficient_status": evidence.get("coefficient", UNKNOWN),
        "coefficient_support_retained": evidence.get("coefficient") == POSITIVE,
    }


def main():
    masked = {
        "carrier": NEGATIVE,
        "coefficient": UNKNOWN,
        "transport": NEGATIVE,
        "physical_readout": UNKNOWN,
    }
    masked_result = classify(masked)
    assert masked_result == {
        "verdict": "underdetermined",
        "required_next": ["derive_source_normalized_cycle_monodromy_and_variation"],
    }

    revealed = dict(masked, physical_readout=NEGATIVE)
    assert classify(revealed)["verdict"] == "apparent_in_declared_scope"

    # Deliberate failure guard: a nontrivial physical variation keeps the
    # candidate live even when upstream gates are negative.
    counterfactual = dict(masked, physical_readout=POSITIVE)
    assert classify(counterfactual) == {
        "verdict": "live_intrinsic_candidate",
        "witnesses": ["physical_readout"],
    }

    # Coefficient presentation data alone cannot manufacture physical support.
    presentation_only = dict(revealed, coefficient=POSITIVE)
    result = classify(presentation_only)
    assert result["verdict"] == "apparent_in_declared_scope"
    assert result["coefficient_support_retained"] is True

    print("PASS: masked replay requests the missing physical-cycle test")
    print("PASS: revealed trivial cycle monodromy closes generic Q as apparent")
    print("PASS: counterfactual physical variation prevents false closure")


if __name__ == "__main__":
    main()
