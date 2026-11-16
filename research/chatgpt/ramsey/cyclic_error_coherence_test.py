#!/usr/bin/env python3
"""Exact 2-letter path dictionary and one-splice error correction audit.

A length-k word with two 'r' letters is a directed, individually retained path
from its first letter to its last letter. A complete tour is a cyclic order of
all words, once each, matching consecutive endpoint letters.

One gluing error swaps the continuation assignments of two incoming path words
ending at the same letter. This preserves endpoint matching, but splits a single
tour into two cycles. Repair is a swap that restores one circle.

This script derives no geometric/physical N or NN fillers and does not assert a
Ramsey number. Its gluing checksum must be transported separately from the
corrupted successor table.
"""

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
import json

OUT = Path('/mnt/data/cyclic_error_coherence_results.json')


def dictionary(k):
    return tuple(''.join(t) for t in product('rs', repeat=k) if t.count('r') == 2)


def is_tour(t):
    return len(set(t)) == len(t) and all(x[-1] == y[0] for x, y in zip(t, t[1:] + t[:1]))


def all_tours(words):
    first = words[0]
    return tuple(t for rest in permutations(words[1:]) for t in [(first,) + rest] if is_tour(t))


def successor(t, words):
    f = dict(zip(t, t[1:] + t[:1]))
    return tuple(words.index(f[w]) for w in words)


def cycle_indices(p):
    visited = set()
    cycles = []
    for root in range(len(p)):
        if root in visited:
            continue
        walk = []
        i = root
        while i not in visited:
            visited.add(i)
            walk.append(i)
            i = p[i]
        assert i == root
        cycles.append(tuple(walk))
    return tuple(cycles)


def swapped_successors(p, i, j):
    q = list(p)
    q[i], q[j] = q[j], q[i]
    return tuple(q)


def splice_errors(tours, words):
    incoming_pairs = [(i, j) for i, j in combinations(range(len(words)), 2)
                      if words[i][-1] == words[j][-1]]
    sources = defaultdict(set)
    for t in tours:
        p = successor(t, words)
        for i, j in incoming_pairs:
            q = swapped_successors(p, i, j)
            assert len(cycle_indices(q)) == 2
            sources[q].add(p)
    all_tour_perms = set(successor(t, words) for t in tours)
    repaired = {}
    for err, old in sources.items():
        candidates = {swapped_successors(err, i, j)
                      for i, j in incoming_pairs
                      if swapped_successors(err, i, j) in all_tour_perms}
        assert candidates == old
        repaired[err] = candidates
    return repaired


def word_error_neighbors(words):
    pred = defaultdict(set)
    for w in words:
        for i in range(len(w)):
            z = w[:i] + ('s' if w[i] == 'r' else 'r') + w[i + 1:]
            pred[z].add(w)
    return pred


def inventory_restoration(tours, words):
    original = set(words)
    checks = 0
    for t in tours:
        for pos, w in enumerate(t):
            for j in range(len(w)):
                z = w[:j] + ('s' if w[j] == 'r' else 'r') + w[j + 1:]
                received = list(t)
                received[pos] = z
                known = set(received)
                missing = original - known
                invalid = known - original
                assert len(missing) == len(invalid) == 1
                assert missing == {w} and invalid == {z}
                received[pos] = next(iter(missing))
                assert tuple(received) == t and is_tour(tuple(received))
                checks += 1
    return checks


def bit_tours_k4():
    # x and x' are the two r->s paths, y and y' the two s->r paths.
    # u and v are respectively the r->r and s->s closed paths.
    x, xp, y, yp, u, v = 'rrss', 'rsrs', 'srsr', 'ssrr', 'rssr', 'srrs'
    result = {}
    for a, b, c in product((0, 1), repeat=3):
        y_first, y_second = (y, yp) if a == 0 else (yp, y)
        t = [x]
        if b == 0:
            t.append(v)
        t.append(y_first)
        if c == 0:
            t.append(u)
        t.append(xp)
        if b == 1:
            t.append(v)
        t.append(y_second)
        if c == 1:
            t.append(u)
        assert is_tour(tuple(t))
        result[(a, b, c)] = tuple(t)
    assert len(set(result.values())) == 8
    return result


def syndrome(bits):
    a, b, c = bits
    return (a, b ^ c)


