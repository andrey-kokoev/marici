"""Exact massless phi^4 tree benchmarks, not an Agda-certified QFT derivation.

L_int = -lambda phi^4/4!, metric +---, all momenta incoming.
Vertex -i lambda; propagator i/(q^2+i0); delta-stripped S contribution i M.
At non-pole rational kinematics, M4=-lambda and
M6=-lambda^2 sum_{unordered 3|3 splits} 1/q^2.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations
import json
from pathlib import Path
import unittest

Momentum = tuple[Q, Q, Q, Q]


def momentum(*components: int) -> Momentum:
    if len(components) != 4:
        raise ValueError("A four-momentum requires four components")
    return tuple(Q(x) for x in components)


def square(p: Momentum) -> Q:
    return p[0] ** 2 - sum(x ** 2 for x in p[1:])


def total(ps: tuple[Momentum, ...], labels: tuple[int, ...]) -> Momentum:
    return tuple(sum((ps[i][mu] for i in labels), Q(0)) for mu in range(4))


def validate(ps: tuple[Momentum, ...]) -> None:
    if len(ps) < 4 or len(ps) % 2:
        raise ValueError("This benchmark requires an even number of legs >= 4")
    if any(square(p) != 0 for p in ps):
        raise ValueError("External momenta must be exactly massless and on shell")
    if any(total(ps, tuple(range(len(ps))))):
        raise ValueError("All-incoming momentum conservation failed")


def partitions_three(labels: tuple[int, ...]):
    """Unordered partitions into three nonempty odd blocks, once each.

    A phi^4 off-shell current has an odd number of external leaves. Fixing
    the smallest unused label in each successive block removes permutations
    of the three identical subcurrents; no extra 3! is then required.
    """
    def visit(rest, blocks):
        if blocks == 1:
            if rest and len(rest) % 2:
                yield (rest,)
            return
        if len(rest) < blocks:
            return
        anchor, *others = rest
        for size in range(1, len(rest) - blocks + 2, 2):
            for tail in combinations(others, size - 1):
                block = (anchor,) + tail
                remainder = tuple(i for i in rest if i not in block)
                for suffix in visit(remainder, blocks - 1):
                    yield (block,) + suffix
    yield from visit(labels, 3)


@dataclass(frozen=True)
class Current:
    leaves: tuple[int, ...]
    momentum: Momentum
    denominator: Q | None
    # Each term retains its three full subcurrents, not just a subtotal.
    terms: tuple[tuple[Current, ...], ...]
    value: Q


def recursive(ps: tuple[Momentum, ...], coupling: Q, root: int = 0):
    validate(ps)
    if not 0 <= root < len(ps):
        raise ValueError("Invalid external root")

    @lru_cache(None)
    def current(labels: tuple[int, ...]) -> Current:
        p = total(ps, labels)
        if len(labels) == 1:
            return Current(labels, p, None, (), Q(1))
        denominator = square(p)
        if denominator == 0:
            raise ValueError("Internal propagator pole: i0 is not a rational number")
        terms = tuple(tuple(current(block) for block in partition)
                      for partition in partitions_three(labels))
        value = coupling * sum((product(c.value for c in term)
                                for term in terms), Q(0)) / denominator
        return Current(labels, p, denominator, terms, value)

    remaining = tuple(i for i in range(len(ps)) if i != root)
    histories = tuple(tuple(current(block) for block in partition)
                      for partition in partitions_three(remaining))
    # The external root is amputated: do NOT divide by its on-shell p^2.
    amplitude = -coupling * sum((product(c.value for c in term)
                                for term in histories), Q(0))
    return amplitude, histories


def product(values) -> Q:
    result = Q(1)
    for value in values:
        result *= value
    return result


def direct_six(ps: tuple[Momentum, ...], coupling: Q):
    validate(ps)
    if len(ps) != 6:
        raise ValueError("Direct reference enumeration is specifically six-point")
    terms = []
    # Exactly one of the complementary triples contains external label 0.
    for other in combinations(range(1, 6), 2):
        left = (0,) + other
        right = tuple(i for i in range(6) if i not in left)
        denominator = square(total(ps, left))
        if denominator == 0:
            raise ValueError("Internal propagator pole")
        terms.append({"split": (left, right), "denominator": denominator,
                      "contribution": -coupling ** 2 / denominator})
    return sum((term["contribution"] for term in terms), Q(0)), terms


FOUR = (momentum(1, 0, 0, 1), momentum(1, 0, 0, -1),
        momentum(-1, -1, 0, 0), momentum(-1, 1, 0, 0))
SIX = (momentum(2, 0, 0, 2), momentum(2, 0, 0, -2),
       momentum(-1, -1, 0, 0), momentum(-1, 1, 0, 0),
       momentum(-1, 0, -1, 0), momentum(-1, 0, 1, 0))
COUPLING = Q(3, 5)


class BenchmarkTests(unittest.TestCase):
    def test_four(self):
        for root in range(4):
            amplitude, histories = recursive(FOUR, COUPLING, root)
            self.assertEqual(amplitude, -COUPLING)
            self.assertEqual(len(histories), 1)

    def test_six_all_roots(self):
        reference, diagrams = direct_six(SIX, COUPLING)
        self.assertEqual(len(diagrams), 10)
        self.assertEqual(reference, Q(6, 25))
        for root in range(6):
            amplitude, histories = recursive(SIX, COUPLING, root)
            self.assertEqual(amplitude, reference)
            self.assertEqual(len(histories), 10)
            for term in histories:
                self.assertEqual(sorted(leaf for c in term for leaf in c.leaves),
                                 [i for i in range(6) if i != root])

    def test_all_six_permutations(self):
        for order in permutations(range(6)):
            ps = tuple(SIX[i] for i in order)
            self.assertEqual(direct_six(ps, COUPLING)[0], Q(6, 25))
            self.assertEqual(recursive(ps, COUPLING)[0], Q(6, 25))

    def test_nonuniform_kinematics(self):
        # Two unequal outgoing back-to-back pairs with rational unit directions.
        # Incoming energy is a+b on each leg; outgoing energies are a,a,b,b.
        u = (Q(3, 5), Q(4, 5), Q(0))
        v = (Q(0), Q(5, 13), Q(12, 13))
        for a, b in ((Q(1), Q(2)), (Q(2, 3), Q(5, 4)), (Q(7, 3), Q(3, 2))):
            energy = a + b
            ps = ((energy, Q(0), Q(0), energy),
                  (energy, Q(0), Q(0), -energy)) + tuple(
                      (-weight,) + tuple(sign * weight * x for x in direction)
                      for weight, direction in ((a, u), (b, v))
                      for sign in (-1, 1))
            reference, _ = direct_six(ps, COUPLING)
            for root in range(6):
                self.assertEqual(recursive(ps, COUPLING, root)[0], reference)

    def test_scaling(self):
        for scale in (Q(1, 3), Q(2), Q(5, 2)):
            ps = tuple(tuple(scale * x for x in p) for p in SIX)
            self.assertEqual(recursive(ps, COUPLING)[0], Q(6, 25) / scale ** 2)
            self.assertEqual(recursive(SIX, scale * COUPLING)[0], Q(6, 25) * scale ** 2)
        self.assertEqual(recursive(SIX, Q(0))[0], 0)

    def test_invalid_inputs(self):
        with self.assertRaisesRegex(ValueError, "on shell"):
            recursive((momentum(2, 0, 0, 1),) + FOUR[1:], COUPLING)
        with self.assertRaisesRegex(ValueError, "conservation"):
            recursive((FOUR[0],) + FOUR[1:3] + (FOUR[2],), COUPLING)

    def test_pole_rejected(self):
        ps = SIX[:2] + (momentum(-1, 0, 0, -1),) * 2 + (momentum(-1, 0, 0, 1),) * 2
        for method in (direct_six, recursive):
            with self.assertRaisesRegex(ValueError, "pole"):
                method(ps, COUPLING)


def json_default(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, Current):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(BenchmarkTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    six, diagrams = direct_six(SIX, COUPLING)
    report = {
        "status": "exact-computational-benchmark-passed",
        "formal_agda_bridge": "not implemented",
        "theory": "massless real scalar, L_int=-lambda*phi^4/4!, tree level",
        "conventions": "metric +---; all incoming; vertex -i lambda; delta-stripped i M",
        "pole_domain": "no internal q^2=0; no numerical i0 replacement",
        "coupling": COUPLING,
        "four": {"momenta": FOUR, "amplitude": recursive(FOUR, COUPLING)[0]},
        "six": {"momenta": SIX, "amplitude": six, "direct_diagrams": diagrams,
                "recursive_routes": [
                    {"root": root, "amplitude": recursive(SIX, COUPLING, root)[0],
                     "histories": recursive(SIX, COUPLING, root)[1]}
                    for root in range(6)]},
        "tests_run": result.testsRun,
        "permutation_cases": 720,
        "novel_physical_prediction": False,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, default=json_default, indent=2) + "\n", encoding="utf-8")
    print(f"M4 = {-COUPLING}; M6 = {six}; 10 six-point diagrams; all checks passed")


if __name__ == "__main__":
    main()
