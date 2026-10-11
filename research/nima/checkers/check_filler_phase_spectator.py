"""Strict monomial lifts of actual Bool fillers; no Bell scalar or physical data.
uv run --with sympy python research/nima/checkers/check_filler_phase_spectator.py
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
CONTRACT = OWNER/'contracts/filler-phase-spectator.v1.json'
OUT = OWNER/'results/filler-phase-spectator.json'
CHECKS = []
z = s.Symbol('z', nonzero=True)  # Unit-circle domain; dagger sends z to 1/z.


def require(name, value):
    if not bool(value):
        raise AssertionError(name)
    CHECKS.append(name)


def tidy(M):
    return M.applyfunc(s.cancel)


def eq(A, B):
    return tidy(A-B) == s.zeros(*A.shape)


def dagger(M):
    return M.H.subs(s.conjugate(z), 1/z)


def compose(p, q):
    return tuple(p[q[j]] for j in range(4))


def inverse(p):
    return tuple(p.index(j) for j in range(4))


def parity(p):
    return (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))


def matrix(p):
    P = s.zeros(4)
    for j, i in enumerate(p):
        P[i, j] = 1
    return P


def residual_gcd(matrices):
    polynomials = [s.Poly(s.cancel(v).as_numer_denom()[0], z)
                   for M in matrices for v in M if s.cancel(v) != 0]
    require('nonempty-residual-ideal', bool(polynomials))
    result = polynomials[0]
    for polynomial in polynomials[1:]:
        result = s.gcd(result, polynomial)
    return result.monic().as_expr()


def encode(M):
    return [[str(v) for v in row] for row in M.tolist()]


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    contract = json.loads(CONTRACT.read_text())
    require('contract-schema', contract['schema'] == 'marici.nima.filler-phase-spectator.v1')
    paths = {name: REPO/path for name, path in contract['source'].items()}
    source_bytes = {p: p.read_bytes() for p in (Path(__file__).resolve(), CONTRACT, *paths.values())}
    protected = [OWNER/'results/gram-selection-principle-repaired.json',
                 OWNER/'results/entanglement-repaired.json',
                 REPO/'research/aspect/results/combined_bell_instrument.json',
                 OWNER/'results/bell-preparation-herald-record.json']
    receipts = {p: p.read_bytes() if p.exists() else None for p in protected}
    gram, quantum, instrument = [runpy.run_path(str(paths[name]))
                                  for name in ('fillers', 'states', 'instrument')]
    require('source-label-order', gram['CODES'] == list(product((False, True), repeat=2)))
    generators = {name: tuple(gram['code'](f(point)) for point in gram['CODES'])
                  for name, f in gram['FILLERS'].items()}
    require('all-five-source-functions', list(generators) == ['id', 'swap', 'twist', 'flip_fst', 'flip_both'])
    identity = tuple(range(4))
    group, frontier = {identity}, [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators.values():
            successor = compose(generator, current)
            if successor not in group:
                group.add(successor)
                frontier.append(successor)
    group = sorted(group)
    require('entire-source-permutation-group', group == list(permutations(range(4))))
    P = {g: matrix(g) for g in group}
    D = s.diag(1, 1, 1, z)
    U = {g: tidy(D*P[g]*dagger(D)) for g in group}
    cayley = []
    for g in group:
        require('unitarity', eq(dagger(U[g])*U[g], s.eye(4)))
        require('unchanged-character', s.trace(U[g]) == s.trace(P[g]))
        row = []
        for h in group:
            gh = compose(g, h)
            require('full-source-composition', eq(U[g]*U[h], U[gh]) and P[g]*P[h] == P[gh])
            require('scalar-character-composition', parity(gh) == parity(g)*parity(h))
            row.append(group.index(gh))
        cayley.append(row)
        for j in range(4):
            E = s.eye(4)[:, j]*s.eye(4)[:, j].T
            require('same-computational-effect-pullback', eq(dagger(U[g])*E*U[g], P[g].T*E*P[g]))
            require('scalar-sign-character-invisible', eq((parity(g)*U[g])*E*dagger(parity(g)*U[g]), U[g]*E*dagger(U[g])))
    require('identity-bypass-identical', U[identity] == s.eye(4))

    # Finite support for the universal strict-lift proof in the packet.
    # A stabilizer character factors through H/[H,H]; both characters extend.
    H = [g for g in group if g[0] == 0]
    commutators = {compose(compose(compose(g, h), inverse(g)), inverse(h)) for g, h in product(H, repeat=2)}
    require('stabilizer-and-abelianization', len(H) == 6 and len(commutators) == 3
            and all(parity(h) == 1 for h in commutators))
    require('commutator-set-is-subgroup', all(compose(g, h) in commutators for g, h in product(commutators, repeat=2)))
    section = {j: next(g for g in group if g[0] == j) for j in range(4)}
    factors = []
    for g, j in product(group, range(4)):
        h = compose(compose(inverse(section[g[j]]), g), section[j])
        require('complete-stabilizer-factorization', h in H and compose(g, section[j]) == compose(section[g[j]], h))
        factors.append({'g': list(g), 'j': j, 'h': list(h)})
    for exponent in (0, 1):
        require('both-stabilizer-characters-extend', all(parity(compose(g, h))**exponent ==
                parity(g)**exponent*parity(h)**exponent for g, h in product(H, repeat=2)))

    d0, d1, d2, d3 = s.symbols('d0 d1 d2 d3', nonzero=True)
    chi = d0*d3/(d1*d2)
    local = s.kronecker_product(s.diag(1, d2/d0), s.diag(1, d1/d0))
    require('all-diagonal-frames-reduce-to-one-phase', eq(s.diag(d0, d1, d2, d3), d0*local*s.diag(1, 1, 1, chi)))
    a0, a1, b0, b1 = s.symbols('a0 a1 b0 b1', nonzero=True)
    require('relative-phase-local-frame-invariant', s.cancel((a0*b0*d0)*(a1*b1*d3)/((a0*b1*d1)*(a1*b0*d2))-chi) == 0)

    I, X, Z = quantum['I2'], quantum['X'], quantum['Z']
    Y = s.I*X*Z
    A = [s.kronecker_product(M, I) for M in (X, Y, Z)]
    B = [s.kronecker_product(I, M) for M in (X, Y, Z)]
    flip = U[generators['flip_fst']]
    pulled_B = [tidy(dagger(flip)*M*flip) for M in B]
    spectator = [tidy(pull-original) for pull, original in zip(pulled_B, B)]
    signalling = [tidy(pull*local-local*pull) for pull, local in product(pulled_B, A)]
    spectator_gcd, signalling_gcd = residual_gcd(spectator), residual_gcd(signalling)
    require('spectator-preservation-iff', spectator_gcd == z-1)
    require('no-A-to-B-signalling-iff', signalling_gcd == z*z-1)
    require('canonical-flip-factorization', flip.subs(z, 1) == s.kronecker_product(X, I))
    require('pi-rival-is-product-but-not-spectator-identity', flip.subs(z, -1) == s.kronecker_product(X, Z))
    require('classical-spectator-always-fixed', spectator[2] == s.zeros(4))

    # Reuse actual supplied instrument functions; neither imported main runs.
    Q = instrument['Q']
    def to_Q(M):
        require('rational-instrument-input', all(v.is_Rational for v in M))
        return [[Q(Fraction(int(v.p), int(v.q))) for v in row] for row in M.tolist()]
    def from_Q(M):
        return s.Matrix([[s.Rational(v.rational.numerator, v.rational.denominator)
                          +s.sqrt(2)*s.Rational(v.root2.numerator, v.root2.denominator) for v in row] for row in M])
    prepared = {}
    for h in range(2):
        prepared[h] = from_Q(instrument['instrument'](to_Q(quantum['states']()['product00']), to_Q((I+(-1)**h*X)/2), False))
        K = s.kronecker_product(I, (I+(-1)**h*X)/2)
        require('actual-preparation-continuation', prepared[h] == K*quantum['states']()['product00']*K)
        require('both-branches-nonzero', s.trace(prepared[h]) == s.Rational(1, 2))
    probabilities, continuations, signed = {}, {}, {}
    for name, operator in (('bypass', s.eye(4)), ('H0', flip.subs(z, 1)), ('Hpi', flip.subs(z, -1))):
        table, states = {}, {}
        for h, a, b in product(range(2), (-1, 1), (-1, 1)):
            rho = operator*prepared[h]*operator.H
            pa, pb = (I+a*Z)/2, (I+b*X)/2
            actual = from_Q(instrument['joint_instrument'](to_Q(rho), to_Q(pa), to_Q(pb)))
            effect = s.kronecker_product(pa, pb)
            require('actual-joint-continuation', actual == effect*rho*effect)
            key = f'{h},{a},{b}'
            table[key], states[key] = s.trace(actual), actual
            require('positive-pairing', table[key] >= 0)
        require('complete-branch-normalization', sum(table.values()) == 1)
        probabilities[name], continuations[name] = table, states
        signed[name] = s.simplify(sum((-1)**h*b*table[f'{h},{a},{b}']
                                    for h, a, b in product(range(2), (-1, 1), (-1, 1))))
    require('fixed-attachment-discriminator', signed == {'bypass': 1, 'H0': 1, 'Hpi': -1})
    forgotten = sum(prepared.values(), s.zeros(4))
    require('forgetting-preparation-label-erases-test', flip.subs(z, 1)*forgotten*flip.subs(z, 1).H == flip.subs(z, -1)*forgotten*flip.subs(z, -1).H)

    covariance_cells = 0
    for g, h, a, b in product(group, range(2), (-1, 1), (-1, 1)):
        E = s.kronecker_product((I+a*Z)/2, (I+b*X)/2)
        Eprime, rhoprime = D*E*dagger(D), D*prepared[h]*dagger(D)
        transported = tidy(Eprime*U[g]*rhoprime*dagger(U[g])*Eprime)
        original = E*P[g]*prepared[h]*P[g].T*E
        require('full-instrument-gauge-covariance', eq(transported, D*original*dagger(D)))
        require('no-discriminator-after-complete-transport', s.cancel(s.trace(transported)-s.trace(original)) == 0)
        covariance_cells += 1
    require('complete-gauge-control', covariance_cells == 192)
    rejected = False
    try:
        require('deliberate-false-classical-selection', flip.subs(z, -1) == flip.subs(z, 1))
    except AssertionError:
        rejected = True
    require('classical-selection-promotion-rejected', rejected)
    require('source-bytes-preserved', all(p.read_bytes() == data for p, data in source_bytes.items()))
    require('foreign-and-predecessor-receipts-preserved', all((p.read_bytes() if p.exists() else None) == data for p, data in receipts.items()))
    result = {'schema': 'marici.nima.filler-phase-spectator-result.v1', 'status': 'pass',
              'classification': 'strict-source-lifts-leave-a-relative-phase-selected-only-by-fixed-spectator-attachments',
              'strength': 'exact finite group and Laurent residual checks supporting the stated strict-lift proof; conditional ordinary-QM discriminator, not physical selection evidence',
              'source_functions': {name: list(g) for name, g in generators.items()},
              'group': [list(g) for g in group], 'cayley_table': cayley,
              'stabilizer': [list(g) for g in H], 'commutator_subgroup': [list(g) for g in sorted(commutators)],
              'stabilizer_factorizations': factors, 'relative_phase': str(chi),
              'flip_fst': encode(flip), 'spectator_residual_gcd': str(spectator_gcd),
              'no_signalling_residual_gcd': str(signalling_gcd),
              'prepared_branches': {str(h): encode(rho) for h, rho in prepared.items()},
              'full_probabilities': {name: {k: str(v) for k, v in table.items()} for name, table in probabilities.items()},
              'full_continuations': {name: {k: encode(v) for k, v in table.items()} for name, table in continuations.items()},
              'branch_signed_X_B': {name: str(value) for name, value in signed.items()},
              'gauge_covariance_cells': covariance_cells, 'checks_passed': len(CHECKS),
              'scope': contract['scope'],
              'source_sha256': {p.relative_to(REPO).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (Path(__file__).resolve(), CONTRACT, *paths.values())}}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'classification', 'spectator_residual_gcd',
                       'no_signalling_residual_gcd', 'branch_signed_X_B', 'gauge_covariance_cells', 'checks_passed')}, indent=2))


if __name__ == '__main__':
    main()
