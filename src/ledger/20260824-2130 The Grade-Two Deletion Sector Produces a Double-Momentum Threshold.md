# 2130 — The Grade-Two Deletion Sector Produces a Double-Momentum Threshold

> **Superseded by Entry 2135.** The grade-two graph is disconnected. Its
> source integrand has separate component-energy poles, not the global sum
> used below. The elimination is algebraically correct for an absent pole and
> has no cosmological Landau authority.

## Hard-to-vary claim

The correctly typed grade-two deletion summand has a relative Landau discriminant supported only on a labelled soft divisor, the external triangle wall, and the source-derived threshold

\[
E_T=\pm2P_2.
\]

It produces no quartic factor.

## Frozen sector

For `S={12,23}`, the summand has the single translated normal

\[
E_T^{(S)}=E_T+2(y_{12}+y_{23}).
\]

Set

\[
a=y_{12},
\qquad
y_{23}=-\frac{E_T}{2}-a,
\qquad
C=y_{31}^2.
\]

Restrict the frozen Cayley--Menger determinant to this hyperplane. The generic critical system is

\[
K_S(a,C)=0,
\qquad
\partial_aK_S=0,
\qquad
\partial_CK_S=0.
\]

## Exact elimination

Eliminating `a,C` gives

\[
\boxed{
32p_2^2(4p_2-E_T^2)^3
\Lambda(p_1,p_2,p_3)^3,
\qquad p_i=P_i^2.
}
\]

Thus the discriminant support is

\[
P_2=0,
\qquad
E_T=\pm2P_2,
\qquad
\Lambda(P_1^2,P_2^2,P_3^2)=0.
\]

The momentum label `2` is the shared endpoint of the two deleted edges. Cyclic transport gives the other grade-two sectors.

## Classification

The factor `4P_2^2-E_T^2` is a genuine source-derived pushforward threshold for this correlator summand. It is generated from the existing translated-normal and Cayley--Menger geometry, so it needs no new Carrier cell.

It is not the homogeneous algebraic-letter quartic \(\mathcal Q\).

Hence

\[
\boxed{
\text{grade-two deletion port}
\longrightarrow
\text{labelled double-momentum threshold coefficient support}.
}
\]

## Verification

The exact calculation is the `grade2_relative_landau` branch of

`research/benincasa/marici-gm/src/bin/three_site_deletion_landau.rs`.

It uses the single source normal, differentiates the restricted determinant, and performs exact Sylvester elimination.

## Next falsifier

Compute the correctly typed grade-three summand with its one normal

\[
E_T+2(y_{12}+y_{23}+y_{31})=0.
\]

Restrict the Cayley--Menger determinant to this hyperplane, solve its two-dimensional critical system, and classify the resulting external discriminant. No simultaneous lower-grade normals may be inserted.
