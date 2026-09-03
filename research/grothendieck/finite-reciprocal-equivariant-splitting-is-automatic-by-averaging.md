# Finite reciprocal-equivariant splitting is automatic by averaging

## Theorem

Let a two-element reciprocal symmetry act by involutions `S` on `X` and `T` on `Y`. Let `B:X->Y` be equivariant,

\[
BS=TB,
\]

and let `K:Y->X` be any right inverse, `BK=I`. Then

\[
K_{\mathrm{eq}}
=\frac12\left(K+SKT\right)
\]

is also a right inverse and is reciprocal-equivariant.

Indeed,

\[
BK_{\mathrm{eq}}
=\frac12(BK+BSKT)
=\frac12(I+TBKT)
=I,
\]

and, using `S^2=T^2=I`,

\[
SK_{\mathrm{eq}}T
=\frac12(SKT+K)
=K_{\mathrm{eq}}.
\]

Thus over coefficients where two is invertible, every split finite reciprocal-equivariant boundary map has an equivariant splitting. This is the elementary averaging form of semisimplicity for the two-element symmetry.

## Hostile implication

The minimal control fixture already exhibits the averaging. For `B=[1,0]`, `S=diag(1,-1)`, `T=1`, and `K_alpha=(1,alpha)^T`, averaging sends every `K_alpha` to `K_0`. The construction does not inspect theta labels, modular sewing, or zero positions. It therefore applies equally to hostile finite sources.

## Consequence for the bold conjecture

Finite reciprocal-equivariant right-inverse existence cannot be the RH-bearing mechanism. The conjecture survives only in the nonsemisimple or completed data:

1. compatibility of the averaged splittings with Euler-cutoff refinement;
2. a uniform operator-norm bound in source-derived norms;
3. extension to the completed graph topology;
4. compatibility with the modularly prescribed endpoint type; and
5. failure of that completed endpoint compatibility at an off-seam Evans zero.

Averaging can worsen norms or fail to commute with refinement when the actions, embeddings, or norms vary with the cutoff. Those residuals, not finite equivariance, are the discriminating quantities.

## Disposition

Retract finite equivariant splitting as a risky theta-specific prediction. The first executable source test remains unavailable until cutoff maps, involutions, norms, and refinement embeddings are materialized. Once supplied, compute the averaged selector and the exact refinement commutator

\[
i_NK_{N,\mathrm{eq}}-K_{N+1,\mathrm{eq}}j_N
\]

plus its norm growth. A nonzero commutator or unbounded norm is the finite precursor of the completed obstruction.
