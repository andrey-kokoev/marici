#!/usr/bin/env python3
"""Lax versus oplax comparison typing on a finite attachment chain."""

import json
from pathlib import Path

OBJECTS = (0, 1, 2)
LABELS = (0, 1)  # identity and idempotent a

def product(left, right): return 0 if left == right == 0 else 1
identity = lambda x: x
up = lambda x: min(x + 1, 2)
down = lambda x: max(x - 1, 0)

def action(endofunctor): return {0: identity, 1: endofunctor}
def compose(left, right, x): return left(right(x))
def leq(source, target): return source <= target

def compositor_components(functors, orientation):
    components = {}
    for g in LABELS:
        for f in LABELS:
            for x in OBJECTS:
                staged = compose(functors[g], functors[f], x)
                direct = functors[product(g, f)](x)
                source, target = (staged, direct) if orientation == "lax" else (direct, staged)
                components[g, f, x] = (source, target, leq(source, target))
    return components

def all_exist(components): return all(entry[2] for entry in components.values())
def failures(components): return tuple((key, value[:2]) for key, value in components.items() if not value[2])
def associative_paths_typed(functors, orientation):
    # In a thin category, the coherence equation is unique once both paths share endpoints and exist.
    comps = compositor_components(functors, orientation)
    if not all_exist(comps): return False
    for h in LABELS:
        for g in LABELS:
            for f in LABELS:
                for x in OBJECTS:
                    staged3 = functors[h](functors[g](functors[f](x)))
                    direct3 = functors[product(h, product(g, f))](x)
                    source, target = (staged3, direct3) if orientation == "lax" else (direct3, staged3)
                    if not leq(source, target): return False
    return True

up_action, down_action = action(up), action(down)
up_lax = compositor_components(up_action, "lax")
up_oplax = compositor_components(up_action, "oplax")
down_lax = compositor_components(down_action, "lax")
down_oplax = compositor_components(down_action, "oplax")
checks = {
    "upward_saturation_admits_oplax": all_exist(up_oplax),
    "upward_saturation_rejects_lax": not all_exist(up_lax),
    "upward_lax_failure_contains_2_to_1": any(pair == (2, 1) for _, pair in failures(up_lax)),
    "downward_saturation_admits_lax": all_exist(down_lax),
    "downward_saturation_rejects_oplax": not all_exist(down_oplax),
    "downward_oplax_failure_contains_1_to_0": any(pair == (1, 0) for _, pair in failures(down_oplax)),
    "upward_oplax_associativity_is_typed": associative_paths_typed(up_action, "oplax"),
    "downward_lax_associativity_is_typed": associative_paths_typed(down_action, "lax"),
    "orientation_depends_on_functor_not_chain": all_exist(up_oplax) and all_exist(down_lax),
    "no_rejected_direction_is_inverted": failures(up_lax) and failures(down_oplax),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.lax-attachment-compositor-coherence.v1", "status": "passed", "checks": checks, "up_lax_failures": failures(up_lax), "down_oplax_failures": failures(down_oplax), "claim_boundary": "Thin three-object chain; nonthin 2-cell equality remains residual."}
output = Path(__file__).parents[1] / "results" / "lax_attachment_compositor_coherence.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "up_lax_failures": len(failures(up_lax)), "down_oplax_failures": len(failures(down_oplax))}, sort_keys=True))
