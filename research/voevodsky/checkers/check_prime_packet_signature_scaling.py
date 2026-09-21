#!/usr/bin/env python3
"""Exact finite-prime signature ranks; spectral diagnostics use NumPy separately.

uv run --with python-flint --with numpy python research/voevodsky/checkers/check_prime_packet_signature_scaling.py
"""
import itertools
import json
import math
import time
import sys
from fractions import Fraction
from collections import defaultdict
from pathlib import Path

import numpy as np
from flint import fmpz_mat

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/voevodsky'))
from prime_packet_block_parity_observer import BlockParityObserver, observe_mixture


def edge_word(word):
    mask = 0
    out = []
    for j in word:
        out.append((mask, j))
        mask |= 1 << j
    return tuple(out)


def parity(word):
    return (-1)**sum(word[i] > word[j] for i in range(len(word)) for j in range(i+1, len(word)))


def feature_rows(words, degree):
    rows = defaultdict(list)
    for index, ww in enumerate(words):
        for positions in itertools.combinations(range(len(ww)), degree):
            rows[tuple(ww[i] for i in positions)].append(index)
    return rows


def gram_from_rows(rows, n):
    gram = np.zeros((n, n), dtype=np.int64)
    for support in rows.values():
        gram[np.ix_(support, support)] += 1
    return gram


def exact_rank(a):
    return int(fmpz_mat(a.tolist()).rank())


def pivot_columns(a):
    reduced, denominator, rank = fmpz_mat(a.tolist()).rref()
    pivots = []
    for i in range(rank):
        pivots.append(next(j for j in range(a.shape[1]) if reduced[i, j] != 0))
    return pivots


def route_indicator_memory(permutations, selected, d):
    """Typed Hankel certificate for fixed-start/full-route indicator outputs.

    Each selected full word has its own output channel. Prefix columns have disjoint
    suffix/output supports. Picking one witness suffix/output per active prefix
    gives an identity submatrix; the prefix trie supplies the matching upper bound.
    """
    chosen = [permutations[i] for i in selected]
    records = []
    for vertex in range(1 << d):
        length = vertex.bit_count()
        prefixes = {}
        for output, w in enumerate(chosen):
            prefix = w[:length]
            if sum(1 << j for j in prefix) == vertex:
                prefixes.setdefault(prefix, (output, w[length:]))
        active = list(prefixes)
        # Exact identity submatrix of the suffix/output vs prefix Hankel block.
        identity_witness = all(
            int(prefix+suffix == chosen[output]) == int(i == j)
            for i, (output, suffix) in enumerate(prefixes.values())
            for j, prefix in enumerate(active))
        records.append({'vertex': vertex, 'rank': len(active),
                        'identity_minor_verified': identity_witness})
    return {
        'contract': 'Fixed empty start, valid cube paths, selected distinct full-route indicator outputs read at the terminal vertex; vertex retained externally',
        'selected_output_count': len(selected),
        'total_fiber_dimension': sum(r['rank'] for r in records),
        'peak_fiber_dimension': max(r['rank'] for r in records),
        'total_by_layer': [sum(r['rank'] for r in records if r['vertex'].bit_count() == k) for k in range(d+1)],
        'vertices': records,
        'all_hankel_identity_minors_verified': all(r['identity_minor_verified'] for r in records),
    }


def signed_output_memory(permutations, output_ids, coefficients, d):
    records = []
    for vertex in range(1 << d):
        k = vertex.bit_count()
        members = [i for i, w in enumerate(permutations)
                   if sum(1 << j for j in w[:k]) == vertex]
        prefixes = sorted({permutations[i][:k] for i in members})
        pindex = {p: j for j, p in enumerate(prefixes)}
        rows = {}
        for i in members:
            w = permutations[i]
            key = (output_ids[i], w[k:])
            if key not in rows:
                rows[key] = [0]*len(prefixes)
            rows[key][pindex[w[:k]]] = coefficients[i]
        rank = int(fmpz_mat(list(rows.values())).rank())
        # Explicit compressed state: completed unordered positional pairs and
        # the pending first element of the next pair; internal flips carry sign.
        descriptors = {(tuple(tuple(sorted(p[j:j+2])) for j in range(0, k-1, 2)),
                        p[-1] if k % 2 else None) for p in prefixes}
        records.append({'vertex': vertex, 'hankel_rank': rank,
                        'compressed_prefix_state_count': len(descriptors),
                        'minimality_verified': rank == len(descriptors)})
    return {'contract': 'Fixed empty start and terminal signed block-parity outputs; trusted endpoints',
            'total_fiber_dimension': sum(r['hankel_rank'] for r in records),
            'peak_fiber_dimension': max(r['hankel_rank'] for r in records),
            'total_by_layer': [sum(r['hankel_rank'] for r in records if r['vertex'].bit_count() == k)
                               for k in range(d+1)],
            'vertices': records,
            'all_minimality_checks': all(r['minimality_verified'] for r in records)}


