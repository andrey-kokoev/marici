"""Exact fixed-carrier Gram tower from stabilizer-indicator probes.

f_i(sigma)=1 when sigma fixes i, sigma in S12, counting inner product.
Divide the full Gram by 10! once: G12=10I+J. Keep that normalization on
all restricted probe spans. This is a Gram-norm budget, not a Hamiltonian.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

# Audit the two distinct counting rules without enumerating S12.
for n in range(4, 8):
    counts = [0, 0, 0]
    for p in permutations(range(n)):
        counts[0] += p[0] == 0
        counts[1] += p[0] == 0 and p[1] == 1
        counts[2] += p[0] == 1
    assert counts == [factorial(n-1), factorial(n-2), factorial(n-1)]


def inner(x, y):
    return 10*sum(a*b for a, b in zip(x, y))+sum(x)*sum(y)


def energy(x):
    return inner(x, x)


def restrict(x):
    r = len(x)
    # G_(r-1)^-1 * overlap column = ones/(r+9).
    y = [v+x[-1]/(r+9) for v in x[:-1]]
    schur = F(10*(r+10), r+9)
    record = schur*x[-1]**2
    embedded = y+[F(0)]
    residual = [a-b for a, b in zip(x, embedded)]
    for i in range(r-1):
        basis = [F(j == i) for j in range(r)]
        assert inner(residual, basis) == 0
    assert energy(x) == energy(y)+record
    return y, record


# A coherent seed and all basis seeds test composition and budget conservation.
for seed in [[F(i+1) for i in range(12)]] + [[F(i == j) for i in range(12)] for j in range(12)]:
    x = seed[:]
    recorded = F(0)
    for r in range(11, 3, -1):
        x, drop = restrict(x)
        recorded += drop
        direct = [v+sum(seed[r:])/F(10+r) for v in seed[:r]]
        assert x == direct
        assert energy(x)+recorded == energy(seed)

print('Counts verified through S7; factorial formulas give G12/10! = 10I+J.')
print('r | common eigenvalue | contrast eigenvalue (multiplicity) | next-step Schur weight')
for r in range(12, 3, -1):
    common = [F(1)]*r
    assert energy(common) == r*(r+10)
    contrast = [F(1), F(-1)]+[F(0)]*(r-2)
    assert energy(contrast) == 10*2
    weight = str(F(10*(r+10), r+9)) if r > 4 else '-'
    print(f'{r:2} | {r+10:2} | 10 ({r-1}) | {weight}')

# Covariance C=G12^-1 gives isotropic excitation in the Gram metric.
# E[||projection to span(first r probes)||_G^2] = tr(G_r L C L^T).
C = [[F(i == j, 10)-F(1, 220) for j in range(12)] for i in range(12)]
for r in range(4, 13):
    L = [[F(i == j) if j < r else F(1, 10+r) for j in range(12)] for i in range(r)]
    cov = [[sum(L[i][a]*C[a][b]*L[j][b] for a in range(12) for b in range(12))
            for j in range(r)] for i in range(r)]
    retained = sum((10*(i == j)+1)*cov[j][i] for i in range(r) for j in range(r))
    assert retained == r
print('Metric-isotropic covariance G12^-1 gives retained mean r and fraction r/12 exactly.')
print('Gram-orthogonal restrictions compose and conserve retained-plus-record norm exactly.')
print('Rebuilding probes on Sr instead gives (r-2)I+J after its own normalization: a different tower.')
