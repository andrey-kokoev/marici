"""Local finite routing test; read-only native source comparison, no producers.

A passing receipt means the positive theorem AND source obstruction were checked,
not that the physical/full-complex conjecture was accepted.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations
from pathlib import Path
import json
import sys

from assemble_metric_coefficient_protocol import ROOT, ZERO, read_operator, product, integer_trace, sharp, encode
from check_port_incidence_conjectures import factor, pivot_columns

HERE = Path(__file__).resolve()
CONTRACT = ROOT / 'research/strominger/contracts/twelve-three-routing-v1.json'
OUT = ROOT / 'research/strominger/results/twelve-three-routing-v1.json'
PROTON = ROOT / 'research/strominger/results/common-three-carrier-protocol/proton.json'
STORE = ROOT / 'research/voevodsky/results/proton_merkle_store.json'
checks = {}


def ck(name, condition):
    assert condition, name
    checks[name] = True


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def parity(p):
    return sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2


def induced(cut, labels):
    """Return output relabeling iff a bijective input cut preserves the fibers."""
    rows = [{labels[cut[i]] for i, v in enumerate(labels) if v == j} for j in range(3)]
    if any(len(row) != 1 for row in rows):
        return None
    result = tuple(next(iter(row)) for row in rows)
    return result if len(set(result)) == 3 else None


def main():
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    assert contract['checker'].endswith(HERE.name)
    group = sorted(p for p in permutations(range(4)) if parity(p) == 0)
    unit = (0, 1, 2, 3)
    klein = [p for p in group if p == unit or all(p[i] != i for i in range(4))]
    ck('A4_is_the_twelve_element_rotation_permutation_group', len(group) == 12 and all(compose(p, q) in group for p in group for q in group))
    ck('Klein_four_is_a_normal_subgroup', len(klein) == 4 and all(compose(p, q) in klein for p in klein for q in klein) and all({compose(g, h) for h in klein} == {compose(h, g) for h in klein} for g in group))
    cosets = sorted({tuple(sorted(compose(g, h) for h in klein)) for g in group})
    labels = tuple(next(j for j, block in enumerate(cosets) if p in block) for p in group)
    ck('routing_is_total_single_valued_and_surjective', len(labels) == 12 and set(labels) == {0, 1, 2})
    ck('three_fibers_each_have_four_inputs', Counter(labels) == {0: 4, 1: 4, 2: 4})
    lookup = {p: i for i, p in enumerate(group)}
    left_cuts = [tuple(lookup[compose(g, p)] for p in group) for g in group]
    cut_count = 0
    for g in group:
        for h in group:
            cut = tuple(lookup[compose(compose(g, p), h)] for p in group)
            result = induced(cut, labels)
            assert result is not None
            assert all(labels[cut[i]] == result[labels[i]] for i in range(12))
            cut_count += 1
    ck('all_144_left_right_group_cut_squares_commute', cut_count == 144)
    # Exhaust balanced UNLABELED partitions, not merely one handpicked example.
    partition_count = 0
    invariant_partitions = []
    all_ids = set(range(12))
    for tail in combinations(range(1, 12), 3):
        first = {0, *tail}
        remaining = sorted(all_ids - first)
        for raw_second in combinations(remaining, 4):
            second = set(raw_second)
            third = all_ids - first - second
            if min(second) > min(third):
                continue
            blocks = (first, second, third)
            lab = tuple(next(j for j, block in enumerate(blocks) if i in block) for i in range(12))
            partition_count += 1
            if all(induced(cut, lab) is not None for cut in left_cuts):
                invariant_partitions.append(lab)
    ck('all_5775_balanced_partitions_are_exhausted', partition_count == 5775)
    ck('A4_regular_action_selects_one_unlabeled_balanced_partition', len(invariant_partitions) == 1 and all((labels[i] == labels[j]) == (invariant_partitions[0][i] == invariant_partitions[0][j]) for i in range(12) for j in range(12)))
    fibers = [[i for i, v in enumerate(labels) if v == j] for j in range(3)]
    within = list(range(12));within[fibers[0][0]], within[fibers[0][1]] = within[fibers[0][1]], within[fibers[0][0]]
    crossing = list(range(12));crossing[fibers[0][0]], crossing[fibers[1][0]] = crossing[fibers[1][0]], crossing[fibers[0][0]]
    whole = list(range(12))
    for a, b in zip(fibers[0], fibers[1]):
        whole[a], whole[b] = whole[b], whole[a]
    ck('within_fiber_and_whole_fiber_relabelings_are_admissible', induced(within, labels) is not None and induced(whole, labels) is not None)
    ck('hostile_single_cross_fiber_swap_breaks_cut_compatibility', induced(crossing, labels) is None)
    retained = [(labels[i], fibers[labels[i]].index(i)) for i in range(12)]
    ck('output_plus_retained_fiber_label_recovers_every_input', len(set(retained)) == 12 and all(fibers[o][k] == i for i, (o, k) in enumerate(retained)))
    ck('output_label_alone_does_not_recover_the_input', len(set(labels)) == 3 and labels[fibers[0][0]] == labels[fibers[0][1]])

    store = json.loads(STORE.read_text(encoding='utf-8'))
    geometry = store['objects'][store['objects'][store['root']]['geometry']]['payload']
    placements = sorted(geometry['triangles_and_transports'], key=lambda r: r['outer_arrow'])
    vertices = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    native_group = {}
    for row in placements:
        rotation = [list(map(F, r)) for r in row['rotation']]
        images = [tuple(sum(rotation[i][j] * v[j] for j in range(3)) for i in range(3)) for v in vertices]
        p = tuple(vertices.index(v) for v in images)
        assert tuple('ABCD'[i] for i in p[:2]) == tuple(row['outer_arrow'])
        native_group[row['outer_arrow']] = p
    ck('actual_twelve_proton_transport_rotations_are_exactly_A4', len(native_group) == 12 and set(native_group.values()) == set(group))
    port_routing = {arrow: labels[lookup[p]] for arrow, p in native_group.items()}
    geometric_fibers = [[arrow for arrow, out in port_routing.items() if out == j] for j in range(3)]
    ck('geometric_fibers_are_opposite_edge_pairs_with_both_directions', sorted(map(sorted, geometric_fibers)) == sorted([['AB', 'BA', 'CD', 'DC'], ['AC', 'BD', 'CA', 'DB'], ['AD', 'BC', 'CB', 'DA']]))

    source = json.loads(PROTON.read_text(encoding='utf-8'))
    n = len(source['source']['coordinates']);metric = tuple(map(F, source['source']['metric']))
    ops = {k: read_operator(source['operators'][k], n) for k in 'LGN'}
    for k, field in [('L', 'local'), ('G', 'alignment')]:
        assert ops[k] == read_operator(source['source'][field], n)
    ck('native_L_G_N_relations_and_original_metric_hold', product(ops['L'], ops['G']) == product(ops['G'], ops['L']) == ops['N'] and all(product(p, p) == p and sharp(p, metric) == p for p in ops.values()))
    local = factor(ops['L'], n, metric)
    aligned = factor(ops['G'], n, metric)
    ck('native_full_image_channels_have_dimensions_12_and_3', local['rank'] == 12 and aligned['rank'] == 3)
    forward = product(aligned['D'], product(ops['G'], local['K']))
    ck('native_forward_square_preserves_all_projected_raw_readers', product(aligned['K'], forward) == product(ops['G'], local['K']))
    outputs = [[i for i in range(3) if forward.get((i, j), ZERO) != ZERO] for j in range(12)]
    deterministic = all(len(row) == 1 for row in outputs)
    surjective = set(i for row in outputs for i in row) == {0, 1, 2}
    rank = len(pivot_columns(forward, 3, 12))
    ck('native_rank_one_obstruction_is_confirmed_exactly', rank == integer_trace(ops['N']) == 1)
    ck('native_transfer_is_not_a_weighted_single_valued_surjection', not (deterministic and surjective))
    # A weighted deterministic surjection has three nonempty disjoint row supports.
    # Those rows are independent, so rank=3. Rank1 excludes it in EVERY invertible
    # 12/3 channel basis, not just the selected factorization chart.
    ck('native_rank_excludes_a_three_output_routing_in_any_channel_basis', rank < 3)
    witness_column = next(j for j, row in enumerate(outputs) if len(row) != 1)
    native = {
        'input_channel_labels': [source['source']['coordinates'][j].split(':')[0] for j in local['columns']],
        'output_basis_raw_pivots': [source['source']['coordinates'][j] for j in aligned['columns']],
        'output_support_for_each_input': outputs,
        'matrix': encode(forward), 'rank': rank, 'single_valued': deterministic,
        'every_output_reached': surjective,
        'witness': {'input_channel': witness_column, 'outputs': outputs[witness_column],
                    'prepared_raw_input': encode({(i, 0): v for (i, j), v in local['K'].items() if j == witness_column}),
                    'decoded_output': encode({(i, 0): v for (i, j), v in forward.items() if j == witness_column})},
        'basis_independent_obstruction': 'A nonzero weighted single-valued surjection 12->3 has rank3; actual native forward rank is1.',
    }
    pins = {str(p.relative_to(ROOT)).replace('\\', '/'): sha256(p.read_bytes()).hexdigest() for p in [CONTRACT, HERE, PROTON, STORE]}
    # Retain exact helper-code evidence without editing or invoking any producer.
    for module in list(sys.modules.values()):
        file = getattr(module, '__file__', None)
        if not file:
            continue
        p = Path(file).resolve()
        try:
            relative = p.relative_to(ROOT)
        except ValueError:
            continue
        if p.is_file() and p.suffix == '.py':
            pins[relative.as_posix()] = sha256(p.read_bytes()).hexdigest()
    report = {
        'schema': 'marici.twelve-three-routing-test.v1', 'status': 'pass', 'checks': checks,
        'verdict': {'abstract_tetrahedral_routing': 'constructed',
                    'geometric_native_rotation_labels': 'realized',
                    'identification_with_native_proton_forward_map': 'rejected_at_full_channel_scope',
                    'full_PNE_complex_and_electron_occupancy': 'not_constructed_or_tested'},
        'abstract': {'inputs': 12, 'outputs': 3, 'fiber_sizes': [4, 4, 4],
                     'geometric_port_fibers': geometric_fibers,
                     'balanced_partitions_examined': partition_count,
                     'A4_equivariant_unlabeled_partitions': len(invariant_partitions),
                     'left_right_cut_tests': cut_count,
                     'cross_fiber_swap': crossing, 'retained_decoding': retained},
        'native': native, 'source_sha256': pins,
        'scope': contract['scope'],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'checks': len(checks), 'abstract_fibers': geometric_fibers,
                      'native_forward_rank': rank, 'native_output_counts': list(map(len, outputs)),
                      'native_single_valued': deterministic, 'receipt': OUT.relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
