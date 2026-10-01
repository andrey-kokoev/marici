"""Classify sibling details outside unchanged-copy images, without new dynamics."""
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import json

import check_natural_tower_return as algebra
from check_whole_seed_occurrence_spectrum import rank
from retained_path_successor import RetainedSuccessorLedger, identity, zero, apply


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Invalid branch comparison was accepted')


def word(path):
    return ' '.join(edge[2] for edge in path)


def sibling_basis(parent, child):
    # Each basis column contrasts a reference sibling with another child of
    # the SAME retained parent. Order fixes a sign convention, not a metric.
    columns, records = [], []
    for slot, prefix in enumerate(parent.paths):
        siblings = [i for i, index in enumerate(child.parent_slots) if index == slot]
        for negative in siblings[1:]:
            positive = siblings[0]
            column = tuple(F(i == positive) - F(i == negative) for i in range(len(child.paths)))
            columns.append(column)
            records.append({'parent': word(prefix), 'positive': word(child.paths[positive]),
                            'negative': word(child.paths[negative])})
    return algebra.transpose(tuple(columns)), records


def main():
    ledger = RetainedSuccessorLedger(algebra.PACKETS)
    stages = [ledger.root]
    for _ in range(5):
        stages.append(ledger.successor(stages[-1]))
    dimensions = [len(stage.paths) for stage in stages]
    assert dimensions == [6, 10, 16, 26, 42, 68]
    bases, reports = [], []
    for parent, child in zip(stages, stages[1:]):
        n, m = len(parent.paths), len(child.paths)
        J, D = child.step_lift, child.step_decoder
        image = algebra.mm(J, D)
        N = algebra.sub(identity(m), image)
        C, records = sibling_basis(parent, child)
        innovation_dimension = m - n
        assert rank(C) == rank(N) == innovation_dimension
        assert algebra.mm(D, C) == tuple((F(0),) * innovation_dimension for _ in range(n))
        assert algebra.mm(N, C) == C
        assert algebra.mm(N, J) == tuple((F(0),) * n for _ in range(m))
        assert algebra.mm(N, N) == N and algebra.transpose(N) == N
        assert algebra.mm(image, N) == zero(m)
        assert rank(child.summary) == 6
        summary_C = algebra.mm(child.summary, C)
        assert rank(summary_C) == 2
        # These are within-source output differences. They complement the
        # rank-four coarse response of copied parent coefficients at THIS step.
        inherited_summary = algebra.mm(child.summary, J)
        assert rank(inherited_summary) == 4
        combined_summary = tuple(a + b for a, b in zip(inherited_summary, summary_C))
        assert rank(combined_summary) == 6
        y = tuple(F(i - 3, 11) for i in range(m))
        means, detail = ledger.split_payload(child, y)
        assert means == apply(D, y) and detail == apply(N, y)
        assert ledger.reassemble_payload(child, means, detail) == y
        assert sum(v * v for v in y) == sum(v * v for v in apply(J, means)) + sum(v * v for v in detail)
        # Above orthogonality uses the existing equal-sibling/counting-metric
        # averaging decoder; it does not make the extension an isometry.
        x = tuple(F(i + 1, 7) for i in range(n))
        copied = ledger.encode(parent, child, x)
        assert ledger.split_payload(child, copied) == (x, (F(0),) * m)
        for column in algebra.transpose(C):
            assert ledger.split_payload(child, column) == ((F(0),) * n, column)
            rejects(lambda column=column: ledger.decode(parent, child, column))
        rejects(lambda child=child, copied=copied, n=n:
                ledger.reassemble_payload(child, (F(0),) * n, copied))
        bases.append(C)
        reports.append({'word_length': child.word_length, 'parent_paths': n, 'child_paths': m,
                        'sibling_detail_dimension': innovation_dimension,
                        'coarse_visible_rank': 2, 'coarse_hidden_dimension': innovation_dimension - 2,
                        'unchanged_copy_detail_is_zero': True,
                        'basis': records})

    # First-stage basis labels and exact visible/hidden combinations.
    first = stages[1]
    columns = {record['parent']: column for record, column in zip(reports[0]['basis'], algebra.transpose(bases[0]))}
    assert set(columns) == {'AB', 'CA', 'BA', 'DB'}
    visible = {key: ledger.summarize(first, v) for key, v in columns.items()}
    expected_B = tuple(F(label == 'BA') - F(label == 'BC') for label in ledger.labels)
    expected_A = tuple(F(label == 'AB') - F(label == 'AD') for label in ledger.labels)
    assert visible['AB'] == visible['DB'] == expected_B
    assert visible['CA'] == visible['BA'] == expected_A
    hidden = (tuple(a - b for a, b in zip(columns['AB'], columns['DB'])),
              tuple(a - b for a, b in zip(columns['CA'], columns['BA'])))
    assert rank(hidden) == 2
    for h in hidden:
        assert any(h) and ledger.summarize(first, h) == (F(0),) * 6
        assert ledger.split_payload(first, h) == ((F(0),) * 6, h)
    # Do not conflate these new hidden details with the original K-zero modes:
    # copied primitive contrasts have nonzero parent means and zero detail.
    old_contrast = tuple(F(label == 'CA') - F(label == 'BA') for label in ledger.labels)
    old_lift = ledger.encode(stages[0], first, old_contrast)
    assert ledger.split_payload(first, old_lift) == (old_contrast, (F(0),) * 10)
    assert ledger.summarize(first, old_lift) == (F(0),) * 6
    assert rank(tuple(algebra.transpose(bases[0])) + (old_lift,)) == 5

    # Every newly introduced detail space remains injectively present at later
    # stages. Its coarse-visible rank stays two; hidden combinations remain hidden.
    transport_reports = []
    for birth, C in enumerate(bases, start=1):
        detail_dimension = len(C[0])
        for later in range(birth, len(stages)):
            L, D = ledger.transition(stages[birth], stages[later])
            transported = algebra.mm(L, C)
            assert algebra.mm(D, transported) == C
            assert rank(transported) == detail_dimension
            coarse = algebra.mm(stages[later].summary, transported)
            assert rank(coarse) == 2
            assert algebra.mm(stages[later].origin_decoder, transported) == tuple(
                (F(0),) * detail_dimension for _ in range(6))
            if birth == 1:
                for h in hidden:
                    h_later = apply(L, h)
                    assert any(h_later)
                    assert ledger.summarize(stages[later], h_later) == (F(0),) * 6
            if later > birth:
                previous_L, _ = ledger.transition(stages[birth], stages[later - 1])
                previous_coarse = algebra.mm(stages[later - 1].summary, algebra.mm(previous_L, C))
                assert coarse == algebra.mm(ledger.continuation, previous_coarse)
            transport_reports.append({'born_at_length': birth + 1, 'observed_at_length': later + 1,
                                      'retained_rank': detail_dimension, 'coarse_rank': 2})

    # Full ancestry decomposition: origin payload plus one zero-sibling-mean
    # component per extension. All birth components are needed for an arbitrary
    # ambient preparation; unchanged-copy data has no such new components.
    ancestry_reports = []
    for end in range(1, len(stages)):
        stage = stages[end]
        y = tuple(F((i * i) % 17 - 8, 13) for i in range(len(stage.paths)))
        current, details = y, {}
        for i in range(end, 0, -1):
            current, details[i] = ledger.split_payload(stages[i], current)
        original = current
        assert original == apply(stage.origin_decoder, y)
        for i in range(1, end + 1):
            current = ledger.reassemble_payload(stages[i], current, details[i])
        assert current == y
        # Concatenate independently transported birth bases. Full rank proves
        # directness and coverage, not just successful reconstruction of a fixture.
        synthesis = stage.origin_lift
        for birth in range(1, end + 1):
            L, _ = ledger.transition(stages[birth], stage)
            lifted_basis = algebra.mm(L, bases[birth - 1])
            synthesis = tuple(a + b for a, b in zip(synthesis, lifted_basis))
        assert len(synthesis[0]) == len(stage.paths)
        assert rank(synthesis) == len(stage.paths)
        ancestry_reports.append({'word_length': stage.word_length,
                                 'dimension_partition': [6] + [len(C[0]) for C in bases[:end]],
                                 'full_synthesis_rank': rank(synthesis)})
    assert ancestry_reports[-1]['dimension_partition'] == [6, 4, 6, 10, 16, 26]

    rejects(lambda: ledger.split_payload(ledger.root, (F(0),) * 6))
    rejects(lambda: ledger.reassemble_payload(ledger.root, (), ()))
    rejects(lambda: ledger.split_payload(replace(first), (F(0),) * 10))
    rejects(lambda: ledger.split_payload(first, (F(0),) * 9))
    rejects(lambda: ledger.split_payload(first, (0.1,) * 10))
    rejects(lambda: ledger.reassemble_payload(first, (F(0),) * 5, (F(0),) * 10))

    report = {
        'status': 'passed',
        'first_stage': {
            'split': 'y=J D y+(I-J D)y', 'detail_dimension': 4,
            'coarse_visible_rank': 2, 'coarse_hidden_dimension': 2,
            'basis_summary': {'AB and DB sibling differences': 'BA-BC',
                             'CA and BA sibling differences': 'AB-AD'},
            'hidden_combinations': ['c_AB-c_DB', 'c_CA-c_BA'],
            'distinct_from_original_K_zero_sector': True},
        'stages': reports, 'transport': transport_reports,
        'ancestry_decomposition': ancestry_reports,
        'negative_controls': ['root split', 'forged stage', 'wrong dimensions', 'float payload',
                              'nonzero sibling mean in remainder', 'strict decode of a pure detail'],
        'scope': 'comparison coordinates relative to the existing equal-sibling decoder, not independently generated amplitudes or a new spectrum',
        'unchanged_copy_prepares_no_branch_detail': True,
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'retained-branch-comparisons.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: four first-stage sibling details; coarse rank two and hidden dimension two.')
    print('PASS: birth-detail spaces remain retained through length six; unchanged copying introduces none.')
    print('PASS: exact ancestry decomposition 68=6+4+6+10+16+26, with full-rank synthesis.')
    print('Report: research/nima/results/retained-branch-comparisons.json')


if __name__ == '__main__':
    main()
