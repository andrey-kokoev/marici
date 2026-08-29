# Locally uniform completion cannot erase bounded zero incidence

## Theorem

Let \(D\subset\mathbf C\) be a domain and let \(F_n\) converge locally
uniformly to a holomorphic function \(F\).  Suppose

\[
F_n(z_n)=0
\]

and the sequence \((z_n)\) remains in a compact subset of \(D\).  Every
convergent subsequence \(z_{n_j}\to z_*\) satisfies

\[
F(z_*)=0.
\]

Indeed, on a compact neighborhood containing the subsequence,

\[
|F(z_*)|
\le
|F(z_*)-F(z_{n_j})|
+|F(z_{n_j})-F_{n_j}(z_{n_j})|.
\]

The first term tends to zero by continuity of \(F\); the second tends to zero
by local uniform convergence.

## Categorical reading

Place holomorphic sections in the compact-open category and retain the
evaluation morphism.  Zero incidence is a closed relation under simultaneous
convergence of the section and its marked point.  Completion need not be an
equivalence for this conclusion.  Continuity of evaluation is enough.

Therefore a completed source that is zero-free in an open half-plane can arise
from zero-bearing finite approximants only if at least one hypothesis fails:

- the zeros escape every compact subset of that half-plane;
- section convergence is not locally uniform there;
- the boundary readout changes with the cutoff;
- the limiting section degenerates or is not defined in the same carrier.

If the theta/Tate cutoff system has a fixed framed readout and locally uniform
completion, only compact escape remains.

## Strengthening of the completion gate

Positive reciprocal finite counterexamples establish that sign, reciprocity,
and symplectic framing do not confine zeros.  They do not yet establish that
zeros occur along the actual directed theta cutoff system.

The source-specific question is now exact:

For every compact \(K\) in either open half-plane, does there exist a cutoff
\(N_K\) such that every later source approximant is zero-free on \(K\)?

This is eventual compact exclusion.  It is weaker than monotone zero motion
and stronger than convergence of scalar values at fixed points.  If proved
together with locally uniform convergence, it yields zero-freeness of the
limit.  If a sequence of cutoff zeros remains in one compact set, it falsifies
the route immediately.

## Two finite witnesses

Persistent bounded incidence:

\[
F_n(z)=z-1/n,
\qquad
F_n\longrightarrow z.
\]

The zeros converge to the limiting zero at the origin.

Permitted escape:

\[
G_n(z)=1-z/n,
\qquad
G_n\longrightarrow1.
\]

The zero is at \(n\) and leaves every compact set.  These examples separate
loss of bounded incidence, which is impossible, from escape to infinity,
which is compatible with locally uniform completion.

## Frontier

The next theta calculation should not seek a sign for individual zero
velocities.  It should derive either an eventual compact-exclusion estimate
for the actual nested source approximants or a source topology strong enough
to imply it.  Arbitrary positive reciprocal mode families cannot settle that
directed-system question.

