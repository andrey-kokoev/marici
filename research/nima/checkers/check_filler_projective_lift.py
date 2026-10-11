"""Exact projective lift of the actual Bool source; no physical/Bell evidence.
uv run --with sympy python research/nima/checkers/check_filler_projective_lift.py
Monomial operators act on column j as i**a[j] |p[j]>; arithmetic is modulo 4.
"""
from fractions import Fraction
from itertools import product, permutations
import hashlib
import json
from pathlib import Path
import runpy
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
CONTRACT = OWNER/'contracts/filler-projective-lift.v1.json'
OUT = OWNER/'results/filler-projective-lift.json'
IDENTITY = (tuple(range(4)), (0, 0, 0, 0))
CHECKS = []


def require(name, value):
    if not bool(value):
        raise AssertionError(name)
    CHECKS.append(name)


def mul(A, B):
    p, a = A
    q, b = B
    return tuple(p[q[j]] for j in range(4)), tuple((b[j]+a[q[j]]) % 4 for j in range(4))


def inv(A):
    p, a = A
    q = tuple(p.index(j) for j in range(4))
    return q, tuple(-a[q[j]] % 4 for j in range(4))


def phase(A, exponent):
    return A[0], tuple((a+exponent) % 4 for a in A[1])


def channel(A):
    p, a = A
    return tuple((p[j], p[k], (a[j]-a[k]) % 4) for j, k in product(range(4), repeat=2))


def word(generators, indices):
    result = IDENTITY
    for index in indices:
        result = mul(result, generators[index])
    return result


def closure(generators):
    found, frontier = {IDENTITY: ()}, [IDENTITY]
    while frontier:
        current = frontier.pop(0)
        for index, generator in enumerate(generators):
            successor = mul(generator, current)
            if successor not in found:
                found[successor] = (index,)+found[current]
                frontier.append(successor)
                if len(found) > 6144:  # Entire C4 wreath S4 monomial universe.
                    raise AssertionError('monomial-universe-bound')
    return found


def matrix(A):
    p, a = A
    M = s.zeros(4)
    for j in range(4):
        M[p[j], j] = s.I**a[j]
    return M


def encode(M):
    return [[str(v) for v in row] for row in M.tolist()]


