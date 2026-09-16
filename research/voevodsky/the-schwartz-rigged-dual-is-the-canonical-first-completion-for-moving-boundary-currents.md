# The Schwartz rigged dual is the canonical first completion for moving boundary currents

## Prior-research alignment

The established rigged-boundary theorem requires a declared test rung

\[
\Phi
\hookrightarrow
H
\hookrightarrow
\Phi'
\]

and treats boundary distributions through continuous transposes, not ambient Hilbert adjoints.

For continuous spectral-boundary currents, the canonical first choice is the Schwartz rigging

\[
\mathcal S(\mathbb R)
\hookrightarrow
L^2(\mathbb R)
\hookrightarrow
\mathcal S'(\mathbb R).
\]

This choice is not yet a Hilbert realization of the current. It is the minimal deformation-stable distributional carrier.

## Boundary-current space

Let

\[
\mathscr I_\partial
=
\mathcal S'(\mathbb R)_\beta
\]

be the strong dual of Schwartz space. Its seminorms are

\[
p_B(\mu)
=
\sup_{\phi\in B}
|\langle\mu,\phi\rangle|,
\]

where \(B\) ranges over bounded subsets of \(\mathcal S(\mathbb R)\).

This space contains:

1. regular functions of polynomial or logarithmic growth;
2. principal-value distributions;
3. finite and polynomially bounded sums of delta derivatives;
4. finite spectral-flow atomic measures.

## Poisson crossing continuity

Define

\[
P_a^\gamma(t)
=
\frac1\pi
\frac{|a|}
{(t-\gamma)^2+a^2}.
\]

For every Schwartz test function \(\phi\),

\[
\lim_{a\to0}
\int
P_a^\gamma(t)
\phi(t)
\,dt
=
\phi(\gamma).
\]

Hence

\[
P_a^\gamma
\longrightarrow
\delta_\gamma
\]

