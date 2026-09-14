"""Audit whether Entry-436 exports the cross-target detector cochains."""

import ast
import json
from pathlib import Path

SOURCE = Path("research/voevodsky/check_physical_derived_pullback_after_transform.py")
OUTPUT = Path("research/nima/results/physical-pullback-target-detector-input-gate.json")


def assigned_names(tree):
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name):
                    names.add(target.id)
    return names


def main():
    text = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(text)
    names = assigned_names(tree)
    required = {
        "c1_basis_labels",
        "s_detector_row",
        "W_detector_row",
        "v_detector_row",
    }
    missing = sorted(required - names)
    assert {"d3", "d2", "d1", "primitive", "road_augmentation"} <= names
    assert missing == sorted(required)

    # The claimed Q and Cartier values are currently print literals, not
    # evaluations of exported target detector rows on the primitive vector.
    assert 'print("generic_Q_leg: +1")' in text
    assert 'print("Cartier_edge_residue: +1")' in text

    result = {
        "schema": "marici.nima.physical-pullback-target-detector-input-gate.v1",
        "upstream": str(SOURCE),
        "available": sorted({"d3", "d2", "d1", "primitive", "road_augmentation"}),
        "required_cross_target_data": sorted(required),
        "missing_cross_target_data": missing,
        "first_undefined_generator": "c1_basis_labels",
        "decision": "cross-target detector cochains cannot be reconstructed from the exported pullback matrices",
        "passed": True,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
