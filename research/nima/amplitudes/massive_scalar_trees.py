"""Exact tree benchmarks for L_int=-g phi^3/3! - lam phi^4/4!.
Metric +---, all incoming, external p^2=m^2, propagator i/(q^2-m^2+i0).
Connected amputated amplitude is i M. Computational, not Agda-certified.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass, is_dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product as cartesian_product
import json
from pathlib import Path
import unittest

from scalar_tree_baseline import square, total, product, FOUR, SIX, recursive as quartic_recursive


@dataclass(frozen=True)
class Theory:
    mass: Q
    cubic: Q
    quartic: Q

    def __post_init__(self):
        if self.mass < 0:
            raise ValueError("Mass must be nonnegative")


def validate(ps, theory):
    if len(ps) < 3:
        raise ValueError("At least three external legs required")
    if any(len(p) != 4 for p in ps):
        raise ValueError("Four components required per momentum")
    if any(square(p) != theory.mass ** 2 for p in ps):
        raise ValueError("External momenta are off shell for the declared mass")
    if any(total(ps, tuple(range(len(ps))))):
        raise ValueError("All-incoming momentum conservation failed")


def partitions(labels, count):
    """Unordered nonempty set partitions; anchor each next block."""
    if count == 1:
        if labels:
            yield (labels,)
        return
    if len(labels) < count:
        return
    for size in range(1, len(labels) - count + 2):
        for tail in combinations(labels[1:], size - 1):
            block = (labels[0],) + tail
            rest = tuple(i for i in labels if i not in block)
            for suffix in partitions(rest, count - 1):
                yield (block,) + suffix


@dataclass(frozen=True)
class Term:
    vertex: str
    coupling: Q
    children: tuple[Current, ...]
    numerator: Q


@dataclass(frozen=True)
class Current:
    leaves: tuple[int, ...]
    momentum: tuple[Q, ...]
    denominator: Q | None
    terms: tuple[Term, ...]
    value: Q


def recursive(ps, theory, root=0):
    validate(ps, theory)
    if not 0 <= root < len(ps):
        raise ValueError("Invalid external root")

    def possible(size):
        return size == 1 or theory.cubic != 0 or (theory.quartic != 0 and size % 2 == 1)

    def assemble(labels):
        terms = []
        for arity, name, coupling in ((2, "cubic", theory.cubic), (3, "quartic", theory.quartic)):
            if coupling == 0:
                continue
            for partition in partitions(labels, arity):
                if not all(possible(len(block)) for block in partition):
                    continue
                children = tuple(current(block) for block in partition)
                terms.append(Term(name, coupling, children,
                                  coupling * product(c.value for c in children)))
        return tuple(terms)

    @lru_cache(None)
    def current(labels):
        p = total(ps, labels)
        if len(labels) == 1:
            return Current(labels, p, None, (), Q(1))
        terms = assemble(labels)
        if not terms:
            return Current(labels, p, None, (), Q(0))
        denominator = square(p) - theory.mass ** 2
        if denominator == 0:
            raise ValueError("Internal propagator pole")
        return Current(labels, p, denominator, terms,
                       sum((t.numerator for t in terms), Q(0)) / denominator)

    terms = assemble(tuple(i for i in range(len(ps)) if i != root))
    # Only the root vertex has the overall minus sign; no external propagator.
    return -sum((t.numerator for t in terms), Q(0)), terms


def direct(ps, theory):
    """Independent four/five-point and pure-quartic six-point enumeration."""
    validate(ps, theory)
    n = len(ps)
    if n not in (4, 5, 6) or (n == 6 and theory.cubic != 0):
        raise ValueError("Reference supports four/five points or pure-quartic six points")
    terms = []

    def add(vertices, channels):
        weight = theory.cubic ** vertices[0] * theory.quartic ** vertices[1]
        if weight == 0:
            return
        ds = tuple(square(total(ps, channel)) - theory.mass ** 2 for channel in channels)
        if 0 in ds:
            raise ValueError("Internal propagator pole")
        terms.append({"vertices": vertices, "channels": channels, "denominators": ds,
                      "contribution": -weight / product(ds)})

    if n == 4:
        add((0, 1), ())
        for i in range(1, 4):
            add((2, 0), ((0, i),))
    elif n == 5:
        # One cubic and one quartic vertex: the cubic side has two externals.
        for pair in combinations(range(5), 2):
            add((1, 1), (pair,))
        # Three cubic vertices form a path: one middle external and two pairs.
        for middle in range(5):
            rest = tuple(i for i in range(5) if i != middle)
            for partner in rest[1:]:
                left = (rest[0], partner)
                right = tuple(i for i in rest if i not in left)
                add((3, 0), tuple(sorted((left, right))))
    else:
        for pair in combinations(range(1, 6), 2):
            add((0, 2), ((0,) + pair,))
    return sum((t["contribution"] for t in terms), Q(0)), terms


def expanded_vertex_counts(current):
    if len(current.leaves) == 1:
        yield (0, 0)
        return
    for term in current.terms:
        yield from term_vertex_counts(term)


def term_vertex_counts(term):
    for children in cartesian_product(*(expanded_vertex_counts(c) for c in term.children)):
        yield (int(term.vertex == "cubic") + sum(x[0] for x in children),
               int(term.vertex == "quartic") + sum(x[1] for x in children))


def canonical_channel(labels, n):
    labels = tuple(sorted(labels))
    other = tuple(i for i in range(n) if i not in labels)
    return min((labels, other), key=lambda block: (len(block), block))


def current_diagrams(current, n):
    if len(current.leaves) == 1:
        yield (0, 0, ())
        return
    edge = canonical_channel(current.leaves, n)
    for term in current.terms:
        for cubic, quartic, edges in term_diagrams(term, n):
            yield cubic, quartic, tuple(sorted(edges + (edge,)))


def term_diagrams(term, n):
    for children in cartesian_product(*(current_diagrams(c, n) for c in term.children)):
        yield (int(term.vertex == "cubic") + sum(c[0] for c in children),
               int(term.vertex == "quartic") + sum(c[1] for c in children),
               tuple(sorted(edge for c in children for edge in c[2])))


def diagram_counters(histories, diagrams, n):
    return (Counter(d for term in histories for d in term_diagrams(term, n)),
            Counter((*d["vertices"], tuple(sorted(canonical_channel(c, n) for c in d["channels"])))
                    for d in diagrams))


def four_channel_residue(theory, t):
    """Algebraic residue at s=m^2 with s+t+u=4m^2.

    Clear all three denominators before setting s-m^2=0. This is a formal
    invariant-space check; no real equal-mass three-point kinematics claimed.
    """
    h = t - theory.mass ** 2
    k = 3 * theory.mass ** 2 - t - theory.mass ** 2
    if h == 0 or k == 0:
        raise ValueError("Overlapping invariant poles")
    d = Q(0)
    numerator = -theory.quartic * d * h * k - theory.cubic ** 2 * (h * k + d * k + d * h)
    return numerator / (h * k)


MODEL = Theory(Q(1), Q(2, 5), Q(3, 5))
MASSIVE_FOUR = ((Q(5, 4), Q(0), Q(0), Q(3, 4)),
                (Q(5, 4), Q(0), Q(0), Q(-3, 4)),
                (Q(-5, 4), Q(-3, 4), Q(0), Q(0)),
                (Q(-5, 4), Q(3, 4), Q(0), Q(0)))
MASSIVE_FIVE = ((Q(7, 4), Q(5, 4), Q(1, 2), Q(1, 2)),
                (Q(7, 4), Q(-5, 4), Q(-1, 2), Q(-1, 2)),
                (Q(-5, 4), Q(3, 4), Q(0), Q(0)),
                (Q(-5, 4), Q(-3, 4), Q(0), Q(0)),
                (Q(-1), Q(0), Q(0), Q(0)))


MASSIVE_SIX = ((Q(5, 2), Q(2), Q(1), Q(1, 2)),
               (Q(5, 2), Q(-2), Q(-1), Q(-1, 2)),
               (Q(-5, 4), Q(3, 4), Q(0), Q(0)),
               (Q(-5, 4), Q(-3, 4), Q(0), Q(0)),
               (Q(-5, 4), Q(0), Q(3, 4), Q(0)),
               (Q(-5, 4), Q(0), Q(-3, 4), Q(0)))


class MassiveTests(unittest.TestCase):
    def test_four_formula(self):
        from collections import Counter
        value, diagrams = direct(MASSIVE_FOUR, MODEL)
        self.assertEqual(len(diagrams), 4)
        # Independent explicit s,t,u invariant check for this sample.
        self.assertEqual(tuple(square(total(MASSIVE_FOUR, (0, i))) for i in range(1, 4)),
                         (Q(25, 4), Q(-9, 8), Q(-9, 8)))
        expected = -MODEL.quartic - MODEL.cubic ** 2 * (Q(4, 21) - Q(8, 17) - Q(8, 17))
        self.assertEqual(value, expected)
        for root in range(4):
            actual, histories = recursive(MASSIVE_FOUR, MODEL, root)
            self.assertEqual(actual, value)
            actual_diagrams, reference_diagrams = diagram_counters(histories, diagrams, 4)
            self.assertEqual(actual_diagrams, reference_diagrams)
            self.assertTrue(all(count == 1 for count in actual_diagrams.values()))
            self.assertEqual(Counter(v for term in histories for v in term_vertex_counts(term)),
                             Counter({(2, 0): 3, (0, 1): 1}))

    def test_five_mixed_and_pure_limits(self):
        from collections import Counter
        for theory, counts in ((MODEL, {(3, 0): 15, (1, 1): 10}),
                               (Theory(Q(1), MODEL.cubic, Q(0)), {(3, 0): 15}),
                               (Theory(Q(1), Q(0), MODEL.quartic), {})):
            expected, diagrams = direct(MASSIVE_FIVE, theory)
            self.assertEqual(len(diagrams), sum(counts.values()))
            for root in range(5):
                actual, histories = recursive(MASSIVE_FIVE, theory, root)
                self.assertEqual(actual, expected)
                actual_diagrams, reference_diagrams = diagram_counters(histories, diagrams, 5)
                self.assertEqual(actual_diagrams, reference_diagrams)
                self.assertTrue(all(count == 1 for count in actual_diagrams.values()))
                self.assertEqual(Counter(v for term in histories for v in term_vertex_counts(term)), Counter(counts))

    def test_massive_quartic_six(self):
        theory = Theory(Q(1), Q(0), MODEL.quartic)
        reference, diagrams = direct(MASSIVE_SIX, theory)
        self.assertEqual(len(diagrams), 10)
        for root in range(6):
            value, histories = recursive(MASSIVE_SIX, theory, root)
            self.assertEqual(value, reference)
            actual_diagrams, reference_diagrams = diagram_counters(histories, diagrams, 6)
            self.assertEqual(actual_diagrams, reference_diagrams)
            self.assertTrue(all(count == 1 for count in actual_diagrams.values()))

    def test_permutations(self):
        for ps in (MASSIVE_FOUR, MASSIVE_FIVE):
            expected = direct(ps, MODEL)[0]
            for order in permutations(range(len(ps))):
                permuted = tuple(ps[i] for i in order)
                self.assertEqual(direct(permuted, MODEL)[0], expected)
                self.assertEqual(recursive(permuted, MODEL)[0], expected)

    def test_massless_quartic_regression(self):
        theory = Theory(Q(0), Q(0), MODEL.quartic)
        for ps in (FOUR, SIX):
            self.assertEqual(recursive(ps, theory)[0], quartic_recursive(ps, MODEL.quartic)[0])

    def test_dimensions(self):
        scale = Q(7, 3)
        scaled_theory = Theory(scale * MODEL.mass, scale * MODEL.cubic, MODEL.quartic)
        for ps in (MASSIVE_FOUR, MASSIVE_FIVE):
            scaled = tuple(tuple(scale * x for x in p) for p in ps)
            self.assertEqual(recursive(scaled, scaled_theory)[0], recursive(ps, MODEL)[0] * scale ** (4 - len(ps)))

    def test_formal_factorization(self):
        for t in (Q(-2), Q(-3, 5), Q(7, 2)):
            self.assertEqual(four_channel_residue(MODEL, t), -MODEL.cubic ** 2)
        with self.assertRaisesRegex(ValueError, "Overlapping"):
            four_channel_residue(MODEL, Q(1))

    def test_invalid_inputs_and_poles(self):
        with self.assertRaisesRegex(ValueError, "off shell"):
            recursive(MASSIVE_FOUR, Theory(Q(2), MODEL.cubic, MODEL.quartic))
        with self.assertRaisesRegex(ValueError, "conservation"):
            recursive(MASSIVE_FOUR[:-1] + (MASSIVE_FOUR[-2],), MODEL)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            Theory(Q(-1), Q(1), Q(1))
        collinear = ((Q(1), Q(0), Q(0), Q(1)),) * 2 + ((Q(-1), Q(0), Q(0), Q(-1)),) * 2
        with self.assertRaisesRegex(ValueError, "pole"):
            recursive(collinear, Theory(Q(0), Q(1), Q(0)))
        # A disabled cubic interaction must not create spurious exchange poles.
        self.assertEqual(recursive(collinear, Theory(Q(0), Q(0), Q(1)))[0], -1)
        self.assertEqual(recursive(collinear, Theory(Q(0), Q(0), Q(0)))[0], 0)


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(MassiveTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    samples = []
    for ps, theory in ((MASSIVE_FOUR, MODEL), (MASSIVE_FIVE, MODEL),
                       (MASSIVE_SIX, Theory(Q(1), Q(0), MODEL.quartic))):
        value, diagrams = direct(ps, theory)
        samples.append({"model": theory, "momenta": ps, "amplitude": value, "diagrams": diagrams,
                        "recursive_routes": [{"root": root, "amplitude": recursive(ps, theory, root)[0],
                                              "histories": recursive(ps, theory, root)[1]}
                                             for root in range(len(ps))]})
    report = {"status": "exact-computational-benchmark-passed", "model": MODEL,
              "conventions": "metric +---; all incoming; delta-stripped i M; vertices -i g, -i lambda",
              "formal_agda_bridge": "not implemented", "novel_physical_prediction": False,
              "samples": samples, "tests_run": result.testsRun,
              "factorization": {"domain": "formal Mandelstam invariants, not real on-shell massive 3-point states",
                                "residue_s_equals_mass_squared": four_channel_residue(MODEL, Q(-2)),
                                "expected": "-g^2 = -M3*M3"}}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, default=encode, indent=2) + "\n", encoding="utf-8")
    print("; ".join(f"M{len(s['momenta'])} = {s['amplitude']} ({len(s['diagrams'])} diagrams)" for s in samples))


if __name__ == "__main__":
    main()
