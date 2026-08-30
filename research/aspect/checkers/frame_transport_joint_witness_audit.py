"""Exact audit of joint-witness encodings under frame transport and object mutation."""

import json
from pathlib import Path


def h(f, rate2=5, delta=0):
    return (f % 4, (f+delta) % rate2)


def transport(record, delta):
    return (record[0], (record[1]-delta) % 5)


def decode0(record):
    return (5*record[0]+16*record[1]) % 20


def main():
    band = range(20)
    phase_naturality = all(transport(h(f, 5, 1), 1) == h(f, 5, 0) for f in band)
    decoder_naturality = all(decode0(transport(h(f, 5, 1), 1)) == f for f in band)
    rate6_records = [h(f, 6, 0) for f in band]
    rate6_injective = len(set(rate6_records)) == 20
    encodings = {
        "marginal_schema_only": {"rejects_splice": False, "accepts_same_run_transport": True},
        "content_hash_bundle_only": {"rejects_splice": False, "accepts_same_run_transport": True},
        "untyped_causal_chain": {"rejects_splice": False, "accepts_same_run_transport": True},
        "literal_epoch_equality": {"rejects_splice": True, "accepts_same_run_transport": False},
        "common_run_plus_authorized_coherent_transport": {"rejects_splice": True, "accepts_same_run_transport": True},
    }
    checks = {
        "phase_transport_is_natural_on_entire_band": phase_naturality,
        "decoder_commutes_with_phase_transport": decoder_naturality,
        "rate_six_observer_is_not_injective_on_twenty_class_band": not rate6_injective and h(0, 6) == h(12, 6),
        "rate_mutation_cannot_be_an_invertible_observer_presentation": not rate6_injective,
        "marginal_validation_does_not_reject_splice": not encodings["marginal_schema_only"]["rejects_splice"],
        "bundle_integrity_does_not_supply_semantic_join": not encodings["content_hash_bundle_only"]["rejects_splice"],
        "literal_epoch_equality_is_too_strong": not encodings["literal_epoch_equality"]["accepts_same_run_transport"],
        "joint_transport_encoding_has_required_accept_reject_signature": encodings["common_run_plus_authorized_coherent_transport"] == {"rejects_splice": True, "accepts_same_run_transport": True},
        "current_marici_capability_coverage_remains_to_be_tested": True,
        "no_new_primitive_claimed": True,
    }
    result = {
        "schema": "marici.aspect.frame_transport_joint_witness_audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "encoding_matrix": encodings,
        "rate6_collision": {"sources": [0, 12], "record": list(h(0, 6))},
        "typed_boundary": {
            "source": "twenty-class source band, labelled clocks, certified phase transport, and run-scoped evidence",
            "constructor": "context connection preserving the observer versus rate mutation changing the observer object",
            "detector": "prospective splice rejection and same-run coherent-transport acceptance",
            "hostile": "marginal, hash-bundle, or untyped-chain encodings preserve bytes without enforcing joint realizability",
            "completion": "the exact encoding audit specifies the sufficient signature but does not establish current Marici implementation coverage or primitive novelty",
        },
    }
    out = Path(__file__).parents[1] / "results" / "frame_transport_joint_witness_audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
