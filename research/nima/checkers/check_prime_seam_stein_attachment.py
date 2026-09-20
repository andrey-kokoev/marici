import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/prime-seam-stein-attachment.json"


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(x) for x in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def rank(a):
    m = [r[:] for r in a]
    r = 0
    for c in range(len(m[0])):
        p = next((i for i in range(r, len(m)) if m[i][c]), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        d = m[r][c]
        m[r] = [x / d for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                f = m[i][c]
                m[i] = [m[i][j] - f*m[r][j] for j in range(len(m[0]))]
        r += 1
    return r


def enc(a):
    return [[str(x) for x in row] for row in a]

# One valuation chain with p=4, so p^(1/2)=2 is exact rational arithmetic.
phi = [Q(1), Q(2), Q(3), Q(1)]
# J e_k(u)=2^{-k} phi(u+k), k=0,1,2; zero outside the displayed source.
J3 = [[(Q(1, 2)**k) * (phi[u+k] if u+k < len(phi) else Q(0))
       for k in range(3)] for u in range(len(phi))]
J2 = [row[:2] for row in J3]
G3 = mm(tr(J3), J3)
G2 = [row[:2] for row in G3[:2]]
# A=2S from the two-column packet into the three-column packet.
A = [[Q(0), Q(0)], [Q(2), Q(0)], [Q(0), Q(2)]]
# First moving window u=0.
B = [[phi[0], Q(1, 2)*phi[1]]]
stein_residual = sub(sub(G2, mm(mm(tr(A), G3), A)), mm(tr(B), B))
# Continuous-tail left shift on the finite supported sequence.
C = [[Q(0), Q(1), Q(0), Q(0)],
     [Q(0), Q(0), Q(1), Q(0)],
     [Q(0), Q(0), Q(0), Q(1)],
     [Q(0), Q(0), Q(0), Q(0)]]
transport_residual = sub(mm(C, J2), mm(J3, A))
# Fixed-origin hostile c=(1,-1): Bc=0 although Jc is nonzero.
c = [[Q(1)], [Q(-1)]]
fixed_obs = mm(B, c)
state = mm(J2, c)
# Transported windows B_j c are direct sequence coordinates of Jc.
transported_energy = sum((x[0]*x[0] for x in state), Q(0))
gram_energy = mm(mm(tr(c), G2), c)[0][0]
checks = {
    "forward_intertwining_exact": all(x == 0 for row in transport_residual for x in row),
    "stein_identity_exact": all(x == 0 for row in stein_residual for x in row),
    "source_map_noncollapsed": rank(J2) == 2,
    "fixed_origin_window_has_kernel": fixed_obs == [[Q(0)]],
    "hostile_state_remains_nonzero": any(x[0] for x in state),
    "transported_window_tower_recovers_gram_energy": transported_energy == gram_energy and gram_energy > 0,
}
assert all(checks.values()), checks
result = {
    "schema": "marici.nima.prime-seam-stein-attachment.v1",
    "claim_strength": "finite-cutoff source-realization and exact observability identity",
    "source_operation": "valuation-chain intertwiner with transported seam-window restriction",
    "matrices": {"J": enc(J2), "G": enc(G2), "A": enc(A), "B": enc(B)},
    "checks": checks,
    "hostile": {"state": [str(x[0]) for x in c], "fixed_window": "0", "full_energy": str(gram_energy)},
    "unsupported": ["determinant-line attachment", "order-three anomaly compatibility", "multi-prime permutohedral sewing", "completion"],
    "passed": True,
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
