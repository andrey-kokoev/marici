"""Exact source-bound native sector calculus. Standard library only."""
from copy import deepcopy
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path

from electron_packet_interface import (ROOT, Interface, ACTIONS, E, I, F, G0, G1,
                                       act, adj, gmm, sm, matrix_add, gm, gc, gt)
from native_path_sector_calculus import (NORMAL_FORMS, ONE, CENTRAL, A, B, C, T,
    multiply, power, phi, word_normal_form, sector_certificate, verify_sector,
    swap_trace, verify_trace)

CONTRACT = ROOT/'research/strominger/contracts/native-path-sector-calculus.v1.json'
RESULT = ROOT/'research/strominger/results/native-path-sector-calculus-v1.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def matrix_power(matrix, n):
    out = I
    for _ in range(n):
        out = gmm(out, matrix)
    return out


def matrix_word(word):
    out = I
    for axis, sign in word:
        out = gmm(out, sm(sign, E[axis]))
    return out


def inner(x, y):
    return gt(gm(gc(a), b) for a, b in zip(x, y))


def reject(action, residual):
    try:
        action()
    except ValueError as error:
        assert residual in str(error), (residual, str(error))
    else:
        raise AssertionError('accepted hostile: '+residual)


def jsonable(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: jsonable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [jsonable(v) for v in value]
    return value


def main():
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    assert contract['accounting']['signed_sector_coverage'] == 12
    assert contract['accounting']['situated_encounter_coverage'] == 36
    pins = {}
    for rel in contract['source']['prerequisite_receipts']:
        path = ROOT/rel
        prior = json.loads(path.read_text(encoding='utf-8'))
        assert prior['status'] == 'pass'
        for source, frozen in prior['source_sha256'].items():
            assert digest(ROOT/source) == frozen, ('stale source', source)
            if source in pins:
                assert pins[source] == frozen
            pins[source] = frozen
        pins[rel] = digest(path)
    for path in (CONTRACT, Path(__file__).resolve(),
                 Path(__file__).with_name('native_path_sector_calculus.py').resolve()):
        pins[path.relative_to(ROOT).as_posix()] = digest(path)

    f = Interface()
    z = sm(-1, I)
    h = I
    for e in E:
        h = matrix_add(h, e)
    t = sm(-F(1, 2), h)
    assert t in ACTIONS and matrix_power(t, 3) == I
    assert E[2] == gmm(E[0], E[1])
    for axis in range(3):
        assert gmm(gmm(t, E[axis]), adj(t)) == E[(axis+1) % 3]
        assert gmm(E[axis], E[axis]) == z
        assert adj(E[axis]) == sm(-1, E[axis])
    assert gmm(E[0], E[1]) == gmm(z, gmm(E[1], E[0]))

    # Evaluate normal forms independently in the already imported source matrices.
    matrices = {}
    for nf in NORMAL_FORMS:
        e, i, j, k = nf
        out = sm((-1)**e, I)
        for matrix, exponent in ((E[0], i), (E[1], j), (t, k)):
            out = gmm(out, matrix_power(matrix, exponent))
        matrices[nf] = out
    assert len(set(matrices.values())) == 24 and set(matrices.values()) == set(ACTIONS)
    for x, y in product(NORMAL_FORMS, repeat=2):
        assert matrices[multiply(x, y)] == gmm(matrices[x], matrices[y])
    for x, y, w in product(NORMAL_FORMS, repeat=3):
        assert multiply(multiply(x, y), w) == multiply(x, multiply(y, w))
    assert matrices[A] == E[0] and matrices[B] == E[1] and matrices[C] == E[2]
    assert matrices[T] == t and matrices[CENTRAL] == z
    assert all(phi(phi(phi(q))) == q for q in product(range(2), repeat=3))
    tokens = tuple(product(range(3), (-1, 1)))
    word_count = 0
    for length in range(5):
        for word in product(tokens, repeat=length):
            assert matrices[word_normal_form(word)] == matrix_word(word)
            word_count += 1

    sectors, encounters = [], []
    for omitted in range(3):
        for signs in product((-1, 1), repeat=2):
            cert = sector_certificate(omitted, signs)
            assert verify_sector(cert)
            r = cert['cyclic_conjugation_power']
            tr = matrix_power(t, r)
            # Transport the ONE seed by an actual native conjugator.
            orbit = tuple(gmm(gmm(tr, a), adj(tr)) for a in E[:2])
            assert orbit == tuple(E[a] for a in cert['orbit_pair'])
            transported = tuple(adj(a) if i in cert['inverted_seed_positions'] else a
                                for i, a in enumerate(orbit))
            if cert['exchange_route_order']:
                transported = tuple(reversed(transported))
            assert transported == tuple(sm(s, E[a]) for a, s in cert['left'])
            left, right = matrix_word(cert['left']), matrix_word(cert['right'])
            assert left == sm(-1, right) and gmm(adj(left), right) == z
            raw_left = gmm(gmm(f.K, left), f.D)
            raw_right = gmm(gmm(f.K, right), f.D)
            assert raw_left == sm(-1, raw_right)
            assert gmm(adj(raw_left), raw_right) == sm(-1, f.N)
            assert gmm(raw_left, f.K) == gmm(f.K, left)
            assert gmm(f.D, raw_left) == gmm(left, f.D)
            for outgoing in range(3):
                # Left and right whiskering: no phase is erased by continuation.
                for prefix in (False, True):
                    l = gmm(E[outgoing], left) if prefix else gmm(left, E[outgoing])
                    r = gmm(E[outgoing], right) if prefix else gmm(right, E[outgoing])
                    assert l == sm(-1, r)
                encounters.append({'sector': len(sectors), 'outgoing_axis': outgoing,
                                   'left_and_right_compatibility': True})
            sectors.append(cert)
    assert len(sectors) == 12 and len(encounters) == 36

    triples = []
    for signs in product((-1, 1), repeat=3):
        word = tuple(zip(range(3), signs))
        first = swap_trace(word, (0, 1, 0))
        second = swap_trace(word, (1, 0, 1))
        assert verify_trace(first) and verify_trace(second)
        assert first['output'] == second['output'] == tuple(reversed(word))
        assert first['phase_bit'] == second['phase_bit'] == 1
        assert first['steps'] != second['steps']  # A join is NOT trace identity.
        assert matrix_word(word) == sm(-1, matrix_word(first['output']))
        permutation_records = []
        for p in permutations(range(3)):
            parity = sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)) % 2
            route = tuple(word[i] for i in p)
            assert matrix_word(route) == sm((-1)**parity, matrix_word(word))
            permutation_records.append({'permutation': p, 'phase_bit': parity})
        triples.append({'signs': signs, 'first': first, 'second': second,
                        'permutations': permutation_records})

    # Deliberate failures retain actual unequal matrices / invalid certificates.
    wrong_sector = deepcopy(sectors[0])
    wrong_sector['phase_bit'] = 0
    reject(lambda: verify_sector(wrong_sector), 'forged sector derivation')
    wrong_trace = deepcopy(triples[0]['first'])
    wrong_trace['steps'][0]['phase_bit'] = 0
    reject(lambda: verify_trace(wrong_trace), 'forged swap trace')
    wrong_output = deepcopy(triples[0]['first'])
    wrong_output['output'] = wrong_output['input']
    reject(lambda: verify_trace(wrong_output), 'forged swap trace')
    reject(lambda: swap_trace(((0, 1), (0, -1)), (0,)), 'distinct axes required')
    reject(lambda: swap_trace(((0, 1), (1, 1)), (2,)), 'swap position')
    reject(lambda: word_normal_form(((0, 0),)), 'signed axis domain')
    left, right = gmm(E[0], E[1]), gmm(E[1], E[0])
    assert left != right
    ref = (G1, G0)
    u, v = act(left, ref), act(right, ref)
    density_u = tuple(tuple(gm(a, gc(b)) for b in u) for a in u)
    density_v = tuple(tuple(gm(a, gc(b)) for b in v) for a in v)
    assert density_u == density_v and inner(u, v) == (-F(1), F(0))
    original = f.extract(f.seed(ref))
    inverse_word = f.packet_step(f.packet_step(original, E[0]), adj(E[0]))
    assert original.spinor == inverse_word.spinor and original.archive != inverse_word.archive
    assert all(digest(ROOT/p) == h for p, h in pins.items()), 'source changed during check'

    checks = {
        'frozen_prerequisite_source_pins': True,
        'native_conjugator_and_seed_relations': True,
        '24_normal_forms_exactly_native_dictionary': True,
        '576_products_and_13824_associativity_checks': True,
        '1555_signed_words_through_length4_match_independent_source_evaluation': word_count == 1555,
        '12_sectors_derived_from_one_seed_with_raw_image_squares': True,
        '36_situated_encounters_with72_compatibility_equations': True,
        '8_three_direction_critical_pairs_join_without_trace_erasure': True,
        '48_permutation_routes_have_source_checked_parity': True,
        'forged_phase_boundary_and_domain_certificates_rejected': True,
        'flat_square_and_density_erasure_hostiles_have_nonzero_residual': True,
        'endpoint_inverse_does_not_erase_execution_archive': True,
    }
    assert all(checks.values())
    report = {
        'schema': 'marici.native-path-sector-calculus-check.v1', 'status': 'pass',
        'checks': checks, 'source_sha256': pins,
        'generators': {'a': E[0], 'b': E[1], 't': t, 'central_z': z},
        'normal_form_dictionary': [{'normal_form': nf, 'matrix': matrices[nf]} for nf in NORMAL_FORMS],
        'sectors': sectors, 'situated_encounters': encounters, 'triple_critical_pairs': triples,
        'hostiles': {'flat_square_residual': matrix_add(left, sm(-1, right)),
                     'equal_density_reference_pairing': inner(u, v),
                     'original_archive_length': len(original.archive.word),
                     'inverse_word_archive_length': len(inverse_word.archive.word)},
        'disposition': 'Reusable native algebraic comparison calculus constructed; literal flat fillers rejected.',
        'scope': 'Endpoint group normal forms and explicit phase-corrected sector/critical-pair certificates on native electron image. No identification of execution traces or all higher homotopies.',
        'coverage': {'directions': 3, 'sectors': 12, 'situated_encounters': 36},
        'cost_minimum': None, 'assembly_stage_correspondence': False,
        'formal_proof_recompiled': False, 'physical_particle_identification': False,
        'original_bridge_status': 'blocked_not_complete',
    }
    RESULT.write_text(json.dumps(jsonable(report), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'checks': checks, 'coverage': report['coverage'],
                      'native_operations': len(matrices), 'disposition': report['disposition']}, indent=2))


if __name__ == '__main__':
    main()