in \(\mathcal S'(\mathbb R)_\beta\). The convergence is uniform on bounded Schwartz sets, so it is strong-dual convergence rather than merely pointwise weak convergence.

For the symmetry-completed crossing,

\[
P_a^\gamma
+
P_a^{-\gamma}
\longrightarrow
\delta_\gamma
+
\delta_{-\gamma}.
\]

Thus each unsigned Poisson profile has a strong-dual delta limit. The signed phase current has opposite one-sided limits and is not itself continuous through the crossing. Continuity requires the affine spectral-flow clutching constructed separately.

## Source test rung

Let \(\mathscr G_r^{\mathcal S}\) be the completion of the degree-\(r\) Mellin--Schwartz core with the existing strip, endpoint, and phase-energy graph seminorms together with the real-boundary Schwartz seminorms

\[
q_{M,N}(p)
=
\sup_{t\in\mathbb R}
|t^M
\partial_t^N m_p(t)|.
\]

The map

\[
(p,q)
\longmapsto
\overline{m_q}m_p
\]

is jointly continuous

\[
\mathscr G_r^{\mathcal S}
\times
\mathscr G_r^{\mathcal S}
\to
\mathcal S(\mathbb R).
\]

This follows from the standard Leibniz estimates for Schwartz seminorms.

## Current observation

For \(\mu\in\mathscr I_\partial\), define

\[
Q_\mu(p,q)
=
\langle
\mu,
\overline{m_q}m_p
\rangle.
\]

This is a continuous sesquilinear form on \(\mathscr G_r^{\mathcal S}\).

For an atomic current,

\[
Q_{\delta_\gamma}(p,q)
=
m_p(\gamma)
\overline{m_q(\gamma)}.
\]

Thus finite divisor crossings are represented by bounded forms on the Schwartz test rung without pretending that delta evaluation is bounded on ambient \(L^2\).

## Uniform family criterion

Let \(A\) be a deformation parameter space and let

\[
a
\longmapsto
\mu_a
\in
\mathscr I_\partial.
\]

If the image of a compact set \(K\subset A\) is bounded in the strong dual, then the forms \(Q_{\mu_a}\) are equicontinuous on bounded subsets of \(\mathscr G_r^{\mathcal S}\).

Explicitly, for every bounded source packet \(P\),

\[
\sup_{
a\in K,
p,q\in P
}
|Q_{\mu_a}(p,q)|
<\infty.
\]

The unsigned one-pole and symmetry-completed Poisson profiles satisfy this criterion on compact parameter intervals. Their signed phase currents are bounded but have opposite one-sided limits; retaining an atom without an oriented index clutching does not make the path continuous.

## Dagger

Define the boundary reflection on Schwartz tests by

\[
(R\phi)(t)
=
\overline{\phi(-t)}.
\]

Its transpose defines the current dagger

\[
\langle
R'\mu,
\phi
\rangle
=
\overline{
\langle
\mu,
R\phi
\rangle
}.
\]

Then

\[
R'\delta_\gamma
=
\delta_{-\gamma}.
\]

The symmetry-completed atomic current is dagger invariant up to its crossing orientation.

## Convolution successors

An admitted convolution successor acts by multiplication with a Mellin amplitude \(m_a\). On polarized Schwartz tests,

\[
\overline{m_q}m_p
\longmapsto
|m_a|^2
\overline{m_q}m_p.
\]

If \(m_a\) and all derivatives have polynomially controlled growth, multiplication by \(|m_a|^2\) is continuous on the selected Schwartz multiplier class.

The transpose action on currents is

\[
M_{|m_a|^2}'
:
\mathscr I_\partial
\to
\mathscr I_\partial.
\]

For atoms,

\[
M_{|m_a|^2}'
\delta_\gamma
=
|m_a(\gamma)|^2
\delta_\gamma.
\]

This gives the exact successor law on the rigged dual.

## Regular current

A regular phase current with at most logarithmic growth defines a tempered distribution by

\[
\langle
\mu_{reg},
\phi
\rangle
=
\int
V_{loc,S}(t)
\phi(t)
\,dt.
\]

The digamma growth and every fixed semilocal prime phase are compatible with this definition.

This proves the finite-stage regular-plus-atomic current belongs to \(\mathscr I_\partial\).

It does not by itself prove that an infinite global prime or divisor sum converges in the strong dual.

## Green identity typing

Let

\[
\gamma_{cur}:
\mathscr G_r^{\mathcal S}
\to
\mathcal S(\mathbb R)
\]

be the polarized boundary-test map. Its continuous transpose sends currents into the rigged source dual:

\[
\gamma_{cur}':
\mathscr I_\partial
\to
(
\mathscr G_r^{\mathcal S}
)'.
\]

The regular, moving-index, and fixed-endpoint Green rows therefore live in a common rigged-dual equation, but only the fixed endpoint row has the previously constructed finite-dimensional graph-Hilbert realization.

No ambient \(L^2\) adjoint is assigned to the atomic current.

## Lattice placement

The terminal node is now typed as

\[
C_{13,7}^{aug}
=
C_{13,7}^{reg}
\oplus
\mathscr I_\partial
\oplus
\mathscr H_{end}.
\]

This is an enriched Hermitian-form presentation on the test rung. It is not an orthogonal Hilbert direct sum.

The signed face \(H_{134}\) reads all three channels through dual pairings. The positive-lift question remains separate because \(\mathscr I_\partial\) is not supplied with a positive Hilbert metric.

## What this closes

For finite semilocal stages and finite moving divisor packets, the construction supplies:

1. a canonical current topology;
2. strong one-sided limits at boundary crossings;
3. continuous source pairing;
4. dagger transport;
5. convolution-successor transport;
6. correct rigged Green typing;
7. placement in the terminal \(C_{13}\) presentation.

## What remains

The following stronger claims are open:

1. strong-dual convergence of the complete infinite prime/divisor current;
2. a graph-Hilbert norm controlling the current uniformly;
3. a physical trace-class realization of arbitrary moving atoms;
4. positivity or Schur domination of the current channel;
5. simultaneous regulator and deformation limits.

## Disposition

The Schwartz rigged dual tames the missing boundary current at the correct distributional level and exposes its two oriented one-sided limits without conflating moving atoms with fixed endpoints or assigning false ambient adjoints. A separate affine spectral-flow clutching is required to obtain a continuous augmented crossing.

This is the maximal unconditional completion supported by the current source estimates.
