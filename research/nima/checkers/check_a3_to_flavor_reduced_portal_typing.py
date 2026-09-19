from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/a3-to-flavor-reduced-portal-typing.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    a3 = load("research/nima/results/a3-flavor-weighted-integration.json")
    cochain = load("research/nima/results/n8-physical-facet-cochain.json")
    wp359 = load("research/flavor/results/wp359_canonical_fluctuation_descent.json")
    wp360 = load("research/flavor/results/wp360_canonical_source_physical16_portal.json")
    wp361 = load("research/flavor/results/wp361_dimensionless_portal_normalization.json")

    checks = {
        "a3_scalar_augmentation_exists": cochain["checks"]["facet_pairing_equals_physical_scalar"],
        "a3_physical_flavor_map_absent": a3["separated_obstructions"]["physical_flavor"].startswith("No sourced map"),
        "wp359_Q_is_Z_times_q": wp359["invariant_readouts"]["Q"] == "Z*q",
        "wp359_source_is_effective_coexistence_quotient": "coexistence" in wp359["admitted_state_domain"],
        "wp360_portal_is_nonfaithful": wp360["checks"]["physical16_hostile_pair_collides_under_portal"],
        "wp361_matching_alpha_remains_free": wp361["checks"]["deliberate_unit_normalization_is_not_unique"],
        "wp361_discards_source_direction": wp361["checks"]["portal_collapses_hostile_source_pair"],
    }

    out = {
        "schema": "marici.nima.a3-to-flavor-reduced-portal-typing.v1",
        "status": "reduced_J2_portal_target_exists_but_CR_source_arrow_untyped" if all(checks.values()) else "failed",
        "checks": checks,
        "objects": {
            "A3_augmentation": {
                "value": cochain["physical_scalar"],
                "type": "dimensionless rational evaluation of an oriented facet cochain",
            },
            "WP359_Q": {
                "formula": wp359["invariant_readouts"]["Q"],
                "type": "canonically normalized mass-dimension-two coexistence displacement",
            },
            "flavor_target": {
                "coordinate": "J^2",
                "type": "CP-even weak-basis invariant, nonfaithful on physical16",
            },
        },
        "type_mismatch": "The symbol Q in WP359 is not the rational coefficient field or the A3 scalar augmentation. No source map supplies Z, q, M2, a mass scale, or a coexistence effective action from the CR carrier.",
        "conditional_chain_if_supplied": "CR -> WP359 (Q,M2) -> rho=Q/M2 -> J^2=alpha*rho",
        "missing_arrows": [
            "a source-derived CR-to-WP359 effective-action map",
            "proof that the induced Q and M2 descend from CR equivalences",
            "microscopic or Ward authority fixing alpha",
            "a common calibrated measurement of rho and J^2",
        ],
        "conclusion": "The invariant J^2 portal is an honest reduced target, but no degree-zero CR readout currently reaches it. Substituting the existing A3 rational scalar for WP359 Q would be dimensionally and source-typologically invalid.",
        "claim_boundary": "This is a source-type obstruction, not a theorem that no future CR/flavor coupling can exist.",
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
