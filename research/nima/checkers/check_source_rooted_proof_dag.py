import json
from pathlib import Path


def audit(nodes, target):
    visiting = set()
    verified = set()

    def visit(node_id):
        if node_id in verified:
            return None
        if node_id in visiting:
            return "cyclic_authority_support"
        node = nodes.get(node_id)
        if node is None:
            return "missing_dependency"
        if node["primitive"]:
            if node["dependencies"]:
                return "primitive_has_dependencies"
            verified.add(node_id)
            return None
        if not node["dependencies"]:
            return "missing_primitive_authority_root"
        visiting.add(node_id)
        for dependency in node["dependencies"]:
            failure = visit(dependency)
            if failure:
                return failure
        visiting.remove(node_id)
        verified.add(node_id)
        return None

    failure = visit(target)
    return {"admitted": failure is None, "residual": failure}


valid = {
    "semantic_source": {"primitive": True, "dependencies": []},
    "operational_source": {"primitive": True, "dependencies": []},
    "semantic_profile": {"primitive": False, "dependencies": ["semantic_source"]},
    "operational_profile": {"primitive": False, "dependencies": ["operational_source"]},
    "interface_cell": {
        "primitive": False,
        "dependencies": ["semantic_profile", "operational_profile"],
    },
    "operative_constructor": {
        "primitive": False,
        "dependencies": ["semantic_profile", "operational_profile", "interface_cell"],
    },
}

cycle = {
    "omega_1": {"primitive": False, "dependencies": ["omega_2"]},
    "omega_2": {"primitive": False, "dependencies": ["omega_1"]},
}

unsupported = {
    "fitted_cell": {"primitive": False, "dependencies": []},
}

valid_result = audit(valid, "operative_constructor")
cycle_result = audit(cycle, "omega_1")
unsupported_result = audit(unsupported, "fitted_cell")

assert valid_result == {"admitted": True, "residual": None}
assert cycle_result == {"admitted": False, "residual": "cyclic_authority_support"}
assert unsupported_result == {
    "admitted": False,
    "residual": "missing_primitive_authority_root",
}

result = {
    "status": "pass",
    "claim": "interface coherence closes only through a finite source-rooted proof DAG",
    "valid_shared_support_dag": valid_result,
    "cyclic_hostile": cycle_result,
    "unsupported_leaf_hostile": unsupported_result,
    "recursive_rule": "every nonprimitive constructor is audited by the same support discipline",
}

out = Path(__file__).parents[1] / "results" / "source-rooted-proof-dag.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

