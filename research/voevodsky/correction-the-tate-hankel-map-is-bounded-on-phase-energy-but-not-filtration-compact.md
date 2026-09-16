# Correction: the Tate--Hankel map is bounded on phase energy but not filtration compact

## Proposed gate

A proposed route to a global physical common strip asked for the observer-localized Tate--Hankel map

\[
\mathcal H_\gamma:m\longmapsto[P,M_\gamma]M_m
\]

to be both bounded and compact relative to a finite-packet filtration.

The bounded part is true on the local phase-energy completion. The compact part is generally false.

## Exact norm identity

After endpoint/index terms are separated, the relative projection kernel is

\[
\Delta q(s,t)
=
\frac1{2\pi i}
\frac{
\gamma(s)\overline{\gamma(t)}-1
}{s-t}.
\]

Define

\[
\kappa_\gamma(t)
=
\frac1{4\pi^2}
\int_\mathbb R
\frac{|
\gamma(s)-\gamma(t)
|^2}{|s-t|^2}ds.
\]

Then Tonelli gives the exact polarized identity

\[
\boxed{
\langle
\mathcal H_\gamma m,
\mathcal H_\gamma n
\rangle_{HS}
=
\int
\kappa_\gamma(t)
\overline{n(t)}m(t)dt.
}
\]

Thus

\[
\boxed{
\|\mathcal H_\gamma m\|_{HS}^2
=
\|m\|_{L^2(\kappa_\gamma dt)}^2.
}
\]

On

\[
\mathscr E_\gamma
=L^2((1+\kappa_\gamma)dt),
\]

the map is bounded with norm at most one.

This closes the weighted Schatten boundedness requested by the previous note.

## Noncompactness

Assume there is a nonatomic measurable set \(B\) of positive measure on which

\[
\kappa_\gamma(t)\ge c>0.
\]

Choose pairwise disjoint measurable subsets \(B_j\subset B\) of positive finite measure and normalize

\[
m_j
=
\frac{1_{B_j}}
{\left(\int_{B_j}\kappa_\gamma(t)dt\right)^{1/2}}.
\]

Then

\[
\|m_j\|_{L^2(\kappa_\gamma dt)}=1
\]

and, by the polarized identity,

\[
\langle
\mathcal H_\gamma m_j,
\mathcal H_\gamma m_k
\rangle_{HS}
=0
\qquad(j\ne k).
\]

Hence \((\mathcal H_\gamma m_j)\) is an orthonormal sequence in the Hilbert--Schmidt carrier. It has no norm-convergent subsequence.

Therefore

\[
\boxed{
\mathcal H_\gamma:
L^2(\kappa_\gamma dt)
\to\mathcal L^2
\text{ is not compact}
}
\]

whenever the positive phase-energy measure has a nonatomic component.

The same conclusion holds for the semilocal orthogonal sum over places and angular characters as soon as one nontrivial radial sector is nonatomic.

## Failure of uniform finite-rank tail removal

Let \(P_n\) be any increasing finite-rank projections on the phase-energy space. If

\[
\|\mathcal H_\gamma(I-P_n)\|
\longrightarrow0,
\]

then \(\mathcal H_\gamma\) would be the operator-norm limit of the finite-rank maps \(\mathcal H_\gamma P_n\), hence compact. This contradicts the preceding result.

Consequently the proposed estimate

\[
\sup_L
\|K_L(I-P_n)\|
\longrightarrow0
\]

cannot hold in operator norm when \(K_L\) contains the full Tate--Hankel phase-energy row.

This is not a technical deficiency of the chosen filtration. It is ruled out by the exact source Gram.

## What remains true

For every fixed observer \(m\in\mathscr E_\gamma\), strong convergence \(P_n\to I\) gives

\[
\boxed{
\|\mathcal H_\gamma(I-P_n)m\|_{HS}^2
=
\int
\kappa_\gamma
|(I-P_n)m|^2
\longrightarrow0.
}
\]

Thus the correct tail statement is pointwise graph-core recovery, not uniform compactness on the energy unit ball.

For a Mosco recovery sequence this pointwise convergence is enough for the upper condition. It is not enough to deduce the lower condition from finite-packet coercivity without an independent global lower-semicontinuity argument.

## Correct global completion

The exact norm identity already supplies a packet-independent global carrier:

\[
\mathscr E_S
=
\bigoplus_\chi
L^2
\left(
\mathbb R,
\left[1+
\sum_{v\in S}
\kappa_{v,\chi}(t)
\right]
\frac{dt}{2\pi}
\right).
\]

On this space:

1. the local Tate--Hankel difference row is bounded;
2. the normalized Tate multiplier
   \[
   \mathcal A_S
   =M_{w_S/e_S}
   \]
   is bounded and self-adjoint;
3. its Jordan square roots define the global positive boundary feature;
4. finite-character Mellin--Schwartz observers form a dense graph core.

Therefore the global positive boundary should be obtained by completing the exact relative difference row in its source-derived phase-energy norm. It should not be obtained by compactly removing that row as a perturbation of the extensive mismatch strip.

## Revised role of the common strip

The pure Hardy mismatch strip remains the correct extensive reference feature and gives finite-packet coercivity. It supports:

- fixed-packet common-edge extraction;
- centered signed regulator comparison;
- asymptotic feature-angle estimates on coercive packets.

It does not supply a uniform global common subfeature after completion. The radial phase-energy row contains infinitely many mutually orthogonal boundary directions of fixed energy.

Thus two levels must remain distinct:

\[
\boxed{
\begin{array}{ll}
\text{finite packets:}&
\text{common-strip removal and physical Douglas extraction};\\
\text{completed source:}&
\text{phase-energy graph completion of the relative row}.
\end{array}}
\]

## Mosco consequence

A global Mosco theorem for raw bulk-removed physical Grams cannot be inferred from finite-packet common-edge removal plus operator-norm tail compactness, because the latter is false.

A viable global theorem must instead compare closed forms directly on the common graph core:

\[
q_{\alpha}^{rel}
\longrightarrow
q_{energy}
\]

using:

1. pointwise convergence on the Mellin--Schwartz core;
2. a regulator-uniform graph bound;
3. weak lower semicontinuity in the phase-energy topology;
4. a separate balanced treatment of the Sonin and endpoint sectors.

No finite-rank uniform approximation of the full phase-energy unit ball should be required.

## Disposition

The weighted Schatten gate is closed exactly:

\[
\boxed{
\|[P,M_\gamma]M_m\|_{HS}^2
=
\int\kappa_\gamma|m|^2.
}
\]

But this identity simultaneously proves that the map is generally noncompact. The previous filtration-compactness target is withdrawn.

The correct next analytic problem is direct Mosco convergence of the centered relative forms in the phase-energy topology, not uniform physical common-strip extraction on the completed observer space.
