# The recentered relative difference leg is exactly cutoff-independent

## Common translation factor

Let

\[
U_L
=M_{e^{2iLs}}.
\]

The Tate and reference projections satisfy

\[
Q_L^T
=U_LQ_0^TU_L^*,
\]

\[
Q_L^0
=U_LQ_0^0U_L^*.
\]

Therefore

\[
\boxed{
\Delta Q_L
=Q_L^T-Q_L^0
=U_L\Delta Q_0U_L^*.
}
\]

All cutoff translation is common to the two projections.

## Observer commutation

In Mellin coordinates, an observer amplitude acts by multiplication `M_m`. Hence

\[
\boxed{
[U_L,M_m]=0.
}
\]

It follows that

\[
\boxed{
U_L^*
\Delta Q_L
M_m
U_L
=
\Delta Q_0
M_m.
}
\]

This is an exact operator identity for every cutoff `L`.

## Difference feature

The Hadamard difference row is

\[
D_L
=
\frac12
(F_{Q_L^T}-F_{Q_L^0}).
\]

Explicitly,

\[
\boxed{
D_Lx
=
\frac12
(\Delta Q_Lx,
-\Delta Q_Lx).
}
\]

Let `mathcal U_L^(2)=U_L \oplus U_L` act on its two output rows. Then

\[
\boxed{
(\mathcal U_L^{(2)})^*
D_L
M_m
U_L
=
D_0
M_m.
}
\]

Thus the observer-localized difference feature becomes exactly independent of cutoff after recentering both source and target by the common translation.

## Hilbert--Schmidt norm

If

\[
\Delta Q_0M_m
\in
\mathcal S_2,
\]

then

\[
D_LM_m
\in
\mathcal S_2
\]

and

\[
\boxed{
\|D_LM_m\|_2
=
\|D_0M_m\|_2
=
\frac1{\sqrt2}
\|\Delta Q_0M_m\|_2.
}
\]

Therefore the difference row has no cutoff growth. Its apparent motion is pure translation gauge.

## Exact recentered convergence

Define the recentered feature

\[
\boxed{
\widetilde D_L(m)
=(\mathcal U_L^{(2)})^*
D_LM_mU_L.
}
\]

Then

\[
\boxed{
\widetilde D_L(m)
=D_0M_m
}
\]

for every `L`. Consequently

\[
\boxed{
\widetilde D_L(m)
\longrightarrow
D_0M_m
}
\]

in Hilbert--Schmidt norm trivially.

This closes positive-leg convergence for the relative difference row.

## Common row

The Hadamard common row is

\[
C_L
=
\frac12
(F_{Q_L^T}+F_{Q_L^0}).
\]

It obeys the same covariance:

\[
(\mathcal U_L^{(2)})^*
C_L
M_m
U_L
=
C_0M_m.
\]

But `C_0M_m` is generally not Hilbert--Schmidt on the noncompact carrier. Recentring removes cutoff motion, not common source-volume divergence.

Thus:

- difference row: stationary and Hilbert--Schmidt;
- common row: stationary only as a multiplier/module map, not as a finite-norm Hilbert--Schmidt feature.

## Signed relative pairing

The relative projection identity becomes, after recentering,

\[
\boxed{
C_0^*J_2D_0
+D_0^*J_2C_0
=
\Delta Q_0.
}
\]

Therefore all Tate scattering information is contained in one fixed cutoff-independent relative pair `(C_0,D_0)`.

The cutoff parameter reappears only when the physical left projection is transported:

\[
\Pi_L^{left}
=U_L^*\PiU_L.
\]

## Placement is the sole moving component

The ordered relative product recenters as

\[
\boxed{
M_{m_h}^*
\Pi_L^{left}
\Delta Q_0
M_{m_g}.
}
\]

Hence the large-cutoff analysis separates exactly into:

1. a fixed trace-ideal relative boundary `Delta Q_0`;
2. a translated placement projection `Pi_L^(left)`;
3. an observer commutator remainder whose modulation vanishes by Riemann--Lebesgue.

No prolate eigenvalue asymptotic is required for this relative boundary limit.

## Endpoint/index row

If

\[
\Delta Q_0
=
\Delta Q_0^{regular}
+
\Delta Q_0^{index},
\]

both pieces are cutoff-independent after recentering. The finite-rank index row is transported by the same common unitary and therefore also becomes stationary.

Thus endpoint/winding multiplicity is preserved exactly under cutoff recentering.

## Angular and conductor compatibility

The unitary `U_L` acts only in the radial Mellin variable and is independent of angular character. It commutes with conductor projections `Z_F`.

Therefore

\[
\boxed{
Z_F\widetilde D_L(m)
=
\widetilde D_L(Z_Fm)
}
\]

and all conductor-successor cells commute exactly.

Angular direct sums preserve the stationary identity characterwise.

## Dyadic Halmos refinement

At each cutoff, the projection pair's generic angle contraction may be dyadically refined. Recentring by `U_L` unitarily identifies the entire Tate/reference projection pair with its `L=0` pair.

Functional calculus commutes with unitary conjugation, so every atom and dyadic defect slot is also stationary after recentering:

\[
\boxed{
U_L^*
f(B_L)
U_L
=f(B_0)
}
\]

for the correctly transported base projection and generic carrier.

Thus cutoff recentering and dyadic refinement commute on the nose.

## Distinction from physical cutoff growth

The exact stationarity concerns the **relative Tate/reference pair after common translation removal**. It does not say that Connes's full physical cutoff feature is cutoff-independent.

The physical volume term and ordered placement are carried by the moving left projection and outer regulator. They are absent from the recentered difference row by construction.

## Positive boundary conclusion

The positive part of the relative feature that genuinely belongs to Tate scattering is

\[
\boxed{
D_0M_m
=
\frac12
(\Delta Q_0M_m,
-\Delta Q_0M_m).
}
\]

It is:

- Hilbert--Schmidt on the observer core;
- independent of cutoff;
- compatible with angular/conductor restriction;
- compatible with dyadic Halmos refinement;
- inclusive of finite-rank endpoint rows.

The divergent common row is retained only as a relative module partner.

## Revised role of near-one asymptotics

Near-one/prolate spectral asymptotics remain relevant for microscopic positive decomposition of the physical Tate pair and for comparing finite generic-angle slots.

They are not needed to prove convergence of the recentered Tate/reference difference row itself. That convergence is exact by covariance.

This sharply separates:

- relative boundary convergence: solved by common translation;
- physical prolate bulk analysis: needed only for refinement/minimalization questions.

## Disposition

The recentered relative leg satisfies

\[
\boxed{
(U_L\oplus U_L)^*
D_LM_mU_L
=D_0M_m
}
\]

exactly. Therefore the positive Hilbert--Schmidt difference leg has a canonical cutoff-independent boundary value. All residual cutoff dependence is confined to the divergent common module and the translated left-placement projection.
