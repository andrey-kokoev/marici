#!/usr/bin/env python3
"""Finite adjunction, reverse composition, and non-adjoint transport diagnostics."""

import itertools
import json
from pathlib import Path

C2 = (0, 1)
C3 = (0, 1, 2)
leq = lambda x, y: x <= y
F = {0: 0, 1: 2}              # C2 -> C3
rF = {0: 0, 1: 0, 2: 1}       # C3 -> C2
G = {0: 0, 1: 0, 2: 1}        # C3 -> C2
rG = {0: 1, 1: 2}              # C2 -> C3

def adjunction(left, right, source, target):
    return all(leq(left[c], d) == leq(c, right[d]) for c in source for d in target)
def compose(left, right): return {x: left[right[x]] for x in right}

forward_composite = compose(G, F)
right_reverse_composite = compose(rF, rG)

def discrete_adjunction(forward, backward, C, D):
    return all((forward[c] == d) == (c == backward[d]) for c in C for d in D)

def all_functions(source, target):
    for values in itertools.product(target, repeat=len(source)):
        yield dict(zip(source, values))

C = ("a", "b")
D = ("x", "y")
constant_backward = {"x": "a", "y": "a"}
bijection_backward = {"x": "a", "y": "b"}
constant_left_candidates = tuple(candidate for candidate in all_functions(C, D) if discrete_adjunction(candidate, constant_backward, C, D))
bijection_left_candidates = tuple(candidate for candidate in all_functions(C, D) if discrete_adjunction(candidate, bijection_backward, C, D))
representable_constant_relation = frozenset((constant_backward[d], d) for d in D)
branching_relation = representable_constant_relation | frozenset({("b", "x")})
def uniquely_backward_representable(relation): return all(sum(1 for c, d2 in relation if d2 == d) == 1 for d in D)

def relation_compose(left, right): return frozenset((x, z) for x, y in right for y2, z in left if y == y2)
identity_C = frozenset((c, c) for c in C)
checks = {
    "F_is_left_adjoint_to_rF": adjunction(F, rF, C2, C3),
    "G_is_left_adjoint_to_rG": adjunction(G, rG, C3, C2),
    "forward_composite_is_identity": forward_composite == {0: 0, 1: 1},
    "right_adjoint_composes_in_reverse": right_reverse_composite == {0: 0, 1: 1},
    "composite_adjunction_holds": adjunction(forward_composite, right_reverse_composite, C2, C2),
    "constant_backward_is_representable_relation": uniquely_backward_representable(representable_constant_relation),
    "constant_backward_has_no_discrete_left_adjoint": len(constant_left_candidates) == 0,
    "bijective_backward_has_unique_left_adjoint": len(bijection_left_candidates) == 1,
    "branching_relation_is_not_backward_representable": not uniquely_backward_representable(branching_relation),
    "branching_relation_still_has_relational_unit": relation_compose(branching_relation, identity_C) == branching_relation,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.forward-backward-adjunction-mates.v1", "status": "passed", "checks": checks, "constant_left_adjoint_count": len(constant_left_candidates), "bijective_left_adjoint_count": len(bijection_left_candidates), "claim_boundary": "Finite chains and discrete categories; general mate formulas are derived in the packet."}
output = Path(__file__).parents[1] / "results" / "forward_backward_adjunction_mates.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks)}, sort_keys=True))
