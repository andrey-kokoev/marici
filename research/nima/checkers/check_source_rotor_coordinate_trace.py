"""Reconnect prior q,p,angular-clock construction to its actual source sector.

Symbolic checks only. The real Clifford product, rotor enlargement, phase
module and lift remain declared. No identification with the rung-4 137-row
fixture or physical unit calibration is manufactured here.
"""
from pathlib import Path
import hashlib
import json
import re
import sympy as S
import check_clifford_retained_order as old

ROOT = Path(__file__).resolve().parents[1]
source_path = ROOT / "agda" / "RetainedComparisonSeries.agda"
text = source_path.read_text(encoding="utf-8")
match = re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$', text, re.M)
assert match is not None
image = tuple(map(int, match.groups()))

anchor, odd = S.Matrix([1, 0, 0, 0]), S.Matrix([0, 1, -1, 0])
B = S.Matrix.hstack(*(S.kronecker_product(a, b)
                     for a, b in ((anchor, anchor), (anchor, odd), (odd, anchor), (odd, odd))))
G = B.T * B
C = G.inv() * B.T
P = B*C
checks = []


def check(name, statement):
    if not statement:
        raise AssertionError(name)
    checks.append(name)


check("source-counting-Gram", G == S.diag(1, 2, 2, 4))
check("coordinate-extraction-left-inverse", C*B == S.eye(4))
check("active-sector-orthogonal-projector", P*P == P and P.T == P and P.rank() == 4)
left = S.zeros(16)
right = S.zeros(16)
for x in range(4):
    for y in range(4):
        left[4*x+y, 4*image[x]+y] = 1
        right[4*x+y, 4*x+image[y]] = 1
check("left-source-action", left*B == B*S.diag(1, 1, -1, -1))
check("right-source-action", right*B == B*S.diag(1, -1, 1, -1))

I, E1, E2, J = (S.Matrix(2, 2, b) for b in old.BASIS)
s, q, p, z, theta, eta = S.symbols("s q p z theta eta", real=True)
kappa = S.symbols("kappa", positive=True)
phi = S.symbols("phi", real=True)
coordinates = S.Matrix([s, q, p, z])
X = B*coordinates
Q = s*I+q*E1+p*E2+z*J
coeff = lambda M: S.Matrix([(M[0, 0]+M[1, 1])/2, (M[0, 0]-M[1, 1])/2,
                            (M[0, 1]+M[1, 0])/2, (M[0, 1]-M[1, 0])/2])
U = lambda a: S.cos(a)*I+S.sin(a)*J
A = lambda a: S.simplify(S.Matrix.hstack(*(coeff(U(a)*b*U(-a)) for b in (I, E1, E2, J))))
D = S.Matrix.hstack(*(coeff(J*b-b*J) for b in (I, E1, E2, J)))
check("actual-coefficients-recovered", C*X == coordinates)
check("source-coefficient-q", (C*X)[1] == q)
check("source-coefficient-p", (C*X)[2] == p)
check("conditional-rotor-generator", D*coordinates == S.Matrix([0, 2*p, -2*q, 0]))
check("rotor-also-preserves-source-counting-metric", S.trigsimp(A(theta).T*G*A(theta)-G) == S.zeros(4))

# On the q,p plane the ACTUAL inherited counting metric is 2I. It supports
# a symplectic form, once the rotor's oriented quarter-turn is supplied.
J2 = S.Matrix([[0, 1], [-1, 0]])
Omega2 = 2*J2
D2 = 2*J2
v2 = S.Matrix([q, p])
Hcount = 2*(q*q+p*p)
check("counting-plane-Hamiltonian", (D2*v2).T*Omega2 == S.Matrix([[S.diff(Hcount, q), S.diff(Hcount, p)]]))
# Canonical coordinates can be q_c=q, p_c=2p rather than silently replacing
# the inherited metric with the Clifford coefficient metric.
R = S.diag(1, 2)
p_c = S.symbols("p_c", real=True)
Hcanonical = 2*q*q+p_c*p_c/2
check("canonical-rescaling-form", R.T*J2*R == Omega2)
check("canonical-equations", R*D2*v2 == S.Matrix([S.diff(Hcanonical, p_c).subs(p_c, 2*p), -S.diff(Hcanonical, q)]))
check("canonical-energy-same-counting-H", Hcanonical.subs(p_c, 2*p) == Hcount)

# Pull back the active form without pretending it is nondegenerate on all
# 16 source coordinates. The remaining 14 directions are in its radical.
active = C[1:3, :]
OmegaSource = active.T*Omega2*active
check("source-presymplectic-rank", OmegaSource.rank() == 2 and OmegaSource.T == -OmegaSource)
check("source-reversers-antisymplectic", left.T*OmegaSource*left == right.T*OmegaSource*right == -OmegaSource)

F = (q*p+s*z)/2
T = F/kappa-phi
newcoords = A(theta)*coordinates
Fnew = (newcoords[1]*newcoords[2]+newcoords[0]*newcoords[3])/2
phinew = phi+(Fnew-F)/kappa-theta
check("clock-extracted-from-retained-phase", S.simplify(Fnew/kappa-phinew-T) == theta)
check("clock-rate-one", S.diff(T+theta, theta) == 1)
check("endpoint-cannot-recover-clock", A(2*S.pi) == S.eye(4) and U(2*S.pi) == I and 2*S.pi != 0)
# Full 4D coefficient metric mismatch remains visible.
check("full-metric-is-not-Clifford-isometry", G != S.eye(4))

out = {
    "schema": "marici.nima.source-rotor-coordinate-trace.v1",
    "status": "pass", "checks": checks,
    "source_basis": "e00 tensor e00, e00 tensor (e01-e10), (e01-e10) tensor e00, (e01-e10) tensor (e01-e10)",
    "source_gram": [1, 2, 2, 4],
    "readout": "(s,q,p,z)=(B^T B)^(-1) B^T X; on the active sector X=B(s,q,p,z)",
    "clifford_realization": "Q=sI+q e1+p e2+zJ",
    "inherited_active_form": "2 dq wedge dp; canonical q_c=q, p_c=2p",
    "inherited_active_H": "2(q^2+p^2)=2q_c^2+p_c^2/2, up to a constant, for the declared angular flow",
    "full_source_form": "rank 2 presymplectic pullback, radical dimension 14",
    "clock": "T=(qp+sz)/(2 kappa)-phi; delta T=theta on the declared lifted phase realization",
    "normalization_boundary": "The inherited-metric Hamiltonian is NOT the earlier module contact Hamiltonian q^2+p^2+kappa. No rescaled phase lift is claimed.",
    "rung4_identification": "not supplied: active source-sector map is distinct from the rung-4 matrix-response and ancestry-coordinate fixtures",
    "uppercase_triple_boundary": "Q is the Clifford observable and T the lifted clock here; no separate uppercase P from the remembered Q,P,T triple was located",
    "scope": "Conditional source-sector/Clifford coordinate derivation; no native selection of analytic realization or physical units",
    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
}
path = ROOT / "results" / "source-rotor-coordinate-trace.json"
path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(f"PASS: {len(checks)} exact/symbolic source-to-rotor coordinate checks")
print("Prior canonical q,p and lifted angular clock recovered; actual source counting normalization made explicit.")
print("No rung-4 identification or separate uppercase P has been manufactured.")
