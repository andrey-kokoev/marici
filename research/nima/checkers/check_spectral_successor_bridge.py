"""Conditional bridge: retained spectral pair -> independent record comparison.

The existing structural constructor is reused unchanged. Numerical payloads use
its explicitly declared free bilinear extension e_a,e_b -> e_(a,b). This is not
a recovered physical response law or source selection of independent pairing.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import check_record4_spectral_promotion as sp
import check_spectral_successor_many_many as rec
import check_recursive_independent_comparison as rc


def tensor_vector(a, b):
    return tuple(sp.zmul(x, y) for x in a for y in b)


def sum_vectors(vectors, dimension):
    result = (rec.Z,) * dimension
    for vector in vectors:
        result = tuple(sp.zadd(a, b) for a, b in zip(result, vector))
    return result


def scalar_sum(vector):
    result = rec.Z
    for value in vector:
        result = sp.zadd(result, value)
    return result


def mean(vector):
    return sp.zscale(scalar_sum(vector), F(1, len(vector)))


@dataclass(frozen=True)
class Packet:
    parent_ids: tuple
    pair_manifest: tuple
    components: tuple


@dataclass(frozen=True)
class Successor:
    left: Packet
    right: Packet
    records: tuple
    # Each component is factored to retain spectral channels without constructing
    # 81 dense 81x81 projector matrices.
    channel_products: tuple


@dataclass(frozen=True)
class EndpointSelection:
    parent: Successor
    admitted: tuple
    excluded: tuple


def main():
    ledger = sp.SpectralLedger()
    words = (('AB', 'BC', 'CA'), ('BA', 'AD', 'DB'))
    roots = tuple(ledger.record4(tuple(sp.TwoPacket(e, e[0], e[1]) for e in word))
                  for word in words)
    ports = tuple(tuple(ledger.promote(root, mode) for mode in rec.MODES) for root in roots)
    parent_ids = tuple(tuple(port.label for port in side) for side in ports)
    manifest = tuple(product(*words))
    projectors = {(a.mode, b.mode): rec.kron(a.projector, b.projector)
                  for a in ports[0] for b in ports[1]}
    assert rec.matrix_sum(projectors.values()) == rec.IDENTITY
    D = rec.matrix_sum(projectors[m, m] for m in rec.MODES)
    R = rec.matrix_sum(projectors[key] for key in rec.KEYS if key[0] != key[1])

    # Endpoint tuples come from the actual occurrences, NOT assigned A->A.
    input_records = {pair: rc.Record(tuple(e[0] for e in pair), tuple(e[1] for e in pair))
                     for pair in manifest}
    next_records, family_parents = rc.compare_families(input_records, level=1)
    output_manifest = tuple(a + b for a, b in product(manifest, repeat=2))
    assert len(next_records) == len(output_manifest) == 81
    assert set(next_records) == set(output_manifest)
    for a, b in product(manifest, repeat=2):
        row = next_records[a + b]
        assert row.parents == (a, b)
        assert row.source == input_records[a].source + input_records[b].source
        assert row.target == input_records[a].target + input_records[b].target
    output_rows = tuple((key, next_records[key]) for key in output_manifest)
    input_families = rc.promote(input_records, level=1)
    output_families = rc.promote(next_records, level=2)
    assert len(input_families) == 9 and all(len(f) == 1 for f in input_families.values())
    assert len(output_families) == 81 and all(len(f) == 1 for f in output_families.values())
    assert len(family_parents) == 81

    # Literal composition in the product endpoint category: each of the two
    # primitive legs must compose. This is an explicit operation alternative,
    # not an equivalence of independent comparison and path composition.
    admitted_indices = tuple(k for k, (a, b) in enumerate(product(manifest, repeat=2))
                             if input_records[a].target == input_records[b].source)
    excluded_indices = tuple(k for k in range(81) if k not in admitted_indices)
    assert len(admitted_indices) == 9 and len(excluded_indices) == 72
    adjacency = tuple(tuple(F(input_records[a].target == input_records[b].source)
                            for b in manifest) for a in manifest)
    assert all(sum(row) == 1 for row in adjacency)
    assert all(sum(row) == 1 for row in sp.transpose(adjacency))
    # The mask is derived from endpoint tuples, not fitted to a desired output.
    cycles = tuple(ledger.validate_root(root) for root in roots)
    M = sp.zreal(adjacency)
    assert M == rec.kron(sp.zreal(cycles[0]), sp.zreal(cycles[1]))
    assert sp.zmm(D, sp.zmm(M, R)) == rec.ZERO
    assert sp.zmm(R, sp.zmm(M, D)) == rec.ZERO
    assert sp.zmm(R, sp.zmm(M, R)) != rec.ZERO

    def restrict(vector):
        return tuple(vector[k] for k in admitted_indices)

    def fixed_join_reader(vector):
        # Keep the original candidate measure: no 81->9 renormalization.
        return sp.zscale(scalar_sum(restrict(vector)), F(1, 81))

    # Readers fixed before hostile selection: unit-mass family means and the
    # full aggregate mean. These reuse prior reader conventions, not physical
    # calibration or a source-selected observation of these new records.
    def family_reader(vector):
        values = dict(zip(output_manifest, vector))
        return tuple(mean(tuple(values[key] for key in family))
                     for family in output_families.values())

    def encode(vector):
        if len(vector) != 9:
            raise ValueError('Wrong input coefficient dimension')
        return Packet(parent_ids, manifest,
                      tuple((key, rec.apply(projectors[key], vector)) for key in rec.KEYS))

    def decode(packet):
        if packet.parent_ids != parent_ids:
            raise ValueError('Spectral parents are not bound to this ordered source')
        recovered_words = []
        for side in packet.parent_ids:
            recovered = []
            for mode, label in zip(rec.MODES, side):
                identity = ledger.identities[label]
                if identity.mode != mode:
                    raise ValueError('Wrong mode-parent binding')
                recovered.append(tuple(p.label for p in ledger.deconstruct(identity)))
            if len(set(recovered)) != 1:
                raise ValueError('Parents do not retain one common triangle history')
            recovered_words.append(recovered[0])
        if packet.pair_manifest != tuple(product(*recovered_words)):
            raise ValueError('Wrong occurrence-pair manifest')
        if tuple(key for key, _ in packet.components) != rec.KEYS:
            raise ValueError('Missing or reordered spectral channels')
        for key, component in packet.components:
            if len(component) != 9 or rec.apply(projectors[key], component) != component:
                raise ValueError('Component outside declared mode-pair image')
        return sum_vectors((v for _, v in packet.components), 9)

    def compare_spectral(left, right):
        decode(left)
        decode(right)
        return Successor(left, right, output_rows,
                         tuple(((a, b), (v, w)) for a, v in left.components for b, w in right.components))

    def decode_successor(successor):
        decode(successor.left)
        decode(successor.right)
        expected = compare_spectral(successor.left, successor.right)
        if successor.records != expected.records or successor.channel_products != expected.channel_products:
            raise ValueError('Corrupt output records, parents or channel products')
        return sum_vectors((tensor_vector(v, w) for _, (v, w) in successor.channel_products), 81)

    def select_endpoints(successor):
        values = decode_successor(successor)
        admitted = []
        for k in admitted_indices:
            key = output_manifest[k]
            a, b = next_records[key].parents
            # Composed endpoints have arity two, unlike the independent
            # comparison record's concatenated arity-four endpoints.
            composed = rc.Record(input_records[a].source, input_records[b].target, (a, b))
            admitted.append((key, composed, values[k]))
        excluded = tuple((output_manifest[k], 'endpoint-mismatch', values[k]) for k in excluded_indices)
        return EndpointSelection(successor, tuple(admitted), excluded)

    def recover_selection(selected):
        expected = select_endpoints(selected.parent)
        if selected.admitted != expected.admitted or selected.excluded != expected.excluded:
            raise ValueError('Corrupt endpoint selection or excluded-candidate ledger')
        values = {key: value for key, _, value in selected.admitted + selected.excluded}
        if set(values) != set(output_manifest):
            raise ValueError('Incomplete retained candidate domain')
        return tuple(values[key] for key in output_manifest)

    # Basis-pair tests determine the complete bilinear commuting square.
    basis = tuple(tuple(rec.ONE if i == j else rec.Z for j in range(9)) for i in range(9))
    encoded = tuple(encode(v) for v in basis)
    for i, j in product(range(9), repeat=2):
        direct = tensor_vector(decode(encoded[i]), decode(encoded[j]))
        successor = compare_spectral(encoded[i], encoded[j])
        assert decode_successor(successor) == direct
        # Restriction is linear on the output. Individual restricted spectral
        # terms need not remain orthogonal; compare their SUM, not intensities.
        restricted_spectral = sum_vectors((restrict(tensor_vector(v, w))
                                          for _, (v, w) in successor.channel_products), 9)
        assert restricted_spectral == restrict(direct)
        selected = select_endpoints(successor)
        assert recover_selection(selected) == direct
        assert tuple(value for _, _, value in selected.admitted) == restrict(direct)
        assert all(len(row.source) == len(row.target) == 2 for _, row, _ in selected.admitted)
        # Mask aggregate has DD and RR blocks but no DR or RD cross terms.
        dx, rx = rec.apply(D, basis[i]), rec.apply(R, basis[i])
        dy, ry = rec.apply(D, basis[j]), rec.apply(R, basis[j])
        assert fixed_join_reader(tensor_vector(dx, ry)) == rec.Z
        assert fixed_join_reader(tensor_vector(rx, dy)) == rec.Z
        assert fixed_join_reader(direct) == sp.zadd(
            fixed_join_reader(tensor_vector(dx, dy)), fixed_join_reader(tensor_vector(rx, ry)))
        assert rec.norm2(direct) == rec.norm2(basis[i]) * rec.norm2(basis[j])
        spectral_budget = sum(rec.norm2(v) * rec.norm2(w)
                              for _, (v, w) in successor.channel_products)
        assert spectral_budget == rec.norm2(direct)
        # Aggregate closure under the old same-mode observation is checked on
        # a spanning set of input pairs, not inferred from one selected state.
        reduced = tensor_vector(rec.apply(D, basis[i]), rec.apply(D, basis[j]))
        assert mean(direct) == mean(reduced)
    # Functional certificate for aggregate closure on all complex inputs.
    for v in basis:
        assert scalar_sum(rec.apply(R, v)) == rec.Z

    x = tuple((F(i - 4, 7), F(i % 3 - 1, 5)) for i in range(9))
    y = tuple((F(2 * i + 1, 11), F(i % 2, 3)) for i in range(9))
    sample = compare_spectral(encode(x), encode(y))
    decoded = decode_successor(sample)
    assert decoded == tensor_vector(x, y)
    assert rec.norm2(decoded) == rec.norm2(x) * rec.norm2(y)
    assert sum(rec.norm2(v) * rec.norm2(w) for _, (v, w) in sample.channel_products) == rec.norm2(decoded)
    assert mean(decoded) == sp.zmul(mean(x), mean(y))
    assert mean(decoded) == mean(tensor_vector(rec.apply(D, x), rec.apply(D, y)))

    # Expand ALL four sectors, not merely DD. No residual dynamics is invented.
    d, r = rec.apply(D, x), rec.apply(R, x)
    e, s = rec.apply(D, y), rec.apply(R, y)
    sectors = (tensor_vector(d, e), tensor_vector(d, s), tensor_vector(r, e), tensor_vector(r, s))
    assert sum_vectors(sectors, 81) == decoded
    assert sum(rec.norm2(v) for v in sectors) == rec.norm2(decoded)

    # Same current D-state, different next fine observations. Reading all
    # singleton target families distinguishes a real omitted contribution.
    x_full, x_coarse, y_fixed = basis[0], rec.apply(D, basis[0]), basis[0]
    assert rec.apply(D, x_full) == rec.apply(D, x_coarse)
    out_full, out_coarse = tensor_vector(x_full, y_fixed), tensor_vector(x_coarse, y_fixed)
    difference = tuple(sp.zadd(a, sp.zscale(b, -1)) for a, b in zip(out_full, out_coarse))
    assert family_reader(out_full) != family_reader(out_coarse)
    assert rec.norm2(difference) == F(2, 3)
    assert mean(out_full) == mean(out_coarse)

    # The bilateral operation is not an injective decoder of its parents:
    # (2x,y/2) gives the same product. Full parent packets must remain retained.
    x2 = tuple(sp.zscale(v, 2) for v in x)
    y2 = tuple(sp.zscale(v, F(1, 2)) for v in y)
    scaled = compare_spectral(encode(x2), encode(y2))
    assert decode_successor(scaled) == decoded
    assert scaled.left != sample.left and scaled.right != sample.right
    assert decode(sample.left) == x and decode(sample.right) == y

    rec.reject(lambda: decode_successor(replace(sample, records=sample.records[:-1])))
    rec.reject(lambda: decode_successor(replace(sample, channel_products=sample.channel_products[:-1])))
    rec.reject(lambda: compare_spectral(replace(sample.left, components=sample.left.components[:-1]), sample.right))
    rec.reject(lambda: compare_spectral(replace(sample.left, parent_ids=()), sample.right))
    bad_rows = ((sample.records[0][0], replace(sample.records[0][1], parents=())),) + sample.records[1:]
    rec.reject(lambda: decode_successor(replace(sample, records=bad_rows)))

    # Fixed preparations, coefficients and reader; only incidence changes.
    join_next = next(j for j in range(9) if adjacency[0][j])
    assert join_next == 4  # (AB,BA) can be followed by (BC,AD).
    first, second = basis[0], basis[join_next]
    first_coarse = rec.apply(D, first)
    assert rec.apply(D, first) == rec.apply(D, first_coarse)
    independent_full = tensor_vector(first, second)
    independent_coarse = tensor_vector(first_coarse, second)
    assert mean(independent_full) == mean(independent_coarse) == (F(1, 81), F(0))
    join_full = fixed_join_reader(independent_full)
    join_coarse = fixed_join_reader(independent_coarse)
    assert join_full == (F(1, 81), F(0))
    assert join_coarse == (F(1, 243), F(0))
    assert sp.zadd(join_full, sp.zscale(join_coarse, -1)) == (F(2, 243), F(0))
    assert mean(restrict(independent_full)) == (F(1, 9), F(0))
    assert mean(restrict(independent_coarse)) == (F(1, 27), F(0))
    # A nonzero entirely hidden pair also has a nonzero joined aggregate.
    hidden_left = rec.apply(R, basis[0])
    hidden_right = rec.apply(sp.dagger(M), hidden_left)
    assert rec.apply(D, hidden_left) == rec.apply(D, hidden_right) == (rec.Z,) * 9
    assert fixed_join_reader(tensor_vector(hidden_left, hidden_right)) == (F(2, 243), F(0))
    assert mean(tensor_vector(hidden_left, hidden_right)) == rec.Z

    selected_sample = select_endpoints(sample)
    assert recover_selection(selected_sample) == decoded
    assert sum_vectors((restrict(v) for v in sectors), 9) == restrict(decoded)
    assert rec.norm2(restrict(decoded)) + rec.norm2(tuple(decoded[k] for k in excluded_indices)) == rec.norm2(decoded)
    rec.reject(lambda: recover_selection(replace(selected_sample, excluded=selected_sample.excluded[:-1])))
    rec.reject(lambda: recover_selection(replace(selected_sample, admitted=selected_sample.admitted[:-1])))
    changed = ((selected_sample.admitted[0][0], replace(selected_sample.admitted[0][1], target=('wrong',)),
                selected_sample.admitted[0][2]),) + selected_sample.admitted[1:]
    rec.reject(lambda: recover_selection(replace(selected_sample, admitted=changed)))

    # Contextual observation profiles. Columns are input coefficient directions;
    # each row is a fixed, independently labelled probe, not a fitted reader.
    full_probes = basis
    visible_probes = tuple(rec.apply(D, v) for v in basis)
    residual_probes = tuple(rec.apply(R, v) for v in basis)

    def observation_matrix(probes):
        return tuple(tuple(fixed_join_reader(tensor_vector(v, probe)) for v in basis)
                     for probe in probes)

    def observation_profile(vector, probes):
        return tuple(fixed_join_reader(tensor_vector(vector, probe)) for probe in probes)

    def rational_rank(matrix):
        # These profiles are rational even though the state carrier is complex.
        # Rational rank equals their rank over the complex coefficient field.
        assert all(z[1] == 0 for row in matrix for z in row)
        rows = [[z[0] for z in row] for row in matrix]
        pivot_row = 0
        for col in range(len(rows[0])):
            pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
            if pivot is None:
                continue
            rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
            value = rows[pivot_row][col]
            rows[pivot_row] = [entry / value for entry in rows[pivot_row]]
            for i in range(len(rows)):
                if i != pivot_row:
                    value = rows[i][col]
                    rows[i] = [entry - value * p for entry, p in zip(rows[i], rows[pivot_row])]
            pivot_row += 1
            if pivot_row == len(rows):
                break
        return pivot_row

    O_full = observation_matrix(full_probes)
    O_visible = observation_matrix(visible_probes)
    O_residual = observation_matrix(residual_probes)
    assert O_full == sp.zmscale(sp.transpose(M), (F(1, 81), F(0)))
    assert O_visible == sp.zmm(O_full, D)
    assert O_residual == sp.zmm(O_full, R)
    assert sp.zmadd(O_visible, O_residual) == O_full
    assert rational_rank(O_full) == 9
    assert rational_rank(O_visible) == 3
    assert rational_rank(O_residual) == 6
    assert len(set(visible_probes)) == 3  # nine labelled probes span three directions
    assert rational_rank(observation_matrix(tuple(dict.fromkeys(visible_probes)))) == 3

    # Exact all-input decoder certificates: same decoder applied to a restricted
    # profile recovers only the corresponding projection, not the full state.
    decoder = sp.zmscale(M, (F(81), F(0)))
    assert sp.zmm(decoder, O_full) == rec.IDENTITY
    assert sp.zmm(decoder, O_visible) == D
    assert sp.zmm(decoder, O_residual) == R
    assert sp.zmm(O_visible, R) == rec.ZERO
    assert sp.zmm(O_residual, D) == rec.ZERO
    for v in basis + (x, y, hidden_left):
        for probes, observation, projection in (
                (full_probes, O_full, rec.IDENTITY),
                (visible_probes, O_visible, D),
                (residual_probes, O_residual, R)):
            measured = observation_profile(v, probes)
            assert measured == rec.apply(observation, v)
            assert rec.apply(decoder, measured) == rec.apply(projection, v)
        assert observation_profile(v, visible_probes) == observation_profile(rec.apply(D, v), visible_probes)
    assert observation_profile(hidden_left, visible_probes) == (rec.Z,) * 9
    assert observation_profile(hidden_left, full_probes) != (rec.Z,) * 9

    # Removing ANY one of the nine independent basis probes leaves an explicit
    # invisible coefficient direction. No probability/noise claims enter this.
    for missing in range(9):
        keep = tuple(probe for j, probe in enumerate(full_probes) if j != missing)
        assert rational_rank(observation_matrix(keep)) == 8
        missing_input = next(i for i in range(9) if adjacency[i][missing])
        undetected = basis[missing_input]
        assert observation_profile(undetected, keep) == (rec.Z,) * 8
        assert observation_profile(undetected, full_probes)[missing] == (F(1, 81), F(0))

    # Correct probe labels/calibration are part of the decoder contract. A
    # swapped response list, decoded as if unswapped, produces a different state.
    original_profile = observation_profile(basis[0], full_probes)
    swap_i = next(i for i, value in enumerate(original_profile) if value != rec.Z)
    swap_j = (swap_i + 1) % 9
    permuted = list(original_profile)
    permuted[swap_i], permuted[swap_j] = permuted[swap_j], permuted[swap_i]
    assert rec.apply(decoder, tuple(permuted)) != basis[0]

    report = {
        'status': 'passed',
        'classification': 'conditional independent-family coefficient bridge',
        'input_dimension_per_operand': 9, 'output_dimension': 81,
        'contextual_observation': {
            'reader': 'J(x,y)=x^T M y/81; complex amplitudes, not intensities',
            'full_occurrence_probe_rank': 9, 'full_kernel_dimension': 0,
            'same_mode_probe_rank': 3, 'same_mode_kernel_dimension': 6,
            'residual_probe_rank': 6, 'residual_kernel_dimension': 3,
            'distinct_same_mode_probe_vectors': 3,
            'decoder': '81 M applied to ordered profile; recovers x, Dx, or Rx respectively',
            'all_nine_basis_probe_deletions_reduce_rank_to_eight': True,
            'missing_probe_invisible_directions_checked': 9,
            'probe_label_corruption_control': True,
            'scope': 'linear complex coefficient observability under declared probe preparation and calibration; histories remain separate'}, 
        'input_families': 9, 'output_families': 81, 'all_families_singleton': True,
        'operation': 'B(x,y)=x tensor y: bilinear; self-comparison B(x,x) is quadratic',
        'basis_pairs_checked': 81,
        'endpoint_composition': {
            'admitted': 9, 'excluded_retained': 72, 'composed_endpoint_arity': 2,
            'spectral_reconstruction_square_commutes': True,
            'reader_denominator_fixed': 81,
            'independent_control_full_and_coarse': '1/81',
            'joined_full': '1/81', 'joined_coarse': '1/243', 'difference': '2/243',
            'admitted_only_means_for_comparison': ['1/9', '1/27'],
            'residual_residual_aggregate_nonzero': True,
            'visible_residual_and_residual_visible_aggregates_zero': True,
            'entire_candidate_domain_recoverable': True,
            'selection_negative_controls': ['missing excluded row', 'missing admitted row', 'wrong composed endpoint'],
            'scope': 'conditional endpoint filter in the product category; not a physical choice of successor'},
        'full_spectral_square_commutes': True,
        'all_four_visible_residual_sectors_retained': True,
        'readers': {'unit_mass_family_means': 'Does not factor through D on both parents',
                    'unit_mass_aggregate_mean': 'Factors through D on both parents'},
        'fine_reader_hostile_squared_difference': '2/3',
        'parent_recovery_requires_retained_packets': True,
        'negative_controls': ['missing output row', 'missing channel product', 'missing input mode',
                              'missing history parent', 'forged output parents'],
        'assumptions': ['selected left-right occurrence product as input domain',
                        'independent all-pairs successor chosen for this pilot',
                        'free complex coefficient extension of labelled products',
                        'unit-mass numerical reader conventions'],
        'not_claimed': ['source-selected horizontal generator', 'physical readout',
                        '81 independent outputs from one separable input pair', 'coupled time evolution'],
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'spectral-successor-bridge.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: existing constructor maps 9 input pair records to 81 four-occurrence records.')
    print('PASS: reconstruct/compare and spectral-compare/reconstruct agree on all 81 basis pairs.')
    print('PASS: full parents and residual sectors are recoverable; product values alone do not recover parents.')
    print('READERS: family means see omitted residual; aggregate mean does not.')
    print('PASS: endpoint composition admits 9/81 candidates; all 72 excluded candidates remain recoverable.')
    print('PASS: restricted spectral square commutes; fixed aggregate exposes RR contribution 2/243.')
    print('PASS: contextual observation ranks 9 (full), 3 (same-mode), 6 (residual), with exact decoders.')
    print('PASS: each single basis-probe deletion leaves rank 8 and an explicit invisible direction.')
    print('BOUNDARY: explicit coefficient/reader adapter, not source-selected succession.')
    print('Report: research/nima/results/spectral-successor-bridge.json')


if __name__ == '__main__':
    main()
