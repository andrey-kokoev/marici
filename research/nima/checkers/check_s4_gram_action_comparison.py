"""Exact comparison of the original full S4 Gram and completed witness actions.
Run: uv run --with sympy python research/nima/checkers/check_s4_gram_action_comparison.py
No historical receipt writes; no physical gauge or matter selection asserted.
"""
import ast
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import runpy
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT/'quarantine/20261007-s4-evidence'
CHECKS = []
PREDECESSORS = [
    'check_carrier_doublet_singlet_split.py', 'check_witness_stabilizer_doublet.py',
    'check_witness_gauge_assignment.py', 'check_witness_charge_operator.py',
    'check_gram_preserving_charge_family.py', 'check_gram_gauge_kinetic_weights.py']


def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def equal(a, b):
    return (a-b).applyfunc(s.simplify) == s.zeros(*a.shape)


def load_original():
    path = ARCHIVE/'checkers/check_baryonic_matter.py'
    tree = ast.parse(path.read_text(encoding='utf-8'))
    body = []
    suppressed = 0
    for node in tree.body:
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Attribute)
                and isinstance(node.value.func.value, ast.Name)
                and node.value.func.value.id == 'out' and node.value.func.attr == 'write_text'):
            suppressed += 1
        else:
            body.append(node)
    require('one-known-historical-write-suppressed', suppressed == 1)
    tree.body = body
    ns = {'__file__': str(path), '__name__': '_historical_diagnostic_'}
    with redirect_stdout(io.StringIO()):
        exec(compile(tree, str(path), 'exec'), ns)
    return ns


def mul(p, q):
    return tuple(p[q[i]] for i in range(4))


def inv(p):
    return tuple(p.index(i) for i in range(4))


