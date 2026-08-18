"""Compute Kummer inertia from the universal critical value E^2*Lambda."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("critical_locus", type=Path)
    parser.add_argument("cyclic_constraint", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    critical = json.loads(args.critical_locus.read_text(encoding="utf-8"))
    cyclic = json.loads(args.cyclic_constraint.read_text(encoding="utf-8"))

    value = critical["interior"]["critical_value"]
    if not value.startswith("E**2*"):
        raise AssertionError("critical value does not have the required E^2 factor")
    if cyclic["invariant_degeneration_divisors"] != ["E=0", "Lambda(P1,P2,P3)=0"]:
        raise AssertionError("unexpected invariant divisor packet")

    valuations = {"E=0": 2, "Lambda=0": 1}
    monodromy = {divisor: (-1 if order % 2 else 1) for divisor, order in valuations.items()}
    result = {
        "schema": "marici.nima.higher_sextic_kummer_ramification.v1",
        "sources": [str(args.critical_locus).replace("\\", "/"), str(args.cyclic_constraint).replace("\\", "/")],
        "smoothing_parameter": "s=E^2*Lambda",
        "anti_invariant_generator": "1/sqrt(s)",
        "divisorial_valuations": valuations,
        "local_kummer_monodromy": monodromy,
        "E_branch": {
            "pullback": "sqrt(E^2*Lambda)=E*sqrt(Lambda) locally after choosing the Lambda sheet",
            "character": "trivial",
            "warning": "trivial Kummer inertia does not by itself determine whether the geometric vanishing-cycle specialization is zero or rank one",
        },
        "Lambda_branch": {
            "pullback": "sqrt(E^2*Lambda)=E*sqrt(Lambda)",
            "character": "sign",
            "warning": "the transverse Kummer character is fixed, but the nonisolated critical-line specialization rank remains a geometric calculation",
        },
        "intersection": {
            "local_inertia_group": "mu2 character factors through the Lambda loop; the E loop acts trivially",
            "commuting_character_pair": [1, -1],
        },
        "cyclic_assembly": "Both divisors are C3-invariant, so the local inertia character tensors with the regular occurrence representation from Entry 808.",
        "conclusion": "The E and Lambda degeneration supports carry different coefficient inertia despite belonging to the same frozen carrier: even E ramification is Kummer-trivial, while Lambda ramification is Kummer-odd.",
        "scope": "coefficient inertia only; no local Milnor/Kato rank or specialization-map surjectivity is inferred",
        "allocator_claim": "seqclaim-7a7480d43fdca8793c13b171",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"valuations": valuations, "monodromy": monodromy, "intersection_character": [1, -1]}))


if __name__ == "__main__":
    main()
