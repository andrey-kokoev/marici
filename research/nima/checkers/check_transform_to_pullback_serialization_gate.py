"""Audit whether the geometric transform-to-pullback edge is serialized."""

import ast
import json
from pathlib import Path

TRANSFORM = Path("research/voevodsky/check_global_mixed_variance_transform.py")
PULLBACK = Path("research/voevodsky/check_physical_derived_pullback_after_transform.py")


def function(tree, name):
    return next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)


def literal_assignments(fn):
    result = {}
    for node in ast.walk(fn):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                result[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
    return result


def main():
    transform_main = function(ast.parse(TRANSFORM.read_text()), "main")
    pullback_main = function(ast.parse(PULLBACK.read_text()), "main")
    transform_literals = literal_assignments(transform_main)
    pullback_literals = literal_assignments(pullback_main)

    signature = transform_literals["transform_signature"]
    copied_signature = any(
        isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "unique_connector_signature" for t in n.targets)
        and isinstance(n.value, ast.Call)
        and isinstance(n.value.func, ast.Name)
        and n.value.func.id == "dict"
        for n in ast.walk(transform_main)
    )
    assert copied_signature

    # Dependency calls are statements; no returned construction is bound.
    component_calls = [
        n for n in transform_main.body
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
        and isinstance(n.value.func, ast.Attribute) and n.value.func.attr == "main"
    ]
    assert len(component_calls) == 6

    # The pullback calls transform.main(), then declares all chain data literally.
    assert all(k in pullback_literals for k in ("d1", "d2", "d3", "primitive"))
    transform_call_index = next(i for i, n in enumerate(pullback_main.body)
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
        and isinstance(n.value.func, ast.Attribute)
        and n.value.func.attr == "main")
    first_matrix_index = next(i for i, n in enumerate(pullback_main.body)
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "d3" for t in n.targets))
    assert transform_call_index < first_matrix_index

    out = {
        "status": "passed",
        "transform_signature_field_count": len(signature),
        "component_main_calls_unbound": len(component_calls),
        "unique_connector_signature_is_copy": copied_signature,
        "pullback_chain_data_are_literals": True,
        "serialized_transform_to_pullback_map": False,
        "first_missing_typed_datum": "constructor exporting connector chain data and the road-inclusion homotopy pullback maps",
        "claim_boundary": "This is a serialization/provenance audit. It does not refute the displayed complex or the prose-level geometric construction.",
    }
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
