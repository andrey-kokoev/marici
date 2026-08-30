#!/usr/bin/env python3
"""Exact finite checks for the reference-groupoid readout DPC."""

import json
from fractions import Fraction
from pathlib import Path


def orbit(seed, actions):
    return {action(seed) for action in actions}


def main():
    # C2 synchronization on a triangle.
    edges = {(0, 1): -1, (1, 2): -1, (2, 0): 1}
    cycle = edges[(0, 1)] * edges[(1, 2)] * edges[(2, 0)]
    assert cycle == 1
    frames = {(1, -1, 1), (-1, 1, -1)}
    assert len(frames) == 2
    anchored = {x for x in frames if x[0] == 1}
    assert anchored == {(1, -1, 1)}

    # A single corrupted edge is detected, but a triangle cannot locate it.
    bad = dict(edges)
    bad[(0, 1)] *= -1
    bad_cycle = bad[(0, 1)] * bad[(1, 2)] * bad[(2, 0)]
    assert bad_cycle == -1
    repairs = []
    for edge in bad:
        trial = dict(bad)
        trial[edge] *= -1
        if trial[(0, 1)] * trial[(1, 2)] * trial[(2, 0)] == 1:
            repairs.append(edge)
    assert len(repairs) == 3

    # The swap-preserved two-point torsor has no fixed representative.
    torsor = {(1, 0), (0, 1)}
    swap = lambda x: (x[1], x[0])
    assert {swap(x) for x in torsor} == torsor
    fixed = {x for x in torsor if swap(x) == x}
    assert fixed == set()

    # The action groupoid remains canonical: one orbit with two objects.
    actions = (lambda x: x, swap)
    assert orbit((1, 0), actions) == torsor

    # Readout descent and orbit faithfulness are independent.
    objects = {"a0", "a1", "b0", "b1", "c0", "c1"}
    pairs = [{"a0", "a1"}, {"b0", "b1"}, {"c0", "c1"}]
    faithful = {"a0": 0, "a1": 0, "b0": 1, "b1": 1, "c0": 2, "c1": 2}
    collapsed = {x: 0 for x in objects}
    gauge_dependent = {"a0": 0, "a1": 1, "b0": 1, "b1": 1, "c0": 2, "c1": 2}

    def descends(readout):
        return all(len({readout[x] for x in pair}) == 1 for pair in pairs)

    def orbit_values(readout):
        return [next(iter({readout[x] for x in pair})) for pair in pairs]

    assert descends(faithful)
    assert len(set(orbit_values(faithful))) == 3
    assert descends(collapsed)
    assert len(set(orbit_values(collapsed))) == 1
    assert not descends(gauge_dependent)

    # Exact binary-tag attenuation.
    omega = Fraction(1, 2)
    attenuation = 1 - 2 * omega
    assert attenuation == 0
    assert 1 - 2 * Fraction(1, 10) == Fraction(4, 5)

    # Same-loop gain cannot improve signal/reference-error ratio.
    signal, reference_error, gain = Fraction(3), Fraction(2), Fraction(7)
    before = signal / reference_error
    after = (gain * signal) / (gain * reference_error)
    assert after == before

    result = {
        "schema": "marici.reference-groupoid-readout-dpc.v1",
        "status": "pass",
        "cycle_closure": cycle,
        "global_gauge_count": len(frames),
        "anchored_frame_count": len(anchored),
        "fault_syndrome": bad_cycle,
        "single_edge_repair_candidates": len(repairs),
        "fixed_selector_count": len(fixed),
        "canonical_groupoid_orbit_size": len(orbit((1, 0), actions)),
        "faithful_readout_descends": descends(faithful),
        "collapsed_readout_descends": descends(collapsed),
        "collapsed_readout_orbit_rank": len(set(orbit_values(collapsed))),
        "gauge_dependent_readout_descends": descends(gauge_dependent),
        "random_tag_attenuation": [attenuation.numerator, attenuation.denominator],
        "common_loop_gain_ratio_preserved": after == before,
        "disposition": "finite DPC resolved; sector-specific source incidence remains open",
    }
    out = Path(__file__).parents[1] / "results" / "reference-groupoid-readout-dpc.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

