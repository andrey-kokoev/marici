---
authors:
  - marici.Nima
date: 2026-08-18
---
# 865 — The Marked Top Channel Does Not Embed in the Known Algebraic Line

## The remaining comparison

Entry 864 leaves only the rank-one marked top quotient as a possible source
for a horizontal quartic residue.  Its scalar connection is

\[
\alpha_{\rm top}=-d\log P,
\qquad P=u(u-2)(v-2).
\]

The nine-master system already has the invariant subline
\(\langle e_6\rangle\).  Direct extraction from the exact connection gives

\[
\boxed{
\alpha_{e_6}=-\frac12d\log D,
}
\]

where

\[
D=4u^4-4u^3v+4u^3+4u^2v-7u^2+2uv-4u+v^2-4v+4.
\]

A rational horizontal map from the top line into \(\langle e_6\rangle\)
would require a gauge proportional to

\[
g=\frac{\sqrt D}{P}.
\]

## The square-root obstruction survives on the quartic

The norm of \(D\) from the quartic function field to \(\mathbb Q(u)\) is

\[
\operatorname{Norm}_{\mathcal Q/\mathbb Q(u)}(D)
=-9u^6(4u^2-13u+8)(4u^2+5u-8).
\]

The two distinct quadratic factors occur to odd order.  Hence this norm is
not a square, and therefore \(D\) is not a square in
\(\mathbb Q(\mathcal Q)\).  Consequently

\[
\boxed{
\mathcal W_{\rm top}|_{\mathcal Q}
\not\longrightarrow
\langle e_6\rangle|_{\mathcal Q}
\quad\text{as a rational horizontal map.}
}
\]

## Why the quotient resemblance is insufficient

The other known algebraic line is the quotient

\[
\langle e_6,v_{\rm alg}\rangle/\langle e_6\rangle,
\]

with connection \(d\log D\).  It is rationally gauge-equivalent to the top
line, using \(g=(PD)^{-1}\).  But this is a quotient of the algebraic
two-plane, not an invariant subline of \(\mathcal M_9\).  Turning it into a
map to \(\mathcal M_9\) would require a horizontal splitting that has not
been derived.  Quotient-level agreement therefore does not construct the
residue demanded by Entry 856.

## Consequence

The last indicially allowed channel is not the already known invariant
algebraic line.  A nonzero quartic residue now requires either a genuinely
new invariant rank-one submodule of \(\mathcal M_9|_{\mathcal Q}\), or a
canonical horizontal splitting of the algebraic two-plane.  Neither is
supplied by the current source geometry.

## Durable verification

- checker: `research/nima/check_q_marked_top_kummer_obstruction.sage`;
- packet: `research/nima/q-marked-top-kummer-obstruction.json`;
- SageMath: version 10.7;
- allocator claim: `seqclaim-8bbdf6e56713ccdfdfa70ce7`.
