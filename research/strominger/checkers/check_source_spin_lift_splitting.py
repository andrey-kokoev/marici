"""Exact source-bound spin extension splitting, not abstract-label inference."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product as cartesian, permutations
import json
from pathlib import Path

from electron_packet_interface import ROOT, ACTIONS, I, E, G0, G1, adj, gmm, sm, gm, ga
from check_baryon_geometric_spin_lifts import matrix, mm, inverse
from check_shared_packet_path_language import (parse_record, sparse, two, product,
    scale, read_operator, encode, LineInterface, A, ZERO, ONE)

CONTRACT = ROOT/'research/strominger/contracts/source-spin-lift-splitting-test.v1.json'
RESULT = ROOT/'research/strominger/results/source-spin-lift-splitting-v1.json'
MINUS_I = sm(-1, I)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def semantic_digest(proposition):
    body = {k: v for k, v in proposition.items() if k not in ('status', 'test_plan', 'disposition')}
    return sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def rational_matrix(M):
    assert all(not any(x.c[1:]) for row in M for x in row)
    return tuple(tuple(x.c[0] for x in row) for row in M)


def ridentity(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def rproduct(M, N):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in zip(*N)) for row in M)


def ract(M, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in M)


def spin_from_encoded(rows):
    out = [[G0]*2 for _ in range(2)]
    for row in rows:
        value = row['coefficient']
        assert set(value) <= {'0', '8'}
        out[row['target']][row['source']] = (F(value.get('0', '0')), F(value.get('8', '0')))
    return tuple(map(tuple, out))


def spin_projection(U):
    columns = []
    for e in E:
        X = gmm(gmm(U, e), adj(U))
        column = []
        for a in E:
            Y = gmm(a, X)
            trace = ga(Y[0][0], Y[1][1])
            assert trace[1] == 0
            column.append(-trace[0]/2)
        columns.append(tuple(column))
    return tuple(zip(*columns))


def verify_projection(U, R):
    det = ga(gm(U[0][0], U[1][1]), tuple(-x for x in gm(U[0][1], U[1][0])))
    if gmm(adj(U), U) != I or det != G1 or spin_projection(U) != R:
        raise ValueError('actual source projection mismatch')


def mode_from_encoded(rows):
    columns = {}
    for row in rows:
        value = row['coefficient']
        assert set(value) == {'0'} and F(value['0']) in (-1, 1)
        j = row['source']
        assert j not in columns
        columns[j] = (row['target'], int(F(value['0'])))
    assert set(columns) == set(range(36))
    assert len({v[0] for v in columns.values()}) == 36
    return tuple(columns[j] for j in range(36))


def mode_product(P, Q):
    return tuple((P[k][0], sign*P[k][1]) for k, sign in Q)


def mode_sparse(P):
    return {(i, j): A(sign) for j, (i, sign) in enumerate(P)}


def source_group(rotations, modes, spins, bound):
    identity = ridentity(3)
    mode_identity = tuple((i, 1) for i in range(36))
    group = [identity]
    positions = {identity: 0}
    words, mode_actions, section = [()], [mode_identity], [I]
    cursor = 0
    while cursor < len(group):
        for j, R in enumerate(rotations):
            target = rproduct(group[cursor], R)
            P = mode_product(mode_actions[cursor], modes[j])
            if target in positions:
                assert mode_actions[positions[target]] == P, 'source rotation/mode relation mismatch'
            else:
                positions[target] = len(group)
                group.append(target)
                words.append(words[cursor]+(j,))
                mode_actions.append(P)
                section.append(gmm(section[cursor], spins[j]))
                assert len(group) <= bound
        cursor += 1
    table = [[positions[rproduct(g, h)] for h in group] for g in group]
    for g, h in cartesian(range(len(group)), repeat=2):
        assert mode_product(mode_actions[g], mode_actions[h]) == mode_actions[table[g][h]]
    return group, words, mode_actions, section, table


def section_defect(section, table, group):
    if section[0] != I:
        return ('identity', 0)
    for g, R in enumerate(group):
        if spin_projection(section[g]) != R:
            return ('projection', g)
    for g, h in cartesian(range(len(group)), repeat=2):
        if gmm(section[g], section[h]) != section[table[g][h]]:
            return ('multiplication', g, h)
    return None


def validate_section(section, table, group):
    if section_defect(section, table, group) is not None:
        raise ValueError('not a source group section')


def validate_obstruction(U, R, claimed_square):
    verify_projection(U, R)
    if R == ridentity(3) or rproduct(R, R) != ridentity(3):
        raise ValueError('not a nonidentity source involution')
    actual = gmm(U, U)
    if claimed_square != actual or actual != MINUS_I:
        raise ValueError('spin square certificate mismatch')


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
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    return value


def main():
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    proposition = json.loads((ROOT/contract['proposition_path']).read_text(encoding='utf-8'))
    assert semantic_digest(proposition) == contract['proposition_semantic_sha256'], 'mathematical proposition changed'
    paths = {
        'frame': 'research/strominger/results/shared-packet-frame-adapter-v1.json',
        'binding': 'research/strominger/results/baryon-coefficient-spin-binding-v1.json',
        'geo': 'research/strominger/results/baryon-geometric-spin-lifts-v1.json'}
    pins, prior = {}, {}
    for name, rel in paths.items():
        path = ROOT/rel
        receipt = json.loads(path.read_text(encoding='utf-8'))
        assert receipt['status'] == 'pass' and all(receipt['checks'].values())
        prior[name] = receipt
        for source, h in receipt['source_sha256'].items():
            assert digest(ROOT/source) == h, ('stale source', source)
            if source in pins:
                assert pins[source] == h
            pins[source] = h
        pins[rel] = digest(path)
    for path in (CONTRACT, Path(__file__).resolve()):
        pins[path.relative_to(ROOT).as_posix()] = digest(path)
    projections = {U: spin_projection(U) for U in ACTIONS}
    for U, R in projections.items():
        verify_projection(U, R)
    results, checks = {}, {'prospective_semantic_statement_and_all_source_pins_fixed': True}
    for name, expected in (('proton', 12), ('neutron', 3)):
        source_rel = prior['geo']['carriers'][name]['source']
        source = json.loads((ROOT/source_rel).read_text(encoding='utf-8'))
        frame = prior['frame']['adapters'][name]
        Fnative = parse_record(frame['proper_source_frame'])
        C, Cinv = parse_record(frame['spin_intertwiner']), parse_record(frame['spin_intertwiner_inverse'])
        generators = [r for r in prior['binding']['bindings'] if r['carrier'] == name]
        rotations, modes, spins, old_spins = [], [], [], []
        for row in generators:
            j = row['source_generator']
            T = matrix(source['generators'][j]['matrix'])
            Rfield = mm(mm(Fnative, T), inverse(Fnative))
            assert Rfield == parse_record(row['construction']['native_spatial_rotation'])
            R = rational_matrix(Rfield)
            transported = next(r for r in prior['frame']['source_bindings'] if r['carrier'] == name and r['source_generator'] == j and r['sign'] == '+1')
            U = spin_from_encoded(transported['transported_lift'])
            Uold = parse_record(prior['geo']['carriers'][name]['generators'][j]['positive_scalar_spin_lift'])
            assert sparse(mm(mm(C, Uold), Cinv)) == two(U)
            assert U in ACTIONS and sm(-1, U) in ACTIONS
            verify_projection(U, R)
            verify_projection(sm(-1, U), R)
            rotations.append(R)
            modes.append(mode_from_encoded(row['coefficient_action']))
            spins.append(U)
            old_spins.append(sparse(Uold))
        group, words, mode_actions, section, table = source_group(rotations, modes, spins, expected)
        assert len(group) == expected
        if name == 'proton':
            vertices = tuple(tuple(map(F, v)) for v in ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)))
            action = [tuple(vertices.index(ract(R, v)) for v in vertices) for R in group]
            even = {p for p in permutations(range(4)) if sum(p[i] > p[j] for i in range(4) for j in range(i+1,4)) % 2 == 0}
            assert set(action) == even and len(set(action)) == len(group)
            for g, h in cartesian(range(len(group)), repeat=2):
                assert action[table[g][h]] == tuple(action[g][action[h][i]] for i in range(4))
            identification = {'group': 'A4', 'actual_tetrahedron_permutations': action,
                              'certificate': 'faithful action equals the full even-permutation group, with every product checked'}
        else:
            R = rotations[0]
            powers = (ridentity(3), R, rproduct(R, R))
            assert len(set(powers)) == 3 and rproduct(powers[2], R) == powers[0]
            assert set(powers) == set(group)
            indices = tuple(group.index(g) for g in powers)
            assert all(table[indices[i]][indices[j]] == indices[(i+j) % 3] for i,j in cartesian(range(3), repeat=2))
            identification = {'group': 'C3', 'source_power_indices': indices,
                              'certificate': 'actual generator powers and multiplication modulo3 checked'}

        fibres = [[U for U, R in projections.items() if R == g] for g in group]
        assert all(len(fibre) == 2 and fibre[0] == sm(-1, fibre[1]) for fibre in fibres)
        assert all(section[g] in fibres[g] for g in range(len(group)))
        extension = [(g, U) for g, fibre in enumerate(fibres) for U in fibre]
        for (g,U), (h,V) in cartesian(extension, repeat=2):
            assert gmm(U,V) in fibres[table[g][h]]
        cocycle = []
        for g in range(len(group)):
            row = []
            for h in range(len(group)):
                actual = gmm(section[g], section[h])
                target = section[table[g][h]]
                assert actual in (target, sm(-1, target))
                row.append(int(actual != target))
            cocycle.append(row)
        assert not any(cocycle[0]) and not any(row[0] for row in cocycle)
        for g,h,k in cartesian(range(len(group)), repeat=3):
            assert (cocycle[g][h]+cocycle[table[g][h]][k]) % 2 == (cocycle[h][k]+cocycle[g][table[h][k]]) % 2
        solutions, failures = [], []
        for suffix in cartesian((0,1), repeat=len(group)-1):
            gauge = (0,)+suffix
            defect = next(((g,h) for g,h in cartesian(range(len(group)), repeat=2)
                           if (cocycle[g][h]+gauge[g]+gauge[h]+gauge[table[g][h]]) % 2), None)
            if defect is None:
                candidate = [sm((-1)**gauge[g], U) for g,U in enumerate(section)]
                validate_section(candidate, table, group)
                solutions.append({'sign_bits': gauge, 'matrices': candidate})
            else:
                failures.append(defect)
        assert len(solutions)+len(failures) == 2**(len(group)-1)

        K, D = read_operator(frame['encoder'],72), read_operator(frame['decoder'],72)
        line = LineInterface(ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json')
        for g, U in enumerate(section):
            P = mode_sparse(mode_actions[g])
            column = {(i,0): x for i,x in enumerate(line.column) if x != ZERO}
            assert product(P,column) == column
            u = two(U)
            # K',D' use common logical coordinates, but the RAW tensor factor
            # still uses the original spin frame. Transport back before tensoring.
            old_u = product(product(sparse(Cinv),u),sparse(C))
            actual_word_u = {(0,0):ONE,(1,1):ONE}
            for generator in words[g]:
                actual_word_u = product(actual_word_u,old_spins[generator])
            assert old_u == actual_word_u, 'raw spin action differs from actual source word'
            raw = {(2*i+a,2*j+b): x*y for (i,j),x in P.items() for (a,b),y in old_u.items() if x*y != ZERO}
            assert product(raw,K) == product(K,u) and product(D,raw) == product(u,D)
        generator_controls = []
        obstruction = None
        if name == 'proton':
            assert not solutions
            g = next(g for g in range(1,len(group)) if table[g][g] == 0 and cocycle[g][g] == 1)
            assert all(gmm(U,U) == MINUS_I for U in fibres[g])
            for U in fibres[g]:
                validate_obstruction(U,group[g],MINUS_I)
            # This diagonal defect cannot change: eps(g)+eps(g)+eps(e)=0.
            assert all((cocycle[g][g]+b+b+0) % 2 == 1 for b in (0,1))
            word = words[g]+words[g]
            for signs in cartesian((-1,1), repeat=len(spins)):
                R, P, U = ridentity(3), tuple((i,1) for i in range(36)), I
                for j in word:
                    R = rproduct(R,rotations[j]);P = mode_product(P,modes[j]);U = gmm(U,sm(signs[j],spins[j]))
                assert R == ridentity(3) and P == tuple((i,1) for i in range(36)) and U == MINUS_I
                cubes = []
                for j,V in enumerate(spins):
                    V = sm(signs[j],V)
                    cubes.append(gmm(gmm(V,V),V) == I)
                generator_controls.append({'signs': signs,'each_generator_order3_passes': all(cubes), 'mixed_identity_word_spin': '-I'})
            assert any(row['each_generator_order3_passes'] for row in generator_controls)
            reject(lambda: validate_obstruction(section[g],group[g],I), 'spin square certificate mismatch')
            reject(lambda: verify_projection(I,group[g]), 'actual source projection mismatch')
            obstruction = {'source_element': g, 'source_element_word': words[g],
                'identity_word': word, 'source_square_index': 0, 'mode_square_identity': True,
                'both_lifts_square': '-I', 'cocycle_diagonal_bit': 1,
                'sign_gauge_invariance': 'c(g,g)+eps(g)+eps(g)+eps(e)=1 for every normalized eps',
                'all_generator_sign_controls': generator_controls}
        else:
            assert len(solutions) == 1
            good = solutions[0]['matrices']
            validate_section(good,table,group)
            g = group.index(rotations[0])
            assert good[g] == sm(-1,spins[0])
            wrong = list(good);wrong[g] = spins[0]
            reject(lambda: validate_section(wrong,table,group), 'not a source group section')
            reject(lambda: verify_projection(spins[0],ridentity(3)), 'actual source projection mismatch')
        checks[name+'_actual_source_rotations_and_all_mode_relations'] = True
        checks[name+'_source_group_identification_not_size_or_label_only'] = True
        checks[name+'_full_two_lift_pullback_and_all_extension_products'] = True
        checks[name+'_normalized_cocycle_all_pairs_and_triples'] = True
        checks[name+'_all_normalized_section_sign_choices_exhausted'] = True
        checks[name+'_transported_raw_source_squares_for_every_element'] = True
        checks[name+'_predicted_splitting_disposition_and_hostiles'] = True
        results[name] = {'source': source_rel, 'group_identification': identification,
            'group_size': len(group), 'full_extension_size': len(extension),
            'source_rotations': group, 'source_words': words, 'multiplication_table': table,
            'mode_actions': mode_actions, 'reference_section': section,
            'cocycle_bits': cocycle, 'normalized_sign_choices_tested': 2**(len(group)-1),
            'homomorphic_sections': solutions, 'section_count': len(solutions),
            'obstruction': obstruction, 'splits': bool(solutions)}
    assert all(digest(ROOT/p) == h for p,h in pins.items())
    checks['all_native_inputs_and_prerequisite_receipts_unchanged'] = True
    report = {'schema': 'marici.source-spin-lift-splitting-check.v1', 'status': 'pass',
        'checks': checks, 'source_sha256': pins,
        'proposition_path': contract['proposition_path'],
        'proposition_semantic_sha256': semantic_digest(proposition), 'carriers': results,
        'disposition': {'neutron': 'split', 'proton': 'nonsplit'},
        'full_preimage_completeness': 'For any two SU(2) lifts of the same SO(3) action their ratio commutes with all three E_j; commuting with E1 and E2 forces a scalar, and determinant1 forces scalar +/-1. The two explicitly verified lifts therefore exhaust each fibre.',
        'physical_source_selection': False,'native_producers_executed': False,
        'formal_proof_recompiled': False, 'original_physical_bridge_complete': False}
    RESULT.write_text(json.dumps(jsonable(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','checks':checks,'disposition':report['disposition'],
        'source_group_sizes':{n:r['group_size'] for n,r in results.items()},
        'section_counts':{n:r['section_count'] for n,r in results.items()},
        'sign_choices_tested':{n:r['normalized_sign_choices_tested'] for n,r in results.items()}},indent=2))


if __name__ == '__main__':
    main()
