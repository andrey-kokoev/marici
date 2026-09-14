# Exact regulator transport aligns the physical product cutoff with the eight-leg Hardy readout

## Characterwise unitary

Fix an angular character `chi`. Let

\[
\mathcal U_\chi:
\mathcal H_{S,\chi}^{physical}
\longrightarrow
L^2(\mathbb R,ds)
\]

be the exact composition of:

1. the conull-orbit/Radon--Nikodym unitary;
2. logarithmic radial coordinates;
3. translation by the cutoff boundary `L=log Lambda`;
4. Mellin/Fourier transform;
5. the fixed reflection convention.

Under this unitary, the physical cutoff becomes a Hardy projection:

\[
\boxed{
\mathcal U_\chi
P_\Lambda
\mathcal U_\chi^*
=
\Pi.
}
\]

The Fourier-conjugate cutoff becomes

\[
\boxed{
\mathcal U_\chi
Q_\Lambda^T
\mathcal U_\chi^*
=
Q_{L,\chi}^T
=
M_{e^{2iLs}\gamma_\chi}
\Pi
M_{e^{2iLs}\gamma_\chi}^*.
}
\]

Exact signs are fixed by choosing the orientation that reproduces the positive `2L h(1)` spectral-flow coefficient.

## Reference projection

On the same Hardy carrier, define

\[
\boxed{
Q_L^0
=
M_{e^{2iLs}}
\Pi
M_{e^{2iLs}}^*.
}
\]

Transport it back to the physical angular fiber:

\[
\boxed{
Q_{\Lambda,\chi}^0
=
\mathcal U_\chi^*
Q_L^0
\mathcal U_\chi.
}
\]

This is the canonical pure-translation reference associated with the same cutoff coordinate and Hardy polarization. It is not introduced by changing the observer or cutoff projection.

## Observer placement

Scaling convolution by an observer amplitude becomes Mellin multiplication:

\[
\boxed{
\mathcal U_\chi
A_g
\mathcal U_\chi^*
=M_{m_{g,\chi}}.
}
\]

Therefore the physical ordered relative product

\[
P_\Lambda
(Q_\Lambda^T-Q_\Lambda^0)
A_g
\]

transports exactly to

\[
\boxed{
\Pi
(Q_{L,\chi}^T-Q_L^0)
M_{m_{g,\chi}}.
}
\]

No observer factor is commuted through `Pi` or either `Q`.

## Finite physical regulator

Let

\[
Z_{\Lambda,R,N}^{physical}
\]

be the exact finite outer/angular regulator used to make the physical product trace ordinary. Restrict to one admitted angular sector and define its transported regulator

\[
\boxed{
\widetilde Z_{L,R,\chi}
=
\mathcal U_\chi
Z_{\Lambda,R,N}^{physical}
\mathcal U_\chi^*.
}
\]

This projection/operator need not be multiplication by a symmetric Mellin interval. It need not commute with `Pi` or `M_m`.

That is harmless: trace invariance requires retaining the transported operator exactly, not replacing it with a convenient model regulator.

## Exact trace identity

At finite regulator, unitary invariance of trace gives

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}
\left(
Z^{physical}
P_\Lambda
(Q_\Lambda^T-Q_\Lambda^0)
A_g
Z^{physical}
\right)\\
&\quad=
\operatorname{Tr}
\left(
\widetilde Z
\Pi
(Q_{L,\chi}^T-Q_L^0)
M_{m_{g,\chi}}
\widetilde Z
\right).
\end{aligned}
}
\]

This is exact for every finite `(Lambda,R,N)`.

## Observer-factor Gram version

For `h=g*k^*`, factor the observer as `A_gA_k^*` with the chosen convolution convention. Cyclicity at finite regulator gives

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}
\left(
Z
P_\Lambda
\Delta Q_\Lambda
A_gA_k^*
Z
\right)\\
&\quad=
\operatorname{Tr}
\left(
(\widetilde ZA_k)^*
\Pi
\Delta Q_L
(A_g\widetilde Z)
\right),
\end{aligned}
}
\]

with the exact left/right regulator positions inherited from cyclic permutation. One must not silently replace both observer legs by the same symmetrically regulated factor unless the regulator commutes with convolution.

The eight-leg construction can accept unequal source legs; its cross-polarized identity is bilinear.

## Eight-leg realization with transported regulator

Let

\[
\Psi_L^*J_4\Psi_L
=
\Delta Q_L
\]

be the four-leg relative projection feature. Define the cross feature using the actual transported observer legs:

\[
\boxed{
\Theta_{L,R,\chi}(g)
=
\frac1{\sqrt2}
\left(
\Psi_L(\Pi M_{m_g}
\widetilde Z),
\Psi_L(M_{m_g}
\widetilde Z)
\right).
}
\]

