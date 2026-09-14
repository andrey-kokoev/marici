# Krein--Langer factorization gives the exact Suzuki positive-minus-defect identity

## Setup

Let

\[
k_F(z,w)=\frac{1-F(z)\overline{F(w)}}{-i(z-\bar w)}
\]

be the upper-half-plane de Branges--Rovnyak kernel. Suppose a meromorphic unimodular boundary function has a Krein--Langer factorization

\[
\Theta(z)=B(z)^{-1}S(z),
\]

where

- `B` is a finite Blaschke product containing the upper-half-plane poles of `Theta`;
- `S` is Schur in the upper half-plane;
- `B` and `S` have no common inner factor.

This is the finite-negative-index case. The algebraic identity below does not use positivity until its final interpretation.

## Exact kernel decomposition

Direct calculation gives

\[
\begin{aligned}
1-\Theta(z)\overline{\Theta(w)}
&=
1-\frac{S(z)\overline{S(w)}}{B(z)\overline{B(w)}}\\
&=
\frac{B(z)\overline{B(w)}-S(z)\overline{S(w)}}
     {B(z)\overline{B(w)}}\\
&=
\frac{[1-S(z)\overline{S(w)}]-[1-B(z)\overline{B(w)}]}
     {B(z)\overline{B(w)}}.
\end{aligned}
\]

Therefore

\[
\boxed{
k_\Theta(z,w)
=
\frac{k_S(z,w)-k_B(z,w)}
     {B(z)\overline{B(w)}}.
}
\]

This is the desired abstract comparison: the meromorphic Suzuki kernel is exactly a positive Schur bulk minus a positive Blaschke defect, followed by an invertible diagonal congruence away from the poles.

For a finite point family `z_1,...,z_n`, write

\[
D_B=\operatorname{diag}(B(z_1),\ldots,B(z_n)).
\]

Then its Gram matrix satisfies

\[
\boxed{
G_\Theta
=D_B^{-1}(G_S-G_B)D_B^{-*}.
}
\]

Both `G_S` and `G_B` are positive semidefinite. The entire sign problem is their domination order.

## Hilbert-space meaning

The Schur kernel and finite Blaschke kernel have Kolmogorov factorizations

\[
k_S(z,w)=\langle v_S(z),v_S(w)\rangle,
\qquad
k_B(z,w)=\langle v_B(z),v_B(w)\rangle.
\]

Hence

\[
k_\Theta(z,w)
=
\left\langle
\frac{v_S(z)}{B(z)},
\frac{v_S(w)}{B(w)}
\right\rangle
-
\left\langle
\frac{v_B(z)}{B(z)},
\frac{v_B(w)}{B(w)}
\right\rangle.
\]

Thus `Suzuki squared` does have a canonical exact realization, but it is a difference of two Hilbert squares:

\[
\boxed{
Q_\Theta(f)=\|A_Sf\|^2-\|A_Bf\|^2.
}
\]

The negative space is the finite-dimensional model space

\[
K_B=H^2\ominus BH^2,
\]

whose dimension equals the degree of `B`, counting multiplicities. Under the coprimeness hypothesis, the kernel has exactly `deg B` negative squares. This recovers the off-axis `(1,1)` orbit calculation globally.

## Why this is stronger than the earlier leakage identity

The Hardy block identity

\[
I-T_\Theta^*T_\Theta=H_\Theta^*H_\Theta
\]

only measured boundary leakage. The Krein--Langer identity identifies the actual interior indefinite term: it is the reproducing kernel of the forbidden pole divisor. It therefore supplies the previously schematic residual with the correct sign and rank.

The two viewpoints agree conceptually:

- `H_Theta` detects failure of Hardy invariance;
- `K_B` records the meromorphic pole directions responsible for that failure;
- cancellation of the negative square requires eliminating `K_B`, not squaring it again.

## Completed-zeta specialization

For

\[
\Theta=E^\#/E,
\qquad
E(z)=\xi(1/2-iz)+\xi'(1/2-iz),
\]

the Blaschke denominator is determined by zeros of `E` in the upper half-plane. Suzuki's Hermite--Biehler theorem identifies absence of the forbidden divisor with the critical-line condition.

Consequently the exact second-stage geometry is

\[
\boxed{
\text{completed-zeta model kernel}
=
\text{positive Schur bulk}
-
\text{positive divisor defect}.
}
\]

This is not yet source-derived in the required arithmetic sense because constructing `B` factors the unknown interior divisor. Nevertheless, it proves that there is no unaccounted indefinite remainder: all negative squares are concentrated in one canonical model space `K_B`.

## The only possible domination mechanism

For a restricted source subspace `M`, positivity is equivalent to

\[
\|A_Bf\|\le\|A_Sf\|
\qquad(f\in M).
\]

Equivalently, by Douglas factorization, there must exist a contraction `C` on the closure of the positive feature range such that

\[
A_B|_M=C A_S|_M.
\]

This is the precise abstract operator requested by the positive-remainder program. It need not annihilate the defect; it must contractively absorb the Blaschke feature into the Schur feature.

For a total Gaussian subspace, universal domination would imply positivity of the full kernel and hence removal of all negative squares. But for a genuinely finite rung-four subspace, this contraction condition is a nontrivial finite-rank target rather than a tautological norm square.

## Source-faithfulness obstruction

A construction of `C` from `B` is spectrally circular. A valid proof must construct the same contraction from endpoint--gamma--prime operations before identifying it with the divisor model. This sharply separates two claims:

1. **classification:** the negative defect is `K_B` -- available abstractly;
2. **arithmetic domination:** a source-defined contraction absorbs `K_B` -- still missing.

Any proposed endpoint or prime repair can now be tested against a rigid requirement: its feature dimension and multiplicity must match the Blaschke model defect, and its comparison map must be contractive.

## Disposition

The abstract `Suzuki squared` construction succeeds as

\[
\boxed{
Q_\Theta=\|A_S\cdot\|^2-\|A_B\cdot\|^2.
}
\]

It does not automatically prove positivity, but it identifies the unique missing operator: a source-derived Douglas contraction

\[
A_B=C A_S,
\qquad \|C\|\le1.
\]

This is narrower and more structural than numerical kernel testing or an unspecified remainder estimate.
