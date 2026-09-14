# Translation covariance plus observer-commutator oscillation makes the left-Hardy placement converge to the full relative trace

## Common cutoff translation

Let

\[
U_L
=M_{e^{2iLs}}.
\]

Write the Tate and reference projections as

\[
Q_L^T
=U_LQ_0^TU_L^*,
\]

\[
Q_L^0
=U_LQ_0^0U_L^*,
\]

where

\[
Q_0^T
=M_\gamma\PiM_\gamma^*,
\qquad
Q_0^0
=\Pi.
\]

Thus

\[
\boxed{
\Delta Q_L
=Q_L^T-Q_L^0
=U_L\Delta Q_0U_L^*,
}
\]

with

\[
\Delta Q_0
=M_\gamma\PiM_\gamma^*-\Pi.
\]

## Observer multiplier commutes with translation phase

Let `M_f` be the observer density multiplier in the Mellin variable. Since both `M_f` and `U_L` are multiplication operators,

\[
\boxed{
[U_L,M_f]=0.
}
\]

Therefore unitary cyclicity gives

\[
\begin{aligned}
\operatorname{Tr}
(M_f\Pi\Delta Q_L)
&=
\operatorname{Tr}
(M_f\PiU_L
\Delta Q_0U_L^*)\\
&=
\operatorname{Tr}
(M_fU_L^*\Pi U_L
\Delta Q_0).
\end{aligned}
\]

Define the translated left Hardy projection

\[
\boxed{
\Pi_L^{left}
=U_L^*\PiU_L.
}
\]

Then

\[
\boxed{
\operatorname{Tr}
(M_f\Pi\Delta Q_L)
=
\operatorname{Tr}
(M_f\Pi_L^{left}\Delta Q_0).
}
\]

This identity is exact whenever the localized product is trace class.

## Strong half-line limit

In the Fourier-dual variable, conjugation by `U_L` translates the Hardy half-line by distance `2L`.

There are two orientations:

\[
\Pi_L^{left}
\xrightarrow[s]{L\to\infty}
I
\]

or

\[
\Pi_L^{left}
\xrightarrow[s]{L\to\infty}
0.
\]

The Connes orientation is the one in which the relative Tate boundary is eventually contained on the accepted side of the physical cutoff:

\[
\boxed{
\Pi_L^{left}
\xrightarrow[s]{L\to\infty}
I.
}
\]

This is the same orientation that gives the positive `2L h(1)` cutoff spectral-flow coefficient.

## Trace-class convergence

Assume the regular observer-localized relative operator

\[
\boxed{
T_f
=M_f\Delta Q_0
\in
\mathcal S_1
}
\]

with endpoint/index terms separated.

Since `Pi_L^(left)->I` strongly and the projections are uniformly bounded,

\[
\boxed{
\|(\Pi_L^{left}-I)T_f\|_1
\longrightarrow0.
}
\]

Therefore

\[
\boxed{
\operatorname{Tr}
(M_f\Pi\Delta Q_L)
\longrightarrow
\operatorname{Tr}
(M_f\Delta Q_0).
}
\]

This evaluates the left-compressed ordered relative product by the full relative projection trace in the large-cutoff limit.

## Two-sided observer placement

For polarized observers define

\[
T_{g,h}
=M_{m_h}^*
\Delta Q_0
M_{m_g}.
\]

Again all observer multipliers commute with `U_L`. Exact cyclic transport gives the left projection `Pi_L^(left)` acting on the trace-class operator `T_(g,h)` in the inherited position.

If

\[
T_{g,h}
\in
\mathcal S_1,
\]

then

\[
\boxed{
\operatorname{Tr}
(M_{m_h}^*
\Pi\Delta Q_L
M_{m_g})
\longrightarrow
\operatorname{Tr}
(M_{m_h}^*
\Delta Q_0
M_{m_g}).
}
\]

The same argument covers unequal left/right regulator factors once the exact finite trace is cyclically arranged around one trace-class relative operator.

## Evaluation of the limit

The standard projection-pair formula gives

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}_{rel}
(M_{m_h}^*
\Delta Q_0
M_{m_g})\\
&\quad=
\frac1{2\pi i}
\int_\mathbb R
\overline{m_h(s)}
m_g(s)
\partial_s
\log\gamma(s)ds
+
e_{end}(g,h).
\end{aligned}
}
\]

Hence

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}
(M_{m_h}^*
\Pi\Delta Q_L
M_{m_g})\\
&\quad\longrightarrow
\frac1{2\pi i}
\int
\overline{m_h}
m_g\partial_s\log\gammads
+
e_{end}(g,h).
\end{aligned}
}
\]

This is the Tate--Weil local boundary form.

## Placement correction coefficient

Recall

\[
\Pi
=
\frac12(I+J_\Pi).
\]

The placement correction was

\[
\mathcal P_L(f)
=
\frac12
\operatorname{Tr}
(M_fJ_\Pi\Delta Q_L).
\]

