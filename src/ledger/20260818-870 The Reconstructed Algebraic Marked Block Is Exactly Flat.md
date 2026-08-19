---
authors:
  - marici.Nima
date: 2026-08-18
---
# 870 — The Reconstructed Algebraic Marked Block Is Exactly Flat

## Induced small system

Entry 869 forces any source-consistent marked block into the algebraic
kernel.  The reconstructed candidate can therefore be tested against the
rank-three wall quotient and rank-four final connection without returning
to the 372 primitive coordinates.

Let

\[
C_\mu=B_\mu^T,
\qquad \mu\in\{u,v\},
\]

so \(C_\mu\) is the \(3\times4\) off-diagonal block from marked generators
to \((e_6,e_7,e_8,e_9)\).

## Convention reconciliation

Both exact packets record derivatives of basis elements by rows.  Their
action on coefficient columns is therefore by transpose.  With the packet
convention

\[
\nabla=d-A,
\]

the mixed-curvature equation is

\[
\partial_uC_v-partial_vC_u
-A_{W,u}^TC_v-C_uA_{4,v}^T
+A_{W,v}^TC_u+C_vA_{4,u}^T=0.
\]

Using either packet without this transpose produces a nonzero expression;
this was a variance mismatch, not a mathematical obstruction.

## Exact result

Substitution of all twenty-four reconstructed rational functions gives

\[
\boxed{
\Theta_{\rm mix}=0_{3\times4}
}

identically in \(\mathbb Q(u,v)\).  All twelve scalar curvature identities
vanish exactly.

Combined with Entry 868,

\[
R_\infty B=0,
\qquad
\Theta_{\rm mix}=0,
\qquad
\operatorname{Res}_{\mathcal Q}B=0
\]

for the reconstructed candidate.

## Status

The candidate is now certified as an exact flat extension of the known wall
and absolute connections, valued in the source-required algebraic kernel.
This eliminates the possibility that modular interpolation produced a
nonflat rational matrix.

It still does not prove that this flat extension is the one selected by the
132 source reduction identities.  Flat algebraic extensions can differ by
horizontal triangular gauges.  The remaining source certificate is now a
normalization/gauge-selection problem inside the two split algebraic lines,
not a connection-existence problem.

## Durable verification

- checker: `research/nima/check_marked_candidate_flatness.sage`;
- packet: `research/nima/marked-candidate-flatness.json`;
- allocator claim: `seqclaim-585b139d1cedafc9b9b513a8`.
