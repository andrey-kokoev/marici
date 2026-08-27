from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "deeper_relational_calculus_layers.json"


def nonlinear_fiber_hostile():
    points = (-2, -1, 0, 1, 2)
    q = lambda x: x * x
    r = lambda x: x * x * x
    # Differential test: dq=2x has zero kernel except at x=0; at zero dr=0.
    tangent_test_passes = all(x != 0 or 3 * x * x == 0 for x in points)
    collisions = []
    for x in points:
        for y in points:
            if x < y and q(x) == q(y) and r(x) != r(y):
                collisions.append((x, y, q(x), r(x), r(y)))
    return tangent_test_passes, collisions


def marginal(distribution, slots):
    out = {}
    for bits, probability in distribution.items():
        key = tuple(bits[i] for i in slots)
        out[key] = out.get(key, F(0)) + probability
    return out


def ternary_hostile():
    even = {bits: F(1, 4) for bits in product((0, 1), repeat=3) if sum(bits) % 2 == 0}
    odd = {bits: F(1, 4) for bits in product((0, 1), repeat=3) if sum(bits) % 2 == 1}
    pairwise_equal = all(marginal(even, slots) == marginal(odd, slots)
                         for slots in ((0, 1), (0, 2), (1, 2)))
    parity_expectation = lambda d: sum(p * (1 if sum(bits) % 2 == 0 else -1)
                                       for bits, p in d.items())
    return even, odd, pairwise_equal, parity_expectation(even), parity_expectation(odd)


def selection_hostile():
    source = ("a", "b")
    quotient = {"a": "star", "b": "star"}
    relation = {"a": 1, "b": 1}
    descends = relation["a"] == relation["b"]
    sections = (("star", "a"), ("star", "b"))
    swap = {"a": "b", "b": "a"}
    invariant_sections = [s for s in sections if swap[s[1]] == s[1]]
    return source, quotient, descends, sections, invariant_sections


def main():
    tangent_ok, collisions = nonlinear_fiber_hostile()
    assert tangent_ok and collisions
    assert (-1, 1, 1, -1, 1) in collisions

    even, odd, pairwise_equal, even_parity, odd_parity = ternary_hostile()
    assert pairwise_equal
    assert even_parity == 1 and odd_parity == -1

    source, quotient, descends, sections, invariant_sections = selection_hostile()
    assert descends and len(sections) == 2 and not invariant_sections

    out = {
        "schema": "marici.aspect.deeper-relational-calculus-layers.v1",
        "status": "pass",
        "nonlinear_fiber_layer": {
            "local_differential_kernel_test_passes": tangent_ok,
            "global_fiber_collision_count": len(collisions),
            "witness": {"x": -1, "y": 1, "q_x=q_y": 1, "r_x": -1, "r_y": 1},
            "repair": "replace kernel annihilation by constancy on the full completion equivalence relation; use kernels only in linear settings",
        },
        "higher_arity_layer": {
            "all_pairwise_marginals_equal": pairwise_equal,
            "even_triple_parity": str(even_parity),
            "odd_triple_parity": str(odd_parity),
            "repair": "retain the common three-instance carrier until a ternary mate, or use a binary tree whose intermediates preserve the full higher coherence",
        },
        "selection_layer": {
            "relation_descends": descends,
            "section_count": len(sections),
            "swap_invariant_section_count": len(invariant_sections),
            "repair": "descent authorizes a quotient readout; selection requires an independently authorized symmetry-breaking or realization section",
        },
        "revised_compiler": [
            "test full fiber congruence before using a local quotient",
            "test target relations at their native arity",
            "separate descent, faithful reconstruction, and realization selection",
        ],
        "time_used": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