def local_two_bit_tags(words):
    # Points 0,1,2,(3) of F_2^2, with XOR representing their pair.
    position_symbols = (0, 1, 2, 3)
    code = {}
    for w in words:
        support = [i for i, char in enumerate(w) if char == 'r']
        t = position_symbols[support[0]] ^ position_symbols[support[1]]
        check_bits = f'{t:02b}'
        binary = ''.join('1' if x == 'r' else '0' for x in w)
        code[w] = binary + check_bits
    assert min(sum(a != b for a, b in zip(v, z)) for v, z in combinations(code.values(), 2)) >= 3
    decoded = {}
    for w, c in code.items():
        for j in range(len(c) + 1):
            z = c if j == len(c) else c[:j] + ('0' if c[j] == '1' else '1') + c[j + 1:]
            assert z not in decoded or decoded[z] == w
            decoded[z] = w
    return code, len(decoded)


def compute():
    result = {'model': 'fixed-weight-two binary path words with one-letter endpoint matching',
              'gluing_error_model': 'transposition of successor assignments at two paths with same ending letter',
              'runs': {}, 'limitations': ['N and NN fillers are not asserted or generated by this test',
                          'global checksum is transmitted or retained independently of corruptible successor assignments',
                          'test is not a proof of Ramsey threshold']}
    for k in (3, 4):
        words = dictionary(k)
        tours = all_tours(words)
        assert all(set(t) == set(words) for t in tours)
        repairs = splice_errors(tours, words)
        corrupted = word_error_neighbors(words)
        checks = inventory_restoration(tours, words)
        tags, ndecoded = local_two_bit_tags(words)
        r = {'word_count': len(words), 'words': list(words),
             'closed_tours_up_to_rotation': len(tours),
             'example_tour': list(tours[0]),
             'distinct_single_splice_errors': len(repairs),
             'repair_multiplicity': dict(Counter(str(len(v)) for v in repairs.values())),
             'corrupted_word_ambiguity': dict(Counter(str(len(v)) for v in corrupted.values())),
             'all_single_letter_inventory_recoveries': checks,
             'local_1_bit_error_correction_length': k + 2,
             'local_tagged_codewords': tags,
             'distinct_received_vectors_within_1_bit': ndecoded}
        if k == 4:
            bt = bit_tours_k4()
            assert set(bt.values()) == set(tours)
            to_bits = {successor(t, words): b for b, t in bt.items()}
            for q, sources in repairs.items():
                labels = [syndrome(to_bits[p]) for p in sources]
                assert len(labels) == len(set(labels))
            assert max(map(len, repairs.values())) == 4
            # The confusion graph has 8 vertices and exactly 4 missing edges.
            confused = set()
            for s in repairs.values():
                for p, q in combinations(sorted(s), 2):
                    confused.add((p, q))
            assert len(confused) == 24
            same_tag_pairs = {tuple(sorted((p, q))) for p, q in combinations(to_bits, 2)
                              if syndrome(to_bits[p]) == syndrome(to_bits[q])}
            assert len(same_tag_pairs) == 4
            assert not (same_tag_pairs & confused)
            assert len(confused) + len(same_tag_pairs) == 28
            r.update({
                'independent_gluing_choices': ['which s->r path is first (a)',
                                               'position of s-loop (b)',
                                               'position of r-loop (c)'],
                'gluing_choice_histories': {''.join(map(str, key)): list(val) for key, val in bt.items()},
                'global_splice_syndrome': 'sigma(a,b,c)=(a,b XOR c)',
                'syndrome_distinct_for_every_possible_repair_set': True,
                'minimum_global_splice_syndrome_bits': 2,
                'confusability_graph_vertices': 8,
                'confusability_graph_edges': 24,
                'unconfusable_pairs': 4,
                'candidate_N_edges_for_3_cube': 12,
                'candidate_NN_square_boundaries_for_3_cube': 6,
                'candidate_higher_cube_boundary': 1,
                'example_four_repair_case': next({
                    'received_two_circles': [[words[i] for i in c] for c in cycle_indices(err)],
                    'repairs': [{'bits': ''.join(map(str, to_bits[p])),
                                 'syndrome': ''.join(map(str, syndrome(to_bits[p])))}
                                for p in sorted(source)]}
                    for err, source in repairs.items() if len(source) == 4)
            })
        result['runs'][str(k)] = r
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print('Wrote:', OUT)
    for k, r in result['runs'].items():
        print(f'k={k}: {r["word_count"]} words, {r["closed_tours_up_to_rotation"]} circles, '
              f'{r["distinct_single_splice_errors"]} single splice errors, '
              f'repairs={r["repair_multiplicity"]}, local tags need 2 bits')
    print('k=4: sigma=(a,b XOR c) corrects all 16 one-splice error states')

if __name__ == '__main__':
    compute()
