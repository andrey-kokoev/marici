"""Independent eight-point phi^4 enumeration and exact on-cut residue check.
Uses the conventions and recursive engine of scalar_tree_baseline.py.
No claim of formal certification, loops, or distributional pole evaluation.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product as cartesian_product
import json
from pathlib import Path
import unittest

from scalar_tree_baseline import (
    Q, COUPLING, SIX, Current, direct_six, json_default, momentum,
    recursive, square, total, validate,
)


def topologies_eight():
    # A three-vertex quartic tree is a path. Its middle vertex has two
    # external legs; each end vertex has three. Count: C(8,2)*C(6,3)/2=280.
    for middle in combinations(range(8), 2):
        rest = tuple(i for i in range(8) if i not in middle)
        for tail in combinations(rest[1:], 2):
            left = (rest[0],) + tail
            right = tuple(i for i in rest if i not in left)
            yield middle, left, right


def direct_eight(ps, coupling):
    validate(ps)
    if len(ps) != 8:
        raise ValueError("Eight external legs required")
    terms = []
    for middle, left, right in topologies_eight():
        denominators = (square(total(ps, left)), square(total(ps, right)))
        if 0 in denominators:
            raise ValueError("Internal propagator pole")
        terms.append({"middle": middle, "ends": (left, right),
                      "denominators": denominators,
                      "contribution": -coupling ** 3 / (denominators[0] * denominators[1])})
    return sum((t["contribution"] for t in terms), Q(0)), terms


def outgoing_pairs(weights):
    directions = ((Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)),
                  (Q(3, 5), Q(0), Q(4, 5)))
    energy = sum(weights, Q(0))
    return ((energy, Q(0), Q(0), energy), (energy, Q(0), Q(0), -energy)) + tuple(
        (-weight,) + tuple(sign * weight * x for x in direction)
        for weight, direction in zip(weights, directions) for sign in (-1, 1))


EIGHT = outgoing_pairs((Q(1), Q(1), Q(1)))


def canonical_channel(labels):
    labels = tuple(sorted(labels))
    complement = tuple(i for i in range(8) if i not in labels)
    # At eight points these internal splits are 3|5; choose the triple.
    return labels if len(labels) == 3 else complement


def expanded_channels(current: Current):
    """Expand retained recursion into individual internal-channel histories."""
    if len(current.leaves) == 1:
        yield ()
        return
    own = (canonical_channel(current.leaves),)
    for term in current.terms:
        for children in cartesian_product(*(expanded_channels(c) for c in term)):
            yield own + tuple(edge for child in children for edge in child)


def recursive_diagram_counter(histories):
    diagrams = Counter()
    for term in histories:
        for children in cartesian_product(*(expanded_channels(c) for c in term)):
            edges = tuple(sorted(edge for child in children for edge in child))
            diagrams[edges] += 1
    return diagrams


def factorization_point():
    # Replace the first leg q of a valid six-point process by three null
    # momenta a,b,c with a+b+c=q. No finite-epsilon pole approximation.
    q = SIX[0]
    a = (Q(-3, 2), Q(-9, 10), Q(-6, 5), Q(0))
    p = tuple(x - y for x, y in zip(q, a))
    energy = square(p) / (2 * (p[0] - p[2]))
    b = (energy, Q(0), energy, Q(0))
    c = tuple(x - y for x, y in zip(p, b))
    return (a, b, c) + SIX[1:]


def residue_eight(ps, coupling, channel=(0, 1, 2)):
    validate(ps)
    if len(ps) != 8 or len(set(channel)) != 3 or any(i not in range(8) for i in channel):
        raise ValueError("An eight-point triple channel is required")
    channel = tuple(sorted(channel))
    if square(total(ps, channel)) != 0:
        raise ValueError("Residue requires exactly on-cut channel momentum")
    zero_channels = [c for c in combinations(range(8), 3)
                     if square(total(ps, c)) == 0]
    if zero_channels != [channel]:
        raise ValueError("Overlapping pole: single-channel residue not isolated")
    contributions = []
    for middle, left, right in topologies_eight():
        if channel == left or channel == right:
            other = right if channel == left else left
            denominator = square(total(ps, other))
            if denominator == 0:
                raise ValueError("Overlapping pole: single-channel residue not isolated")
            contributions.append({"middle": middle, "other_channel": other,
                                  "denominator": denominator,
                                  "residue": -coupling ** 3 / denominator})
    return sum((t["residue"] for t in contributions), Q(0)), contributions


class EightTests(unittest.TestCase):
    def test_diagram_bijection_all_roots(self):
        amplitude, diagrams = direct_eight(EIGHT, COUPLING)
        expected = Counter(tuple(sorted(t["ends"])) for t in diagrams)
        self.assertEqual(len(expected), 280)
        self.assertTrue(all(n == 1 for n in expected.values()))
        for root in range(8):
            value, histories = recursive(EIGHT, COUPLING, root)
            self.assertEqual(value, amplitude)
            # Compare full labelled channel sets, not merely numerical sums.
            self.assertEqual(recursive_diagram_counter(histories), expected)

    def test_nonuniform_energies_and_scaling(self):
        for weights in ((Q(1), Q(2), Q(3)), (Q(2, 3), Q(5, 4), Q(7, 5))):
            ps = outgoing_pairs(weights)
            expected, _ = direct_eight(ps, COUPLING)
            for root in range(8):
                self.assertEqual(recursive(ps, COUPLING, root)[0], expected)
        amplitude = direct_eight(EIGHT, COUPLING)[0]
        scale = Q(7, 3)
        scaled = tuple(tuple(scale * x for x in p) for p in EIGHT)
        self.assertEqual(recursive(scaled, COUPLING)[0], amplitude / scale ** 4)
        self.assertEqual(recursive(EIGHT, scale * COUPLING)[0], amplitude * scale ** 3)

    def test_crossing_permutations(self):
        expected = direct_eight(EIGHT, COUPLING)[0]
        # Eight cyclic shifts and their reversals, not all 8! permutations.
        for shift in range(8):
            order = tuple(range(shift, 8)) + tuple(range(shift))
            for perm in (order, order[::-1]):
                ps = tuple(EIGHT[i] for i in perm)
                self.assertEqual(direct_eight(ps, COUPLING)[0], expected)
                self.assertEqual(recursive(ps, COUPLING)[0], expected)

    def test_factorization(self):
        ps = factorization_point()
        validate(ps)
        zeros = [c for c in combinations(range(8), 3) if square(total(ps, c)) == 0]
        self.assertEqual(zeros, [(0, 1, 2)])
        q = total(ps, (0, 1, 2))
        left = ps[:3] + (tuple(-x for x in q),)
        right = (q,) + ps[3:]
        m4 = recursive(left, COUPLING)[0]
        m6 = direct_six(right, COUPLING)[0]
        residue, terms = residue_eight(ps, COUPLING)
        self.assertEqual(len(terms), 10)
        self.assertEqual(residue, -m4 * m6)
        self.assertEqual(residue, Q(18, 125))
        # Test relabelled versions of the same cut, including changed roots.
        for shift in range(8):
            order = tuple(range(shift, 8)) + tuple(range(shift))
            permuted = tuple(ps[i] for i in order)
            channel = tuple(order.index(i) for i in (0, 1, 2))
            self.assertEqual(residue_eight(permuted, COUPLING, channel)[0], residue)

    def test_no_evaluation_at_pole(self):
        ps = factorization_point()
        for evaluator in (direct_eight, recursive):
            with self.assertRaisesRegex(ValueError, "pole"):
                evaluator(ps, COUPLING)
        with self.assertRaisesRegex(ValueError, "on-cut"):
            residue_eight(EIGHT, COUPLING)
        overlapping = EIGHT[:2] + (momentum(-1, 0, 0, -1),) * 3 + (momentum(-1, 0, 0, 1),) * 3
        with self.assertRaisesRegex(ValueError, "Overlapping"):
            residue_eight(overlapping, COUPLING, (2, 3, 4))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(EightTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    amplitude, diagrams = direct_eight(EIGHT, COUPLING)
    ps = factorization_point()
    residue, residue_terms = residue_eight(ps, COUPLING)
    report = {
        "status": "exact-computational-benchmark-passed",
        "formal_agda_bridge": "not implemented", "novel_physical_prediction": False,
        "theory": "massless phi^4, tree level; baseline conventions unchanged",
        "coupling": COUPLING, "momenta": EIGHT, "amplitude": amplitude,
        "diagrams": diagrams,
        "recursive_root_zero": recursive(EIGHT, COUPLING)[1],
        "factorization": {"momenta": ps, "channel": (0, 1, 2),
                          "isolated_pole": True, "residue": residue, "terms": residue_terms,
                          "convention": "Res M8 = - M4 M6 for delta-stripped i M"},
        "tests_run": result.testsRun,
        "scope": "eight-point topology bijection; finite rational kinematic tests; one isolated cut and relabellings",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, default=json_default, indent=2) + "\n", encoding="utf-8")
    print(f"M8 = {amplitude}; 280 diagrams; isolated residue = {residue}")


if __name__ == "__main__":
    main()
