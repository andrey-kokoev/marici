"""Inspect the mixed sector and test a Frobenius candidate with exact tensors."""
from itertools import product
from pathlib import Path
import hashlib
import json
import check_reversible_trivalent_census as census

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / 'research/nima/results/trivalent-mixed-candidate.json'


def evaluate(g, mu, split):
    """Integer matrix of a port graph. Rows=outputs, columns=inputs.

    mu[out][in0][in1]; split[out0][out1][in]. Internal labels are summed.
    Boundary tuple positions are preserved; no symmetry is assumed.
    """
    ts, es, ins, outs = g
    d = len(mu)
    cols = list(product(range(d), repeat=len(ins)))
    rows = list(product(range(d), repeat=len(outs)))
    matrix = []
    for row in rows:
        line = []
        for col in cols:
            total = 0
            for internal in product(range(d), repeat=len(es)):
                ip, op = dict(zip(ins, col)), dict(zip(outs, row))
                for (a, b, c, e), label in zip(es, internal):
                    op[a, b] = label
                    ip[c, e] = label
                term = 1
                for v, t in enumerate(ts):
                    term *= (mu[op[v, 0]][ip[v, 0]][ip[v, 1]] if t == 0
                             else split[op[v, 0]][op[v, 1]][ip[v, 0]])
                total += term
            line.append(total)
        matrix.append(line)
    return matrix


def transpose_mu(mu):
    d = len(mu)
    return [[[mu[i][a][b] for i in range(d)] for b in range(d)] for a in range(d)]


def multiply(a, b):
    assert len(a[0]) == len(b)
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def first_difference(a, b):
    return next(({'output_index': i, 'input_index': j, 'left': x, 'right': b[i][j]}
                 for i, row in enumerate(a) for j, x in enumerate(row) if x != b[i][j]), None)


def named(g):
    ts, es, _, _ = g
    merge = ts.index(0)
    if len(es) == 1:
        a, b, c, d = es[0]
        return 'K' if a == merge else f'A{b}{d}'
    pairs = sorted((b, d) for a, b, c, d in es)
    return 'L_parallel' if pairs == [(0, 0), (1, 1)] else 'L_crossed'