results = []
for d in (4, 5, 6):
    start = time.monotonic()
    permutations = list(itertools.permutations(range(d)))
    words = [edge_word(w) for w in permutations]
    n = len(words)
    minimum_order = d//2
    cumulative = np.zeros((n, n), dtype=np.int64)
    degree_rows = []
    all_rows = {}
    grams = {}
    signs = [parity(w) for w in permutations]
    for degree in range(1, minimum_order+1):
        rows = feature_rows(words, degree)
        all_rows[degree] = rows
        degree_gram = gram_from_rows(rows, n)
        cumulative += degree_gram
        grams[degree] = cumulative.copy()
        pure_rank = exact_rank(degree_gram)
        cumulative_rank = exact_rank(cumulative)
        eigenvalues = np.linalg.eigvalsh(cumulative.astype(float))
        positive = eigenvalues[eigenvalues > 1e-7]
        annihilates_parity = all(sum(signs[j] for j in support) == 0 for support in rows.values())
        degree_rows.append({
            'degree': degree, 'feature_count': len(rows),
            'pure_degree_rank': pure_rank, 'cumulative_rank': cumulative_rank,
            'nullity': n-cumulative_rank,
            'parity_collision': annihilates_parity,
            'smallest_positive_gram_eigenvalue_numeric': float(positive[0]),
            'largest_gram_eigenvalue_numeric': float(positive[-1]),
            'nonzero_singular_condition_number_numeric': float(np.sqrt(positive[-1]/positive[0])),
            'condition_scope': 'Euclidean route coefficients and unscaled complete degree-1-through-k signature rows; finite floating spectral diagnostic',
        })
        print(f'd={d} k={degree}: rows={len(rows)} rank={cumulative_rank}/{n}', flush=True)

    # A minimal-order coordinate subfamily already identifies every route.
    selected_positions = tuple(range(1, d, 2))  # 1-indexed positions 2,4,...
    selected = [tuple(w[i] for i in selected_positions) for w in words]
    selected_unique = len(set(selected)) == n
    selected_supports = feature_rows(words, minimum_order)
    selected_is_identity = all(selected_supports[key] == [j] for j, key in enumerate(selected))

    completion = None
    block_kernel = None
    if d == 5:
        # Independent columns of the edge Gram identify the complementary
        # coordinate readouts needed to complete its nullspace.
        pivots = set(pivot_columns(grams[1]))
        chosen_indices = [i for i in range(n) if i not in pivots]
        base_degree = 1
    elif d == 6:
        # Ordered blocks of unordered pairs: 90 disjoint eight-route supports.
        blocks = defaultdict(list)
        for j, w in enumerate(permutations):
            key = tuple(tuple(sorted(w[k:k+2])) for k in range(0, d, 2))
            blocks[key].append(j)
        keys = sorted(blocks)
        K = np.zeros((n, len(keys)), dtype=np.int64)
        chosen_indices = []
        for j, key in enumerate(keys):
            canonical = tuple(x for pair in key for x in pair)
            chosen_indices.append(permutations.index(canonical))
            for i in blocks[key]:
                flips = sum(permutations[i][k] > permutations[i][k+1] for k in range(0, d, 2))
                K[i, j] = (-1)**flips
        all_annihilated = all(np.all(K[support, :].sum(axis=0) == 0)
                             for degree in (1, 2) for support in all_rows[degree].values())
        # Rows isolating a swap in each adjacent positional pair.
        two_path_supports = {tuple(support) for support in all_rows[2].values() if len(support) == 2}
        swap_rows_present = True
        for i, w in enumerate(permutations):
            for k in range(0, d, 2):
                other = list(w)
                other[k], other[k+1] = other[k+1], other[k]
                j = permutations.index(tuple(other))
                swap_rows_present &= tuple(sorted((i, j))) in two_path_supports
        first_support = blocks[keys[0]]
        block_kernel = {
            'dimension': len(keys), 'support_size_per_basis_vector': 8,
            'independent_disjoint_supports': np.array_equal(K.T@K, 8*np.eye(len(keys), dtype=np.int64)),
            'all_first_and_second_order_rows_annihilate_basis': all_annihilated,
            'all_pair_swap_sum_rows_present': swap_rows_present,
            'basis_exhausts_exact_nullspace': len(keys) == n-degree_rows[1]['cumulative_rank'],
            'witness': [{'word': list(permutations[i]), 'coefficient': int(K[i, 0])} for i in first_support],
            'selected_coordinate_pairing_is_identity': np.array_equal(K[chosen_indices, :], np.eye(len(keys), dtype=np.int64)),
        }
        # Convert NumPy booleans for JSON.
        block_kernel = {k: bool(v) if isinstance(v, np.bool_) else v for k, v in block_kernel.items()}
        base_degree = 2
        # Half-parity readouts K^T/2 give an exact rational, balanced completion.
        balanced_scaled_gram = 4*grams[2]+K@K.T
        balanced_eigenvalues = np.linalg.eigvalsh(balanced_scaled_gram.astype(float))/4
        test_source = np.array([((17*i*i+3*i+5) % 37)-18 for i in range(n)], dtype=np.int64)
        adjoint_base_output = np.zeros(n, dtype=np.int64)
        for degree in (1, 2):
            for support in all_rows[degree].values():
                measured_value = int(test_source[support].sum())
                adjoint_base_output[support] += measured_value
        twice_parity_output = K.T@test_source
        rhs = 4*adjoint_base_output+K@twice_parity_output
        recovered = fmpz_mat(balanced_scaled_gram.tolist()).solve(fmpz_mat([[int(v)] for v in rhs]))
        exact_reconstruction = all(recovered[i, 0] == int(test_source[i]) for i in range(n))
        output_ids = [int(np.flatnonzero(K[i])[0]) for i in range(n)]
        coefficients = [int(K[i, output_ids[i]]) for i in range(n)]
        runtime_ok = True
        for i, w in enumerate(permutations):
            observer = BlockParityObserver(d)
            for j in w:
                observer = observer.step(j)
            key, value = observer.output()
            runtime_ok &= key == keys[output_ids[i]] and value == Fraction(coefficients[i], 2)
        witness_output = observe_mixture(d, [(int(K[i, 0]), permutations[i]) for i in first_support])
        block_kernel['balanced_parity_completion'] = {
            'output_formula': 'K^T x / 2; one signed sum over each eight-route block',
            'output_count': len(keys),
            'streaming_observer_matches_all_720_routes': runtime_ok,
            'streaming_local_collision_readout': str(witness_output.get(keys[0], 0)),
            'streaming_local_collision_detected': witness_output == {keys[0]: Fraction(4)},
            'completed_exact_rank': exact_rank(balanced_scaled_gram),
            'exact_reconstruction_from_measured_outputs': exact_reconstruction,
            'base_annihilates_kernel_exactly': bool(np.all(grams[2]@K == 0)),
            'base_gram_constant_row_sum': int(grams[2].sum(axis=1)[0]),
            'base_row_sum_verified': bool(np.all(grams[2].sum(axis=1) == 438)),
            'added_probe_gram': '2 I_90',
            'smallest_gram_eigenvalue_numeric': float(balanced_eigenvalues[0]),
            'largest_gram_eigenvalue_numeric': float(balanced_eigenvalues[-1]),
            'condition_number_numeric': float(np.sqrt(balanced_eigenvalues[-1]/balanced_eigenvalues[0])),
            'proved_gram_lower_bound': 2,
            'proved_gram_upper_bound': 438,
            'proved_condition_upper_bound_squared': 219,
            'bound_premises_verified': swap_rows_present and all_annihilated
                and np.array_equal(K.T@K, 8*np.eye(len(keys), dtype=np.int64))
                and bool(np.all(grams[2].sum(axis=1) == 438)),
            'observer_memory': signed_output_memory(permutations, output_ids, coefficients, d),
        }
        block_kernel['balanced_parity_completion']['bound_premises_verified'] = bool(
            block_kernel['balanced_parity_completion']['bound_premises_verified'])
    if d in (5, 6):
        augmented = grams[base_degree].copy()
        augmented[chosen_indices, chosen_indices] += 1
        ev = np.linalg.eigvalsh(augmented.astype(float))
        selected_feature_keys = [tuple(words[i][j] for j in selected_positions) for i in chosen_indices]
        completion = {
            'base_signature_degree': base_degree,
            'added_probe_degree': minimum_order,
            'added_probe_count': len(chosen_indices),
            'lower_bound_from_nullity': n-exact_rank(grams[base_degree]),
            'completed_exact_rank': exact_rank(augmented),
            'selected_words': [list(permutations[i]) for i in chosen_indices],
            'selected_features_are_route_indicators': all(all_rows[minimum_order][key] == [i]
                for key, i in zip(selected_feature_keys, chosen_indices)),
            'smallest_gram_eigenvalue_numeric': float(ev[0]),
            'largest_gram_eigenvalue_numeric': float(ev[-1]),
            'condition_number_numeric': float(np.sqrt(ev[-1]/ev[0])),
            'counting_metric_added_probe_norm': 1,
            'observer_memory': route_indicator_memory(permutations, chosen_indices, d),
        }

    results.append({
        'prime_count': d, 'route_count': n,
        'edge_count': d*2**(d-1), 'vertex_count': 2**d,
        'predicted_first_order_rank': d*2**(d-1)-2**d+2,
        'minimum_signature_order': minimum_order,
        'orders': degree_rows,
        'selected_positions_one_indexed': [i+1 for i in selected_positions],
        'selected_minimal_order_rows_are_permutation_matrix': selected_unique and selected_is_identity,
        'parity_positive_mass': sum(x > 0 for x in signs),
        'parity_negative_mass': sum(x < 0 for x in signs),
        'minimal_completion': completion,
        'three_block_kernel': block_kernel,
        'elapsed_seconds': round(time.monotonic()-start, 3),
    })

