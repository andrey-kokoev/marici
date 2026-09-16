# The strong sewing completion exists only for the relative difference row, not the physical common row

## Correction to the two-route interface

The abstract implication

\[
(B_\lambda,C_\lambda)\to(B,C)\text{ in }\mathcal S_2\oplus\mathcal S_2
\Longrightarrow
B_\lambda^*C_\lambda\to B^*C\text{ in }\mathcal S_1
\]

is valid. It does not follow that both physical semilocal sewing legs admit such limits.

After Hadamard rotation, the actual Tate/reference feature has:

- a relative difference row \(D_L\);
- a common row \(C_L\).

Only the first belongs to the observer-localized Hilbert--Schmidt class.

## Exact strong completion of the difference row

Common Mellin translation gives

\[
(U_L\oplus U_L)^*D_LM_mU_L=D_0M_m
\]

for every \(L\). Moreover,

\[
\|D_0M_m\|_2^2
=
\frac12\int_{\mathbb R}\kappa_\gamma(t)|m(t)|^2dt,
\]

where

\[
\kappa_\gamma(t)
=
\frac1{4\pi^2}
\int_{\mathbb R}
\frac{|\gamma(s)-\gamma(t)|^2}{|s-t|^2}ds.
\]

Thus the positive relative feature is already complete on the weighted graph domain

\[
\mathcal D_D
=
L^2(\mathbb R,(1+\kappa_\gamma(t))dt).
\]

No \(L\)-dependent prolate estimate is needed for this row.

## No ordinary strong completion of the common row

The recentered common row is stationary only as a module map:

\[
(U_L\oplus U_L)^*C_LM_mU_L=C_0M_m.
\]

On the noncompact regular carrier, \(C_0M_m\) is generally not Hilbert--Schmidt. At finite radial volume \(V\), its squared norm has the form

\[
\|C_{0,V}M_m\|_2^2
=V\,\rho(m)+O(1),
\]

with nonzero bulk density \(\rho(m)\). Orthogonal subtraction of a single finite-dimensional vector cannot remove this translation-module divergence.

Consequently there is no ordinary \(\mathcal S_2\oplus\mathcal S_2\) completion of the full physical pair unless one first specifies a genuine bulk quotient, a semifinite density completion, or a two-copy channelwise counterterm.

## The two valid completions

The source therefore supports two different objects.

### Positive relative completion

\[
\boxed{m\longmapsto D_0M_m\in\mathcal S_2.}
\]

This is positive, cutoff-independent, conductor-compatible, and stable under angular direct sum when

\[
\sum_\chi
\int\kappa_{\gamma_\chi}(t)|m_{g,\chi}(t)|^2dt<\infty.
\]

### Signed product completion

The common row may pair with the difference row through a localized relative product even though it is not itself Hilbert--Schmidt:

\[
\boxed{
M_{m_h}^*\Pi_L^{left}\Delta Q_0M_{m_g}.
}
\]

Trace-class localization and the vanishing translated observer-commutator remainder can give a trace-norm or relative-trace limit. This is the minimal product route.

## Angular certificate

A direct source-compatible strong certificate is not a bound on raw prolate mass. It is

\[
E_G(\chi)
=
\int\kappa_{\gamma_\chi}(t)|m_{g,\chi}(t)|^2dt,
\qquad
\sum_\chi E_G(\chi)<\infty.
\]

Polynomial gamma-factor derivative bounds combined with Schwartz decay of the angular Mellin coefficients are sufficient for this summation. The remaining estimate is an observer-weighted polynomial bound for \(\kappa_{\gamma_\chi}\), not a growing bare transition trace.

## Revised frontier

The positive rung-four feature is closed for the **relative difference row** on its phase-energy graph domain. The full physical common-plus-difference pair is not closed in ordinary Hilbert--Schmidt space.

The unresolved sewing statement is narrower:

1. prove angular summability of the local phase energies \(E_G(\chi)\);
2. prove trace-class convergence of the localized common--difference product under translated placement;
3. retain the common row in a module, semifinite-density, or explicit bulk-quotient completion rather than declaring it Hilbert--Schmidt.
