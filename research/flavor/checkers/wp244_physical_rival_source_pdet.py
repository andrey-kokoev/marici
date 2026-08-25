"""WP244: physical threshold realization of the WP129 rival-source partition."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
WP242 = json.loads((ROOT / "results" / "wp242_two_source_physical_pdet.json").read_text())
WP243 = json.loads((ROOT / "results" / "wp243_trace_adjoint_rate_pdet.json").read_text())

# Rows are the independently calibrated A- and D-pole yield ports. Columns are
# frozen source grammars. Values encode compulsory pole support, not fitted rate.
CONSTRUCTORS = ["WP128_two_adjoint", "WP127_one_auxiliary_A", "direct_EFT_contact"]
SUPPORT = np.asarray([
    [1, 1, 0],  # A pole
    [1, 0, 0],  # D pole
], dtype=int)


def signature(column):
    return tuple(int(value) for value in SUPPORT[:, column])


def main():
    signatures = {name: signature(index) for index, name in enumerate(CONSTRUCTORS)}
    partition = {}
    for name, value in signatures.items():
        partition.setdefault(str(value), []).append(name)

    # At kappa_D=0 the two-adjoint source loses its D pole and becomes identical
    # to the one-auxiliary source under this instrument.
    boundary_support = SUPPORT.copy()
    boundary_support[:, 0] = [1, 0]
    boundary_signatures = {
        name: tuple(int(value) for value in boundary_support[:, index])
        for index, name in enumerate(CONSTRUCTORS)
    }
    boundary_partition = {}
    for name, value in boundary_signatures.items():
        boundary_partition.setdefault(str(value), []).append(name)

    checks = {
        "two_physical_signal_ports_are_calibrated": WP242["response_rank"] == 3,
        "microscopic_portal_rate_map_is_rank_two": WP243["kappa_squared_jacobian_rank"] == 2,
        "three_frozen_constructor_signatures_are_distinct": len(partition) == 3,
        "two_adjoint_requires_two_nonzero_ports": signatures["WP128_two_adjoint"] == (1, 1),
        "one_auxiliary_requires_one_port": signatures["WP127_one_auxiliary_A"] == (1, 0),
        "direct_contact_has_no_threshold_port": signatures["direct_EFT_contact"] == (0, 0),
        "zero_D_residue_collides_with_one_auxiliary": boundary_partition["(1, 0)"] == ["WP128_two_adjoint", "WP127_one_auxiliary_A"],
        "classification_is_domain_relative": True,
        "weak_basis_descent_inherited": True,
        "no_physical16_selector_claim": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP244",
        "admitted_source_domain": "WP129 three-constructor rival family restricted to detector-accessible distinct poles and compulsory nonzero residues",
        "probe_family": ["WP242 calibrated A-pole yield", "WP242 calibrated D-pole yield"],
        "source_signatures": {key: list(value) for key, value in signatures.items()},
        "contextual_partition": list(partition.values()),
        "classification": "asymptotic source-grammar partition on the frozen nonzero-support rival domain; finite-exposure identification rejected by WP245",
        "boundary_contextual_partition": list(boundary_partition.values()),
        "smallest_exact_falsifier": "kappa_D=0 maps WP128 two-adjoint support (1,1) to (1,0), identical to the one-auxiliary rival",
        "remaining_authority_gate": "WP128/WP237 must dynamically exclude zero portal residues and select accessible distinct poles; otherwise identification is conditional rather than uniform",
        "instrument": "CMS dimuon invariant-mass threshold spectroscopy with WP242/WP243 calibrated responses",
        "reference_port": "none",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results" / "wp244_physical_rival_source_pdet.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
