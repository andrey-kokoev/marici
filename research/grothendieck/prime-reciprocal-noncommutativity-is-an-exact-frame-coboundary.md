# Prime reciprocal noncommutativity is an exact frame coboundary

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact correction theorem

## Source-native frames

On the critical seam, put

\[
\theta_p=t\log p,
\qquad
R_p=\operatorname{diag}\left(e^{-i\theta_p/2},e^{i\theta_p/2}\right).
\]

The normalized reciprocal exchange is

\[
X_p=\begin{pmatrix}0&e^{-i\theta_p}\\e^{i\theta_p}&0\end{pmatrix}
=R_p\sigma_1R_p^{-1}.
\]

Thus every prime exchange is the same universal reflection in its own
source-native frame:

\[
R_p^{-1}X_pR_p=\sigma_1.
\]

## Exact comparison cocycle

Define the comparison from the (p)-frame to the (q)-frame by

\[
T_{pq}=R_p^{-1}R_q.
\]

Then

\[
T_{pq}T_{qr}=T_{pr},
\qquad
T_{pq}T_{qr}T_{rp}=I.
\]

The phase differences therefore form an exact one-coboundary. They have
trivial cycle holonomy and supply no intrinsic two-cell curvature.

## What survives from the raw commutator

In one fixed ambient frame,

\[
[X_p,X_q]=2i\sin(\theta_q-\theta_p)\sigma_3.
\]

Ledger 3062 correctly proves that the corresponding absolute pair sum
diverges. The present theorem changes its meaning: the divergence is the
non-summable cost of comparing all prime-local axes without first applying
their canonical frame transitions. It is not evidence of a nontrivial
source curvature.

After coherent parallelization, every exchange becomes \(\sigma_1\), so the
cross-prime commutator vanishes identically. The ordered product has returned
to a single universal channel.

## Consequence for the RH programme

This closes the raw cross-prime noncommutativity route. Neither scalar prime
phases nor their doubled Pauli realization creates an intrinsic global
curvature: both factor through the single potential \(p\mapsto t\log p\).

A genuine additional comparison channel must fail to factor through that
potential. The live candidates are source operations that retain boundary
incidence—primitive, prime-square, mixed-seam, or archimedean currents. They
must produce a nontrivial coherence residual after canonical
parallelization, not merely a commutator in an untransported common basis.

This is the precise normalization lesson: compare source objects only after
transporting them to a common normal form. Apparent noncommutativity before
that transport is not invariant evidence.

## Falsifier and scope

The theorem would fail if the source-native transition around some prime
cycle had nonidentity holonomy, or if a normalized exchange retained a
prime-dependent component. Neither occurs for the local reciprocal exchange.

The result does not prove that every enlarged theta/Tate comparison is flat.
It proves only that the prime exchange family by itself is flat and therefore
cannot carry the missing RH orientation.

## Verification

Run:

```powershell
uv run --with sympy python research/grothendieck/checkers/prime_reciprocal_frame_coboundary.py
```

The checker verifies the conjugation, normalization, cocycle, cycle
holonomy, normalized commutation, and the unchanged raw sine commutator.
