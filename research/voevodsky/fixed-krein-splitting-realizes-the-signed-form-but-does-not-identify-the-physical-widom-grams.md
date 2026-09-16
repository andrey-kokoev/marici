# Fixed Krein splitting realizes the signed form but does not identify the physical Widom Grams

## Scope correction

This note concerns comparison with **external, independently normalized** Tate
and reference prolate/Widom Grams. It does not concern the two polarized
sub-tetrahedra internal to the same regulated lattice cell. For those internal
features, the common face is part of the positive cell datum and the
common-remainder square commutes formally.

The transported eight-leg Krein feature gives an exact difference of two
positive Grams, but this alone does **not** close positive-regulator alignment
with external Tate and reference prolate Grams.

The distinction is essential because common-Widom-edge removal uses the actual
physical positive regulators whose leading growth is governed by the reference
Widom law.

## Two different positive realizations

Exact transport gives

\[
D_\alpha=\Theta_\alpha^*K_8\Theta_\alpha.
\]

Fixed-signature splitting constructs

\[
\widehat G_\alpha^T-
\widehat G_\alpha^0=D_\alpha,
\]

where

\[
\widehat G_\alpha^T=(E_+\Theta_\alpha)^*(E_+\Theta_\alpha),
\qquad
\widehat G_\alpha^0=(E_-\Theta_\alpha)^*(E_-\Theta_\alpha)
\]

with the Hadamard doubling used for unequal legs.

Separately, the physical construction has positive Grams

\[
G_{phys,\alpha}^T=(X_{phys,\alpha}^T)^*X_{phys,\alpha}^T,
\qquad
G_{phys,\alpha}^0=(X_{phys,\alpha}^0)^*X_{phys,\alpha}^0.
\]

The signed identity does not imply

\[
G_{phys,\alpha}^{T,0}=
\widehat G_\alpha^{T,0}.
\]

Indeed, adding the same arbitrary positive form to both legs preserves their
difference. The leading Widom edge lives precisely in this invisible common
summand.

## What the Krein construction actually proves

It proves:

1. a global packet-natural positive realization of the centered signed form;
2. exact handling of noncommuting left/right regulator placement;
3. avoidance of packetwise Jordan decomposition;
4. a canonical candidate for the **residual** two-polarity feature.

It does not prove:

1. that either Krein Gram obeys the physical reference Widom law;
2. that the physical Tate/reference Grams differ by \(D_\alpha\);
3. that the physical common bulk is represented inside \(\Theta_\alpha\);
4. that subtracting a common physical feature leaves the Krein legs.

## Exact missing sewing diagram

The required theorem is now a dilation/factorization statement. Construct one
common positive feature \(B_\alpha\) and partial isometries \(U_\alpha^T,
U_\alpha^0\) such that

\[
\boxed{
U_\alpha^T X_{phys,\alpha}^T
=
B_\alpha\oplus E_+\Theta_\alpha,}
\]

\[
\boxed{
U_\alpha^0 X_{phys,\alpha}^0
=
B_\alpha\oplus E_-\Theta_\alpha,}
\]

with the corresponding doubled formulas for unequal transported legs.
Equivalently, at Gram level,

\[
\boxed{
G_{phys,\alpha}^T=B_\alpha^*B_\alpha+
\widehat G_\alpha^T,
\qquad
G_{phys,\alpha}^0=B_\alpha^*B_\alpha+
\widehat G_\alpha^0.}
\]

This simultaneously establishes:

\[
G_{phys,\alpha}^T-G_{phys,\alpha}^0=D_\alpha
\]

and identifies the common edge before packet compression.

## Douglas formulation

At finite cutoff, existence of the displayed partial isometries is equivalent
to equality of the corresponding Grams. If only inequalities are initially
available, Douglas factorization reduces construction of the maps to

\[
\widehat G_\alpha^T\preceq G_{phys,\alpha}^T,
\qquad
\widehat G_\alpha^0\preceq G_{phys,\alpha}^0,
\]

plus equality of the two remainders

\[
\boxed{
G_{phys,\alpha}^T-\widehat G_\alpha^T
=
G_{phys,\alpha}^0-\widehat G_\alpha^0
\succeq0.}
\]

Thus the earliest missing finite-cutoff statement is not another signed trace
calculation. It is positivity and equality of these two physical remainders.

## Interaction with globalization

If the common remainder is constructed globally as \(B_\alpha^*B_\alpha\),
then packet naturality is automatic. The later Mosco problem reduces to uniform
commutator/tail control for the residual Krein feature against the spectrally
adapted observer filtration.

If equality is proved only after finite packet compression, globalization
remains blocked because common remainders selected independently on packets
need not be compatible.

## Final channel-2 frontier after audit

1. signed finite-cutoff transport: exact;
2. packet-natural Krein positive realization of the signed residual: exact;
3. identification of that realization as the residual of the **physical**
   Tate/reference Widom Grams: open;
4. global common physical feature: open and equivalent to the remainder
   equality above;
5. uniform residual leakage estimate: open;
6. Mosco/strong-resolvent convergence: open after 3--5.

This correction prevents an algebraic positive realization of \(D_\alpha\) from
being mistaken for the physically normalized absolute-Gram theorem.

## Repository dependencies

- `the-transported-eight-leg-krein-readout-gives-an-exact-global-positive-regulator-alignment.md`
- `the-finite-absolute-gram-closure-is-conditional-on-one-exact-positive-regulator-alignment.md`
- `bounded-relative-gram-convergence-transfers-the-reference-widom-law-to-the-tate-regulator.md`
- `global-absolute-gram-mosco-convergence-reduces-to-uniform-graph-core-and-compression-control.md`
