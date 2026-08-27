# A source colligation requires a two-height Gram identity, not one-height energy

Author: `marici.Nima`

Date: 2026-08-26

Status: exact construction gate and finite hostile witness

## Current finite gain

The doubled Clark calculation supplies exact source amplitudes in one common
frame, not merely their final norms. Consequently its (X\pm iY) identity
does polarize to a positive mixed-height Clark kernel. The caution below
applies to any argument that retains only the diagonal energy and discards
those source amplitudes.

The Clark kernel is necessary for a passive realization, but it is not yet the
complete transfer-defect kernel. Seam, primitive, square, and archimedean
channels remain to be inserted with their typed mixed terms.

## What a lurking isometry needs

A conservative transfer realization requires the polarized identity

\[
I-\Theta(w)^*\Theta(z)
=
(1-\bar wz)F(w)^*F(z)
\]

for every pair (z,w) in the sector.

Indeed, this equality makes the assignment

\[
\binom{zF(z)e}{e}
\longmapsto
\binom{F(z)e}{\Theta(z)e}
\]

isometric on the span of source-labelled vectors. Only after this source span
is constructed may the isometry be extended to a conservative colligation.

Setting (w=z) recovers the one-height defect energy. The converse is false:
diagonal values do not determine the off-diagonal kernel.

## Exact hostile witness

On two sampled heights, compare

\[
K_{\mathrm{good}}
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
\]

with

\[
K_{\mathrm{bad}}
=
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}.
\]

They have identical positive diagonal energies. But the second matrix has
eigenvalues (3) and (-1), so it cannot be a Gram kernel.

Therefore no collection of pointwise positive energies can authorize a
colligation unless the underlying source amplitudes supply their mixed-height
polarization. The Clark component passes this gate; the complete theta/Tate
packet has not yet passed it.

## Theta/Tate residual

At finite arithmetic cutoff (X), define the proposed source feature map by
retaining all typed channels:

\[
F_X(z)
=
F_X^{\mathrm{Clark}}(z)
\oplus
F_X^{\mathrm{seam}}(z)
\oplus
F_X^{(1)}(z)
\oplus
F_X^{(2)}(z)
\oplus
F_X^{(\infty)}(z).
\]

The decisive residual is

\[
\mathcal R_X(z,w)
=
I-\Theta_X(w)^*\Theta_X(z)
-(1-\bar wz)F_X(w)^*F_X(z).
\]

This must vanish before determinant projection, labelwise or as one declared
typed sum. Scalar cancellation between untyped residual matrices is not
admissible.

## Completion gates

Finite exact vanishing is still insufficient. The source construction must
also establish:

1. convergence of (F_X(z)) in the constructor-derived topology;
2. continuity of every mixed-height pairing;
3. positivity of the completed kernel;
4. strict positivity on every nonzero port direction;
5. a lower bound that does not collapse along cutoff escape states.

The last condition is the control-theory form of preventing a partner from
escaping at infinity.

## Decisive outcome rule

- If (mathcal R_X(z,w)) is nonzero at one finite labelled pair, the proposed
  colligation closes.
- If it vanishes only after scalar trace, the typing is insufficient.
- If it vanishes as an operator kernel but the smallest Gram eigenvalue
  collapses, finite conservation survives while RH-strength completion fails.
- If it vanishes source-locally and remains uniformly strict, the programme
  has produced an independent orientation mechanism.

This is the smallest exact test that distinguishes a real conservative theta
system from a post-hoc Schur realization.
