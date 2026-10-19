"""Shared typed grammar, conditional signed paths, and native-line obstruction.

Exact inherited number field; no producer or physical selection is executed.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product as cartesian
import json
from pathlib import Path

from assemble_metric_coefficient_protocol import (ROOT, A, ZERO, ONE, product,
    sharp, integer_trace, read_operator, encode)
from check_rank_one_return_packets import LineInterface
from check_baryon_doublet_extension import two, I2, scale, add, tensor_identity
from check_baryon_coefficient_spin_binding import parse_record, tensor, sparse
from native_path_sector_calculus import (NORMAL_FORMS, CENTRAL, multiply,
    word_normal_form, sector_certificate, verify_sector, swap_trace, verify_trace)

CONTRACT = ROOT/'research/strominger/contracts/shared-packet-path-language.v1.json'
RESULT = ROOT/'research/strominger/results/shared-packet-path-language-v1.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def coefficient(z):
    c = [F(0)]*16
    for value, mask in zip([v for pair in z for v in pair], (0, 2, 8, 10)):
        c[mask] = F(value)
    return A(tuple(c))


def adjoint(matrix):
    return {(j, i): x.flip(8) for (i, j), x in matrix.items()}


def matrix_key(matrix):
    return tuple((i, j, v.c) for (i, j), v in sorted(matrix.items()))


def reject(action, residual):
    try:
        action()
    except ValueError as error:
        assert residual in str(error), (residual, str(error))
    else:
        raise AssertionError('accepted hostile: '+residual)


@dataclass(frozen=True)
class BoundWord:
    carrier: str
    source_sha256: str
    enlarged: bool
    tokens: tuple = ()


@dataclass
class Language:
    carrier: str
    source_sha256: str
    enlarged: bool
    spin_allowed: bool
    logical_identity: dict
    spin_dictionary: dict

    def empty(self):
        return BoundWord(self.carrier, self.source_sha256, self.enlarged)

    def validate(self, word):
        if (word.carrier, word.source_sha256) != (self.carrier, self.source_sha256):
            raise ValueError('source binding')
        if word.enlarged != self.enlarged:
            raise ValueError('carrier enlargement flag')
        for kind, token in word.tokens:
            if kind == 'stage' and token in 'LGN' and len(token) == 1:
                continue
            if kind == 'spin' and self.spin_allowed and token in self.spin_dictionary:
                continue
            raise ValueError('operation unavailable')

    def append(self, word, kind, token):
        self.validate(word)
        out = replace(word, tokens=word.tokens+((kind, token),))
        self.validate(out)
        return out

    def evaluate(self, word):
        self.validate(word)
        out = self.logical_identity
        # Match the declared left-to-right matrix product convention.
        for kind, token in word.tokens:
            out = product(out, self.logical_identity if kind == 'stage' else self.spin_dictionary[token])
        return out


def main():
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    pins, receipts = {}, {}
    for rel in contract['prerequisite_receipts']:
        path = ROOT/rel
        prior = json.loads(path.read_text(encoding='utf-8'))
        assert prior['status'] == 'pass' and all(prior['checks'].values())
        receipts[rel] = prior
        for source, frozen in prior['source_sha256'].items():
            assert digest(ROOT/source) == frozen, ('stale prerequisite', source)
            if source in pins:
                assert pins[source] == frozen
            pins[source] = frozen
        pins[rel] = digest(path)
    for path in (CONTRACT, Path(__file__).resolve()):
        pins[path.relative_to(ROOT).as_posix()] = digest(path)

    native = receipts['research/strominger/results/native-path-sector-calculus-v1.json']
    dictionary = {}
    for row in native['normal_form_dictionary']:
        U = tuple(tuple(tuple(F(x) for x in entry) for entry in r) for r in row['matrix'])
        dictionary[tuple(row['normal_form'])] = two(U)
    assert len(dictionary) == 24
    keys = {matrix_key(U) for U in dictionary.values()}
    for x, y in cartesian(NORMAL_FORMS, repeat=2):
        assert product(dictionary[x], dictionary[y]) == dictionary[multiply(x, y)]
    z = dictionary[CENTRAL]
    assert z == scale(-ONE, I2)

    electron_path = ROOT/contract['source_identity']['electron']
    store = json.loads(electron_path.read_text(encoding='utf-8'))
    Ke = {(2*f+i, j): coefficient(p[i][j])
          for f, p in enumerate(store['face_projectors']) for i in range(2) for j in range(2)
          if coefficient(p[i][j]) != ZERO}
    De = scale(A(F(1, 2)), adjoint(Ke))
    assert product(De, Ke) == I2
    Ne = product(Ke, De)
    native_rows, enlarged_rows, languages, native_lines = {}, {}, {}, {}
    electron_language = Language('electron', digest(electron_path), False, True, I2, dictionary)
    languages['electron'] = electron_language
    # Electron source attachment for all SAME logical tokens.
    for U in dictionary.values():
        W = product(product(Ke, U), De)
        assert product(W, Ke) == product(Ke, U)
        assert product(De, W) == product(U, De)
    for stage in 'LGN':
        M = {(r['target'], r['source']): coefficient(r['weight'])
             for r in store['arrows'] if r['stage'] == stage}
        assert product(M, Ke) == Ke and product(De, M) == De
    native_rows['electron'] = {'raw_coordinates': 8, 'return_rank': 2,
        'spin_dictionary_native': True, 'stage_letters': list('LGN'), 'native_spin_tokens': 24}

    sector_count = encounter_count = placement_count = triple_count = permutation_count = 0
    for name in ('proton', 'neutron'):
        source_path = ROOT/contract['source_identity'][name]
        line = LineInterface(source_path)
        native_lines[name] = line
        K1 = {(i, 0): x for i, x in enumerate(line.column) if x != ZERO}
        D1 = {(0, i): x for i, x in enumerate(line.row) if x != ZERO}
        I1 = {(0, 0): ONE}
        assert product(D1, K1) == I1 and product(K1, D1) == line.ops['N']
        for M in line.ops.values():
            assert product(M, K1) == K1 and product(D1, M) == D1
        language = Language(name, digest(source_path), False, False, I1, dictionary)
        languages[name] = language
        empty = language.empty()
        for stage in 'LGN':
            word = language.append(empty, 'stage', stage)
            assert language.evaluate(word) == I1 and word != empty
        reject(lambda: language.append(empty, 'spin', (0, 1, 0, 0)), 'operation unavailable')
        # Actual native L/G routes agree, whereas anticommutation requires their negatives.
        left = product(product(line.ops['L'], line.ops['G']), K1)
        right = product(product(line.ops['G'], line.ops['L']), K1)
        obstruction = add(left, right)
        assert left == right == K1 and obstruction == scale(A(2), K1) and obstruction
        native_rows[name] = {'raw_coordinates': 36, 'return_rank': 1,
            'spin_dictionary_native': False, 'stage_letters': list('LGN'),
            'native_spin_tokens': 0, 'anticommutation_residual': encode(obstruction),
            'general_obstruction': 'All complex-linear endomorphisms of a complex line are scalars. In characteristic zero, invertible scalars cannot satisfy AB=-BA.'}

        K = {(2*i+a, a): x for i, x in enumerate(line.column) for a in range(2) if x != ZERO}
        D = {(a, 2*i+a): x for i, x in enumerate(line.row) for a in range(2) if x != ZERO}
        metric = tuple(w for w in line.metric for _ in range(2))
        ops = {s: tensor_identity(M) for s, M in line.ops.items()}
        assert product(D, K) == I2 and product(K, D) == ops['N']
        assert integer_trace(ops['N']) == 2
        weighted_adjoint = {(a, i): x.flip(8)*A(metric[i]) for (i, a), x in K.items()}
        assert product(weighted_adjoint, K) == scale(line.rho, I2)
        identity_raw = {(i, i): ONE for i in range(72)}
        for U in dictionary.values():
            S = {(2*i+a, 2*i+b): x for i in range(36) for (a, b), x in U.items()}
            assert product(S, K) == product(K, U)
            assert product(D, S) == product(U, D)
            assert product(sharp(S, metric), S) == identity_raw
        extension = Language(name, digest(source_path), True, True, I2, dictionary)
        languages[name+'_doublet'] = extension
        reject(lambda: extension.validate(empty), 'carrier enlargement flag')
        for omitted in range(3):
            for signs in cartesian((-1, 1), repeat=2):
                cert = sector_certificate(omitted, signs)
                assert verify_sector(cert)
                l = dictionary[word_normal_form(cert['left'])]
                r = dictionary[word_normal_form(cert['right'])]
                assert product(K, l) == scale(-ONE, product(K, r))
                sector_count += 1
                for outgoing in range(3):
                    U = dictionary[word_normal_form(((outgoing, 1),))]
                    for prefix in (False, True):
                        lu = product(U, l) if prefix else product(l, U)
                        ru = product(U, r) if prefix else product(r, U)
                        assert product(K, lu) == scale(-ONE, product(K, ru))
                        placement_count += 1
                    encounter_count += 1
        for signs in cartesian((-1, 1), repeat=3):
            word = tuple(zip(range(3), signs))
            first, second = swap_trace(word, (0, 1, 0)), swap_trace(word, (1, 0, 1))
            assert verify_trace(first) and verify_trace(second)
            assert first['output'] == second['output'] and first['phase_bit'] == second['phase_bit'] == 1
            assert product(K, dictionary[word_normal_form(word)]) == scale(-ONE, product(K, dictionary[word_normal_form(first['output'])]))
            triple_count += 1
            for p in permutations(range(3)):
                parity = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)) % 2
                route = tuple(word[i] for i in p)
                assert product(K, dictionary[word_normal_form(route)]) == scale(A((-1)**parity), product(K, dictionary[word_normal_form(word)]))
                permutation_count += 1
        enlarged_rows[name] = {'raw_coordinates': 72, 'return_rank': 2,
            'source_metric_retained': True, 'squared_normalizer': line.rho.record(),
            'native_stage_supports': [len(line.ops[s]) for s in 'LGN'],
            'enlarged_stage_supports': [len(ops[s]) for s in 'LGN'],
            'shared_logical_operations': 24, 'spin_action_status': 'explicit supplied tensor extension, not selected physical spin'}

    # Actual geometric attachment: test both lift signs, without assuming finite-dictionary closure.
    binding = receipts['research/strominger/results/baryon-coefficient-spin-binding-v1.json']
    geo = json.loads((ROOT/'research/strominger/results/baryon-geometric-spin-lifts-v1.json').read_text(encoding='utf-8'))
    geometric_rows = []
    for row in binding['bindings']:
        name, index = row['carrier'], row['source_generator']
        line = native_lines[name]
        K = {(2*i+a, a): x for i, x in enumerate(line.column) for a in range(2) if x != ZERO}
        D = {(a, 2*i+a): x for i, x in enumerate(line.row) for a in range(2) if x != ZERO}
        P = read_operator(row['coefficient_action'], 36)
        assert P != {(i, i): ONE for i in range(36)}
        Upositive = sparse(parse_record(geo['carriers'][name]['generators'][index]['positive_scalar_spin_lift']))
        for sign in (ONE, -ONE):
            Ugeo = scale(sign, Upositive)
            Tg = {(2*i+a, 2*j+b): x*y for (i, j), x in P.items()
                  for (a, b), y in Ugeo.items() if x*y != ZERO}
            assert product(Tg, K) == product(K, Ugeo)
            assert product(D, Tg) == product(Ugeo, D)
            normalization_count, first_outside = 0, None
            for nf, U in dictionary.items():
                conjugated = product(product(Ugeo, U), adjoint(Ugeo))
                if matrix_key(conjugated) in keys:
                    normalization_count += 1
                elif first_outside is None:
                    first_outside = {'logical_normal_form': nf, 'conjugated_matrix': encode(conjugated)}
                SU = {(2*i+a, 2*i+b): x for i in range(36) for (a, b), x in U.items()}
                # Both orders are attached, not silently commuted or forced back into24.
                assert product(Tg, product(SU, K)) == product(K, product(Ugeo, U))
                assert product(SU, product(Tg, K)) == product(K, product(U, Ugeo))
            geometric_rows.append({'carrier': name, 'source_generator': index,
                'lift_sign': '+1' if sign == ONE else '-1',
                'actual_lift_in_shared_dictionary': matrix_key(Ugeo) in keys,
                'conjugated_shared_operations_remaining_in_dictionary': normalization_count,
                'normalizes_entire_dictionary': normalization_count == 24,
                'first_outside_conjugation': first_outside,
                'actual_mode_action_is_nonidentity': True, 'both_mixed_orders_checked': 24})

    proton_word = languages['proton'].empty()
    reject(lambda: languages['neutron'].validate(proton_word), 'source binding')
    reject(lambda: languages['proton'].validate(replace(proton_word, source_sha256='0'*64)), 'source binding')
    for key in ('electron', 'proton_doublet', 'neutron_doublet'):
        language = languages[key]
        empty = language.empty()
        a, inverse_a = (0, 1, 0, 0), (1, 1, 0, 0)
        word = language.append(language.append(empty, 'spin', a), 'spin', inverse_a)
        assert language.evaluate(word) == I2 and word != empty and len(word.tokens) == 2
    assert (sector_count, encounter_count, placement_count, triple_count, permutation_count) == (24, 72, 144, 16, 96)
    assert len(geometric_rows) == 6
    assert all(digest(ROOT/p) == h for p, h in pins.items()), 'upstream changed'
    checks = {
        'all_inherited_source_and_contract_pins_current': True,
        'shared_typed_native_source_recovery_grammar_three_carriers': True,
        'same24_tokens_and576_products_in_common_exact_field': True,
        'both_doublets_retain_metric_normalizer_rank_and_source': True,
        'both_doublets_all24_action_and_metric_squares': True,
        'both_doublets_all12_sectors36_encounters_and8_critical_pairs': True,
        'both_doublets_all48_permutation_routes': True,
        'all3_actual_generators_both_lift_signs_and_both_mixed_orders': True,
        'actual_geometric_dictionary_closure_measured_not_assumed': True,
        'native_rank_one_nonabelian_language_has_nonzero_residual': True,
        'source_enlargement_and_operation_guards_enforced': True,
        'equal_endpoint_does_not_erase_any_source_word': True,
    }
    report = {'schema': 'marici.shared-packet-path-language-check.v1', 'status': 'pass',
        'checks': checks, 'source_sha256': pins, 'native_models': native_rows,
        'conditional_doublets': enlarged_rows, 'geometric_attachments': geometric_rows,
        'coverage_on_two_doublets': {'sectors': sector_count, 'situated_encounters': encounter_count,
            'placement_equations': placement_count, 'critical_pair_joins': triple_count,
            'permutation_routes': permutation_count},
        'dispositions': {'shared_native_grammar': 'constructed',
            'conditional_shared_path_language': 'constructed_on_explicit_doublet_extensions',
            'unextended_native_full_spin_language': 'rejected'},
        'rank_one_scope': 'Complex-linear normalized native return carriers, not physical proton/neutron spin states.',
        'physical_lift_frame_or_coupling_selected': False, 'original_bridge_status': 'blocked_not_complete',
        'native_producers_executed': False, 'formal_proof_recompiled': False}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    summary = {k: v for k, v in report.items() if k not in ('source_sha256', 'native_models', 'conditional_doublets', 'geometric_attachments')}
    summary['geometric_dictionary_tests'] = [{k: v for k, v in r.items() if k != 'first_outside_conjugation'} for r in geometric_rows]
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
