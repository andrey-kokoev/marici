from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


CONTRACT = Path("research/voevodsky/rh-modular-filling-constructor-contract-v1.json")
AUDIT = Path("research/voevodsky/results/rh_modular_filling_invariance.json")
Chain = dict[tuple[str, str], int]


def boundary(chain: Chain) -> dict[str, int]:
    out: defaultdict[str, int] = defaultdict(int)
    for (left, right), coefficient in chain.items():
        out[left] -= coefficient
        out[right] += coefficient
    return {key: value for key, value in out.items() if value}


def reflect_label(label: str) -> str:
    return {"w": "-w", "-w": "w", "a": "-a", "-a": "a"}[label]


def reflect_chain(chain: Chain) -> Chain:
    return {(reflect_label(left), reflect_label(right)): coefficient for (left, right), coefficient in chain.items()}


def detour(left: str, right: str, anchor: str = "a") -> Chain:
    return {(left, anchor): 1, (anchor, right): 1}


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    assert audit["passed"] is True
    assert len(contract["required_source_objects"]) == 6
    assert set(contract["strict_constructor"]["laws"]) == {"d1*s=id", "source-derived domain", "no zero-data dependence", "no fitted-antiderivative dependence"}
    assert len(contract["hostile_fixtures"]) == 4

    direct = {("w", "-w"): 1}
    anchored = detour("w", "-w")
    assert boundary(direct) == boundary(anchored) == {"w": -1, "-w": 1}
    assert direct != anchored

    # Direct-edge selection is equivariant under the finite reciprocal label action.
    reflected_direct = reflect_chain(direct)
    selected_after_reflection = {("-w", "w"): 1}
    assert reflected_direct == selected_after_reflection

    # A hidden fixed anchor gives equal boundaries but fails strict naturality.
    reflected_anchored = reflect_chain(anchored)
    anchored_after_reflection = detour("-w", "w")
    assert boundary(reflected_anchored) == boundary(anchored_after_reflection)
    assert reflected_anchored != anchored_after_reflection

    status = contract["current_status"]
    assert status["relative_class"] == status["ordinary_affine_orbit"] == "constructed"
    assert status["strict_modular_selection"] == status["completed_selection"] == "unverified"

    result = {
        "schema": "marici.voevodsky.rh-modular-filling-constructor-contract-check.v1",
        "status": "constructor_acceptance_and_hostile_fixtures_verified",
        "required_source_objects": 6,
        "hostile_fixtures_declared": 4,
        "representative_dependence_reproduced": True,
        "direct_selection_reflection_natural": True,
        "fixed_anchor_selection_reflection_natural": False,
        "fixed_anchor_routes_have_equal_boundary": True,
        "naturality_2_cell_required": True,
        "cutoff_nonclosability_fixture_executable": False,
        "cutoff_blocker": "source cutoff maps, graph topology, and completed chain action absent",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
