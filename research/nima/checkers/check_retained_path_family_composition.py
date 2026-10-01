"""Associative weighted path composition with non-erased assembly provenance."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

import check_natural_tower_return as algebra
from check_whole_seed_occurrence_spectrum import rank
from retained_path_successor import RetainedSuccessorLedger


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Invalid retained composition was accepted')


def main():
    ledger = RetainedSuccessorLedger(algebra.PACKETS)
    stages = [ledger.root]
    for _ in range(3):
        stages.append(ledger.successor(stages[-1]))

    def supplied(length, offset):
        stage = stages[length - 1]
        return ledger.retain_payload(stage, tuple(F((i + offset) ** 2 - 7, 11 + offset) for i in range(len(stage.paths))))

    def table(payload):
        return dict(zip(payload.paths, payload.values))

    def leaves(payload):
        parents, _ = ledger.deconstruct_payload(payload)
        if not parents:
            return (payload.label,)
        return tuple(label for parent in parents for label in leaves(parent))

    def audit_assembly(payload):
        parents, slots = ledger.deconstruct_payload(payload)
        if not parents:
            assert payload.operation == 'supplied' and not slots
            return
        left, right = parents
        assert payload.word_length == left.word_length + right.word_length
        assert len(slots) == len(payload.paths) == len(payload.values)
        for path, value, (i, j) in zip(payload.paths, payload.values, slots):
            assert left.paths[i][-1][1] == right.paths[j][0][0]
            assert left.paths[i] + right.paths[j] == path
            assert path[:left.word_length] == left.paths[i]
            assert path[left.word_length:] == right.paths[j]
            assert left.values[i] * right.values[j] == value
        for block in ledger.composition_blocks(left, right, payload):
            assert block.rank_at_most_one and rank(block.matrix) <= 1
        for parent in parents:
            audit_assembly(parent)

    association_reports = []
    for lengths in ((1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2), (2, 2, 2)):
        x, y, z = (supplied(length, i + 1) for i, length in enumerate(lengths))
        xy = ledger.compose_payloads(x, y)
        yz = ledger.compose_payloads(y, z)
        left = ledger.compose_payloads(xy, z)
        right = ledger.compose_payloads(x, yz)
        assert left.paths == right.paths and left.values == right.values
        assert left is not right and left.label != right.label
        assert ledger.assembly_history(left) != ledger.assembly_history(right)
        assert leaves(left) == leaves(right) == (x.label, y.label, z.label)
        assert ledger.deconstruct_payload(left)[0] == (xy, z)
        assert ledger.deconstruct_payload(right)[0] == (x, yz)
        audit_assembly(left)
        audit_assembly(right)
        # Every resulting word is bound to all three retained leaves; do not
        # identify equality of flattened words with equality of assembly IDs.
        lx, ly, lz = lengths
        xt, yt, zt = table(x), table(y), table(z)
        for path, value in zip(left.paths, left.values):
            assert value == xt[path[:lx]] * yt[path[lx:lx + ly]] * zt[path[lx + ly:]]
        assert all(block.rank_at_most_one for block in ledger.composition_blocks(x, yz, left))
        assert all(block.rank_at_most_one for block in ledger.composition_blocks(xy, z, right))
        association_reports.append({'operand_lengths': lengths, 'output_length': sum(lengths),
                                    'output_words': len(left.paths), 'weighted_words_equal': True,
                                    'assembly_histories_distinct': True, 'leaf_records_recovered': True})

    # Full primitive trilinear basis certificate, including incompatible and
    # zero-coefficient cases. All slots remain, even when the payload is zero.
    basis = tuple(tuple(F(i == j) for j in range(6)) for i in range(6))
    basis_records = tuple(ledger.retain_payload(stages[0], v) for v in basis)
    pair_records = {(i, j): ledger.compose_payloads(a, b)
                    for (i, a), (j, b) in product(enumerate(basis_records), repeat=2)}
    for i, j in product(range(6), repeat=2):
        assert pair_records[i, j].paths == stages[1].paths
        assert pair_records[i, j].values == ledger.compose_primitive_payloads(stages[1], basis[i], basis[j])
    for i, j, k in product(range(6), repeat=3):
        left = ledger.compose_payloads(pair_records[i, j], basis_records[k])
        right = ledger.compose_payloads(basis_records[i], pair_records[j, k])
        assert left.paths == right.paths == stages[2].paths
        assert left.values == right.values

    # Fourfold associativity: all five binary parenthesizations retain the same
    # words and coefficients, not the same binary assembly records.
    a, b, c, d = (supplied(1, i + 1) for i in range(4))
    op = ledger.compose_payloads
    fourfold = (op(op(op(a, b), c), d), op(op(a, op(b, c)), d), op(op(a, b), op(c, d)),
                op(a, op(op(b, c), d)), op(a, op(b, op(c, d))))
    assert all(table(p) == table(fourfold[0]) for p in fourfold)
    assert len({ledger.assembly_history(p) for p in fourfold}) == 5
    assert all(leaves(p) == (a.label, b.label, c.label, d.label) for p in fourfold)
    for p in fourfold:
        audit_assembly(p)

    # General composition with the all-ones primitive right input is precisely
    # the earlier unchanged-copy successor on arbitrary parent coefficients.
    ones = ledger.retain_payload(stages[0], (F(1),) * 6)
    for parent, child in zip(stages, stages[1:]):
        payload = supplied(parent.word_length, 4)
        extended = op(payload, ones)
        assert extended.paths == child.paths
        assert extended.values == ledger.encode(parent, child, payload.values)
        assert ledger.decode(parent, child, extended.values) == payload.values
        assert ledger.summarize(child, extended.values) == tuple(
            sum(row[i] * ledger.summarize(parent, payload.values)[i] for i in range(6))
            for row in ledger.continuation)

    # A supplied two-word payload need not split into primitive factors. It can
    # still compose with a third input. Eligibility must be indexed by the cut.
    word_index = {tuple(e[2] for e in p): i for i, p in enumerate(stages[1].paths)}
    nonfactor_values = [F(0)] * 10
    nonfactor_values[word_index['AB', 'BA']] = F(1)
    nonfactor_values[word_index['DB', 'BC']] = F(1)
    nonfactor = ledger.retain_payload(stages[1], nonfactor_values)
    primitive_blocks = ledger.composition_blocks(ones, ones, nonfactor)
    assert any(block.vertex == 'B' and not block.rank_at_most_one and rank(block.matrix) == 2
               for block in primitive_blocks)
    extended_nonfactor = op(nonfactor, ones)
    assert all(block.rank_at_most_one for block in ledger.composition_blocks(nonfactor, ones, extended_nonfactor))
    right_two = ledger.retain_payload(stages[1], (F(1),) * 10)
    alternative_blocks = ledger.composition_blocks(ones, right_two, extended_nonfactor)
    assert any(not block.rank_at_most_one for block in alternative_blocks)
    assert nonfactor.operation == 'supplied' and ledger.deconstruct_payload(nonfactor) == ((), ())
    # The supplied rank-two fixture is a sum of two single-product word basis
    # vectors, but it is not silently assigned their composition provenance.
    index = {label: i for i, label in enumerate(ledger.labels)}
    term1 = pair_records[index['AB'], index['BA']]
    term2 = pair_records[index['DB'], index['BC']]
    assert nonfactor.values == tuple(x + y for x, y in zip(term1.values, term2.values))

    # Genuine path subsets, zero support and structurally absent products.
    primitive_path = {p[0][2]: p for p in ledger.root.paths}
    AB = ledger.retain_path_payload((primitive_path['AB'],), (F(3),))
    BA = ledger.retain_path_payload((primitive_path['BA'],), (F(5),))
    CA = ledger.retain_path_payload((primitive_path['CA'],), (F(7),))
    ABA = op(AB, BA)
    assert ABA.paths == (primitive_path['AB'] + primitive_path['BA'],)
    assert ABA.values == (F(15),)
    assert len(ABA.paths[0]) == 2  # return words do not cancel to identities
    assert all(block.rank_at_most_one for block in ledger.composition_blocks(AB, BA, ABA))
    empty = op(AB, CA)
    assert empty.paths == empty.values == empty.parent_slots == ()
    assert empty.word_length == 2 and ledger.deconstruct_payload(empty)[0] == (AB, CA)
    empty_left, empty_right = op(empty, ones), op(AB, op(CA, ones))
    assert empty_left.paths == empty_right.paths == ()
    assert empty_left.values == empty_right.values == ()
    assert empty_left.word_length == empty_right.word_length == 3
    assert ledger.composition_blocks(AB, CA, empty) == ()
    zero_BA = ledger.retain_path_payload((primitive_path['BA'],), (F(0),))
    zero_word = op(AB, zero_BA)
    assert zero_word.paths == ABA.paths and zero_word.values == (F(0),)
    assert zero_word.paths != empty.paths
    assert ledger.deconstruct_payload(zero_word)[0][0] is AB  # recover operand even when product vanishes

    # Parallel primitive IDs survive arbitrary-family composition as distinct
    # complete words, even though their endpoint sequence is identical.
    parallel = RetainedSuccessorLedger(algebra.PACKETS + (('AB:second', 'A', 'B'),))
    px = parallel.retain_payload(parallel.root, (F(1),) * 6 + (F(2),))
    py = parallel.retain_payload(parallel.root, (F(1),) * 7)
    pp = parallel.compose_payloads(px, py)
    assert len(pp.paths) == 14
    ptable = {tuple(edge[2] for edge in path): value for path, value in zip(pp.paths, pp.values)}
    assert ptable['AB', 'BA'] == 1 and ptable['AB:second', 'BA'] == 2

    foreign = RetainedSuccessorLedger(algebra.PACKETS)
    foreign_payload = foreign.retain_payload(foreign.root, (F(1),) * 6)
    rejects(lambda: ledger.compose_payloads(ones, foreign_payload))
    rejects(lambda: ledger.compose_payloads(replace(ones), ones))
    rejects(lambda: ledger.deconstruct_payload(replace(ABA)))
    rejects(lambda: ledger.retain_payload(ABA, (F(0),)))
    rejects(lambda: ledger.retain_path_payload((primitive_path['AB'],) * 2, (F(1), F(1))))
    rejects(lambda: ledger.retain_path_payload((primitive_path['AB'], ABA.paths[0]), (F(1), F(1))))
    rejects(lambda: ledger.retain_path_payload((primitive_path['AB'] + primitive_path['CA'],), (F(1),)))
    rejects(lambda: ledger.retain_path_payload(((('A', 'C', 'AB'),),), (F(1),)))
    rejects(lambda: ledger.retain_path_payload((primitive_path['AB'],), (0.1,)))
    rejects(lambda: ledger.retain_path_payload((primitive_path['AB'],), ()))
    rejects(lambda: ledger.retain_path_payload((), ()))
    rejects(lambda: ledger.composition_blocks(ones, ones, ABA))  # omitted domain slots, not implicit zeros
    rejects(lambda: ledger.composition_blocks(ones, ones, ones))  # wrong cut length

    report = {
        'status': 'passed', 'interface': 'RetainedSuccessorLedger weighted path families',
        'associativity': association_reports,
        'all_216_primitive_basis_triples': True,
        'all_five_fourfold_bracketings': True,
        'distinct_assembly_histories_and_exact_parent_slot_deconstruction': True,
        'all_ones_right_operand_recovers_unchanged_copy': True,
        'arbitrary_supplied_intermediate_payloads_supported': True,
        'boundary_constraints': 'rank at most one in each endpoint-interface block at the specified cut',
        'rank_two_supplied_fixture': {'eligible_at_cut_1_1': False, 'extended_eligible_at_cut_2_1': True,
                                     'extended_eligible_at_cut_1_2': False},
        'parallel_ids_and_nonempty_return_words_preserved': True,
        'empty_domain_distinguished_from_zero_coefficients': True,
        'negative_controls': ['forged or foreign records', 'weighted record used as copy stage',
                              'duplicate/mixed-length/unsewn/unknown words', 'float or wrong-size payload',
                              'empty supplied family', 'wrong or incomplete boundary domain'],
        'scope': 'homogeneous finite positive-length words with supplied rational coefficients; no physical execution, zero-length units, implicit mixtures, or ambient spectral promotion'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'retained-path-family-composition.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: arbitrary retained families compose associatively in weighted words, with distinct assembly provenance.')
    print('PASS: primitive basis triples, five fourfold bracketings, and mixed lengths through six.')
    print('PASS: cut-dependent single-product constraints; empty/zero, parallel-ID and hostile controls.')
    print('Report: research/nima/results/retained-path-family-composition.json')


if __name__ == '__main__':
    main()
