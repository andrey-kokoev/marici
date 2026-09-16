# The placement bound is graph-metric, not Plancherel, and forces an observer-energy filtration

## The proposed bound

Finite filtered common-bulk positivity would follow from

\[
-K_FI
\preceq
D_{L,F}-A_F
\preceq
K_FI
\]

on the conductor-truncated Plancherel source.

The Hardy commutator estimate shows that this is still too strong without an observer-energy cutoff.

## Hardy commutator norm

For a scalar observer multiplier \(M_m\), the standard estimate is

\[
\boxed{
\|[M_m,\Pi]\|_2^2
\asymp
\|m\|_{\dot H^{1/2}}^2.
}
\]

The placement remainder satisfies

\[
|\mathcal C_L(g,h)|
\le
\|[M_{m_h},\Pi_L]\|_2
\|\Delta Q_0M_{m_g}\|_2.
\]

Translation preserves the first norm, so uniformly in \(L\),

\[
|\mathcal C_L(g,h)|
\lesssim
\|m_h\|_{H^{1/2}}
\|m_g\|_{H^{1/2}}

times
\text{fixed symbol constants}.
\]

Thus the remainder is bounded in the observer graph metric, not generally in the unweighted Plancherel metric.

## Failure of an unweighted global bound

Choose normalized observer amplitudes with increasing Mellin oscillation:

\[
\|m_k\|_2=1,
\qquad
\|m_k\|_{H^{1/2}}\to\infty.
\]

The Hardy commutator estimate supplies no constant \(K_F\) satisfying

\[
|\mathcal C_L(g,g)|
\le K_F\|m_g\|_2^2
\]

uniformly over this sequence. Conductor truncation does not control Mellin frequency.

Therefore fixed conductor alone does not justify a Plancherel-order placement bound.

## Observer-energy filtration

Let

\[
\mathcal E
\]

be a positive observer-energy operator controlling the local \(H^{1/2}\) norm and the localized Hankel factor. Introduce

\[
Y_N=1_{[0,N]}(\mathcal E).
\]

On

\[
H_{F,N}=Z_FY_N\mathscr H_S,
\]

the graph norm is bounded by the Plancherel norm:

\[
\|m\|_{H^{1/2}}^2
\le c_N\|m\|_2^2.
\]

Consequently there is a finite constant \(K_{F,N}\) such that

\[
\boxed{
-K_{F,N}I
\preceq
Y_NZ_F(D_{L}-A)Z_FY_N
\preceq
K_{F,N}I
}
\]

uniformly in the placement translation \(L\), provided all other finite regulator coordinates remain in the declared compact range.

## Positive admissibility condition

If the reference Gram obeys

\[
G_{L,F,N}^0
\succeq
(L-\delta_{L,F,N})I,
\]

then the Tate Gram satisfies

\[
G_{L,F,N}^T
\succeq
\left(
L-
\delta_{L,F,N}-
F-C_S-K_{F,N}
\right)I.
\]

A common positive bulk therefore exists whenever

\[
\boxed{
L
\ge
\delta_{L,F,N}+F+C_S+K_{F,N}.
}
\]

## Directed index region

The positive physical system must include observer energy as a genuine filtration coordinate:

\[
\boxed{
\mathfrak I_S^{phys}
=
\left\{
(L,n,F,N):
L\ge
\delta_{L,F,N}+F+C_S+K_{F,N}
\right\}.
}
\]

Given two finite packets \((F_1,N_1)\) and \((F_2,N_2)\), enlarge to

\[
F_3=\max(F_1,F_2),
\qquad
N_3=\max(N_1,N_2)
\]

and then choose \(L_3\) above the resulting finite threshold. Hence the region is directed whenever \(K_{F,N}\) and \(\delta_{L,F,N}\) are finite on every packet.

## Boundary passage

For each fixed \((F,N)\), the placement remainder converges weakly on observer pairs by kernel oscillation. One then takes the directed union

\[
F,N\to\infty
\]

while increasing \(L\) sufficiently fast.

There is no claim of a uniform finite-\(L\) positive filler over the unfiltered observer Hilbert space.

## Relation to the regulator tuple

The finite regulator tuple was already written schematically as

\[
\alpha=(\Lambda,R,N,n,F).
\]

The coordinate \(N\) must be interpreted, or refined, as controlling the observer graph energy required by the Hardy commutator estimate. It cannot be treated merely as an inert finite multiplicity label.

If the existing \(N\) has a different meaning, an additional energy coordinate must be introduced.

## Disposition

The desired uniform bound is available only packetwise:

\[
\boxed{
\sup_L
\|Y_NZ_F(D_L-A)Z_FY_N\|
<\infty.
}
\]

Thus the physical polarity cube is jointly filtered by conductor and observer energy. The cutoff must dominate both the negative Tate conductor budget and the Hardy-placement graph-energy budget.