checks = {
    'exact_edge_rank_formula': all(r['orders'][0]['cumulative_rank'] == r['predicted_first_order_rank'] for r in results),
    'minimum_order_sufficient': all(r['orders'][-1]['cumulative_rank'] == r['route_count'] for r in results),
    'all_lower_orders_have_positive_mixture_collision': all(o['parity_collision'] for r in results for o in r['orders'][:-1]),
    'minimal_order_has_explicit_identity_submatrix': all(r['selected_minimal_order_rows_are_permutation_matrix'] for r in results),
    'minimal_completions_reach_full_rank': all(r['minimal_completion']['completed_exact_rank'] == r['route_count']
        and r['minimal_completion']['added_probe_count'] == r['minimal_completion']['lower_bound_from_nullity']
        for r in results if r['minimal_completion']),
    'typed_memory_certificates': all(r['minimal_completion']['observer_memory']['all_hankel_identity_minors_verified']
        for r in results if r['minimal_completion']),
    'streaming_parity_realization': results[-1]['three_block_kernel']['balanced_parity_completion']['streaming_observer_matches_all_720_routes']
        and results[-1]['three_block_kernel']['balanced_parity_completion']['streaming_local_collision_detected'],
    'balanced_completion_and_memory': results[-1]['three_block_kernel']['balanced_parity_completion']['completed_exact_rank'] == 720
        and results[-1]['three_block_kernel']['balanced_parity_completion']['exact_reconstruction_from_measured_outputs']
        and results[-1]['three_block_kernel']['balanced_parity_completion']['bound_premises_verified']
        and results[-1]['three_block_kernel']['balanced_parity_completion']['observer_memory']['all_minimality_checks'],
    'six_prime_kernel_fully_characterized': all(results[-1]['three_block_kernel'][k] for k in (
        'independent_disjoint_supports', 'all_first_and_second_order_rows_annihilate_basis',
        'all_pair_swap_sum_rows_present', 'basis_exhausts_exact_nullspace', 'selected_coordinate_pairing_is_identity')),
}
out = {
    'schema': 'marici.voevodsky.prime-packet-signature-scaling.v1',
    'exact_rank_backend': 'FLINT integer matrix rank of signature Gram matrices',
    'spectral_backend': 'NumPy floating eigvalsh, reported separately from exact ranks',
    'packets': results, 'checks': checks, 'passed': all(checks.values()),
}
p = ROOT/'research/voevodsky/results/prime-packet-signature-scaling.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
raise SystemExit(0 if out['passed'] else 1)
