# Reciprocal and Real covariance classify diagonal bulk-multiplier observers

## Question

Which diagonal bulk weights on the radial double preserve reciprocal and fixed-fiber Real structure?

## Claim boundary

A diagonal multiplier commuting with the reciprocal swap must use the same weight on both oriented channels. Commutation with the twisted Real structure further requires that weight to be real-valued. Reciprocal-odd multipliers use opposite real weights and intertwine with the sign-twisted target action. These are exact classifications inside the diagonal multiplier class.

## Problem

Let

\[
H_{\rm rad}
=L^2(\mathbb R_+)\oplus L^2(\mathbb R_+)
\]

with

\[
W_u=
\begin{pmatrix}
0&u^{-1}\\
u&0
\end{pmatrix}
\]

and

\[
J_u=\operatorname{diag}(1,u^2)K.
\]

Consider a bounded diagonal multiplication observer

\[
D_{a,b}
=
\begin{pmatrix}
M_a&0\\
0&M_b
\end{pmatrix},
\qquad
a,b\in L^\infty(\mathbb R_+).
\]

## Bold conjecture

Any independently chosen pair of channel weights preserves reciprocal and Real symmetry because the multiplier is diagonal.

## Named rivals

1. Reciprocal-even covariance forces \(a=b\).
2. Reciprocal-odd covariance forces \(a=-b\).
3. Fixed-fiber Real covariance forces real-valued weights.
4. Equal modulus \(|a|=|b|\) is sufficient.

## Reciprocal-even classification

Direct multiplication gives

\[
D_{a,b}W_u
=
\begin{pmatrix}
0&u^{-1}M_a\\
u M_b&0
\end{pmatrix}
\]

and

\[
W_uD_{a,b}
=
\begin{pmatrix}
0&u^{-1}M_b\\
u M_a&0
\end{pmatrix}.
\]

Therefore

\[
D_{a,b}W_u=W_uD_{a,b}
\]

if and only if

\[
a=b
\]

almost everywhere.

Thus every reciprocal-even diagonal bulk observer has the form

\[
D_w^{+}
=
\operatorname{diag}(M_w,M_w).
\]

Equal modulus alone does not suffice, rejecting rival 4.

## Reciprocal-odd classification

Similarly,

\[
D_{a,b}W_u=-W_uD_{a,b}
\]

if and only if

\[
a=-b
\]

almost everywhere. Therefore every reciprocal-odd diagonal observer has the form

\[
D_w^{-}
=
\operatorname{diag}(M_w,-M_w).
\]

It does not commute with reciprocal symmetry. It is an intertwiner from the source reciprocal representation \(W_u\) to a target representation with action \(-W_u\).

## Real classification

For scalar multiplication,

\[
M_aK=KM_a
\]

if and only if

\[
a=\bar a
\]

almost everywhere. Since the diagonal phase in \(J_u\) commutes with diagonal multipliers,

\[
D_{a,b}J_u=J_uD_{a,b}
\]

if and only if both \(a\) and \(b\) are real-valued.

Combining with reciprocal covariance gives:

- Real reciprocal-even observers: \(D_w^+\) with real \(w\);
- Real reciprocal-odd observers: \(D_w^-\) with real \(w\).

This proves rivals 1--3.

## Parity-basis action

The reciprocal eigenspaces are

\[
X_+(u)=\{(f,uf)\},
\qquad
X_-(u)=\{(f,-uf)\}.
\]

For the even multiplier,

\[
D_w^+(f,\pm uf)
=(wf,\pm uwf),
\]

so each parity sector is preserved.

For the odd multiplier,

\[
D_w^-(f,\pm uf)
=(wf,\mp uwf),
\]

so the positive and negative sectors are exchanged. This is the operational meaning of reciprocal parity of the observer.

## Stability

For either sign,

\[
\|D_w^\pm(f_+,f_-)\|^2
=
\|wf_+\|^2+
\|wf_-\|^2.
\]

Thus even and odd multipliers have identical lower-modulus behavior as ungraded Hilbert maps. Their difference is symmetry variance, not observation strength.

If \(w\) satisfies the uniform local-mass condition, combining either multiplier with the doubled derivative yields graph-norm stability. The even version preserves sectors; the odd version exchanges them and requires the sign-twisted target action.

## Green structure

Both diagonal multipliers commute with

\[
J_\partial=\operatorname{diag}(-1,1)
\]

as matrices, but they are observers rather than carrier automorphisms unless \(|w|=1\) almost everywhere. Commuting with the Green matrix does not make a nonunitary multiplier a Green comparison cell.

This separates `green_compatible_observer` from `green_isometry`.

## Phase-gauge naturality

For

\[
G_{v,u}=\operatorname{diag}(1,v/u),
\]

all diagonal multipliers commute with \(G_{v,u}\). Therefore the even and odd observer classes transport naturally across wall-phase gauges. Their classification is independent of \(u\).

## Constructor-role signatures

The roles are:

- `reciprocal_even_bulk_observer`: same real weight on both channels;
- `reciprocal_odd_bulk_observer`: opposite real weights, parity-exchanging;
- `green_compatible_observer`: commutes with the Green matrix but need not be unitary;
- `green_comparison_cell`: unitary and domain transporting;
- `thick_bulk_complement`: either parity type plus a declared lower-mass condition.

A contract must record observer parity and target action. Equal norms do not identify the even and odd roles.

## Strongest falsification attempt

Choosing \(a=e^{i\theta}w\) and \(b=e^{-i\theta}w\) with equal modulus appears compatible with the phase-decorated swap. Direct multiplication shows that the fixed source and target action still compares \(a\) with \(b\), forcing equality for even covariance. A phase-twisted target action could absorb the difference, but that is a new representation and must be declared as a comparison, not inferred from equal modulus.

## Disposition

The bold conjecture is rejected. Within diagonal bulk multipliers, reciprocal and Real covariance completely determine the channel pattern: equal real weights for even observers and opposite real weights for odd observers. Stability is controlled separately by the weight thickness. This gives a fully typed family of essential bulk complements for the principal Green/Real example.
