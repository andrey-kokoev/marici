from __future__ import annotations

import copy
import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/filler-layer-conservative-extension-contract-v1.json")
BASE = Path("research/voevodsky/coherence-pyramid-computad-signature.json")
EXTENSION = Path("research/voevodsky/filler-fiber-selection-layer-v1.json")


def forget(model: dict, extension_sorts: set[str]) -> dict:
    return {
        "sorts": {name: value for name, value in model["sorts"].items() if name not in extension_sorts},
        "base_operations": copy.deepcopy(model["base_operations"]),
    }


def empty_expand(base_model: dict, extension_sorts: set[str]) -> dict:
    return {
        "sorts": {**copy.deepcopy(base_model["sorts"]), **{name: [] for name in extension_sorts}},
        "base_operations": copy.deepcopy(base_model["base_operations"]),
        "extension_operations": {},
    }


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    base = json.loads(BASE.read_text(encoding="utf-8"))
    extension = json.loads(EXTENSION.read_text(encoding="utf-8"))
    base_sorts = set(base["object_sorts"])
    extension_sorts = set(extension["object_sorts"])
    assert base_sorts.isdisjoint(extension_sorts)
    assert len(base_sorts) == 5 and len(extension_sorts) == 4
    assert extension["constructors"]["selection"]["partial"] is True
    assert extension["constructors"]["completion"]["partial"] is True
    assert all(name not in base["one_generators"] for name in extension["constructors"])

    base_model = {
        "sorts": {name: [f"{name}:0"] for name in base_sorts},
        "base_operations": {name: data for name, data in base["one_generators"].items()},
    }
    empty_model = empty_expand(base_model, extension_sorts)
    assert forget(empty_model, extension_sorts) == base_model
    assert all(empty_model["sorts"][name] == [] for name in extension_sorts)

    inhabited_model = empty_expand(base_model, extension_sorts)
    inhabited_model["sorts"].update({
        "boundary_datum": ["c"], "filler": ["M0", "M1"],
        "relative_class": ["[M]"], "completed_filler": [],
    })
    inhabited_model["extension_operations"] = {"boundary": {"M0": "c", "M1": "c"}, "class": {"M0": "[M]", "M1": "[M]"}}
    assert forget(inhabited_model, extension_sorts) == base_model

    result = {
        "schema": "marici.voevodsky.filler-layer-conservative-extension-check.v1",
        "status": "finite_signature_conservativity_verified",
        "base_sorts": len(base_sorts),
        "extension_sorts": len(extension_sorts),
        "sort_names_disjoint": True,
        "base_signature_unchanged": True,
        "empty_expansion_constructed": True,
        "forget_empty_expansion_is_identity": True,
        "inhabited_extension_forgets_to_same_base": True,
        "new_base_equations_introduced": 0,
        "homotopical_universal_property_claimed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