def main():
    out = ROOT/'results/s4-gram-action-comparison.json'
    out.unlink(missing_ok=True)
    CHECKS.clear()
    for line in (ARCHIVE/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        digest, path = line.split(maxsplit=1)
        path = path.lstrip('*')
        require('archive:' + path, hashlib.sha256((ARCHIVE/path).read_bytes()).hexdigest() == digest)
    historical_receipt = ROOT/'results/baryonic-matter-bridge.json'
    before = historical_receipt.read_bytes() if historical_receipt.exists() else None
    prior = {}
    with redirect_stdout(io.StringIO()):
        for name in PREDECESSORS:
            prior[name] = runpy.run_path(str(ROOT/'checkers'/name))
        current = runpy.run_path(str(ROOT/'checkers/check_baryonic_matter.py'))
    require('completed-predecessors-rerun', len(prior) == 6)
    old = load_original()
    require('full-old-data-preserved', all(old[k] == current[k]
            for k in ('s4', 'G', 'char_table', 'class_sizes')))
    perms = current['s4']
    index = {p: i for i, p in enumerate(perms)}
    P = [s.Matrix(4, 4, lambda i, j: int(i == p[j])) for p in perms]
    require('source-composition', all(P[index[mul(g,h)]] == P[i]*P[j]
            for i,g in enumerate(perms) for j,h in enumerate(perms)))
    Phi = s.Matrix.hstack(*(s.Matrix(list(p)) for p in P))
    K = s.Matrix(old['G'])
    require('actual-Gram-factorization', K == Phi.T*Phi)
    E0 = s.ones(24)/24
    E3 = (K-24*E0)/8
    Ez = s.eye(24)-E0-E3
    for name, e, rank in [('trivial', E0, 1), ('standard', E3, 9), ('kernel', Ez, 14)]:
        require('spectral-projector:' + name, e.T == e and e*e == e and s.trace(e) == rank)
    require('spectral-projectors-orthogonal', E0*E3 == s.zeros(24))
    require('kernel-exact', Phi*Ez == s.zeros(16, 24) and Phi.rank() == 10)
    quotient = E0+E3
    chars = {'left': [], 'conjugation': []}
    for mode in chars:
        for g in perms:
            moved = [index[mul(g,h) if mode == 'left' else mul(mul(g,h),inv(g))] for h in perms]
            require('quotient-invariant:' + mode + ':' + str(index[g]),
                    quotient.extract(moved, moved) == quotient)
            chars[mode].append(sum(quotient[i,moved[i]] for i in range(24)))
    multiplicities = {}
    for mode, character in chars.items():
        multiplicities[mode] = {name: s.simplify(sum(character[i]*chi[current['conj_class'](g)]
                      for i,g in enumerate(perms))/24) for name,chi in current['char_table'].items()}
    require('left-quotient-content', multiplicities['left'] ==
            {'Triv': 1, 'Sign': 0, 'Std2': 0, 'Std3a': 3, 'Std3b': 0})
    require('conjugation-quotient-content', multiplicities['conjugation'] ==
            {'Triv': 2, 'Sign': 0, 'Std2': 1, 'Std3a': 1, 'Std3b': 1})

    # Explicit operator doublet, not a four-point state decomposition.
    doubles = [i for i,g in enumerate(perms) if current['conj_class'](g) == 2]
    Z1, Z2 = P[doubles[0]]-P[doubles[1]], P[doubles[0]]-P[doubles[2]]
    require('operator-doublet-nonzero', s.Matrix.hstack(s.Matrix(list(Z1)), s.Matrix(list(Z2))).rank() == 2)
    require('operator-doublet-character', all(
        sum(mul(mul(g,perms[d]), inv(g)) == perms[d] for d in doubles)-1
        == current['char_table']['Std2'][current['conj_class'](g)] for g in perms))

    I = s.eye(4)
    Pu = s.ones(4)/4
    Ps = I-Pu
    carrier_gram = 11*I+s.ones(4)
    require('image-in-carrier-Gram-commutant', all(p*carrier_gram == carrier_gram*p for p in P))
    # Inclusion plus rank 10 equals the 1^2+3^2 dimensional block commutant.
    require('commutant-dimension-matched', Phi.rank() == 1**2+3**2)
    witness = prior['check_witness_stabilizer_doublet.py']
    u, v = s.Matrix(witness['u']), s.Matrix(witness['v'])
    B = s.Matrix.hstack(u/2, v/s.sqrt(12), s.Matrix([0,1,-1,0])/s.sqrt(2),
                       s.Matrix([0,1,1,-2])/s.sqrt(6))
    require('actual-witness-basis-orthonormal', equal(B.T*B,I))
    family = prior['check_gram_preserving_charge_family.py']
    require('actual-carrier-Gram-compared', equal(B*s.diag(*family['G'])*B.T, carrier_gram))
    def lift_diagonal(values):
        return (B*s.diag(*values)*B.T).applyfunc(s.simplify)
    operators = {key: lift_diagonal(family[key]) for key in ('Q0', 'Qw', 'T3')}
    a1, a2 = s.zeros(4), s.zeros(4)
    a1[2,3] = a1[3,2] = s.Rational(1,2)
    a2[2,3], a2[3,2] = -s.I/2, s.I/2
    operators.update(T1=B*a1*B.T, T2=B*a2*B.T)
    for a,b,c in [('T1','T2','T3'), ('T2','T3','T1'), ('T3','T1','T2')]:
        require('weak-Lie-bracket:' + a+b, equal(operators[a]*operators[b]-operators[b]*operators[a], s.I*operators[c]))
    def coefficients(X):
        weighted = Pu*X*Pu/24+Ps*X*Ps/8
        return [(p.T*weighted).trace().simplify() for p in P]
    def reconstruct(X):
        return sum((c*p for c,p in zip(coefficients(X),P)), s.zeros(4)).applyfunc(s.simplify)
    for name, X in operators.items():
        require('full-Gram-lift:' + name, equal(reconstruct(X), X))
    Yraw = s.Matrix(prior['check_witness_charge_operator.py']['Y'])
    Ypin = lift_diagonal(family['Ypin'])
    require('pinching-is-operator-image-projection', equal(reconstruct(Yraw), Ypin)
            and equal(Ypin, Pu*Yraw*Pu+Ps*Yraw*Ps) and not equal(Yraw,Ypin))
    error = Yraw-Ypin
    require('unpinched-obstruction-nonzero', s.simplify(s.trace(error.T*error)) == s.Rational(3,8))
    require('S3-witness-still-reduces-symmetry', sum(g[0] == 0 for g in perms) == 6)
    caught = False
    try:
        require('injected-false-faithful-regular-Gram', Ez == s.zeros(24))
    except AssertionError:
        caught = True
    require('failure-gate-refuses-regular-misidentification', caught)
    require('historical-receipt-untouched', before ==
            (historical_receipt.read_bytes() if historical_receipt.exists() else None))
    sources = [Path(__file__).resolve(), ROOT/'checkers/check_baryonic_matter.py',
               ARCHIVE/'checkers/check_baryonic_matter.py', ARCHIVE/'SHA256SUMS',
               ROOT/'weak-doublet-singlet-weight-and-s4-representation-audit.md']
    sources += [ROOT/'checkers'/name for name in PREDECESSORS]
    result = {
        'schema': 'marici.nima.s4-gram-action-comparison.v1', 'status': 'pass',
        'scientific_disposition': 'operator-comparison-constructed; old-matter-identification-withdrawn; prior-underdetermination-retained',
        'gram_spectrum': {'24': 1, '8': 9, '0': 14},
        'matrix_coefficient_map_shape': [16,24], 'rank': 10,
        'quotient_multiplicities': {mode: {k:int(v) for k,v in d.items()} for mode,d in multiplicities.items()},
        'operator_image': 'Comm(11I+J) = C direct-sum M3(C)',
        'lift_formula': 'c_g=Tr(P_g^*(Pu X Pu/24 + Ps X Ps/8))',
        'lifted_completed_operators': sorted(operators),
        'unpinched_charge_projection_error_squared': '3/8',
        'scope': 'Declared complex permutation-operator realization. Conjugation doublet is not a matter doublet; witness SU2 remains a supplied continuous extension. No physical charge, gauge group, matter count, generation count or weak angle is selected.',
        'checks': CHECKS, 'check_count': len(CHECKS),
        'source_sha256': {str(p.relative_to(ROOT)).replace('\\','/'):
                          hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','scientific_disposition','gram_spectrum','quotient_multiplicities','check_count')},indent=2))


if __name__ == '__main__':
    main()
