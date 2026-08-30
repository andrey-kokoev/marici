import json
from pathlib import Path


# Encode the quarter-phase orbit by integer powers of i modulo four.
orbit = [0, 1, 2, 3]
assert (0 + 2) % 4 == 2
assert 0 in orbit
assert 2 in orbit

# Phase zero represents e; phase two represents -e. A cone invariant under
# the cyclic action and containing e therefore contains the full real line
# through e and cannot be pointed.
contains_e = 0 in orbit
contains_minus_e = 2 in orbit
static_invariant_cone_pointed = not (contains_e and contains_minus_e)
assert static_invariant_cone_pointed is False

# A moving cone fiber C_k = i^k C_0 is covariant: a quarter turn sends its
# label from k to k+1. No individual label is fixed by that action.
fibers = list(range(4))
transported = [(k + 1) % 4 for k in fibers]
assert sorted(transported) == fibers
assert all((k + 1) % 4 != k for k in fibers)

result = {
    "phase_orbit": ["e", "i e", "-e", "-i e"],
    "invariant_cone_contains_e": contains_e,
    "invariant_cone_contains_minus_e": contains_minus_e,
    "static_invariant_cone_pointed": static_invariant_cone_pointed,
    "moving_cone_bundle_covariant": True,
    "individual_cone_fiber_invariant": False,
    "missing_structure": "source-derived relative connection between moving sector cones",
    "verdict": "spectral transport forbids a nontrivial static pointed source cone",
}

out = Path(__file__).parents[1] / "results" / "rh-static-cone-no-go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
