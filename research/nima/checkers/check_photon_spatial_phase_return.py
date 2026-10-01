"""Full spatial placement at a phase return, using existing S4 realizations.

Global S4 words and native endpoint paths have different types. Do not invent
an edge-to-permutation map: enumerate its existing pointed witness fiber and
compare the two previously classified equivariant policies.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

import check_photon_native_spatial_step as native_check
import check_retained_pointed_comparison_groupoid as pointed
import check_equivariant_carrier_edge_lifts as edge_lifts
import check_twenty_four_triangle_shared_seed as geometry
from photon_native_spatial_step import ClockedHistory

LABELS = geometry.LABELS
UNIT = tuple(range(4))
GROUP = tuple(pointed.G)
POINTS = tuple(geometry.POINTS[k] for k in LABELS)
SPACE = {g: geometry.proper(g) for g in GROUP}
ZERO3 = (F(0),) * 3


def sign(g):
    return int(geometry.det(geometry.rotation(g)))


def word_product(word):
    answer = UNIT
    for g in word:
        answer = pointed.mul(g, answer)
    return answer


def body_placement(g, area=True):
    matrix = SPACE[g] if area else geometry.rotation(g)
    return tuple(geometry.mv(matrix, p) for p in POINTS)


def realize_path(path, witnesses):
    """Require actual supplied witnesses; labels alone cannot make this call."""
    if witnesses is None or len(witnesses) != len(path.packets) - 1:
        raise ValueError('One explicit pointed S4 witness per appended packet is required')
    arrows = []
    for packet, g in zip(path.packets[1:], witnesses):
        i, j = LABELS.index(packet.source), LABELS.index(packet.target)
        if g not in GROUP or g[i] != j:
            raise ValueError('Witness does not transport the packet source to its target')
        arrows.append(pointed.Arrow(i, j, g))
    start = LABELS.index(path.packets[0].target)
    composed = pointed.Arrow(start, start, UNIT)
    if arrows:
        composed = arrows[0]
        for arrow in arrows[1:]:
            composed = pointed.compose(arrow, composed)
    assert composed.source == start
    assert composed.target == LABELS.index(path.packets[-1].target)
    assert composed.witness == word_product(witnesses)
    placement = body_placement(composed.witness)
    anchor = geometry.mv(SPACE[composed.witness], POINTS[start])
    return {'comparison': composed, 'placement': placement, 'anchor': anchor,
            'centre': geometry.mean(placement), 'body_sign': sign(composed.witness)}


def policy_witnesses(path, spectator_swap=False):
    answer = []
    for packet in path.packets[1:]:
        i, j = LABELS.index(packet.source), LABELS.index(packet.target)
        g = edge_lifts.swap(i, j)
        if spectator_swap:
            k, l = (n for n in range(4) if n not in (i, j))
            g = pointed.mul(edge_lifts.swap(k, l), g)
        answer.append(g)
    return tuple(answer)


def rejects(fn):
    try:
        fn()
    except (ValueError, AssertionError):
        return
    raise AssertionError('Missing or incompatible spatial witness was silently supplied')


def main():
    native_check.main()  # includes fresh phase-clock and native path audit
    geometry.main()      # existing complete two-body placement/geometry checks
    assert edge_lifts.result['checks']['equivariant_lift_count'] == 2
    assert pointed.result['checks']['witnesses_per_endpoint_pair'] == 6

    # Test real labelled positions and face-centre triangles, NOT phase vectors
    # or signed amplitude contrasts. The existing realization is X_g=rho(g)X0.
    reference = (geometry.mean([geometry.POINTS[k] for k in 'ABC']),
                 geometry.POINTS['A'], geometry.POINTS['B'])
    global_cycle_word = (geometry.A,) * 3
    assert word_product(global_cycle_word) == UNIT
    global_return_checks = 0
    for initial_frame in GROUP:
        original = tuple(geometry.mv(SPACE[initial_frame], p) for p in reference)
        state = original
        for operation in global_cycle_word:
            state = tuple(geometry.mv(SPACE[operation], p) for p in state)
        assert state == original
        global_return_checks += 1
    for g in GROUP:
        placed = body_placement(g)
        assert geometry.mean(placed) == ZERO3
        assert placed == tuple(tuple(sign(g) * x for x in POINTS[g[i]]) for i in range(4))
        assert {p for p in placed} == {tuple(sign(g) * x for x in p) for p in POINTS}
        for h in GROUP:
            assert geometry.mm(SPACE[g], SPACE[h]) == SPACE[pointed.mul(g, h)]
    assert len({body_placement(g) for g in GROUP}) == 24
    assert len({frozenset(body_placement(g)) for g in GROUP}) == 2

    initial = ClockedHistory.initial()
    assert tuple(initial.paths[0].packets[0].__dataclass_fields__) == ('label', 'source', 'target')
    returned = initial.advance().advance().advance()
    assert returned.summary() == initial.summary()
    assert returned.clock_over_pi == 1 and initial.clock_over_pi == 0
    assert len(returned.paths) == 26 and returned.paths != initial.paths
    rows = []
    closed_count = 0
    total_choices = 0
    for path in returned.paths:
        start = LABELS.index(path.packets[0].target)
        end = LABELS.index(path.packets[-1].target)
        fibers = [tuple(g for g in GROUP if g[LABELS.index(p.source)] == LABELS.index(p.target))
                  for p in path.packets[1:]]
        assert len(fibers) == 3 and all(len(f) == 6 for f in fibers)
        composites = Counter()
        anchors = Counter()
        body_signs = Counter()
        for witnesses in product(*fibers):
            result = realize_path(path, witnesses)
            g = result['comparison'].witness
            composites[g] += 1
            anchors[result['anchor']] += 1
            body_signs[result['body_sign']] += 1
            assert result['centre'] == ZERO3
            assert result['anchor'] == tuple(sign(g) * x for x in POINTS[end])
        assert sum(composites.values()) == 216
        assert set(composites) == {g for g in GROUP if g[start] == end}
        assert set(composites.values()) == {36}
        assert len(anchors) == 2 and set(anchors.values()) == {108}
        assert body_signs == {1: 108, -1: 108}
        # Counts enumerate possible supplied witness choices, NOT probabilities.
        total_choices += 216
        fixed = realize_path(path, policy_witnesses(path, False))
        swapped = realize_path(path, policy_witnesses(path, True))
        assert fixed['body_sign'] == -1 and swapped['body_sign'] == 1
        if start == end:
            closed_count += 1
            assert fixed['comparison'].witness != UNIT
            assert swapped['comparison'].witness == UNIT
            assert fixed['anchor'] == tuple(-x for x in POINTS[start])
            assert swapped['anchor'] == POINTS[start]
            # Repeat the same triangle: even the nontrivial area return is an
            # involution, not a translation accumulating on each phase cycle.
            assert pointed.mul(fixed['comparison'].witness, fixed['comparison'].witness) == UNIT
        rows.append({'path': [p.label for p in path.packets], 'endpoint_loop': start == end,
                     'admissible_witness_histories': 216, 'composite_witnesses': 6,
                     'area_anchor_candidates': [[str(x) for x in p] for p in sorted(anchors)],
                     'endpoint_swap_composite': list(fixed['comparison'].witness),
                     'double_swap_composite': list(swapped['comparison'].witness)})
    assert closed_count == 10 and total_choices == 5616

    example = next(p for p in returned.paths if tuple(q.label for q in p.packets) == ('AB', 'BC', 'CA', 'AB'))
    fixed_witnesses = policy_witnesses(example, False)
    fixed = realize_path(example, fixed_witnesses)
    swapped = realize_path(example, policy_witnesses(example, True))
    assert fixed['comparison'].witness == edge_lifts.swap(0, 2)  # (AC), fixing the based label B
    assert SPACE[fixed['comparison'].witness] == ((0, 0, 1), (0, -1, 0), (1, 0, 0))
    assert fixed['anchor'] == (-1, 1, 1) and swapped['anchor'] == (1, -1, -1)
    assert geometry.sub(fixed['anchor'], POINTS[1]) == (-2, 2, 2)
    assert fixed['centre'] == swapped['centre'] == ZERO3
    assert body_placement(fixed['comparison'].witness, area=False)[1] == POINTS[1]
    # Omitting the area-sheet sign falsely reports a spatial anchor return.
    assert fixed['anchor'] != POINTS[fixed['comparison'].witness[1]]
    # Same endpoints plus different retained S4 witnesses genuinely give
    # different full placements. The source comparison carries that witness.
    assert fixed['placement'] != swapped['placement']
    left = fixed['comparison']
    a, b, c = [pointed.Arrow(LABELS.index(p.source), LABELS.index(p.target), g)
               for p, g in zip(example.packets[1:], fixed_witnesses)]
    right = pointed.compose(pointed.compose(c, b), a)
    assert left.payload() == right.payload() and left != right
    assert pointed.leafword(left) == pointed.leafword(right)
    rejects(lambda: realize_path(example, None))
    rejects(lambda: realize_path(example, (UNIT,) * 3))
    # The global triangle successor is not the composite of a pointed B->B loop.
    assert geometry.A[1] != 1
    rejects(lambda: pointed.Arrow(1, 1, geometry.A))

    # An actual translation cannot hide in this centered placement action.
    # Any finite global word still has rho(product), hence fixes the body centre.
    # The proof is representation composition; the loop checks are witnesses.
    d = (F(1), F(0), F(0))
    shifted = tuple(tuple(x + y for x, y in zip(p, d)) for p in POINTS)
    assert geometry.mean(shifted) == d != ZERO3
    assert shifted not in {body_placement(g) for g in GROUP}

    inventory = [
        'research/nima/agda/WholePackageResolution.agda',
        'research/nima/retained-pointed-comparison-groupoid.md',
        'research/nima/equivariant-edge-lifts-and-spectator-policy.md',
        'research/nima/seed-edge-action-extension-obstruction.md',
        'research/nima/twenty-four-triangle-shared-seed.md',
        'research/nima/stagewise-positive-atlas-witness.md',
    ]
    root = Path(__file__).resolve().parents[3]
    report = {
        'status': 'existing spatial phase-return tested; global orbit returns, native-path placement needs retained comparison witnesses',
        'global_S4_word': {'word': '(ABC)^3', 'initial_placement_frames_checked': global_return_checks,
                          'final_placement': 'exact initial labelled triangle', 'translation': [0, 0, 0]},
        'native_three_step_return': {'clock_advance': 'pi in the attached unit-rate rotor clock',
                                    'coefficient_summary_returns': True, 'retained_paths': 26,
                                    'endpoint_closed_paths': 10, 'endpoint_open_paths': 16},
        'pointed_witness_fiber': {'per_appended_edge': 6, 'per_three_step_path': 216,
                                 'total_examined': 5616, 'composites_per_path': 6,
                                 'labelled_body_placements_per_path': 6, 'area_anchor_positions_per_path': 2,
                                 'counts_are_probabilities': False},
        'closed_example': {'prepared_packet': 'AB', 'timed_continuation': ['BC', 'CA', 'AB'],
                           'base_label': 'B', 'initial_area_anchor': [1, -1, -1],
                           'endpoint_swap': {'holonomy': '(AC)', 'final_area_anchor': [-1, 1, 1],
                                             'effect': 'half-turn exchanging T and -T; repeated loop returns',
                                             'body_centre': [0, 0, 0]},
                           'double_swap': {'holonomy': 'identity', 'final_area_anchor': [1, -1, -1],
                                           'body_centre': [0, 0, 0]}},
        'source_gate': 'compare-rule requires a supplied equivalence and pointed-value proof; the six bare TwoPacket labels do not contain these witnesses',
        'conclusion': 'phase return alone does not determine native-path spatial return; existing centered S4 placement gives no translational drift',
        'boundaries': ['global cyclic vertex action is not pointed triangle-loop holonomy',
                       'standard contrast action and proper area action give different odd-operation anchor readings',
                       'the phase clock timestamps the native coefficient update; no joint per-edge phase/spatial transport law is inferred',
                       'no fresh Agda compilation or new spatial carrier is claimed'],
        'next_gate': 'Supply or extract the actual comparison witness on primitive continuations (including spectator action) and check its compatibility with the retained phase evolution; do not choose the policy to obtain desired propagation.',
        'source_inventory_sha256': {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in inventory},
        'path_returns': rows,
    }
    dest = root / 'research/nima/results/photon-spatial-phase-return.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: global (ABC)^3 restores every existing labelled spatial frame with zero translation.')
    print('PASS: 26 retained phase-return paths have 5616 pointed witness assignments; labels alone do not fix placement.')
    print('PASS: the existing area realization can exchange T and -T on a closed labelled path; this is rotation, not translation.')
    print('BOUNDARY: actual source comparison witnesses, not a new clock or space, are the missing native-path placement input.')
    print('Report: research/nima/results/photon-spatial-phase-return.json')


if __name__ == '__main__':
    main()
