"""Exact image obstruction for the declared retained unitary Tick annotations.

Reuses the source-backed native square, not the quarantined general audit.
The full Bool Tick is retained mathematically; Python does not evaluate Agda
records. Universal image claims use exact polynomial coefficient identities.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import check_native_square_controlled_hamiltonian as native

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/tick-unitary-image-nonuniqueness.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    source = native.main()
I, L, R = (source[k] for k in ('I', 'L', 'R'))
PL, PR, joints = (source[k] for k in ('PL', 'PR', 'joints'))
M = native.mm(PL, PR)
ONE, ZERO = native.ONE, native.ZERO
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


proof = json.loads((ROOT/'results/agda-TickRetainedStructure.json').read_text(encoding='utf-8-sig'))
check('full-Tick-classification-closure', proof['passed'] and proof['ignore_interfaces']
      and proof['inputs_stable_during_check'])
check('classification-source-current', proof['source_sha256'] == hashlib.sha256(
    (ROOT/'agda/TickRetainedStructure.agda').read_bytes()).hexdigest())


def generators(k):
    return native.add(PL, native.scale(k, M)), native.add(PR, native.scale(k, M))


def E(k, z, w):
    # Orthogonal joint spectral projectors give the whole analytic formula.
    return tuple(tuple(native.zsum(native.zscale(native.zmul(
        native.power(z, l+k*l*r), native.power(w, r+k*l*r)), J[i][j])
        for (l, r), J in joints.items()) for j in range(4)) for i in range(4))


def amplitude_determinant(state):
    return native.zadd(native.zmul(state[0], state[3]),
                       native.zscale(native.zmul(state[1], state[2]), -1))


# Polynomial arithmetic in independent complex parameters z,w. No grid-to-
# continuum inference: coefficient cancellation proves the baseline invariant.
def padd(a, b, sign=1):
    out = dict(a)
    for power, value in b.items():
        out[power] = out.get(power, F(0)) + sign*value
    return {power: value for power, value in out.items() if value}


def pmul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            power = (i+k, j+l)
            out[power] = out.get(power, F(0)) + x*y
    return {power: value for power, value in out.items() if value}


for speed in (1, 3):
    for s in range(4):
        coeff = [{(speed*l, speed*r): J[i][s] for (l, r), J in joints.items()}
                 for i in range(4)]
        determinant = padd(pmul(coeff[0], coeff[3]), pmul(coeff[1], coeff[2]), -1)
        check(f'all-parameter-product-invariant/{speed}/{s}', determinant == {})

ci = native.cm(I)
minus = native.zscale(ONE, -1)
roots = source['roots']
swap = source['swap']
for k in (0, 2):
    HL, HR = generators(k)
    check(f'Hermitian/{k}', native.transpose(HL) == HL and native.transpose(HR) == HR)
    check(f'commuting/{k}', native.mm(HL, HR) == native.mm(HR, HL))
    check(f'axis-symmetry/{k}', native.mm(native.mm(swap, HL), swap) == HR)
    for (l, r), J in joints.items():
        check(f'exact-nonnegative-joint-eigenvalues/{k}/{l}/{r}',
              native.mm(HL, J) == native.scale(l+k*l*r, J)
              and native.mm(HR, J) == native.scale(r+k*l*r, J)
              and l+k*l*r >= 0 and r+k*l*r >= 0)
    for a, b in product((0, 1), repeat=2):
        want = I if (a, b) == (0, 0) else L if (a, b) == (1, 0) else R if (a, b) == (0, 1) else native.mm(L, R)
        check(f'corner/{k}/{a}/{b}', E(k, minus if a else ONE, minus if b else ONE) == native.cm(want))
    for n, (z, w) in enumerate(product(roots, repeat=2)):
        U = E(k, z, w)
        check(f'unitary/{k}/{n}', native.cmm(native.adj(U), U) == ci)
        check(f'group-law-control/{k}/{n}', native.cmm(U, E(k, roots[1], roots[2]))
              == E(k, native.zmul(z, roots[1]), native.zmul(w, roots[2])))
        check(f'reflected-square/{k}/{n}',
              E(k, native.zscale(native.zconj(z), -1), native.zscale(native.zconj(w), -1))
              == native.cmm(native.cm(native.mm(L, R)), native.adj(U)))
        if k == 0:
            check(f'unchanged-predecessor-family/{n}', U == source['E'](z, w))

witnesses = []
for s in range(4):
    seed = tuple(ONE if i == s else ZERO for i in range(4))
    for first in ('leftFirst', 'rightFirst'):
        z, w = (roots[1], ONE) if first == 'leftFirst' else (ONE, roots[1])
        state = native.mv(E(2, z, w), seed)
        determinant = amplitude_determinant(state)
        check(f'outside-whole-baseline-image/{s}/{first}', native.znorm(determinant) == F(3, 16))
        check(f'normalized-rival-state/{s}/{first}', native.norm(state) == 1)
        for phase in roots:
            moved = tuple(native.zmul(phase, value) for value in state)
            check(f'phase-control/{s}/{first}/{phase}',
                  amplitude_determinant(moved) == native.zmul(native.power(phase, 2), determinant))
        # Both possible comparison tags remain admissible, including repetition.
        for second in ('leftFirst', 'rightFirst'):
            for k in (0, 2):
                end = native.cmm(E(k, ONE, minus), E(k, minus, ONE)) if second == 'leftFirst' else native.cmm(E(k, minus, ONE), E(k, ONE, minus))
                check(f'comparison-tag-endpoint/{s}/{first}/{second}/{k}',
                      native.mv(end, seed) == native.mv(native.cm(native.mm(L, R)), seed))
        witnesses.append({'source': s, 'schedule': first,
                          'determinant_Q_i_sqrt3': list(map(str, determinant)),
                          'determinant_squared_norm': str(native.znorm(determinant))})

# Expose the omitted locality axiom rather than claiming the rival satisfies it.
# A first-axis operator confined to the first tensor factor must commute with
# every second-factor observable, in particular the second-bit Z operator.
Zright = tuple(tuple(F((1 if j % 2 == 0 else -1) if i == j else 0)
                     for j in range(4)) for i in range(4))
HL, _ = generators(2)
check('baseline-tensor-locality', native.mm(PL, Zright) == native.mm(Zright, PL))
locality_defect = native.add(native.mm(HL, Zright), native.scale(-1, native.mm(Zright, HL)))
check('rival-not-tensor-local', any(x for row in locality_defect for x in row))
check('odd-mixed-coefficient-refused', E(1, minus, ONE) != native.cm(L))
refused = False
try:
    check('deliberate-failure', False)
except AssertionError:
    refused = True
check('required-failure-gate', refused)

files = [Path(__file__), ROOT/'checkers/check_native_square_controlled_hamiltonian.py',
         ROOT/'checkers/check_triangle_half_phase.py', ROOT/'agda/TickRetainedStructure.agda',
         ROOT/'agda/NativeSquareHamiltonianSkeleton.agda', ROOT/'agda/ObserverCoherenceCube.agda']
result = {
    'schema': 'marici.nima.tick-unitary-image-nonuniqueness.v1', 'status': 'pass',
    'scientific_disposition': 'nonuniqueness-beyond-parameter-and-overall-phase-in-declared-unitary-annotation-class',
    'arithmetic': 'Fractions in Q(i*sqrt(3)); exact polynomial coefficient identity',
    'generators': {'baseline': ['PL', 'PR'], 'rival': ['PL+2*PLPR', 'PR+2*PLPR']},
    'universal_invariant': 'baseline amplitude determinant identically zero for all complex z,w and every source basis vector',
    'rival_obstruction': 'squared determinant 3/16 at first-axis angle pi/3; outside baseline image for ANY real angle pair, even up to phase',
    'witnesses': witnesses, 'checks': checks, 'check_count': len(checks),
    'retention_boundary': 'entire native Tick retained as structural component; Python checks analytic tag-indexed data, not Agda terms or a functor on dependent return sections',
    'scope': 'not unique dynamics under every additional axiom, not a physical Hamiltonian selection theorem; tensor-locality would exclude this rival',
    'source_sha256': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
}
OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'PASS: {len(checks)} exact controls; product-image invariant 0 versus squared determinant 3/16')
