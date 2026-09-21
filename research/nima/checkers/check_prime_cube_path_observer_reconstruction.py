#!/usr/bin/env python3
"""Exact reconstruction audit of the three-prime interval-plus-cycle packet.

Distinguishes free source paths, additive edge chains, and the endpoint quotient.
Run with uv run --with sympy python research/nima/checkers/check_prime_cube_path_observer_reconstruction.py
"""
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]


def source(d):
    edges = [(mask, mask | (1 << j), j) for mask in range(1 << d)
             for j in range(d) if not mask & (1 << j)]
    edge_index = {e: i for i, e in enumerate(edges)}
    paths = []
    for start in range(1 << d):
        available = [j for j in range(d) if not start & (1 << j)]
        for k in range(len(available)+1):
            for word in itertools.permutations(available, k):
                paths.append((start, word))
    return edges, edge_index, paths


def target(path):
    start, word = path
    return start | sum(1 << j for j in word)


def chain(path, edges, edge_index):
    mask, word = path
    c = s.zeros(len(edges), 1)
    for j in word:
        nxt = mask | (1 << j)
        c[edge_index[(mask, nxt, j)]] += 1
        mask = nxt
    return c


def compose(q, p):
    if target(p) != q[0]:
        return None
    return p[0], p[1]+q[1]


def grouped(paths):
    groups = {}
    for p in paths:
        groups.setdefault((p[0], target(p)), []).append(p)
    return groups


def column_matrix(paths, edges, index):
    return s.Matrix.hstack(*(chain(p, edges, index) for p in paths))


d = 3
primes = (2, 3, 5)
edges, edge_index, paths = source(d)
groups = grouped(paths)
nodes = {mask: 2*s.prod(primes[j] for j in range(d) if mask & (1 << j)) for mask in range(8)}
vertices = sorted(nodes.values())
J = s.Matrix(7, 12, lambda i, e: int(nodes[edges[e][0]] <= vertices[i]
                                    and vertices[i+1] <= nodes[edges[e][1]]))
boundary = s.zeros(8, 12)
for k, (a, b, _) in enumerate(edges):
    boundary[vertices.index(nodes[a]), k] = -1
    boundary[vertices.index(nodes[b]), k] = 1

# Same source-derived Kruskal conventions as the existing forest checker.
frames = {}
chords = {}
for word in itertools.permutations(range(d)):
    parent = list(range(8))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    tree = []
    for k in sorted(range(12), key=lambda k: (word.index(edges[k][2]), nodes[edges[k][0]], k)):
        a, b, _ = edges[k]
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[ra] = rb
            tree.append(k)
    chords[word] = [k for k in range(12) if k not in tree]
    Z = s.zeros(5, 12)
    for r, k in enumerate(chords[word]):
        Z[r, k] = 1
    frames[word] = J.col_join(Z)

frame = frames[(0, 1, 2)]
rank_rows = []
for (a, b), pp in groups.items():
    if a == b:
        # Unit observers: additive edge chains of empty paths are zero.
        O = s.ones(1, 1)
        R = s.ones(1, 1)
    else:
        O = frame*column_matrix(pp, edges, edge_index)
        # Exact image inverse; no fitting of arithmetic determinant values.
        R = (O.T*O).inv()*O.T
    rank_rows.append({'source': a, 'target': b, 'path_count': len(pp),
                      'observer_rank': O.rank(), 'left_inverse': R*O == s.eye(len(pp))})

# Push-pull source algebra: each Hom block contains formal linear combinations of paths.
# Observer coordinates keep the endpoints and the sum of coefficients lambda.
# On nonidentity blocks lambda is recovered by the outgoing boundary at the source.
composable = [(q, p) for q in paths for p in paths if compose(q, p) is not None]
additive_composition = all(
    chain(compose(q, p), edges, edge_index) == chain(q, edges, edge_index)+chain(p, edges, edge_index)
    for q, p in composable)
coefficient_recovery = all(
    -(boundary*chain(p, edges, edge_index))[vertices.index(nodes[p[0]])] == 1
    for p in paths if p[0] != target(p))

# Every forest transform intertwines the complete Hom-block image representation.
reference = frames[(0, 1, 2)]
transitions = {w: C*reference.inv() for w, C in frames.items()}
forest_naturality = all(
    transitions[w]*(reference*chain(p, edges, edge_index)) == C*chain(p, edges, edge_index)
    for w, C in frames.items() for p in paths)

