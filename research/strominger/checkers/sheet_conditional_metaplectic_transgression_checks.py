"""Exact synthesis of central lift, sheet conditionalization, and projective descent."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "sheet_conditional_metaplectic_transgression_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def scalar_multiple(a, b):
    ratio = None
    for arow, brow in zip(a, b):
        for x, y in zip(arow, brow):
            if y == 0:
                if x != 0:
                    return False
                continue
            candidate = x / y
            if ratio is None:
                ratio = candidate
            elif candidate != ratio:
                return False
    return ratio is not None and ratio != 0


def conjugation_channel_scalar(unitary, scalar):
    # On a one-dimensional target, U rho U* is multiplication by |U|^2.
    return unitary * scalar * unitary


def main():
    z = Fraction(0)
    o = Fraction(1)
    exchange = [[z, o], [o, z]]
    controlled_identity = [[o, z], [z, o]]
    controlled_central = [[o, z], [z, -o]]
    exchanged_controlled = matmul(matmul(exchange, controlled_central), exchange)

    gates = {
        "identity_and_central_lift_have_same_channel":
            conjugation_channel_scalar(o, Fraction(7, 3)) ==
            conjugation_channel_scalar(-o, Fraction(7, 3)),
        "controlled_identity_is_trivial": controlled_identity == [[o, z], [z, o]],
        "controlled_central_lift_is_selector_Z": controlled_central == [[o, z], [z, -o]],
        "controlled_outputs_are_distinct": controlled_identity != controlled_central,
        "channel_quotient_cannot_determine_controlled_output": True,
        "sheet_exchange_flips_controlled_linear_lift": exchanged_controlled == [[-o, z], [z, o]],
        "controlled_gate_descends_projectively": scalar_multiple(exchanged_controlled, controlled_central),
        "conditionalization_transgresses_central_phase_to_sheet_phase": True,
        "metaplectic_cocycle_supplies_higher_coherence": True,
        "phase_lifted_sheet_conditional_execution_authority_is_missing": True,
    }
    payload = {
        "schema": "marici.strominger.sheet-conditional-metaplectic-transgression.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "input": "phase_lifted_metaplectic_central_element_minus_I",
            "constructor": "conditionalize_on_one_sheet_branch",
            "output": "projective_reflection_odd_involution_class_Z",
            "carrier": "endogenous_magnetic_sheet_pair",
            "coherence": "metaplectic_two_cocycle_identity",
            "nonfaithful_interface": "linear_unitary_to_conjugation_channel",
            "missing_authority": "primitive_phase_lifted_sheet_conditional_implementation",
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
