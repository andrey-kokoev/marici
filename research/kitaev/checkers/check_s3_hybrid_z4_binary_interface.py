#!/usr/bin/env python3
"""Exact digit-interface reduction of hybrid controlled-Z4 phases."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
NATIVE = K / "results" / "s3-native-ququart-wilson-compiler.json"
BINARY = K / "results" / "s3-pointer-fourier-lens-cost.json"
ENCODING = K / "results" / "mod4-phase-kernel-encoding-boundary.json"
CS_FACTORY = K / "results" / "controlled-s-from-t-factory.json"
OUT = K / "results" / "s3-hybrid-z4-binary-interface.json"


def main() -> None:
    # Basis order |b,a,d>, with the ququart digit map r=2a+d.
    targets = {}
    for coefficient in (1, 2, 3):
        hybrid = np.diag([1j ** (coefficient * b * (2*a + d))
                          for b in range(2) for a in range(2) for d in range(2)]).astype(complex)
        if coefficient == 1:
            digit = np.diag([(-1) ** (a*b) * 1j ** (b*d)
                             for b in range(2) for a in range(2) for d in range(2)]).astype(complex)
            decomposition = "CZ(b,a) * CS(b,d)"
            cs_count = 1
        elif coefficient == 2:
            digit = np.diag([(-1) ** (b*d)
                             for b in range(2) for a in range(2) for d in range(2)]).astype(complex)
            decomposition = "CZ(b,d)"
            cs_count = 0
        else:
            digit = np.diag([(-1) ** (a*b) * (-1j) ** (b*d)
                             for b in range(2) for a in range(2) for d in range(2)]).astype(complex)
            decomposition = "CZ(b,a) * CS_dagger(b,d)"
            cs_count = 1
        residual = float(np.max(np.abs(hybrid - digit)))
        assert residual == 0.0
        targets[str(coefficient)] = {"decomposition": decomposition,
                                     "matrix_max_residual": residual,
                                     "CS_or_CSdagger_count": cs_count}

    native = json.loads(NATIVE.read_text(encoding="utf-8"))
    binary = json.loads(BINARY.read_text(encoding="utf-8"))
    encoding = json.loads(ENCODING.read_text(encoding="utf-8"))
    cs_factory = json.loads(CS_FACTORY.read_text(encoding="utf-8"))
    cdfg = native["families"]["CDFG"]
    odd = cdfg["odd_nonClifford_hybrid_phase_invocations_full_cycle"]
    conjunction = cdfg["ideal_shared_conjunction_episodes"]
    assert odd == 26 and conjunction == 4
    assert cs_factory["resources"]["T_or_T_dagger_injections"] == 3
    conditional_t = 3 * odd + 14 * conjunction
    binary_total = binary["binary_lens"]["CDFG_upper_bound_including_pointer_Fouriers"]
    threshold = binary_total - conditional_t
    assert conditional_t == 134 and threshold == 83
    assert encoding["pauli_lens_no_isomorphism"]["pauli_preserving_relabelling_exists"] is False
    result = {
        "schema": "marici.kitaev.s3-hybrid-z4-binary-interface.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (NATIVE, BINARY, ENCODING, CS_FACTORY)
        },
        "digit_map": "r=2a+d",
        "exact_hybrid_decompositions": targets,
        "magic_species_result": "odd native hybrid controlled-Z4 phases become the existing CS/CS-dagger species under the digit interface; coefficient two is Clifford",
        "conditional_CDFG_accounting": {
            "odd_hybrid_invocations": odd,
            "T_from_three_T_CS_reduction": 3 * odd,
            "shared_conjunction_episodes": conjunction,
            "T_from_7T_Toffoli_compute_uncompute_pairs": 14 * conjunction,
            "subtotal_excluding_lens_switch": conditional_t,
            "binary_full_cycle_reference": binary_total,
            "available_total_lens_switch_budget_for_strict_improvement": threshold,
            "strict_improvement_condition": "total lens-switch/interface T-equivalent cost < 83",
        },
        "interface_boundary": {
            "free_digit_relabelling_allowed": False,
            "reason": "the ququart and two-qubit projective Pauli label groups are not isomorphic",
            "full_native_extract_lookup_unextract_if_interactions_use_binary_digits": "four directional native-to-binary/binary-to-native transitions per pointer, sixteen across four pointers, unless a persistent hybrid interface or direct native resource injection is supplied",
            "source_status": "no admitted code-switch interface or direct verified native hybrid-phase factory",
        },
        "verdict": "The native odd hybrid phase introduces no new abstract magic species under an explicit digit interface: it is CS/CS-dagger plus Clifford CZ. Conditional on a charged interface, CDFG has a 134T subtotal before switching and beats the 217T binary route exactly when all lens-switch costs total less than 83T-equivalent units. Without that interface the conversion is algebraic, not executable.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