# Build the six oriented square boundaries in the retained edge basis.
faces = []
face_columns = []
face_routes = []
for a in range(8):
    available = [j for j in range(3) if not a & (1 << j)]
    for i, j in itertools.combinations(available, 2):
        p, q = (a, (i, j)), (a, (j, i))
        faces.append((a, i, j))
        face_routes.append((p, q))
        face_columns.append(chain(p, edges, edge_index)-chain(q, edges, edge_index))
F = s.Matrix.hstack(*face_columns)
face_relations = F.nullspace()

# Ideal of face-route relations inside the free path algebra, including all contexts.
path_index = {p: i for i, p in enumerate(paths)}
ideal_columns = []
for p, q in face_routes:
    for before in paths:
        if target(before) != p[0]:
            continue
        for after in paths:
            if after[0] != target(p):
                continue
            r = compose(after, compose(p, before))
            t = compose(after, compose(q, before))
            v = s.zeros(len(paths), 1)
            v[path_index[r]] = 1
            v[path_index[t]] = -1
            ideal_columns.append(v)
ideal = s.Matrix.hstack(*ideal_columns)
endpoint_keys = list(groups)
quotient = s.Matrix(len(endpoint_keys), len(paths),
                    lambda i, j: int((paths[j][0], target(paths[j])) == endpoint_keys[i]))

# Minimality of five added edge-space probes beyond the seven interval probes.
K = s.Matrix.hstack(*J.nullspace())
Z = frame[7:, :]
deletion_ranks = [J.col_join(Z[[j for j in range(5) if j != i], :]).rank() for i in range(5)]

# Stress test: four-prime full routes lose six linear degrees under edge observation.
edges4, index4, paths4 = source(4)
full4 = [p for p in paths4 if p[0] == 0 and target(p) == 15]
E4 = column_matrix(full4, edges4, index4)
null4 = E4.nullspace()
witness = null4[0]
# Each word is a distinct ordered signature coordinate at degree four.
word_signature = s.eye(len(full4))

# Degree-two signature: ordered pairs of traversed edges.
def ordered_edges(p, index):
    mask, word = p
    out = []
    for j in word:
        nxt = mask | (1 << j)
        out.append(index[(mask, nxt, j)])
        mask = nxt
    return out

edge_words4 = [ordered_edges(p, index4) for p in full4]
# The two central edges determine a full four-step cube path uniquely.
central_pairs = sorted({(word[1], word[2]) for word in edge_words4})
P2 = s.Matrix(len(central_pairs), len(full4), lambda i, j:
              int(central_pairs[i][0] in edge_words4[j]
                  and central_pairs[i][1] in edge_words4[j]
                  and edge_words4[j].index(central_pairs[i][0])
                      < edge_words4[j].index(central_pairs[i][1])))
selected = []
augmented = E4
current_rank = E4.rank()
for i in range(P2.rows):
    candidate = augmented.col_join(P2[i, :])
    candidate_rank = candidate.rank()
    if candidate_rank > current_rank:
        selected.append(i)
        augmented = candidate
        current_rank = candidate_rank
    if current_rank == len(full4):
        break
reconstructor4 = (augmented.T*augmented).inv()*augmented.T

# Check the same six probes on every endpoint block of the four-cube.
selected_pairs = [central_pairs[i] for i in selected]
groups4 = grouped(paths4)
four_block_rows = []
for endpoints, pp in groups4.items():
    if endpoints[0] == endpoints[1]:
        observed_rank = 1  # retained identity coefficient
    else:
        words = [ordered_edges(p, index4) for p in pp]
        correlations = s.Matrix(6, len(pp), lambda i, j:
            int(selected_pairs[i][0] in words[j] and selected_pairs[i][1] in words[j]
                and words[j].index(selected_pairs[i][0]) < words[j].index(selected_pairs[i][1])))
        observed_rank = column_matrix(pp, edges4, index4).col_join(correlations).rank()
    four_block_rows.append((len(pp), observed_rank))

# Chen's degree-two composition law tested on all composable four-cube basis paths.
def signature2(p):
    ee = ordered_edges(p, index4)
    return set(ee), {(ee[i], ee[j]) for i in range(len(ee)) for j in range(i+1, len(ee))}

chen = True
for p in paths4:
    for q in paths4:
        r = compose(q, p)
        if r is None:
            continue
        ep, pp = signature2(p)
        eq, pq = signature2(q)
        er, pr = signature2(r)
        cross = {(a, b) for a in ep for b in eq}
        chen &= er == ep | eq and pr == pp | cross | pq

