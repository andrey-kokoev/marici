# Higher-coherence topology iteration 04: weak and distributional limits can hide energy only by dropping the Haar observer

## Candidate topology

Let the completed carrier be a rigged triple

\[
\mathcal S\subset H\subset\mathcal S'
\]

or a weak Hilbert carrier `H_w`. Higher-cone representatives may then converge
weakly or distributionally even when they do not converge in norm.

This topology genuinely differs from the preceding projective, LF, and corona
models. For example, an orthonormal sequence satisfies

\[
e_N\rightharpoonup0,
\qquad
\|e_N\|=1.
\]

Thus positive energy can escape weakly while every fixed compact observer tends
to zero.

## Residual tested by a retained functional

Suppose the relative-Haar readout is retained as a continuous test functional

\[
\ell_p\in\mathcal S
\quad\text{or}\quad
\ell_p\in H^*.
\]

If higher representatives `r_N` converge weakly to zero, then

\[
\ell_p(r_N)\longrightarrow0.
\]

But compatibility of the fixed-prime packet gives

\[
\ell_p(r_N)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z)

defeq r_p(z)
\]

for every sufficiently large `N`. Therefore weak convergence to zero implies

\[
r_p(z)=0.
\]

Weak topology does not weaken a scalar obstruction seen by a retained
continuous observer.

## How apparent absorption occurs

There are only two ways to make the residual distributionally invisible.

### Restrict the test class

Choose a test space whose annihilator contains the Haar coordinate. Then the
residual represents zero in the induced weak quotient. But the topology no
longer contains the observer needed to distinguish

\[
E_p(b_z)>0
\]

from zero.

### Move the state to weak infinity

Allow higher fillers to replace `b_z` by representatives analogous to `e_N`.
Their weak limit may vanish while energies remain one. This does not produce an
energy-cycle equality; it removes the state from the limit. Weak lower
semicontinuity only gives

\[
E(0)\le\liminf_NE(b_N),
\]

not preservation of positive noncollapse.

## Distributional separation

On the Schwartz rigging, the distributions already used by the six-port packet
are separated by Schwartz tests. In particular, `delta_a`, `delta_a'`,
`|q-a|`, principal-value channels, and their finite linear combinations do not
vanish in `S'` unless all pairings vanish. The strong-dual or weak-star topology
changes convergence, not algebraic separation.

Hence the rigged extension that admitted `K_(1,a)` cannot simultaneously make
its nonzero Haar readout disappear while retaining the full six-port test
space.

## Verdict for topology 4

Weak/distributional topology can absorb norm-bounded sequences that move to
infinity, but only at the cost of one of the two hypotheses required for
confinement:

1. continuity of the relative-Haar observer; or
2. noncollapse of the Xi state in the completed carrier.

With both retained, a constant scalar readout remains constant under weak
limits and must already vanish.

The next nonredundant topology to test is a Krein/Pontryagin or symplectic
quotient topology, where a nonzero positive component might be paired with an
opposite-sign higher-cone component without making the state weakly zero.