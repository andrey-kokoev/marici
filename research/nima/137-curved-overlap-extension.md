# Curved overlap extension of the137 comparisons

## Independent overlap phases

The previous endpoint frame adapter only conjugated a fixed Gram and preserved
its loop phases. To admit independent curvature, extend each four-probe Gram:

    G_aa=11,
    G_ab=exp(i A_ab),
    G_ba=conjugate(G_ab).

Six edge phases are independent inputs on each carrier. A local diagonal phase
change conjugates G; products G_ab G_bc G_ca are invariant and can now have
nonzero phase. These are connection-like overlap holonomies.

Every such Hermitian G is positive definite: Gershgorin gives eigenvalue lower
bound11-3=8. Hence it is realizable as a Gram matrix, although its probes are
no longer the original unmodified stabilizer indicators. This is an extension
of that geometry, not a deduction of these phases from its counting rule.

For the Hom-like tensor representation use K=conjugate(G_A) tensor G_B.
Its eigenvalues are at least64. Retain the137 labelled comparison features,
normalize them in K, and whiten before adding their comparison records.

## Response with curvature

The137 complex reflection normals remain independent because each owns a
separate record coordinate. Their nonorthogonality graph is connected in the
five tested phase fixtures. For Hermitian covariance invariant under all
individual comparisons, the same connected-eigenvector argument forces a
scalar covariance on their span. Positive active variance therefore still
gives normalized mismatch response1/137.

| Selected edge phase | Triangle holonomy phase | Minimum K eigenvalue |
|---:|---:|---:|
| 0 | 0 | 100 |
| 0.2 | 0.2 | 98.19589468 |
| 0.7 | 0.7 | 94.01813319 |
| 1.4 | 1.4 | 89.09612263 |
| pi | pi | 82.39161721 |

These fixtures establish that admitting curvature need not change the normalized
137 result. They do not establish a connectivity theorem for every phase choice,
or an instantaneous equilibrium when phases vary dynamically. The stationary
argument applies with each metric frozen and with the stated schedule assumptions.

## A changing metric needs transport

When K depends on time, keeping x fixed changes its norm. One compatible
transport is

    dot(x) = -(1/2) K^-1 dot(K) x.

It satisfies d(x^dagger K x)/dt=0. More generally any additional generator B
with B^dagger K+K B=0 preserves this identity. Thus norm compatibility does not
select a unique dynamics. Under time-dependent changes of frame the connection
must transform with the corresponding inhomogeneous term; this particular
formula is a frame choice, not by itself a full gauge-dynamical law.

The checker verifies the balance with an analytic phase derivative. No field
trajectory, source backreaction, Hamiltonian, or physical clock is inferred from
this compatibility condition.

## Current synthesis boundary

The comparison construction now accommodates genuine overlap holonomy and a
positive phase-dependent metric, alongside conserved comparison/record budgets.
It still needs a source-selected law for those phase variables and an identification
with the dynamical links in the separate feedback Hamiltonian. The137 statistic
stays unchanged across the tested curvatures, so it cannot alone determine that
law, a field stiffness, or the decimal correction to inverse alpha.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_137_curved_overlap.py

Checks positivity, actual loop phase, independence and connectivity of reflection
normals, active projector and equal normalized variance, and metric-transport
balance for five phase fixtures. NumPy calculations use explicit tolerances.