def channel_trace(A):
    return s.simplify(sum(s.I**power for (j, k), (u, v, power)
                          in zip(product(range(4), repeat=2), channel(A)) if (j, k) == (u, v)))


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    contract = json.loads(CONTRACT.read_text())
    require('frozen-contract', contract['schema'] == 'marici.nima.filler-projective-lift.v1')
    paths = {name: REPO/path for name, path in contract['source'].items()}
    inputs = (Path(__file__).resolve(), CONTRACT, *paths.values())
    before = {p: p.read_bytes() for p in inputs}
    protected = [OWNER/'results/filler-phase-spectator.json', OWNER/'results/entanglement-repaired.json',
                 OWNER/'results/bell-preparation-herald-record.json', OWNER/'results/gram-selection-principle-repaired.json',
                 REPO/'research/aspect/results/combined_bell_instrument.json']
    receipts = {p: p.read_bytes() if p.exists() else None for p in protected}
    gram, quantum, instrument = [runpy.run_path(str(paths[name])) for name in ('fillers', 'states', 'instrument')]
    require('source-labels', gram['CODES'] == list(product((False, True), repeat=2)))
    source = {name: (tuple(gram['code'](f(point)) for point in gram['CODES']), (0,)*4)
              for name, f in gram['FILLERS'].items()}
    expected = {'id': (0,1,2,3), 'swap': (0,2,1,3), 'twist': (0,1,3,2),
                'flip_fst': (2,3,0,1), 'flip_both': (3,2,1,0)}
    require('all-actual-source-actions', {name: A[0] for name, A in source.items()} == expected)
    source_group = closure(list(source.values()))
    permutations4 = sorted(A[0] for A in source_group)
    require('full-source-S4', permutations4 == list(permutations(range(4))))
    adjacent = [word(source, names) for names in contract['search']['source_words']]
    require('source-derived-adjacent-generators', [list(A[0]) for A in adjacent] == contract['search']['adjacent_permutations'])
    require('source-flip-word', word(adjacent, (1,0,2,1)) == source['flip_fst'])

    negative_identity = phase(IDENTITY, 2)
    candidates = [[(P[0], phases) for phases in product(range(4), repeat=4)
                   if mul((P[0], phases), (P[0], phases)) == negative_identity] for P in adjacent]
    require('complete-generator-search', [len(row) for row in candidates] == [16]*3)
    survivors, relation_survivors, searched = [], 0, 0
    for T in product(*candidates):
        searched += 1
        if word(T, (0,1,0)) != word(T, (1,0,1)) or word(T, (1,2,1)) != word(T, (2,1,2)):
            continue
        if mul(T[0], T[2]) != phase(mul(T[2], T[0]), 2):
            continue
        relation_survivors += 1
        if channel(word(T, (1,0,2,1))) == channel(source['flip_fst']):
            survivors.append(T)
    require('all-triples-searched', searched == 4096)
    require('projective-rival-exists-with-old-channel', len(survivors) > 0)
    T = min(survivors, key=lambda triple: tuple(A[1] for A in triple))
    group = closure(T)
    require('central-extension-order', len(group) == 48)
    fibers = {p: sorted(A for A in group if A[0] == p) for p in permutations4}
    require('all-source-fibers-retained', all(len(fiber) == 2 for fiber in fibers.values()))
    require('central-kernel', fibers[IDENTITY[0]] == [IDENTITY, negative_identity])
    lift = {p: fiber[0] for p, fiber in fibers.items()}
    require('distinct-completed-channels', len({channel(A) for A in group}) == 24)
    for A in group:
        M = matrix(A)
        require('all-lifts-unitary', M.H*M == s.eye(4))
        for scalar in range(4):
            require('all-central-rephasings-channel-invisible', channel(phase(A, scalar)) == channel(A))
    cocycle, cayley, matrix_cells = {}, [], 0
    for p in permutations4:
        row = []
        for q in permutations4:
            product_lift = mul(lift[p], lift[q])
            pq = product_lift[0]
            differences = tuple((a-b) % 4 for a, b in zip(product_lift[1], lift[pq][1]))
            require('scalar-multiplier-only', len(set(differences)) == 1 and differences[0] in (0,2))
            cocycle[p,q] = differences[0]
            row.append(permutations4.index(pq))
            for actual, expected_cell in zip(channel(product_lift), channel(lift[pq])):
                require('complete-matrix-algebra-composition', actual == expected_cell)
                matrix_cells += 1
        cayley.append(row)
    require('all-channel-cells', matrix_cells == 9216)
    cocycle_cells = 0
    for p, q, r in product(permutations4, repeat=3):
        pq, qr = mul(lift[p], lift[q])[0], mul(lift[q], lift[r])[0]
        require('full-cocycle-associativity', (cocycle[p,q]+cocycle[pq,r]-cocycle[q,r]-cocycle[p,qr]) % 4 == 0)
        cocycle_cells += 1
    require('normalized-cocycle', all(cocycle[IDENTITY[0],p] == cocycle[p,IDENTITY[0]] == 0 for p in permutations4))
    commutator = mul(mul(mul(T[0], T[2]), inv(T[0])), inv(T[2]))
    require('nontrivial-class-witness', commutator == negative_identity)
    require('commuting-source-pair', mul(adjacent[0], adjacent[2]) == mul(adjacent[2], adjacent[0]))
    for a, b in product(range(4), repeat=2):
        V, W = phase(T[0], a), phase(T[2], b)
        require('commutator-rephasing-control', mul(mul(mul(V,W),inv(V)),inv(W)) == negative_identity)
    require('minus-identity-not-directly-observable', channel(commutator) == channel(IDENTITY))
    require('strict-control-has-trivial-commutator', mul(mul(mul(adjacent[0],adjacent[2]),inv(adjacent[0])),inv(adjacent[2])) == IDENTITY)

    for p in permutations4:
        for j in range(4):
            M, P = matrix(lift[p]), matrix((p, (0,)*4))
            E = s.eye(4)[:, j]*s.eye(4)[:, j].T
            require('all-classical-effect-pullbacks', M.H*E*M == P.T*E*P)
    twist = lift[source['twist'][0]]
    flip = lift[source['flip_fst'][0]]
    require('entire-old-flip-channel-identical', channel(flip) == channel(source['flip_fst']))
    require('twist-fixes-test-labels', twist[0][0:2] == (0,1))
    require('fixed-ray-relative-phase', (twist[1][0]-twist[1][1]) % 4 == 2)
    require('channel-family-not-a-common-basis-change', channel_trace(twist) == 0 and channel_trace(source['twist']) == 4)
    for p in permutations4:
        require('unitary-word-witnesses', word(T, group[lift[p]]) == lift[p])

    I, X, Z = quantum['I2'], quantum['X'], quantum['Z']
    Q = instrument['Q']
    def to_Q(M):
        M = M.applyfunc(s.simplify)
        require('exact-real-instrument-input', all(v.is_Rational for v in M))
        return [[Q(Fraction(int(v.p), int(v.q))) for v in row] for row in M.tolist()]
    def from_Q(M):
        return s.Matrix([[s.Rational(v.rational.numerator, v.rational.denominator)
                          +s.sqrt(2)*s.Rational(v.root2.numerator,v.root2.denominator) for v in row] for row in M])
    prepared = {h: from_Q(instrument['instrument'](to_Q(quantum['states']()['product00']),
                to_Q((I+(-1)**h*X)/2), False)) for h in range(2)}
    require('both-preparations-nonzero', all(s.trace(rho) == s.Rational(1,2) for rho in prepared.values()))
    # Every strict lift acts scalarly on these two fixed rays, hence preserves
    # their entire coherent density, regardless of diagonal phase frame.
    z = s.Symbol('z', nonzero=True)
    D = s.diag(1,1,1,z)
    strict_twist = D*matrix(source['twist'])*D.inv()
    for rho in prepared.values():
        require('whole-strict-relative-phase-family', strict_twist*rho*strict_twist.inv() == rho)
    operators = {'bypass': s.eye(4), 'strict_flip': matrix(source['flip_fst']),
                 'projective_flip': matrix(flip), 'strict_twist': matrix(source['twist']),
                 'projective_twist': matrix(twist)}
    records, continuations, statistics = {}, {}, {}
    for name, M in operators.items():
        table, states = {}, {}
        for h, a, b in product(range(2), (-1,1), (-1,1)):
            rho = (M*prepared[h]*M.H).applyfunc(s.simplify)
            pa, pb = (I+a*Z)/2, (I+b*X)/2
            actual = from_Q(instrument['joint_instrument'](to_Q(rho), to_Q(pa), to_Q(pb)))
            E = s.kronecker_product(pa,pb)
            require('full-instrument-continuation', actual == E*rho*E)
            key = f'{h},{a},{b}'
            table[key], states[key] = s.trace(actual), actual
            require('positive-effect-pairing', table[key] >= 0)
        require('all-ideal-records-normalized', sum(table.values()) == 1)
        records[name], continuations[name] = table, states
        statistics[name] = sum((-1)**h*b*table[f'{h},{a},{b}'] for h,a,b in product(range(2),(-1,1),(-1,1)))
    require('old-test-cannot-identify-source-model', records['strict_flip'] == records['projective_flip'])
    require('new-fixed-ray-witness', statistics == {'bypass':1, 'strict_flip':1, 'projective_flip':1, 'strict_twist':1, 'projective_twist':-1})
    require('inputs-preserved', all(p.read_bytes() == data for p,data in before.items()))
    require('predecessor-and-foreign-receipts-preserved', all((p.read_bytes() if p.exists() else None) == data for p,data in receipts.items()))
    result = {'schema':'marici.nima.filler-projective-lift-result.v1', 'status':'pass',
              'classification':'completed-channel-source-lift-escapes-strict-unitary-class',
              'source_functions':{name:list(A[0]) for name,A in source.items()},
              'triples_searched':searched, 'relation_survivors':relation_survivors,
              'old_channel_survivors':len(survivors),
              'all_survivor_phase_triples':[[list(A[1]) for A in triple] for triple in survivors],
              'selected_generator_phases':[list(A[1]) for A in T],
              'selected_generator_matrices':[encode(matrix(A)) for A in T],
              'lift_group_order':len(group), 'channel_group_order':len(lift),
              'representatives':[{'permutation':list(p),'phase_exponents':list(lift[p][1]),'word':list(group[lift[p]])} for p in permutations4],
              'cayley_table':cayley, 'cocycle_exponents':[[cocycle[p,q] for q in permutations4] for p in permutations4],
              'matrix_unit_cells':matrix_cells, 'cocycle_cells':cocycle_cells,
              'commutator':encode(matrix(commutator)), 'central_phase_channel_is_identity':True,
              'source_operator_matrices':{name:encode(matrix(lift[A[0]])) for name,A in source.items()},
              'twist_channel_trace':{'strict':str(channel_trace(source['twist'])),'projective':str(channel_trace(twist))},
              'prepared_branches':{str(h):encode(rho) for h,rho in prepared.items()},
              'full_records':{name:{key:str(p) for key,p in row.items()} for name,row in records.items()},
              'full_continuations':{name:{key:encode(rho) for key,rho in row.items()} for name,row in continuations.items()},
              'branch_signed_X_B':{name:str(v) for name,v in statistics.items()},
              'checks_passed':len(CHECKS), 'scope':contract['scope'],
              'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','classification','triples_searched','relation_survivors',
                      'old_channel_survivors','selected_generator_phases','lift_group_order','channel_group_order',
                      'branch_signed_X_B','checks_passed')},indent=2))


if __name__ == '__main__':
    main()
