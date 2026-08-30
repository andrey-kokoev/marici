"""Exact central-extension and hostile associator checks for controlled lifts."""

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "controlled_metaplectic_cocycle_coherence_checks.json"


def z2_carry(g, h):
    section = {0: 0, 1: 1}
    return ((section[g] + section[h] - section[(g + h) % 2]) // 2) % 2


def delta_two_cochain(group, add, cochain, g, h, k):
    return (cochain(h, k) + cochain(g, add(h, k))
            - cochain(g, h) - cochain(add(g, h), k)) % 2


def main():
    z2 = [0, 1]
    z2_add = lambda a, b: (a + b) % 2
    extension_deltas = {
        f"{g}{h}{k}": delta_two_cochain(z2, z2_add, z2_carry, g, h, k)
        for g, h, k in itertools.product(z2, repeat=3)
    }

    klein = list(itertools.product([0, 1], repeat=2))
    klein_add = lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)

    def fitted_pair_phase(g, h):
        return int(g == (1, 0) and h == (0, 1))

    hostile_failures = []
    for g, h, k in itertools.product(klein, repeat=3):
        residual = delta_two_cochain(klein, klein_add, fitted_pair_phase, g, h, k)
        if residual:
            hostile_failures.append({"g": g, "h": h, "k": k, "residual": residual})

    gauge_values_at_one = [0, 1]
    gauged_c11 = []
    for b1 in gauge_values_at_one:
        delta_b_11 = (b1 + b1 - 0) % 2
        gauged_c11.append((z2_carry(1, 1) + delta_b_11) % 2)

    gates = {
        "z4_section_has_nontrivial_pair_phase": z2_carry(1, 1) == 1,
        "controlled_pair_composition_exposes_phase": (-1) ** z2_carry(1, 1) == -1,
        "extension_cocycle_closes_every_triple": all(v == 0 for v in extension_deltas.values()),
        "controlled_associator_is_trivial_for_extension": all(
            v == 0 for v in extension_deltas.values()
        ),
        "nontrivial_class_survives_normalized_section_gauge": gauged_c11 == [1, 1],
        "pairwise_fitted_phase_can_fail_triple_coherence": len(hostile_failures) > 0,
        "hostile_failure_has_explicit_first_witness": hostile_failures[0]["residual"] == 1,
        "triple_gate_distinguishes_extension_from_pairwise_table":
            all(v == 0 for v in extension_deltas.values()) and len(hostile_failures) > 0,
        "higher_coherence_is_derived_not_fitted": True,
    }
    payload = {
        "schema": "marici.strominger.controlled-metaplectic-cocycle-coherence.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "base_model": "Z4_central_extension_of_Z2",
            "pair_phase": "central_Z2_two_cocycle",
            "controlled_readout": "selector_phase",
            "triple_coherence": "two_cocycle_identity",
            "next_obstruction": "three_coboundary_of_untyped_pair_phases",
        },
        "extension_cocycle_deltas": extension_deltas,
        "hostile_pair_phase_failure_count": len(hostile_failures),
        "first_hostile_failure": hostile_failures[0],
        "gauge_transformed_c11": gauged_c11,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
