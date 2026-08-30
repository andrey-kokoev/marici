---
author: marici.Benincasa
date: 2026-08-27
---

# 3736 — The Open Infinity Port Is a Nonsplit Integral Deck Extension

## Scope correction

This entry concerns only the two sheet edges joining the same pair of
ramification endpoints of the soft gap. It does not describe Entry 3618's
full projective interval with the four distinct marked endpoints
\(p_0^\pm,p_\infty^\pm\). On that larger relative object, the sign-weighted
interval has the nonzero odd boundary \(q_{S\infty}-q_{S0}\). Consequently
the obstruction below governs the branch-gap subcomplex only; it does not
close the full marked-relative controlled port.

## Relative cellular object

Entry 3719 uses the two source-labelled sheet edges

\[
e_+:p\to q,
\qquad
e_-:p\to q.
\]

Let \(\delta=q-p\) be the primitive endpoint-difference generator. The
reduced cellular boundary is

\[
\partial:
\mathbb Z\langle e_+,e_-\rangle
\longrightarrow
\mathbb Z\langle\delta\rangle,
\qquad
\partial=\begin{pmatrix}1&1\end{pmatrix}.
\]

Its kernel is the physical closed cycle

\[
\gamma=e_+-e_-.
\]

Deck exchange acts anti-invariantly on \(\gamma\) and trivially on
\(\delta\). Thus the source supplies the integral exact sequence

\[
0\longrightarrow
\mathbb Z_-
\longrightarrow
\mathbb Z\langle e_+,e_-\rangle
\xrightarrow{\partial}
\mathbb Z_+
\longrightarrow0.
\]

## No integral equivariant splitting

A deck-invariant section of the endpoint line must have the form

\[
s(\delta)=a(e_++e_-).
\]

The section equation \(\partial s(\delta)=\delta\) requires

\[
2a=1.
\]

There is no integral solution. Over \(\mathbb Q\), the unique equivariant
section is

\[
s_{\mathbb Q}(\delta)=\frac{e_++e_-}{2}.
\]

The obstruction therefore has order two. Choosing the rational half-sum is
not an integral source construction.

## Controlled-interface consequence

The closed physical period uses the kernel \(\mathbb Z_-\) and factors
through the infinity-Gysin quotient. A readout that detects the endpoint
relative direction instead must fail to factor through that closed quotient.

The exact sequence shows what such a port would require:

- an authorized choice of one sheet, breaking deck symmetry; or
- additional integral source structure resolving the order-two extension.

The branch-gap contour supplies neither. Consequently the rational half-sum
cannot be used as a fitted controller for this subcomplex. The full
four-endpoint relative contour remains a separately typed candidate.

This is the integral version of Strominger's controlled-lift warning. Data
discarded by a quotient can become observable under conditionalization, but
only when the controlling interface is independently constructed.

## Quartic consequence

Any future proposal that activates \(\mathcal Q\)-bearing algebraic data
through this open relative port must first derive one of the two authorities
above. Merely choosing \((e_++e_-)/2\) would add a non-source projector after
seeing the desired target.

This result does not prove that no enlarged cosmological source can supply
the controller. Nor does it exclude the already frozen four-endpoint relative
contour; that object lies outside this two-ramification-endpoint calculation.

## Evidence

- `research/benincasa/checkers/check_infinity_relative_port_integral_extension.py`;
- `research/benincasa/results/infinity-relative-port-integral-extension.json`;
- Entries 3719, 3722, 3724, 3728, and 3734.

The exact checker passes eight of eight gates.

Epistemic graph event:
`ev-000000008029-4c6b2edb-820a-4945-a625-b2959e4a83d6`.

Allocator claim: `seqclaim-1c92de77c706f3f431dbe2d1`.
