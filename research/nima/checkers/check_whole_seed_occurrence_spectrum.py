"""Source-factorized whole-seed continuation and occurrence spectral retention.

Column convention: K[b,a]=1 iff a can be followed by b. Thus local blocks
transpose the earlier row-successor cyclic matrices. Matrices describe the
retained incidence; applying them as physical dynamics is not asserted.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import check_natural_tower_return as native
import check_record4_spectral_promotion as sp
import check_spectral_successor_many_many as rec
from check_indexed_path_synthesis import compose


def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def zeros(n, m=None):
    return tuple((F(0),) * (n if m is None else m) for _ in range(n))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def rank(matrix):
    rows = [list(row) for row in matrix]
    pivot_row = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        divisor = rows[pivot_row][col]
        rows[pivot_row] = [entry / divisor for entry in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row:
                factor = rows[i][col]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def apply(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) for row in a)


def main():
    prior = native.main()  # fresh whole-seed spectrum and reconstruction checks
    packets = prior['packets']
    labels = tuple(p[0] for p in packets)
    vertices = tuple(native.LABELS)
    registry = {label: (s, t) for label, s, t in packets}
    I4, I6, Z6 = eye(4), eye(6), zeros(6)
    add, sub, scale, mm, transpose = native.add, native.sub, native.scale, native.mm, native.transpose

    # B copies a vertex coefficient to its outgoing occurrences; H aggregates
    # occurrence coefficients at their target vertices. Both are actual 0/1 incidence.
    B = tuple(tuple(F(s == v) for v in vertices) for _, s, _ in packets)  # 6x4
    H = tuple(tuple(F(t == v) for _, _, t in packets) for v in vertices)  # 4x6
    M = mm(H, B)
    K = mm(B, H)
    assert M == prior['matrix'] == native.incidence(packets)
    assert K == tuple(tuple(F(ta == sb) for _, _, ta in packets) for _, sb, _ in packets)
    assert rank(B) == rank(H) == rank(K) == rank(M) == 4
    assert mm(H, K) == mm(M, H)
    assert mm(K, B) == mm(B, M)
    assert sum(sum(row) for row in K) == 10

    primitive = {((s, t, label),) for label, s, t in packets}
    actual_paths = compose(primitive, primitive)
    table_words = {(p[0][2], p[1][2]) for p in actual_paths}
    matrix_words = {(labels[a], labels[b]) for a, b in product(range(6), repeat=2) if K[b][a]}
    assert matrix_words == table_words and len(table_words) == 10
    # The matrix can recover these words only with its retained ordered labels
    # and registry. Keep endpoint-bearing path rows, not just ten scalar ones.
    path_records = tuple(sorted(actual_paths))
    assert all(registry[p[0][2]][1] == registry[p[1][2]][0] for p in path_records)

    # Separate retained continuation records from their final-occurrence summary.
    # L copies an input coefficient to each of its admitted labelled extensions;
    # A sums complete path coefficients by their final primitive occurrence.
    ordered_words = tuple((p[0][2], p[1][2]) for p in path_records)
    L = tuple(tuple(F(first == label) for label in labels) for first, _ in ordered_words)  # 10x6
    A = tuple(tuple(F(last == label) for _, last in ordered_words) for label in labels)  # 6x10
    assert mm(A, L) == K
    assert rank(L) == 6 and rank(A) == 6
    extension_counts = tuple(sum(row[i] for row in L) for i in range(6))
    assert extension_counts == (2, 1, 2, 2, 1, 2)
    # A rational averaging decoder on im(L); it does not change the lift's
    # preparation or normalize its output norm. Its image check rejects
    # independently changed extension coefficients.
    L_decode = tuple(tuple(L[row][i] / extension_counts[i] for row in range(10)) for i in range(6))
    assert mm(L_decode, L) == I6
    image_projection = mm(L, L_decode)
    assert mm(image_projection, image_projection) == image_projection
    assert rank(image_projection) == 6
    assert mm(transpose(L), L) == tuple(tuple(extension_counts[i] if i == j else F(0)
                                             for j in range(6)) for i in range(6))

    def decode_lift(coefficients):
        if len(coefficients) != 10:
            raise ValueError('Ten retained path coefficients required')
        recovered = apply(L_decode, coefficients)
        if apply(L, recovered) != tuple(coefficients):
            raise ValueError('Path coefficients are outside the unchanged-extension image')
        return recovered

    # Full path coefficients have a four-dimensional aggregation kernel. Only
    # two of those cancellation directions are reachable from this lift.
    assert 10 - rank(A) == 4
    assert 6 - rank(mm(A, L)) == 2
    for i in range(6):
        input_basis = tuple(F(i == j) for j in range(6))
        retained = apply(L, input_basis)
        assert decode_lift(retained) == input_basis
        assert apply(A, retained) == apply(K, input_basis)
    arbitrary = tuple(F(i - 3, 7) for i in range(6))
    assert decode_lift(apply(L, arbitrary)) == arbitrary
    complex_input = tuple((F(i - 2, 7), F(i % 3 - 1, 5)) for i in range(6))
    assert rec.apply(sp.zreal(L_decode), rec.apply(sp.zreal(L), complex_input)) == complex_input
    rec.reject(lambda: decode_lift((F(0),) * 9))
    off_image = [F(0)] * 10
    off_image[next(i for i, (first, _) in enumerate(ordered_words) if first == 'AB')] = F(1)
    rec.reject(lambda: decode_lift(tuple(off_image)))

    # Reconstruction of the original formal occurrence record from the first
    # path component must use its retained ID/endpoints, not just amplitudes.
    recovered_registry = {p[0][2]: p[0][:2] for p in path_records}
    assert recovered_registry == registry  # no sinks in this particular seed
    assert tuple((label, *recovered_registry[label]) for label in labels) == packets

    # The known M polynomial yields an exact inverse. No reference inverse is
    # inserted here; this is an inverse of this finite incidence fixture only.
    assert native.power(M, 4) == add(add(native.power(M, 2), scale(M, 2)), I4)
    M_inverse = sub(sub(native.power(M, 3), M), scale(I4, 2))
    assert mm(M_inverse, M) == mm(M, M_inverse) == I4
    F_active = mm(B, mm(M_inverse, H))
    P_zero = sub(I6, F_active)
    assert mm(F_active, F_active) == F_active and trace(F_active) == 4
    assert mm(P_zero, P_zero) == P_zero and rank(P_zero) == trace(P_zero) == 2
    assert mm(K, P_zero) == mm(P_zero, K) == Z6
    assert mm(H, P_zero) == zeros(4, 6)
    assert F_active != transpose(F_active)  # oblique, not counting-metric orthogonal

    # Independent contrasts between arrows entering the same vertex.
    basis6 = tuple(tuple(F(i == j) for j in range(6)) for i in range(6))
    kernel_vectors = (tuple(F(label == 'CA') - F(label == 'BA') for label in labels),
                      tuple(F(label == 'AB') - F(label == 'DB') for label in labels))
    assert rank(kernel_vectors) == 2
    path_contrast_profiles = []
    for v in kernel_vectors:
        assert apply(H, v) == (F(0),) * 4 and apply(K, v) == (F(0),) * 6
        assert apply(P_zero, v) == v
        lifted_contrast = apply(L, v)
        assert lifted_contrast != (F(0),) * 10
        assert decode_lift(lifted_contrast) == v
        assert apply(A, lifted_contrast) == (F(0),) * 6
        path_contrast_profiles.append({' '.join(path): str(value) for path, value in zip(ordered_words, lifted_contrast) if value})
    assert rank(tuple(apply(L, v) for v in kernel_vectors)) == 2
    assert rank(mm(L, P_zero)) == 2
    assert mm(A, mm(L, P_zero)) == Z6
    for x in basis6 + (tuple(F(i - 3, 7) for i in range(6)),):
        z = apply(M_inverse, apply(H, x))
        residual = apply(P_zero, x)
        assert tuple(a + b for a, b in zip(apply(B, z), residual)) == x
        assert apply(K, x) == apply(B, apply(M, z))

    # Iterate retained extension, not the coarse operator as a substitute for
    # it. Each stage admits arbitrary coefficients on its CURRENT path domain;
    # the composite lift of six initial coefficients has only a six-dimensional
    # image even as the ambient path domain grows.
    current_paths = tuple(((s, t, label),) for label, s, t in packets)
    summarize = I6
    composite_lift = I6
    composite_decode = I6
    K_power = I6
    tower = [{'word_length': 1, 'retained_paths': 6, 'primitive_lift_rank': 6,
              'coarse_primitive_response_rank': 6}]
    for length in range(2, 7):
        next_paths = tuple(sorted(compose(set(current_paths), primitive)))
        J = tuple(tuple(F(child[:-1] == parent) for parent in current_paths) for child in next_paths)
        counts = tuple(sum(row[i] for row in J) for i in range(len(current_paths)))
        assert all(count > 0 for count in counts)  # this seed has no sinks
        D = tuple(tuple(J[row][i] / counts[i] for row in range(len(next_paths)))
                  for i in range(len(current_paths)))
        assert mm(D, J) == eye(len(current_paths))
        next_summary = tuple(tuple(F(path[-1][2] == label) for path in next_paths) for label in labels)
        # This is an equality on the full CURRENT path space, not only the
        # six-dimensional subspace generated from initial primitive payloads.
        assert mm(next_summary, J) == mm(K, summarize)
        composite_lift = mm(J, composite_lift)
        composite_decode = mm(composite_decode, D)
        K_power = mm(K, K_power)
        assert mm(composite_decode, composite_lift) == I6
        assert mm(next_summary, composite_lift) == K_power
        assert rank(composite_lift) == 6 and rank(K_power) == 4
        assert rank(mm(composite_lift, P_zero)) == 2
        assert mm(next_summary, mm(composite_lift, P_zero)) == Z6
        if length == 2:
            assert next_paths == path_records and J == L and next_summary == A
        # Every parent record is literally the child's retained prefix; no
        # inverse-arrow equation or erasure of a traversed return is introduced.
        assert {child[:-1] for child in next_paths} == set(current_paths)
        tower.append({'word_length': length, 'retained_paths': len(next_paths),
                      'extension_rank': len(current_paths),
                      'primitive_lift_rank': 6, 'coarse_primitive_response_rank': 4,
                      'zero_sector_retained_rank': 2,
                      'extension_summary_square_commutes': True})
        current_paths, summarize = next_paths, next_summary
    assert [step['retained_paths'] for step in tower] == [6, 10, 16, 26, 42, 68]

    # Observation audit: preserve the existing source-indexed families before
    # aggregating by target. This changes readout resolution, not the state.
    source_groups = native.group(packets, 1)
    assert set(native.unpack(source_groups)) == set(packets)
    selectors = {}
    for vertex, members in source_groups:
        member_labels = {record[0] for record in members}
        selectors[vertex] = tuple(tuple(F(i == j and labels[i] in member_labels) for j in range(6))
                                  for i in range(6))
    assert sum(len(members) for _, members in source_groups) == 6
    total_selector = Z6
    for selector in selectors.values():
        total_selector = add(total_selector, selector)
    assert total_selector == I6

    O_source_target = tuple(row for vertex in vertices for row in mm(H, selectors[vertex]))
    assert len(O_source_target) == 16 and rank(O_source_target) == 6
    # On this primitive registry every (source,target) pair names at most one
    # occurrence. Hence the six supported entries form an explicit decoder.
    O_decode = transpose(O_source_target)
    assert mm(O_decode, O_source_target) == I6
    collapse_source = tuple(tuple(F(column % 4 == target_index) for column in range(16))
                            for target_index in range(4))
    assert mm(collapse_source, O_source_target) == H
    assert rank(mm(O_source_target, P_zero)) == 2
    assert rank(mm(O_source_target, K)) == 4
    assert mm(mm(O_source_target, K), P_zero) == zeros(16, 6)

    def indexed_profile(vector):
        # Source grouping retains the IDs; use them, not the groups' iteration
        # position, when associating numerical payloads with records.
        payload = dict(zip(labels, vector))
        return tuple(sum((payload[label] for label, _, endpoint in members if endpoint == target_vertex), F(0))
                     for _, members in source_groups for target_vertex in vertices)

    def decode_profile(profile):
        if len(profile) != 16:
            raise ValueError('Expected source-major four-by-four profile')
        recovered = apply(O_decode, profile)
        if apply(O_source_target, recovered) != tuple(profile):
            raise ValueError('Profile has coefficients outside the retained primitive support')
        return recovered

    profiles = []
    for contrast in kernel_vectors:
        measured = indexed_profile(contrast)
        assert measured == apply(O_source_target, contrast)
        assert measured != (F(0),) * 16
        assert decode_profile(measured) == contrast
        assert apply(collapse_source, measured) == (F(0),) * 4
        assert indexed_profile(apply(K, contrast)) == (F(0),) * 16
        profiles.append({f'{s}->{t}': str(measured[4 * i + j])
                         for i, s in enumerate(vertices) for j, t in enumerate(vertices)
                         if measured[4 * i + j]})
    for x in basis6 + (tuple(F(i - 3, 7) for i in range(6)),):
        assert indexed_profile(x) == apply(O_source_target, x)
        assert decode_profile(indexed_profile(x)) == x
        assert apply(collapse_source, indexed_profile(x)) == apply(H, x)
        # Hx and H(x+k) coincide, but retained source-resolved readings differ.
        x_with_contrast = tuple(a + b for a, b in zip(x, kernel_vectors[0]))
        assert apply(H, x_with_contrast) == apply(H, x)
        assert indexed_profile(x_with_contrast) != indexed_profile(x)
        assert indexed_profile(apply(K, x_with_contrast)) == indexed_profile(apply(K, x))
    complex_x = tuple((F(i - 2, 7), F(i % 3 - 1, 5)) for i in range(6))
    assert rec.apply(sp.zreal(O_decode), rec.apply(sp.zreal(O_source_target), complex_x)) == complex_x

    # Indexed observation is not equivalent to actually discarding all but one
    # source sector before applying K. These noncommutations delimit the scope.
    noncommuting_sources = [v for v in vertices if mm(K, selectors[v]) != mm(selectors[v], K)]
    assert noncommuting_sources
    assert any(mm(mm(H, selector), P_zero) != zeros(4, 6) for selector in selectors.values())

    # The absence of parallel primitive arrows is essential to coefficient
    # recovery from endpoint cells alone. A retained duplicate-ID control breaks
    # injectivity, while leaving its provenance explicitly distinct.
    parallel_packets = packets + (('AB:separate-occurrence', 'A', 'B'),)
    O_parallel = tuple(tuple(F(s == from_vertex and t == to_vertex) for _, s, t in parallel_packets)
                       for from_vertex in vertices for to_vertex in vertices)
    parallel_contrast = tuple(F(i == 0) - F(i == 6) for i in range(7))
    assert rank(O_parallel) == 6
    assert apply(O_parallel, parallel_contrast) == (F(0),) * 16
    assert parallel_packets[0][0] != parallel_packets[-1][0]
    rec.reject(lambda: decode_profile((F(0),) * 15))
    forged_profile = [F(0)] * 16
    forged_profile[0] = F(1)  # no primitive A->A edge in this registry
    rec.reject(lambda: decode_profile(tuple(forged_profile)))

    # Lift the already checked four vertex eigenprojectors, exactly in their
    # original quadratic fields: E_edge = B * lambda^-1 * E_vertex * H.
    lifted = []
    for radicand, eigenvalue, vertex_projector in prior['modes']:
        a, b = eigenvalue
        denominator = a * a - radicand * b * b
        assert denominator != 0
        inverse = (a / denominator, -b / denominator)
        raw = tuple(mm(B, mm(part, H)) for part in vertex_projector)
        edge_projector = native.rscale(raw, *inverse, radicand)
        assert native.rmul(edge_projector, edge_projector, radicand) == edge_projector
        assert (trace(edge_projector[0]), trace(edge_projector[1])) == (F(1), F(0))
        assert native.rmul((K, Z6), edge_projector, radicand) == native.rscale(edge_projector, a, b, radicand)
        assert native.rmul(edge_projector, (K, Z6), radicand) == native.rscale(edge_projector, a, b, radicand)
        for part in edge_projector:
            assert mm(P_zero, part) == mm(part, P_zero) == Z6
        lifted.append((radicand, eigenvalue, edge_projector))
    for i, (d, _, E) in enumerate(lifted):
        for j, (e, _, Fp) in enumerate(lifted):
            if i == j:
                continue
            if d == e:
                assert native.rmul(E, Fp, d) == (Z6, Z6)
            else:
                # Distinct even/odd sectors annihilate coefficientwise, so no
                # approximate eigensolver or implicit field identification.
                assert all(mm(a, b) == Z6 for a in E for b in Fp)
    total = Z6
    synthesized = Z6
    for radicand in (5, -3):
        channel_sum = (Z6, Z6)
        weighted = (Z6, Z6)
        for d, eigenvalue, E in lifted:
            if d == radicand:
                channel_sum = native.radd(channel_sum, E)
                weighted = native.radd(weighted, native.rscale(E, *eigenvalue, d))
        assert channel_sum[1] == weighted[1] == Z6
        total = add(total, channel_sum[0])
        synthesized = add(synthesized, weighted[0])
    assert total == F_active
    assert add(total, P_zero) == I6 and synthesized == K
    # The two zero directions require their whole eigenspace projector; no
    # canonical rank-one split of that degenerate sector is claimed.

    # Reuse local spectral records to diagnose mixing, with conventions aligned.
    words = (('AB', 'BC', 'CA'), ('BA', 'AD', 'DB'))
    assert labels == sum(words, ())
    ledger = sp.SpectralLedger()
    local = {}
    local_incoming = Z6
    for side, word in enumerate(words):
        root = ledger.record4(tuple(sp.TwoPacket(label, *registry[label]) for label in word))
        C = ledger.validate_root(root)
        incoming = transpose(C)
        rows = [list(row) for row in local_incoming]
        for i, j in product(range(3), repeat=2):
            rows[3 * side + i][3 * side + j] = incoming[i][j]
        local_incoming = tuple(tuple(row) for row in rows)
        for mode in rec.MODES:
            identity_record = ledger.promote(root, mode)
            E = [list(row) for row in sp.zreal(Z6)]
            for i, j in product(range(3), repeat=2):
                E[3 * side + i][3 * side + j] = identity_record.projector[i][j]
            E = tuple(tuple(row) for row in E)
            local[side, mode] = E
            assert tuple(p.label for p in ledger.deconstruct(identity_record)) == word
    cross = sub(K, local_incoming)
    assert {(labels[a], labels[b]) for a, b in product(range(6), repeat=2) if cross[b][a]} == {
        ('AB', 'BA'), ('BA', 'AB'), ('CA', 'AD'), ('DB', 'BC')}
    mixing = []
    Kc = sp.zreal(K)
    for key, E in local.items():
        side, mode = key
        # Earlier row-successor eigenvalue is conjugated for the incoming block.
        assert sp.zmm(sp.zreal(local_incoming), E) == sp.zmscale(E, sp.zconj(sp.MODES[mode]))
        outside = sp.zmadd(sp.zreal(I6), sp.zmscale(E, (F(-1), F(0))))
        assert sp.zmm(outside, sp.zmm(Kc, E)) != sp.zreal(Z6)
        destinations = [other for other, Fp in local.items() if sp.zmm(Fp, sp.zmm(Kc, E)) != sp.zreal(Z6)]
        assert destinations == [other for other in local if other == key or other[0] != side]
        mixing.append({'input': key, 'nonzero_output_local_channels': destinations})
    assert K != transpose(K) and mm(K, transpose(K)) != mm(transpose(K), K)

    report = {
        'status': 'passed',
        'convention': 'column incoming; K[b,a]=1 iff target(a)=source(b)',
        'factorization': {'B': '6x4 source lift', 'H': '4x6 target aggregation', 'M': 'H B', 'K': 'B H'},
        'rank': {'B': 4, 'H': 4, 'M': 4, 'K': 4},
        'retained_path_factorization': {
            'identity': 'K=A L',
            'L': '10x6 unchanged coefficient extension to all admitted two-step words',
            'A': '6x10 aggregation by final occurrence',
            'ranks': {'L': 6, 'A': 6, 'A_L': 4},
            'extension_counts_in_packet_order': [int(n) for n in extension_counts],
            'decoder': 'diag(extension_counts)^-1 L^T, valid on im(L)',
            'L_decode_L_identity': True,
            'arbitrary_path_coefficients_not_assumed_in_image': True,
            'aggregation_kernel_dimension': 4,
            'aggregation_kernel_intersection_lift_image_dimension': 2,
            'nonzero_retained_contrast_profiles': path_contrast_profiles,
            'zero_sector_survives_L_and_is_killed_by_A': True,
            'not_norm_preserving': True,
            'source_registry_and_original_order_recovered': True,
            'negative_controls': ['wrong path coefficient count', 'off-image unequal sibling extensions'],
            'scope': 'retained possible continuations and explicit coefficient-copying convention; no executed event schedule'}, 
        'retained_extension_tower': tower,
        'tower_scope': 'fresh bounded prefix-retention and summary squares through word length six; possible paths, not executed events',
        'two_step_words': sorted(table_words),
        'occurrence_eigenvalues': ['0 (multiplicity 2)', '(1+sqrt(5))/2', '(1-sqrt(5))/2',
                                  '(-1+i*sqrt(3))/2', '(-1-i*sqrt(3))/2'],
        'zero_sector_contrasts': ['CA-BA', 'AB-DB'],
        'source_indexed_observation': {
            'coarse_H_rank': 4,
            'source_resolved_target_profile_rank': 6,
            'zero_sector_visible_rank': 2,
            'profile_after_applying_K_rank': 4,
            'contrast_profiles': profiles,
            'decoder': 'transpose(O) on the six supported source-target cells; O^T O=I6',
            'forget_source_recovers_H': True,
            'indexed_profiles_recover_rational_and_complex_coefficients': True,
            'source_selection_noncommutes_with_K': noncommuting_sources,
            'parallel_occurrence_control': {'occurrences': 7, 'observation_rank': 6,
                                            'equal_endpoint_occurrence_contrast_invisible': True},
            'negative_controls': ['wrong profile length', 'payload on absent primitive endpoint cell'],
            'scope': 'source-indexed observation of retained coefficients, not inversion of K or physical measurement authority'}, 
        'active_projector': 'B M^-1 H; rank 4; non-orthogonal in counting metric',
        'retained_decode': 'x=B z+k, z=M^-1 H x, k=(I-B M^-1 H)x',
        'spectral_reconstruction': 'sum(nonzero E_lambda)+P_zero=I6; sum(lambda E_lambda)=K',
        'local_mode_mixing': mixing,
        'scope': 'source incidence representation with unit entries; not physical dynamics, norm conservation, or a rung identity',
        'not_claimed': ['native seed-arrow equivalences', 'path history recovery from eigenvalues alone',
                        'canonical basis in the degenerate zero eigenspace', 'finite raw-operator return'],
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'whole-seed-occurrence-spectrum.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: six-occurrence continuation factors through the existing four-vertex incidence matrix.')
    print('PASS: four nonzero eigenmodes lift exactly; two zero directions retained; full spectral reconstruction.')
    print('PASS: every isolated local triangle mode mixes under glued continuation; all ten path words retained.')
    print('PASS: source-resolved target readings have rank 6 and recover both contrasts invisible to H.')
    print('PASS: after K is applied the same reader has rank 4; reindexing cannot restore erased coefficients.')
    print('PASS: K=A L with injective six-to-ten retained path lift and an exact image decoder.')
    print('PASS: both zero contrasts survive in distinct path records and cancel only under final-occurrence aggregation.')
    print('PASS: injective prefix extension and commuting coarse-summary squares through word length six (68 paths).')
    print('BOUNDARY: incidence representation, not physical time evolution or norm-preserving dynamics.')
    print('Report: research/nima/results/whole-seed-occurrence-spectrum.json')
    return {'packets': packets, 'continuation': K, 'nonzero_modes': tuple(lifted),
            'zero_projector': P_zero}


if __name__ == '__main__':
    main()