Since the full ordered trace tends to the uncompressed relative trace,

\[
\boxed{
\mathcal P_L(f)
\longrightarrow
\frac12
\operatorname{Tr}_{rel}
(M_f\Delta Q_0).
}
\]

Thus the left-Hardy reflection contributes the missing half of the Tate projection-pair trace. It does not vanish.

## Linear-phase calibration

Take

\[
\gamma(s)
=e^{ibs}.
\]

Then `Delta Q_0` is the signed projection onto the interval between two Hardy boundaries separated by `b`.

In the Connes orientation, translating the left projection by `2L` eventually places that entire fixed interval inside its range. Therefore

\[
\Pi_L^{left}\Delta Q_0
=
\Delta Q_0
\]

for all sufficiently large `L` in the exact compact-interval model.

Hence the ordered trace equals the full interval trace, confirming the coefficient `1`, while the reflection placement term supplies one half after the decomposition `Pi=(I+J)/2`.

## Opposite orientation

If

\[
\Pi_L^{left}
\xrightarrow[s]0,
\]

then

\[
\operatorname{Tr}
(M_f\Pi\Delta Q_L)
\longrightarrow0.
\]

This orientation cannot represent Connes's nonzero local Weil term without reversing the projection difference or the cutoff polarity.

Thus the strong-limit test fixes the orientation unambiguously.

## Endpoint/index part

Let

\[
\Delta Q_0
=
\Delta Q_0^{regular}
+
\Delta Q_0^{index}.
\]

The regular observer-localized part is trace class by two-sided Schwartz localization. The index part is finite rank or a declared endpoint graph channel.

Strong convergence of `Pi_L^(left)` to `I` applies to both:

\[
\Pi_L^{left}
\Delta Q_0^{index}
\to
\Delta Q_0^{index}
\]

in trace norm for finite-rank index operators. Therefore endpoint multiplicity is preserved.

## Transported outer regulators

At finite physical outer regulator, exact unitary transport gives `widetilde Z_R`. For fixed `L`, first send

\[
R,N\to\infty
\]

using trace-class localization. This produces the unregulated ordered Hardy trace.

Then send

\[
L\to\infty
\]

using the strong translated-half-line limit above.

Thus the admitted iterated order is

\[
\boxed{
(R,N)
\to\infty
\quad
\text{first},
\qquad
L\to\infty
\quad
\text{second}.
}
\]

No uniform simultaneous regulator estimate is required.

## Angular assembly

On a Bruhat--Schwartz observer, finite conductor support reduces the angular sum to finitely many sectors. Apply the strong-limit argument characterwise and sum.

For an infinite smooth angular expansion, use a trace-norm majorant for `T_(g,h,chi)` and dominated convergence. The translated projection norm is at most one, so it introduces no additional angular growth.

## Relation to Connes finite part

After angular assembly,

\[
\boxed{
\lim_{L\to\infty}
\operatorname{Tr}
(M_{m_h}^*
\Pi\Delta Q_L
M_{m_g})
=
W_S(g*h^*).
}
\]

This is exactly the ordered Hardy relative form needed to align the finite part of Connes's product cutoff with the Tate scattering connection.

The universal `2L h(1)` reference term remains in the pure translated projection and was removed before forming `Delta Q_L`.

## Consequence for the anti-Hermitian channel

The limit on the right is Hermitian. Therefore the anti-Hermitian eight-leg readout converges to zero by reality and polarization, while the Hermitian readout converges to `W_S`.

This closes both placement channels at the form level.

## Scope warning

The conclusion relies on:

1. exact common-translation factorization of `Q_L^T` and `Q_L^0`;
2. observer multipliers commuting with `U_L`;
3. trace-class localization of `Delta Q_0` after observer sandwiching;
4. the Connes orientation `Pi_L^(left)->I`;
5. iterated regulator limits.

If a transported observer is not a Mellin multiplier or the physical regulator limit must be simultaneous, additional estimates are required.

## Subsequent correction

Strong convergence cannot pass through the left observer multiplier directly. Commuting the translated Hardy projection outward leaves `[M_m^*,Pi_L] Delta Q_0 M_g`. Under the available two Hilbert--Schmidt bounds, its kernel pairing is `L1` and carries modulation `exp(-2iL(s-t))`, so Riemann--Lebesgue makes it vanish. See `correction-translation-strong-convergence-leaves-an-observer-hardy-commutator-remainder.md`.

## Disposition

With that oscillatory commutator argument, the placement gate is closed in the iterated Hardy model:

\[
\boxed{
\operatorname{Tr}
(M_{m_h}^*
\Pi
(Q_L^T-Q_L^0)
M_{m_g})
\longrightarrow
\operatorname{Tr}_{rel}
(M_{m_h}^*
(Q_0^T-Q_0^0)
M_{m_g}).
}
\]

The left Hardy projection becomes the identity after conjugating out the common cutoff translation. The surviving trace is exactly the Tate logarithmic-derivative plus endpoint form.
