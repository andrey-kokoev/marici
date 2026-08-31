# The retained history graph realizes the G1.1 shifted squares with the theta-mass bound

## Ledger focus

G1.1 asks for:

1. a source-derived causal-history auxiliary block;
2. uniform lower bounds for \(I\pm iH\);
3. incidence compression to \(\tau\).

The recent endpoint work should not replace this ledger clause.  Its relevant
contribution is the retained-source graph mechanism.

## Relative wall--history graph

Let \(H\) be the causal theta history on the declared half-line/cutoff carrier,
with kernel \(\Phi\).  Retain the input coordinate and history output before
codiagonalization:

\[
\Gamma_Hx=(x,Hx).
\]

Equip the direct sum with its source Hilbert form.  The graph Gram is

\[
\Gamma_H^*\Gamma_H=I+H^*H.
\]

The first coordinate is the analytic identity wall under the multiplication
representation.  It is retained as source/kernel data even when a downstream
completion differential annihilates constant walls.  Thus the graph is a
relative mapping-cone carrier rather than an ordinary completed image.

The graph map has closed range because its first-coordinate projection is a
bounded inverse on the range.  Its positive form has zero radical.

## Reciprocal quarter-turn outputs

Define the two reciprocal output maps

\[
Q_\pm x=\frac1{\sqrt2}(x\pm iHx).
\]

Their Grams are exactly

\[
\boxed{
Q_\pm^*Q_\pm
=\frac12(I\pm iH)^*(I\pm iH).
}
\]

No finite identity wall is inserted after completion: both terms descend from
the two retained coordinates of the same source graph.  This realizes the
required shifted squares on one common carrier.

The sum identity

\[
Q_+^*Q_++Q_-^*Q_-=I+H^*H
\]

shows that the two reciprocal squares are the Hadamard/quarter-turn
polarizations of the retained graph energy.

## Uniform theta-mass estimate

For every half-line cutoff \(L\), the causal convolution satisfies

\[
\|H_L\|\le M_\Phi,
\qquad
M_\Phi=\int_0^\infty\Phi(r)\,dr.
\]

The frozen theta normalization identifies

\[
M_\Phi=\xi\!\left(\frac12\right)<\frac12.
\]

Therefore, for either sign,

\[
\|(I\pm iH_L)x\|
\ge(1-\|H_L\|)\|x\|
>(1-M_\Phi)\|x\|
>\frac12\|x\|.
\]

Consequently

\[
\boxed{
Q_{L,\pm}^*Q_{L,\pm}
\ge\frac18I
}
\]

uniformly in the cutoff and prime label.  The same estimate holds on every
translation-equivalent theta-label fiber.

## What this closes in G1.1

On the retained relative graph carrier:

- the source wall and causal history coexist without identifying kernel and
  image coordinates;
- the reciprocal shifted-square factorization is exact;
- the graph is closed and nondegenerate;
- the \(1/8\) lower bound is cutoff- and prime-uniform;
- no endpoint Stieltjes metric is substituted.

Thus the common-carrier and shifted-history estimate portions of G1.1 are
closed, subject to the already frozen equality
\(M_\Phi=\xi(1/2)\).

## Remaining G1.1 clause

The unresolved part is incidence compression.  Existing relative calculations
give

\[
c_+=\frac{M_\Phi^2}{2},
\qquad
c_-=-\|\Phi\|_2^2,
\]

with nonzero odd channel and fixed sign.  One must still prove that the
Hadamard/Wronskian compression of these two retained graph coordinates is
exactly the ledger coefficient \(\tau\), with the same Euler loading and
orientation conventions used by the first-Adams incidence.

That is now the earliest unresolved implication inside G1.1.  G1.2 endpoint
closure, G1.3 typed loading, and later global gates remain separate.  No RH
conclusion is authorized.
