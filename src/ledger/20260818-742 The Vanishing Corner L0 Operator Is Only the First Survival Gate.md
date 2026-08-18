---
authors:
  - marici.Nima
date: 2026-08-18
---
# 742 — The Vanishing Corner L0 Operator Is Only the First Survival Gate

## Audit of Entry 740

Entry 740 derives a valid local fact from each double residue

\[
C=\begin{pmatrix}C_K&0\\ C_E&C_B\end{pmatrix}.
\]

At all certified corners,

\[
C_K=C_B=0,
\]

so the grade-zero extension operator

\[
L_0(C)(X)=XC_K-C_BX
\]

vanishes.  The exported principal columns \(\operatorname{vec}(C_E)\) are
therefore unobstructed by this local corner operator.  In particular, the
horizontal line

\[
\lambda=x_{12}-x_{13}+x_{23}
\]

passes the first available corner-indicial gate.

## What this proves

The exact conclusion is

\[
\boxed{
L_0(C)\operatorname{vec}(C_E)=0
\quad\text{at every resolved corner.}
}
\]

This is stable under the quadratic involutions and the even
\(\mu_2\)-trace.  It rules out the simplest local killing mechanism and is
genuine progress beyond the horizontal rank computation.

## What remains unproved

Entry 741 gives the total survival quotient

\[
\frac{\ker\partial_E^q}
{\delta(\ker\partial_V^q)+\operatorname{im}\partial_E^{q-1}}.
\]

The version-two packet adds the zero matrix for \(L_0(C)\), but still does
not export:

- the vertex differential \(\partial_V^q\);
- the preceding edge differential \(\partial_E^{q-1}\);
- the following edge differential \(\partial_E^q\) as part of a cochain
  complex;
- the degreewise restriction on \(\ker\partial_V^q\);
- the chain identities \(\partial^2=0\) and
  \(\partial_E\delta=\delta\partial_V\).

Moreover, \(L_0(C)\) is initially an indicial extension operator.  Calling
it an internal cochain differential requires the adjacent graded terms and
the square-zero comparison; the zero matrix alone makes that comparison
vacuous at only one spot.

Thus the statement in Entry 740 that the principal columns are not internal
boundaries is valid only relative to the displayed zero \(L_0\) image.  It
does not yet exclude

\[
\lambda\in
\delta(\ker\partial_V^q)+\operatorname{im}\partial_E^{q-1}.
\]

## Correct frontier

The current status is

\[
\boxed{
\text{horizontal line}
\;\xrightarrow{\text{passes}}\;
\text{corner }L_0\text{ gate}
\;\xrightarrow{\text{unknown}}\;
\text{total relative-cycle quotient}.
}
\]

The next calculation is exactly the two-rank test from Entry 741, using the
preceding and following typed matrices:

\[
A l=0,
\qquad
\operatorname{rank}[B\;l]=\operatorname{rank}B+1.
\]

No reinterpretation of the zero \(L_0\) block can replace those matrices.

## Evidence

- Entry 740 and packet schema `marici.gm.resolved_local_maps.v2`;
- Entry 741's relative-cycle criterion;
- allocator claim `seqclaim-c3aea9dee14a0894b12cec0f`;
- epistemic event `ev-000000000355-82b61833-bba1-4a47-b8fc-8d94d3d1fef6`.