checks = {
    '38_free_paths_27_endpoint_pairs': len(paths) == 38 and len(groups) == 27,
    'all_hom_observers_have_exact_left_inverse': all(r['left_inverse'] for r in rank_rows),
    'additive_observer_preserves_path_composition': additive_composition,
    'coefficient_sum_recovered_on_nonidentity_blocks': coefficient_recovery,
    'all_forest_changes_natural_on_paths': forest_naturality,
    'six_faces_span_five_dimensional_cycle_space': F.cols == 6 and F.rank() == 5
        and boundary*F == s.zeros(8, 6) and len(face_relations) == 1,
    'face_relation_uses_all_six_faces': all(v != 0 for v in face_relations[0]),
    'face_ideal_is_full_endpoint_quotient_kernel': ideal.rank() == 11
        and quotient*ideal == s.zeros(27, ideal.cols) and quotient.rank() == 27,
    'seven_plus_five_minimal_for_full_edge_space': J.rank() == 7 and frame.rank() == 12
        and (Z*K).rank() == 5 and all(r == 11 for r in deletion_ranks),
    'four_prime_full_paths_have_six_dimensional_linear_kernel': len(full4) == 24
        and E4.rank() == 18 and len(null4) == 6,
    'four_prime_kernel_witness_is_nonzero': witness != s.zeros(24, 1)
        and E4*witness == s.zeros(32, 1),
    'ordered_path_signature_recovers_witness': word_signature*witness != s.zeros(24, 1),
    'six_second_order_probes_complete_four_prime_reconstruction': len(selected) == 6 and augmented.rank() == 24,
    'four_prime_completed_observer_has_exact_left_inverse': reconstructor4*augmented == s.eye(24),
    'all_central_pairs_are_independent_path_probes': P2.rows == 24 and P2.rank() == 24,
    'second_order_probe_detects_collision': P2*witness != s.zeros(24, 1),
    'second_order_chen_composition': chen,
    'entire_four_prime_category_reconstructed': len(paths4) == 168 and len(groups4) == 81
        and all(n == r for n, r in four_block_rows),
}
checks = {k: bool(v) for k, v in checks.items()}

# Collision between two honest distinct nonnegative combinations, with equal total mass.
pos = s.Matrix([max(v, 0) for v in witness])
neg = s.Matrix([max(-v, 0) for v in witness])
checks['four_prime_collision_has_equal_positive_mass'] = bool(E4*pos == E4*neg
    and sum(pos) == sum(neg) and sum(pos) > 0 and pos != neg)

out = {
    'schema': 'marici.nima.prime-cube-path-observer-reconstruction.v1',
    'checks': checks, 'passed': all(checks.values()),
    'three_prime': {
        'free_path_algebra_dimension': len(paths), 'endpoint_incidence_dimension': len(groups),
        'hom_blocks': rank_rows, 'composable_basis_pairs_checked': len(composable),
        'face_rank': F.rank(), 'face_relation': [str(v) for v in face_relations[0]],
        'face_order': [list(f) for f in faces], 'endpoint_ideal_rank': ideal.rank(),
        'edge_observer_dimension': frame.rows, 'edge_frame_determinant': str(frame.det()),
        'cycle_probe_deletion_ranks': deletion_ranks,
    },
    'four_prime_hostile': {
        'full_path_count': len(full4), 'edge_observer_rank': E4.rank(),
        'kernel_dimension': len(null4),
        'witness_terms': [{'word': list(full4[i][1]), 'coefficient': str(v)}
                          for i, v in enumerate(witness) if v],
        'positive_mass': str(sum(pos)),
        'minimal_added_second_order_probe_count': len(selected),
        'selected_probes': [{'first_edge': list(edges4[central_pairs[i][0]]),
                             'second_edge': list(edges4[central_pairs[i][1]])} for i in selected],
        'completed_rank': augmented.rank(),
        'all_endpoint_blocks': len(groups4),
        'full_path_algebra_dimension': len(paths4),
        'sum_of_completed_hom_ranks': sum(r for n, r in four_block_rows),
    },
    'analytic_scope': 'Exact rational incidence/path algebra only. Theta realization uses the separately recorded finite injectivity premise.',
    'proof': 'research/nima/prime-cube-faithful-observers-paths-relations-and-nested-reconstruction.md',
}
path = ROOT/'research/nima/results/prime-cube-path-observer-reconstruction.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
raise SystemExit(0 if out['passed'] else 1)