For unequal left/right regulator placements, use the polarized pairing between the corresponding `g` and `k` features rather than forcing one common vector formula.

Its Hermitian `K_8` readout is exactly the symmetrized transported ordered product; its `K_8^(skew)` readout is exactly the placement commutator channel.

## No auxiliary-window descent problem

Earlier auxiliary arguments introduced a symmetric finite Mellin window and then faced a descent problem to Connes's one-sided cutoff.

The transported-regulator construction avoids that substitution:

\[
\boxed{
\text{physical finite regulator}
\xrightarrow{\mathcal U_\chi}
\text{exact transported Hardy regulator}.
}
\]

There is no claim that the transported regulator is simple. Simplicity is unnecessary for exact typing and finite trace identities.

A simple Hardy window may still be useful for estimates, but then comparison with `widetilde Z` is a separate approximation theorem rather than an identity.

## Angular assembly

At finite angular cutoff `N`, take the direct sum

\[
\mathcal U_N
=
\bigoplus_{|\chi|\le N}
\mathcal U_\chi.
\]

All trace and eight-leg identities hold blockwise and therefore after finite direct sum.

Removing `N` uses rapid observer angular decay and the polynomial/conductor bounds of the Tate symbols. The exact finite identities ensure that no angular multiplicity or observer placement changes during this limit.

## Reference calibration

Define the physical reference trace by transport:

\[
\boxed{
T_{\Lambda,R,N}^0(h)
=
\sum_\chi
\operatorname{Tr}
\left(
\widetilde Z
\Pi Q_L^0
M_{m_{h,\chi}}
\widetilde Z
\right).
}
\]

To conclude

\[
T_{\Lambda}^0(h)
=2Lh(1)+o(1),
\]

one still needs the pure translated-Hardy strip calibration with this exact transported regulator. The simple translation-invariant calculation proves the coefficient for a multiplier-localized model, not automatically for arbitrary `widetilde Z`.

Thus exact alignment is solved, while asymptotic evaluation of the transported reference remains analytic.

## Relative trace limit

The Tate/reference difference is

\[
\boxed{
T_{\Lambda,R,N}^T(h)
-T_{\Lambda,R,N}^0(h)
\]

and transports exactly to the localized relative Hardy projection pair.

If regulator removal is admitted in the relative product class, the projection-pair formula yields

\[
\boxed{
\lim_{R,N,\Lambda}
(T^T-T^0)
=
\sum_\chi
\frac1{2\pi i}
\int
m_{h,\chi}(s)
\partial_s
\log\gamma_\chi(s)ds
+
E_{end}(h).
}
\]

For `h=g*k^*`, this is the polarized Tate--Weil form.

## Relation to Connes's theorem

Connes's theorem evaluates the physical Tate product directly:

\[
T_\Lambda^T(h)
=
2Lh(1)
+W_S(h)
+o(1).
\]

The local Tate identity evaluates the relative difference as `W_S(h)`. Therefore, once the exact relative regulator limit above is justified, subtraction implies the reference calibration

\[
\boxed{
T_\Lambda^0(h)
=
2Lh(1)
+o(1).
}
\]

This derives the transported-reference asymptotic without replacing its regulator by a simple Mellin window.

## Logical circle warning

The preceding subtraction is valid only if the relative Hardy limit is proved for the exact transported regulator. It cannot be used to prove that same regulator limit.

A noncircular route is:

1. exact unitary transport at finite regulator;
2. relative trace convergence for `widetilde Z`;
3. local Tate projection-pair identity;
4. Connes theorem;
5. derive pure-reference calibration.

## Placement channel

Because the transport preserves the ordered product exactly, the anti-Hermitian channel is the imaginary part of Connes's ordered relative trace. Reality plus polarization then proves its form-level vanishing.

Thus no separate operator-placement approximation remains after exact transport; only relative regulator removal is analytic.

## What is solved

Solved exactly:

1. physical-to-Hardy unitary conjugation on each angular fiber;
2. definition of the pure reference on the physical carrier;
3. observer position under conjugation;
4. finite regulator transport;
5. finite ordered trace identity;
6. eight-leg positive realization of Hermitian and skew placements.

Still analytic:

1. relative trace convergence with the transported outer regulator;
2. angular dominated convergence at unbounded conductor;
3. endpoint branch/index compatibility;
4. comparison of physical generic-angle dyadic refinement with the four/eight-leg carrier.

## Disposition

The correct alignment rule is

\[
\boxed{
\widetilde Z_{L,R,\chi}
=
\mathcal U_\chi
Z_{\Lambda,R,N}^{physical}
\mathcal U_\chi^*,
}
\]

not replacement by a convenient Hardy window. With this rule, Connes's finite ordered product is exactly the eight-leg Hardy readout with unchanged observer placement. The remaining `C_34` regulator gate is relative trace convergence for this transported regulator, not operator alignment.