def main():
    base, _, _ = census.skeletons(2)
    mixed = {named(g): g for g in base if sorted(g[0]) == [0, 1]}
    # Ordered boundaries make the proposed comparisons unambiguous.
    k = ((0, 1), ((0, 0, 1, 0),), ((0, 0), (0, 1)), ((1, 0), (1, 1)))
    left = ((0, 1), ((1, 0, 0, 1),), ((0, 0), (1, 0)), ((0, 0), (1, 1)))
    right = ((0, 1), ((1, 1, 0, 0),), ((1, 0), (0, 1)), ((1, 0), (0, 0)))
    for g in (k, left, right):
        census.validate(g)
        assert census.canonical(g, False) == mixed[named(g)]
    assert census.canonical(census.reverse(k), True) == census.canonical(k, True)
    assert census.canonical(census.reverse(left), True) == census.canonical(right, True)

    # Dual numbers in basis (1, epsilon), epsilon^2=0, Euclidean transpose split.
    dual = [[[1, 0], [0, 0]], [[0, 1], [1, 0]]]
    copy = [[[1, 0], [0, 0]], [[0, 0], [0, 1]]]
    scaled = [[[2*x for x in row] for row in layer] for layer in copy]
    models = {'dual_numbers_transpose': dual, 'copy_delete_transpose': copy,
              'scaled_copy_transpose': scaled}
    assoc_left = census.graph((0, 0), ((0, 0, 1, 0),))
    assoc_right, = census.merge_rotations(assoc_left)
    evidence = {}
    for name, mu in models.items():
        split = transpose_mu(mu)
        ev = lambda g: evaluate(g, mu, split)
        assoc = ev(assoc_left) == ev(assoc_right)
        coassoc = ev(census.reverse(assoc_left)) == ev(census.reverse(assoc_right))
        assert assoc and coassoc
        km, lm, rm = ev(k), ev(left), ev(right)
        lp = ev(mixed['L_parallel'])
        # Reversal is genuinely matrix transpose in these models, even though
        # the proposal does not require a dagger. Check every enumerated mixed graph.
        for g in mixed.values():
            assert ev(census.reverse(g)) == [list(row) for row in zip(*ev(g))]
        evidence[name] = {
            'mu': mu, 'split': split, 'associative': assoc, 'coassociative': coassoc,
            'reversal_is_matrix_transpose_on_mixed_sector': True,
            'K_matrix': km, 'left_matrix': lm, 'right_matrix': rm,
            'frobenius_left': km == lm, 'frobenius_right': km == rm,
            'left_counterexample': first_difference(km, lm),
            'right_counterexample': first_difference(km, rm),
            'L_parallel_matrix': lp, 'L_is_identity': lp == identity(len(lp)),
            'K_is_idempotent': multiply(km, km) == km,
            'mixed_matrices_with_recorded_boundary_order': {n: ev(g) for n, g in sorted(mixed.items())}}
    assert not evidence['dual_numbers_transpose']['frobenius_left']
    assert not evidence['dual_numbers_transpose']['frobenius_right']
    dual_ev = evidence['dual_numbers_transpose']
    # Input epsilon tensor epsilon: K gives zero, both slide routes give
    # epsilon tensor epsilon. Basis index 3 denotes (epsilon, epsilon).
    assert dual_ev['K_matrix'][3][3] == 0
    assert dual_ev['left_matrix'][3][3] == dual_ev['right_matrix'][3][3] == 1
    assert evidence['copy_delete_transpose']['frobenius_left'] and evidence['copy_delete_transpose']['frobenius_right']
    sc = evidence['scaled_copy_transpose']
    assert sc['frobenius_left'] and sc['frobenius_right']
    assert not sc['L_is_identity'] and not sc['K_is_idempotent']

    # The elementary same-boundary candidate plus reversal connects only these
    # three classes at two vertices. Boundary permutations do not move a local
    # internal slot. No claim about arbitrary contexts or higher completion.
    edges = [('K', 'A01'), ('K', 'A10')]
    adj = {n: set() for n in mixed}
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    unseen = set(mixed); components = []
    while unseen:
        seen, todo = set(), [min(unseen)]
        while todo:
            x = todo.pop()
            if x not in seen:
                seen.add(x); todo.extend(adj[x]-seen)
        unseen -= seen
        components.append(sorted(seen))
    report = {
        'schema': 'marici.nima.trivalent-mixed-candidate.v1',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'census_checker_sha256': hashlib.sha256(Path(census.__file__).read_bytes()).hexdigest(),
        'scope': 'Two-vertex connected DAG sector, local slots distinguished, boundary permutation quotient; candidate tested with ordered boundaries',
        'candidate': {'name': 'Frobenius',
                      'K': 'split o merge',
                      'left': '(merge tensor id) o (id tensor split)',
                      'right': '(id tensor merge) o (split tensor id)',
                      'status': 'additional candidate law, not derived or admitted',
                      'ordered_graphs': {'K': k, 'left': left, 'right': right},
                      'reversal': 'fixes K and exchanges left/right after vertex relabelling'},
        'mixed_classes': {n: {'graph': g, 'boundary': [len(g[2]), len(g[3])],
                              'reversed_class': named(census.reverse(g))} for n, g in sorted(mixed.items())},
        'candidate_elementary_edges': edges, 'candidate_elementary_components': components,
        'models': evidence,
        'checks_passed': True,
        'conclusions': ['Associativity, coassociativity and even transpose reversal do not force Frobenius.',
                        'Frobenius is consistent with the primitive equations in these finite integer tensor models.',
                        'Frobenius does not force L=identity or K idempotent without extra normalization.',
                        'These are strict linear-model tests, not a theorem about all higher-cell interpretations.']}
    RESULT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('Mixed classes:', ', '.join(sorted(mixed)))
    print('Candidate components:', components)
    for n, e in evidence.items():
        print(n, {k: e[k] for k in ('associative', 'coassociative', 'frobenius_left',
                                   'frobenius_right', 'L_is_identity', 'K_is_idempotent')})
    print('All exact tensor checks passed.')


if __name__ == '__main__':
    main()
