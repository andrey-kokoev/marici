"""Source-bound mixed-Poisson-rank obstruction, not a new mechanical model.

Reruns the strongest existing shared all-port recoil implementation. Brackets
are on the full inherited source, NOT unconstrained ambient body coordinates.
Exit zero means the stated obstruction and its scope controls are verified.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'results/old-spatial-recoil-poisson-obstruction.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    recoil = runpy.run_path(str(HERE / 'check_shared_recoil_cotangent_binding.py'))
canon = recoil['canon']
R, q, p = canon['R'], canon['q'], canon['p']
coords = canon['coords']  # R, phi, q[6], p[6]
K, Ki, mu = canon['K'], canon['Ki'], canon['mu']
A, W = canon['X'], canon['W']
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def expand(matrix):
    return matrix.applyfunc(S.expand)


def strings(matrix):
    return [[str(x) for x in matrix.row(i)] for i in range(matrix.rows)]


# The existing change matrix maps (phi,-Q,q,p) tangents to (R,phi,q,p).
# With {q,p}=+I the Poisson matrix is -Omega^{-1}, not Omega^{-1}.
change = canon['change']
poisson = expand(change * canon['expected_canonical'] * change.T)
check('full-source-form-inverse', expand(canon['Omega'] * poisson) == -S.eye(14))
check('full-poisson-skew', poisson.T == -poisson)
check('canonical-sign', poisson[2:8, 8:14] == S.eye(6))

x = A*q
momentum = recoil['Cp'] * S.Matrix([R, *q, *p])
Q, phi = canon['charge'], coords[1]
readings = momentum.col_join(S.Matrix([Q, phi]))
dx = x.jacobian(coords)
dy = readings.jacobian(coords)
mixed = expand(dx * poisson * dy.T)
v = -A*Ki*p/(4*mu*R)
w = recoil['Br'].col_join(S.zeros(2, 1))
check('whole-reader-mixed-bracket-factorization', expand(mixed-v*w.T) == S.zeros(3, 14))
check('reference-pair-does-not-add-directions', mixed[:, 12:] == S.zeros(3, 2))
check('nontrivial-recoil-anchor-direction', recoil['Br'] != S.zeros(12, 1))
check('spatial-rank-is-three', A.rank() == 3)
# For ANY C1 triple f(readings), Df is 3x14. The chain rule gives
# {x,f}=mixed*Df^T=v*(w^T*Df^T), hence rank <=1, never I_3.
# This analytic implication, not a sample census, supplies the quantifier.

# Existing positive alternative on the SAME source: (Aq,Wp).
canonical_momentum = W*p
dcanonical = canonical_momentum.jacobian(coords)
check('existing-canonical-pair-retained', expand(dx*poisson*dcanonical.T) == S.eye(3))
check('existing-momenta-commute', expand(dcanonical*poisson*dcanonical.T) == S.zeros(3))
check('existing-positions-commute', expand(dx*poisson*dx.T) == S.zeros(3))

# Full-domain witness with v=-e_1: the answer is rank ONE, not identically zero.
q0 = S.zeros(6, 1)
p0 = 4*mu*K*W.T*S.eye(3)[:, 0]
Q0 = S.simplify(mu + canon['active_budget'](q0, p0))
trial = canon['Chart'](1, Q0, S.ImmutableMatrix(q0), S.ImmutableMatrix(p0), None)
eta, _ = canon['from_chart'](trial)
check('nonzero-bracket-witness-in-source-domain', eta[0] == 1 and Q0 > 0)
trial_body = recoil['to_body'](trial)
check('strong-recoil-roundtrip', recoil['from_body'](trial_body) == trial)
sub = {R: 1, phi: 0, **dict(zip(q, q0)), **dict(zip(p, p0))}
nonzero_mixed = expand(mixed.subs(sub))
check('full-domain-mixed-rank-one', nonzero_mixed.rank() == 1)
check('sharp-mixed-direction', expand(v.subs(sub)) == -S.eye(3)[:, 0])

# Hostile to an overstrong zero-bracket claim: falsely fixing the reference
# kills the REAL RECOIL mixed bracket, and is not the full form's inverse.
frozen_anchor_poisson = S.diag(S.zeros(2), canon['J'](6))
naive = dx*frozen_anchor_poisson*momentum.jacobian(coords).T
check('silent-anchor-fixing-loses-nonzero-response', naive == S.zeros(3, 12)
      and nonzero_mixed[:, :12] != S.zeros(3, 12))
check('dropped-reference-is-not-source-inverse',
      expand(canon['Omega']*frozen_anchor_poisson) != -S.eye(14))

# Same recoil readings AND same full reference pair, different known canonical
# momentum. This is a full-state-domain witness, not two asserted native words.
minus = canon['Chart'](1, Q0, S.ImmutableMatrix(q0), S.ImmutableMatrix(-p0), None)
minus_body = recoil['to_body'](minus)
check('reader-fiber-hostile-same-momenta', minus_body.momentum == trial_body.momentum)
check('reader-fiber-hostile-same-reference', minus.phase == trial.phase and minus.charge == trial.charge)
check('reader-fiber-hostile-distinct-canonical-momentum', W*p0 != -W*p0)
check('reader-fiber-hostile-retained-configurations-differ', minus_body.position != trial_body.position)

# Also use an actual registered source endpoint; no arbitrary-state witness is
# substituted for the native path census. All 68 were rerun by the predecessor.
endpoint = next(packet for packet in canon['packets'] if packet.record[2] == 2)
endpoint_body = recoil['to_body'](endpoint)
restored = recoil['from_body'](endpoint_body)
check('actual-endpoint-record-identity', restored.record is endpoint.record)
end_sub = {R: 1, **dict(zip(q, endpoint.q)), **dict(zip(p, endpoint.p))}
check('actual-endpoint-mixed-bracket-zero', expand(mixed.subs(end_sub)) == S.zeros(3, 14))
family, slot, sample = endpoint.record
word = [edge[2] for edge in family.paths[slot]]

# Failure gate control without executing or weakening the scientific predicates.
refused = False
try:
    check('deliberately-false-property', False)
except AssertionError:
    refused = True
check('false-required-property-refused', refused)

hashes = dict(recoil['result']['source_sha256'])
hashes[str(Path(__file__).relative_to(ROOT))] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
result = {
    'schema': 'marici.nima.old-spatial-recoil-poisson-obstruction.v1',
    'status': 'pass', 'scientific_disposition': 'joint-canonical-reading-excluded-in-declared-reader-class',
    'question': 'Can x=Aq have three canonical momenta f(P0,pi,Q,phi)?',
    'domain': 'full nonzero-anchor source chart R>0; all six q,p pairs and reference pair retained',
    'reader_class': 'C1 functions of all 12 real recoil momenta and the reference pair (Q,phi)',
    'poisson_convention': '{q_i,p_j}=delta_ij; {phi,Q}=-1; Pi=-Omega^-1',
    'mixed_bracket': '-(A*K^-1*p)/(4*mu*R) * (b^T,b^T,0,0)',
    'rank_bound': 1, 'canonical_rank_required': 3,
    'rank_strata': {'rank_1': 'A*K^-1*p != 0', 'rank_0': 'A*K^-1*p == 0'},
    'nonlinear_extension': 'chain rule: {x,f}=v*(w^T*Df^T); rank at most one for every admitted C1 triple',
    'generic_witness': {'R': '1', 'q': list(map(str, q0)), 'p': list(map(str, p0)), 'Q': str(Q0),
                        'mixed_bracket': strings(nonzero_mixed), 'rank': nonzero_mixed.rank()},
    'actual_endpoint': {'word': word, 'sample': sample, 'rank': 0, 'record_identity_preserved': True},
    'surviving_alternative': 'existing (Aq,Wp) is canonical but Wp does not factor through the admitted recoil/reference readings',
    'not_claimed': ['no mechanics', 'no physical joint reading with noncanonical brackets',
                    'physical position or momentum selected', 'zero-anchor extension',
                    'new native proof root or NumPy/137-port comparison'],
    'checks': checks, 'check_count': len(checks),
    'upstream_checks': {'shared_recoil': recoil['result']['check_count'], **recoil['result']['upstream_checks']},
    'source_sha256': hashes,
}
OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print('PASS: mixed Poisson rank <= 1, required canonical rank 3; nonlinear recoil/reference readers excluded')
print(f'{len(checks)} source-bound controls; full shared-recoil predecessor rerun')
