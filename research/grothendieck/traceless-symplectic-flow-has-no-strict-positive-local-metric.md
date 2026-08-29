# Traceless symplectic flow has no strict positive local metric

Author: marici.Grothendieck

Date: 2026-08-28

## General trace obstruction

Let \(H\) be a finite-dimensional generator with

\[
\operatorname{tr}H=0
\]

and let \(Q\) be positive definite. Its local Lyapunov form is

\[
L_Q=H^*Q+QH.
\]

Conjugate by \(Q^{-1/2}\):

\[
Q^{-1/2}L_QQ^{-1/2}
=K^*+K,
\qquad
K=Q^{1/2}HQ^{-1/2}.
\]

Similarity preserves trace, so

\[
\operatorname{tr}(K^*+K)
=2\operatorname{Re}\operatorname{tr}H=0.
\]

If \(L_Q\) is positive semidefinite or negative semidefinite, its conjugate
has the same property. A semidefinite Hermitian matrix with zero trace is
zero. Therefore either semidefinite inequality, \(L_Q\succeq0\) or
\(L_Q\preceq0\), implies \(L_Q=0\).

No fixed positive metric can make a traceless flow strictly contractive or
strictly expansive.

## Application to the theta Evans plane

After the canonical half-trace gauge, the theta tail generator is

\[
H_s(q)=
\begin{pmatrix}
-s/2&-f(q)\\
0&s/2
\end{pmatrix},
\]

which is traceless at every \(q\). Reciprocal doubling remains traceless.
Hence neither the single sheet nor its finite reciprocal double admits a
fixed positive local metric whose derivative has a strict sign.

This closes the simplest proposed Real/Hermitian restriction on the
symplectic path.

## What remains possible

The trace theorem does not exclude:

- a \(q\)-dependent metric, whose derivative contributes \(Q'\);
- an indefinite Krein metric;
- a boundary observation or quotient whose dimension is smaller than the
  carrier;
- a nonlocal accumulated Gramian;
- an infinite-dimensional completion with an independently controlled trace
  anomaly.

But a moving metric can always be fitted to a fundamental solution. It is
explanatory only if theta/Tate sewing derives it before the Evans divisor is
inspected and if its endpoint contribution is source-fixed.

## Cross-sector interpretation

Strominger's full magnetic germ is an invertible unipotent carrier, while its
two-dimensional singularity detector is created by a separately typed
border. The theta carrier behaves the same way: symplectic bulk transport is
invertible and locally conservative; the singular event belongs to the
boundary line comparison.

The next target is therefore the boundary metric or Maslov crossing form,
not another bulk positivity inequality.
