"""Test the tempting axis-wise attachment against the ACTUAL square face.
The source square has equal left/right schedules. Kick and free drift do
not commute on observable positions; a whole-Tick policy is weaker than
an interpretation preserving that face. No native impossibility claimed.
"""
from pathlib import Path
import hashlib
import json
import sympy as S
from check_retained_interaction_pipeline import (
    State, F, ZERO, c, initial, add, scale, impulse, energy, kinetic)

ROOT = Path(__file__).resolve().parents[1]
proof_path = ROOT/'results/agda-RetainedTickStateAction.json'
proof = json.loads(proof_path.read_text(encoding='utf-8-sig'))
source_path = ROOT/'agda/RetainedTickStateAction.agda'
assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
assert proof['source_sha256'] == hashlib.sha256(source_path.read_bytes()).hexdigest()


def kick(s):
    j, k = impulse(c.q1, c.q2, c.kernel)
    p1, p2 = add(s.p1, j), add(s.p2, k)
    work = energy(p1, c.m1)+energy(p2, c.m2)-kinetic(s, c)
    return State(s.x1, s.x2, p1, p2, s.supply-work)


def drift(s, tau):
    return State(add(s.x1, scale(tau/c.m1, s.p1)),
                 add(s.x2, scale(tau/c.m2, s.p2)), s.p1, s.p2, s.supply)


left_first = drift(kick(initial), F(1))
right_first = kick(drift(initial, F(1)))
assert left_first.p1 == right_first.p1 and left_first.p2 == right_first.p2
assert left_first.supply == right_first.supply
assert left_first.x1 != right_first.x1 and left_first.x2 != right_first.x2
assert left_first.x1 == (F(-1), F(-2), F(1))
assert left_first.x2 == (F(2, 3), F(4, 3), F(-2, 3))
assert right_first.x1 == right_first.x2 == ZERO

# Universal affine calculation on six canonical position/momentum pairs.
x = S.Matrix(S.symbols('x0:6'))
p = S.Matrix(S.symbols('p0:6'))
j = S.Matrix(S.symbols('j0:6'))
a = S.Matrix(S.symbols('a0:6', positive=True))
tau = S.symbols('tau', positive=True)
Minv = S.diag(*a)
x_kd = x+tau*Minv*(p+j)
x_dk = x+tau*Minv*p
residual = S.expand(x_kd-x_dk)
assert residual == tau*Minv*j
assert (tau*Minv).det() != 0

result = {
    'schema': 'marici.nima.tick-interaction-attachment.v1',
    'status': 'pass',
    'candidate_disposition': 'axis identification rejected: nonzero commuting-face residual',
    'candidate': 'source left axis -> physical kick; source right axis -> free drift',
    'source_requirement': 'both schedules have equal realized target',
    'physical_residual': 'delta position = tau * inverse_mass * balanced_impulse; momentum and supply residuals vanish',
    'fixture_position_residual': [[str(v) for v in left_first.x1], [str(v) for v in left_first.x2]],
    'nondegenerate_boundary': 'positive masses and positive duration imply residual zero only for zero impulse',
    'formal_result': 'actual Tick histories act and survive cone encoding for any supplied whole-Tick step policy',
    'distinction': 'a list action on complete records does not by itself interpret the internal square face',
    'next_requirement': 'supply an internal realization that preserves the source face, or justify a changed target comparison; do not discard positions silently',
    'scope': 'one natural axis assignment rejected; neither all physical realizations nor all WG source sectors excluded',
    'formal_receipt_sha256': hashlib.sha256(proof_path.read_bytes()).hexdigest(),
}
(ROOT/'results/tick-interaction-attachment.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print('PASS: native action receipt checked; exact candidate face residual retained.')
print('REJECTED: kick/drift as commuting source axes when position remains observable.')
