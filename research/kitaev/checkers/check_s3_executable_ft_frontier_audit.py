#!/usr/bin/env python3
"""Digest-bound consolidation of the executable FT frontier."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


RESULTS = (
    "s3-five-rail-code-freeze.json",
    "s3-five-rail-transversal-gate-obstructions.json",
    "s3-encoded-clifford-teleportation.json",
    "s3-clifford-choi-verification.json",
    "s3-controlled-inversion-magic-obstruction.json",
    "s3-record-phase-magic-obstruction.json",
    "s3-transporter-and-label-lookup.json",
    "s3-five-rail-shor-recovery.json",
    "s3-26-contact-exrec-fault-pairs.json",
)

CHECKERS = (
    ("check_s3_five_rail_code_freeze.py", False),
    ("check_s3_five_rail_transversal_gate_obstructions.py", False),
    ("check_s3_encoded_clifford_teleportation.py", True),
    ("check_s3_clifford_choi_verification.py", False),
    ("check_s3_controlled_inversion_magic_obstruction.py", True),
    ("check_s3_record_phase_magic_obstruction.py", True),
    ("check_s3_transporter_and_label_lookup.py", True),
    ("check_s3_five_rail_shor_recovery.py", False),
    ("check_s3_26_contact_exrec_fault_pairs.py", False),
)


def main():
    checker_dir = Path(__file__).parent
    replay_rows = []
    for checker_name, needs_numpy in CHECKERS:
        checker = checker_dir / checker_name
        command = (["uv", "run", "--with", "numpy", "python", str(checker)]
                   if needs_numpy else [sys.executable, str(checker)])
        run = subprocess.run(command, cwd=Path(__file__).parents[3], text=True,
                             capture_output=True, timeout=120)
        assert run.returncode == 0, f"{checker_name}: {run.stderr[-1000:]}"
        replay_rows.append({"checker": checker_name, "returncode": run.returncode})
    assert len(replay_rows) == 9

    result_dir = Path(__file__).parents[1] / "results"
    packets = {}
    loaded = {}
    for name in RESULTS:
        raw = (result_dir / name).read_bytes()
        packets[name] = hashlib.sha256(raw).hexdigest()
        loaded[name] = json.loads(raw)

    code = loaded[RESULTS[0]]
    obstruction = loaded[RESULTS[1]]
    teleport = loaded[RESULTS[2]]
    choi = loaded[RESULTS[3]]
    controlled_inversion = loaded[RESULTS[4]]
    phase = loaded[RESULTS[5]]
    transporter = loaded[RESULTS[6]]
    recovery = loaded[RESULTS[7]]
    exrec = loaded[RESULTS[8]]

    assert code["six_level_bus"]["distance"] == 3
    assert code["eight_level_bus"]["distance"] == 3
    assert not obstruction["s3_multiplication_consequence"]["railwise_s3_multiplication_preserves_code"]
    assert teleport["total_logical_bell_outcomes_checked"] == 110
    assert choi["components"]["qubit"]["sum_choi"]["cat_data_contacts"] == 90
    assert controlled_inversion["teleportation"]["nonclifford_feedforward_branches"] == 32
    assert phase["nonclifford_controlled_powers"] == [1, 2]
    assert not transporter["alignment"]["is_product_clifford"]
    assert transporter["encoded_label_copy"]["all_64_source_target_cases_clean"]
    assert recovery["six_level_bus_recovery"]["cat_data_contacts"] == 105
    assert exrec["single_faults"]["malignant"] == 0
    assert exrec["fault_pairs"]["malignant"] == 220

    result = {
        "schema": "marici.kitaev.s3-executable-ft-frontier-audit.v1",
        "digest_bound_results": packets,
        "explicit_encodings": {
            "six_level": "five rails of [[5,1,3]]_2 tensor [[5,1,3]]_3",
            "eight_level": "five rails of three [[5,1,3]]_2 components",
            "four_encoded_data_blocks_rails": 20,
            "three_encoded_bus_blocks_rails": 15,
            "three_encoded_record_qubits_rails": 15,
            "core_quantum_rails_during_acquisition": 50,
            "final_classical_record_bits": 6,
        },
        "proved_executable_with_stabilizer_resources": [
            "single-rail syndrome decoding and Pauli recovery",
            "coordinate inversion",
            "logical H and F3 by verified encoded Choi teleportation",
            "logical qubit and qutrit SUM by verified encoded Choi teleportation",
            "generalized Shor recovery after each contact",
            "controlled power 4 binary record-label phase",
        ],
        "proved_unavailable_in_frozen_resource_theory": [
            "deterministic qubit-controlled qutrit inversion",
            "deterministic controlled-power-1 record-label phase",
            "deterministic controlled-power-2 record-label phase",
            "full S3 multiplication assembled only from the frozen stabilizer interfaces",
            "the explicit 36-state holonomy-conditioned transporter",
        ],
        "still_typed_as_nonstabilizer_lookup": [
            "class-conditioned selection between H and F3",
            "coherent flux/charge-to-three-bit sector lookup",
        ],
        "resource_accounting": {
            "macro_gates_per_controlled_power_before_nonstabilizer_expansion": 49,
            "macro_contacts_per_controlled_power": 26,
            "recovery_layers_per_controlled_power": 26,
            "six_level_recovery_cat_data_contacts": 105,
            "eight_level_recovery_cat_data_contacts": 144,
            "fourier_choi_verification_contacts": 36,
            "sum_choi_verification_contacts": 90,
            "full_physical_gate_count": "undefined: no admitted factory exists for the required nonstabilizer resources",
            "full_depth": "undefined for the same source reason",
            "full_magic_ancilla_count": "not zero and not derivable from the frozen interfaces",
        },
        "fault_accounting": {
            "macro_single_faults": 78,
            "malignant_macro_single_faults": 0,
            "macro_fault_pairs": 3081,
            "malignant_macro_pairs": 220,
            "minimum_distance_if_missing_magic_modules_are_one_fault_tolerant": 3,
            "distance_three_is_executable_for_full_compiler": False,
            "reason": "the full compiler is not an executable circuit until the nonstabilizer modules and their verified factories are supplied",
        },
        "final_disposition": "OBSTRUCTED_WITHIN_FROZEN_INTERFACES",
        "verdict": "The executable stabilizer subcompiler is explicit and distance-three at macro single-fault level. The full D(S3) sector compiler is impossible in the frozen stabilizer resource theory: controlled inversion and two record phases are proven non-Clifford, and three coherent lookup controls remain nonstabilizer. Therefore full gate/depth/magic costs and an executable full-compiler distance cannot be assigned without inventing a magic-state source. Adding verified one-fault-tolerant magic modules would make distance three sufficient at the audited contact level, but that is a conditional extension, not the current source theory.",
    }
    output = result_dir / "s3-executable-ft-frontier-audit.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
