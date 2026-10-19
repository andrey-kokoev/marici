"""Source-Cartesian spin-frame adapters; exact scalar normalization retained."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product as cartesian, permutations
import json
from pathlib import Path

from check_shared_packet_path_language import (ROOT, A, ZERO, ONE, product, scale,
    add, two, I2, matrix_key, LineInterface, parse_record, sparse, encode, read_operator)
from check_baryon_geometric_spin_lifts import (S2, S3, mm, adj, transpose, inverse,
    identity, clifford, E, record, lift_order3, matrix)
from native_path_sector_calculus import (CENTRAL, word_normal_form, sector_certificate,
    verify_sector, swap_trace, verify_trace)

CONTRACT = ROOT/'research/strominger/contracts/shared-packet-frame-adapter.v1.json'
RESULT = ROOT/'research/strominger/results/shared-packet-frame-adapter-v1.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def determinant3(M):
    return sum((A((-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)))*
                M[0][p[0]]*M[1][p[1]]*M[2][p[2]] for p in permutations(range(3))), ZERO)


def intertwiner(O):
    equations = []
    for j in range(3):
        target = clifford(tuple(O[i][j] for i in range(3)))
        for a in range(2):
            for b in range(2):
                row = [ZERO]*4
                for k in range(2):
                    row[2*a+k] += E[j][k][b]
                    row[2*k+b] -= target[a][k]
                equations.append(row)
    # Exact RREF over the inherited complex number field; no spectral fit.
    rows = [row[:] for row in equations]
    pivots, cursor = [], 0
    for col in range(4):
        pivot = next((i for i in range(cursor, len(rows)) if rows[i][col] != ZERO), None)
        if pivot is None:
            continue
        rows[cursor], rows[pivot] = rows[pivot], rows[cursor]
        d = rows[cursor][col]
        rows[cursor] = [x/d for x in rows[cursor]]
        for i in range(len(rows)):
            if i != cursor and rows[i][col] != ZERO:
                q = rows[i][col]
                rows[i] = [x-q*y for x, y in zip(rows[i], rows[cursor])]
        pivots.append(col)
        cursor += 1
    free = [i for i in range(4) if i not in pivots]
    assert len(free) == 1, 'Clifford intertwiner space is not a line'
    vector = [ZERO]*4
    vector[free[0]] = ONE
    for i, col in enumerate(pivots):
        vector[col] = -rows[i][free[0]]
    assert all(sum((x*y for x, y in zip(row, vector)), ZERO) == ZERO for row in equations)
    C = (tuple(vector[:2]), tuple(vector[2:]))
    Cinv = inverse(C)
    assert mm(C, Cinv) == identity(2)
    gram = mm(adj(C), C)
    r = gram[0][0]
    assert r != ZERO and r.flip(8) == r and gram == tuple(tuple(r if i == j else ZERO for j in range(2)) for i in range(2))
    for j in range(3):
        assert mm(C, E[j]) == mm(clifford(tuple(O[i][j] for i in range(3))), C)
    return C, Cinv, r


def main():
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    pins, priors = {}, {}
    for rel in contract['source_receipts']:
        path = ROOT/rel
        prior = json.loads(path.read_text(encoding='utf-8'))
        assert prior['status'] == 'pass'
        priors[rel] = prior
        for p, h in prior['source_sha256'].items():
            assert digest(ROOT/p) == h, ('stale source', p)
            if p in pins:
                assert pins[p] == h
            pins[p] = h
        pins[rel] = digest(path)
    for path in (CONTRACT, Path(__file__).resolve()):
        pins[path.relative_to(ROOT).as_posix()] = digest(path)
    native_path = ROOT/'research/strominger/results/native-path-sector-calculus-v1.json'
    native = json.loads(native_path.read_text(encoding='utf-8'))
    dictionary = {tuple(row['normal_form']): two(tuple(tuple(tuple(F(x) for x in entry) for entry in r) for r in row['matrix']))
                  for row in native['normal_form_dictionary']}
    keys = {matrix_key(U) for U in dictionary.values()}
    geo = priors['research/strominger/results/baryon-geometric-spin-lifts-v1.json']
    binding = priors['research/strominger/results/baryon-coefficient-spin-binding-v1.json']
    old = priors['research/strominger/results/shared-packet-path-language-v1.json']
    # These are the source-to-native Cartesian adapters already used by coefficient binding.
    vertices = matrix(((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)))
    Vp = tuple(tuple(vertices[j+1][i]-vertices[0][i] for j in range(3)) for i in range(3))
    Vn = ((ZERO,A(F(2,3))*S2,A(F(4,3))),(-A(2),A(F(2,3))*S2,-A(F(2,3))),(A(2),A(F(2,3))*S2,-A(F(2,3))))
    frames = {'proton': Vp, 'neutron': tuple(tuple(S2*S3*x/A(4) for x in row) for row in Vn)}
    outputs, source_rows = {}, []
    for name in ('proton', 'neutron'):
        source = json.loads((ROOT/geo['carriers'][name]['source']).read_text(encoding='utf-8'))
        M = matrix(source['metric'])
        B = parse_record(geo['carriers'][name]['whitening'])
        Fnative = frames[name]
        assert mm(transpose(Fnative), Fnative) == M
        O = mm(Fnative, inverse(B))
        determinant = determinant3(O)
        assert determinant in (ONE, -ONE)
        orientation_corrected = determinant == -ONE
        if orientation_corrected:
            Fnative = tuple(tuple(-x for x in row) for row in Fnative)
            O = tuple(tuple(-x for x in row) for row in O)
        assert determinant3(O) == ONE and mm(transpose(O), O) == identity(3)
        C, Cinv, r = intertwiner(O)
        Cs, Cis = sparse(C), sparse(Cinv)
        line = LineInterface(ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json')
        Kold = {(2*i+a, a): x for i, x in enumerate(line.column) for a in range(2) if x != ZERO}
        Dold = {(a, 2*i+a): x for i, x in enumerate(line.row) for a in range(2) if x != ZERO}
        Knew, Dnew = product(Kold, Cis), product(Cs, Dold)
        assert product(Dnew, Knew) == I2 and product(Knew, Dnew) == product(Kold, Dold)
        metric = tuple(w for w in line.metric for _ in range(2))
        weighted_adjoint = {(a, i): x.flip(8)*A(metric[i]) for (i, a), x in Knew.items()}
        new_rho = line.rho/r
        assert product(weighted_adjoint, Knew) == scale(new_rho, I2)
        assert new_rho != line.rho, 'old normalizer happens to remain valid; do not claim hostile here'
        for U in dictionary.values():
            old_frame_U = product(product(Cis, U), Cs)
            S = {(2*i+a, 2*i+b): x for i in range(36) for (a, b), x in old_frame_U.items()}
            assert product(S, Knew) == product(Knew, U)
            assert product(Dnew, S) == product(U, Dnew)
        for omitted in range(3):
            for signs in cartesian((-1, 1), repeat=2):
                cert = sector_certificate(omitted, signs)
                assert verify_sector(cert)
                l, q = (dictionary[word_normal_form(cert[k])] for k in ('left', 'right'))
                assert product(Knew, l) == scale(-ONE, product(Knew, q))
                for outgoing in range(3):
                    U = dictionary[word_normal_form(((outgoing, 1),))]
                    assert product(Knew, product(U, l)) == scale(-ONE, product(Knew, product(U, q)))
                    assert product(Knew, product(l, U)) == scale(-ONE, product(Knew, product(q, U)))
        for signs in cartesian((-1, 1), repeat=3):
            word = tuple(zip(range(3), signs))
            first, second = swap_trace(word, (0, 1, 0)), swap_trace(word, (1, 0, 1))
            assert verify_trace(first) and verify_trace(second)
            assert first['output'] == second['output'] and first['phase_bit'] == second['phase_bit']
            assert product(Knew, dictionary[word_normal_form(word)]) == scale(-ONE, product(Knew, dictionary[word_normal_form(first['output'])]))
        for row in binding['bindings']:
            if row['carrier'] != name:
                continue
            index = row['source_generator']
            Tvector = matrix(source['generators'][index]['matrix'])
            Rnative = mm(mm(Fnative, Tvector), inverse(Fnative))
            assert Rnative == parse_record(row['construction']['native_spatial_rotation'])
            Utarget = lift_order3(Rnative)
            Uold = parse_record(geo['carriers'][name]['generators'][index]['positive_scalar_spin_lift'])
            assert mm(mm(C, Uold), Cinv) == Utarget
            P = read_operator(row['coefficient_action'], 36)
            for sign in (ONE, -ONE):
                V = scale(sign, sparse(Utarget))
                U = scale(sign, sparse(Uold))
                assert matrix_key(V) in keys
                assert all(matrix_key(product(product(V, Q), adjoint_sparse(V))) in keys for Q in dictionary.values())
                raw = {(2*i+a, 2*j+b): x*y for (i, j), x in P.items() for (a, b), y in U.items() if x*y != ZERO}
                assert product(raw, Knew) == product(Knew, V)
                assert product(Dnew, raw) == product(V, Dnew)
                hostile = add(product(raw, Kold), scale(-ONE, product(Kold, V)))
                assert hostile, 'unchanged encoder unexpectedly accepts changed logical frame'
                previous = next(x for x in old['geometric_attachments'] if x['carrier'] == name and x['source_generator'] == index and x['lift_sign'] == ('+1' if sign == ONE else '-1'))
                assert previous['normalizes_entire_dictionary'] is False
                source_rows.append({'carrier': name, 'source_generator': index,
                    'sign': '+1' if sign == ONE else '-1',
                    'old_frame_conjugations_remaining': previous['conjugated_shared_operations_remaining_in_dictionary'],
                    'transported_lift_in_common_dictionary': True,
                    'transported_conjugations_remaining': 24,
                    'old_encoder_changed_logical_action_hostile': encode(hostile),
                    'transported_lift': encode(V)})
        outputs[name] = {'proper_source_frame': record(Fnative), 'source_frame_map': record(O),
            'orientation_corrected_by_global_negation': orientation_corrected,
            'spin_intertwiner': record(C), 'spin_intertwiner_inverse': record(Cinv),
            'spin_intertwiner_squared_normalizer': r.record(),
            'old_encoder_gram_factor': line.rho.record(), 'new_encoder_gram_factor': new_rho.record(),
            'encoder': encode(Knew), 'decoder': encode(Dnew),
            'logical_ops_checked': 24, 'sectors_checked': 12,
            'encounters_checked': 36, 'critical_pairs_checked': 8}
    assert len(source_rows) == 6
    assert all(digest(ROOT/p) == h for p, h in pins.items())
    checks = {'all_prerequisite_pins_and_old_frame_failures_retained': True,
        'both_native_cartesian_frames_source_metric_and_proper_orientation': True,
        'both_exact_clifford_intertwiner_spaces_are_lines': True,
        'both_intertwiners_invertible_with_scalar_gram': True,
        'both_new_encoders_decoders_keep_original_raw_projector': True,
        'both_metric_normalizers_explicitly_transported': True,
        'all24_words12_sectors36_encounters8_joins_on_each_source': True,
        'all3_source_generators_both_lifts_in_common24_after_transport': True,
        'all6_transported_lifts_normalize_all24_operations': True,
        'old_encoder_and_old_normalizer_substitution_hostiles_nonzero': True}
    report = {'schema': 'marici.shared-packet-frame-adapter-check.v1', 'status': 'pass',
        'checks': checks, 'source_sha256': pins, 'adapters': outputs, 'source_bindings': source_rows,
        'disposition': 'Source-frame coordinate obstruction resolved on explicit tensor doublets; old-frame nonclosure remains true.',
        'physical_frame_lift_or_coupling_selected': False,
        'original_bridge_status': 'blocked_not_complete', 'native_producers_executed': False,
        'formal_proof_recompiled': False}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in ('source_sha256', 'adapters', 'source_bindings')}, indent=2))


def adjoint_sparse(M):
    return {(j, i): x.flip(8) for (i, j), x in M.items()}


if __name__ == '__main__':
    main()
