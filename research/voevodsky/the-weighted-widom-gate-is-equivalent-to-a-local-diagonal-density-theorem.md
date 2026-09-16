# The weighted Widom gate is equivalent to a local diagonal-density theorem

## Localized trace

Let

\[
T_c^q
=
\eta(B_c^q),
\qquad q\in\{T,0\}.
\]

For each finite cutoff, \(T_c^q\) is positive and trace class on the generic prolate carrier. Let its integral kernel be

\[
K_c^q(s,t).
\]

Define the diagonal density

\[
\rho_c^q(s)=K_c^q(s,s).
\]

## Exact reduction of two observer legs

For bounded observer multipliers with sufficient decay, cyclicity gives

\[
\begin{aligned}
\mathcal E_c^q(g,h)
&=
\operatorname{Tr}
\left(
M_{m_h}^*T_c^qM_{m_g}
\right)\\
&=
\operatorname{Tr}
\left(
T_c^qM_{m_g\overline{m_h}}
\right).
\end{aligned}
\]

Therefore

\[
\mathcal E_c^q(g,h)
=
\int
m_g(s)\overline{m_h(s)}
\rho_c^q(s)
\frac{ds}{2\pi},
\]

with the measure adjusted to the declared kernel normalization.

Thus the weighted edge theorem is entirely a theorem about the diagonal density of \(\eta(B_c^q)\).

## Desired density statement

The proposed Plancherel leading Gram is equivalent to

\[
\frac{ho_c^q}{\log c}
\longrightarrow
2C_W\log2
\]

as a distribution on the admitted observer-product class.

Explicitly, for every product

\[
a_{g,h}=m_g\overline{m_h},
\]

one needs

\[
\int a_{g,h}(s)
\left[
\rho_c^q(s)
-2C_W(\log2)\log c
\right]
\frac{ds}{2\pi}
=O_{g,h}(1).
\]

This is the exact localized Widom remainder estimate.

## What the scalar trace law proves

The scalar Widom law gives only

\[
\int\rho_c^q(s)
\frac{ds}{2\pi}
=
2C_W(\log2)\log c+O(1)
\]

in the normalization where the unweighted trace is finite.

This controls the total mass of \(\rho_c^q\). It does not determine how that mass is distributed in \(s\).

Consequently the scalar coefficient \(2\log2\) does not by itself prove that the observer-weighted leading form is Plancherel. The density could concentrate near moving cutoff boundaries or another phase-space locus.

## Translation test

Let \(V_a\) translate the Mellin variable and define translated observer amplitudes

\[
m_{g,a}(s)=m_g(s-a).
\]

If the leading density is asymptotically constant, then

\[
\frac{
\mathcal E_c^q(g_a,g_a)
}{\log c}
\]

has the same limit for every fixed \(a\).

If the edge density is boundary-localized, translating the observer relative to the boundary changes or annihilates the limit.

This gives a direct diagnostic distinguishing a Plancherel edge from a moving boundary-evaluation edge.

## Common-translation covariance

Suppose the cutoff family satisfies

\[
B_c^q
=U_cB_1^qU_c^*
\]

for a common translation or modulation \(U_c\). Then

\[
T_c^q
=U_cT_1^qU_c^*.
\]

The diagonal density is transported rather than flattened. In that case, a fixed observer does not automatically see a constant \(\log c\) density.

The physical prolate family also changes window width, so it is not merely a unitary orbit. The widening component is exactly what must be analyzed to decide the local density law.

## Tate/reference comparison

The equality of normalized Tate and reference edge Grams is equivalent to

\[
\frac{ho_c^T-ho_c^0}{\log c}
\longrightarrow0
\]

on the observer-product test class.

A sufficient stronger estimate is

\[
\sup_c
\left|
\int a_{g,h}(s)
\left(
\rho_c^T(s)-ho_c^0(s)
\right)
\frac{ds}{2\pi}
\right|
<\infty.
\]

This isolates the scattering-stability problem from the reference local-density problem.

## Packet norm

For a finite observer packet \(E\), define

\[
\|\sigma\|_{E^*}
=
\sup_{
\|g\|_E,\|h\|_E\le1
}
\left|
\int
m_g\overline{m_h}\,\sigma
\frac{ds}{2\pi}
\right|.
\]

Then the required packet estimates are

\[
\left\|
\rho_c^0
-2C_W(\log2)\log c
\right\|_{E^*}
=O_E(1),
\]

and

\[
\|\rho_c^T-ho_c^0\|_{E^*}
=O_E(1).
\]

These imply the normalized common edge law on \(E\).

## Exact next calculation

The next calculation must derive or estimate

\[
K_c^0(s,s)
\]

for

\[
T_c^0=\eta(B_c^0).
\]

One then determines whether its logarithmic term is:

1. constant in \(s\), producing a Plancherel edge;
2. translated with the cutoff, producing a moving edge;
3. localized at finitely many boundaries, producing an evaluation-type edge;
4. dependent on the full observer profile through a nonlocal kernel.

Only the first case gives the previously proposed Gram

\[
2C_W(\log2)G_{Pl}.
\]

## Disposition

The two-observer weighted Widom theorem reduces exactly to diagonal-density asymptotics for \(\eta(B_c^q)\). The scalar Widom trace fixes the total coefficient \(2\log2\), but not the source Gram carrying that coefficient.

The Plancherel leading Gram remains a candidate until the local diagonal density of the reference prolate operator is computed.
