# Dark matter as Gram remainder

The dark matter abundance is not a particle physics parameter. It is a geometric ratio: the weighted contribution of the dark Gram entries to the total gravitational coupling.

## Setup

Full Gram on carrier \(X = \{x_1, \dots, x_N\}\) with \(\operatorname{Aut}(X) = S_N\):

\[
G_{ij} = \langle f_j | f_i \rangle \quad (N\times N \text{ matrix})
\]

Irrep decomposition under visible gauge group \(S_4 \times S_4 \times S_4 \subset S_N\) gives a projection \(P_{\text{vis}}\). Dark remainder:

\[
G_{\text{dark}} = G - P_{\text{vis}} G P_{\text{vis}}
\]

## Weighting

The energy density contributed by a Gram sector to the Einstein equations is

\[
\rho_{\text{sector}} = \kappa \cdot \frac{\operatorname{Tr}(G_{\text{sector}} \circ W)}{\operatorname{Vol}(X)}
\]

where:
- \(\kappa\) is the gravitational coupling scale (Planck scale from Gram normalization)
- \(W\) is a weighting matrix determined by the fibration rotation phases \(\theta_i\)
- \(\operatorname{Vol}(X) = \det(g_{ab})^{1/2}\) from the stabilizer Gram

## Phase decoherence

The fibration rotation gives each carrier point an internal phase \(\theta_i\). The field interference pattern is

\[
I(\theta) = \sum_{i,j} G_{ij} e^{i(\theta_j - \theta_i)}
\]

The visible sector phases are SM-gauge-rotated. The dark sector phases are frozen (no SM gauge coupling to rotate them). This decoherence suppresses the dark contribution to visible interactions by a statistical factor:

\[
W_{ij} = \langle e^{i(\theta_j - \theta_i)} \rangle_{\text{thermal}}
\]

For visible-visible pairs: \(W \sim 1\) (coherent, SM thermalizes them).
For dark-dark pairs: \(W \sim 0\) (decohered, no SM interaction to align phases).
For visible-dark pairs: \(W \sim \epsilon\) (small portal coupling).

Hence the dark sector contributes to gravity (Gram eigenvalues) but not to SM scattering (phase-averaged interference). This is why it clusters gravitationally but does not collide or radiate.

## Abundance ratio

For S₁₂ (12 points, 3 visible S₄ factors):

\[
\Omega_{\text{DM}} = \frac{\operatorname{Tr}(G_{\text{dark}} \circ W_{\text{dark}})}{\operatorname{Tr}(G_{\text{total}} \circ W_{\text{total}})}
\]

The weighting \(W\) is determined by:
1. Which phases are thermalized (visible: yes; dark: no)
2. The Gram eigenvalue distribution (mass scales)
3. The decoherence factor (portal coupling \(\epsilon\))

This ratio is not a free parameter—it follows from the carrier geometry and the fibration rotation. But the precise \(W\) kernel is the remaining gate.

## Open

The weighting kernel \(W\) must be derived from the fibration rotation's phase measure. If the phases are uniformly random for dark entries, then \(W_{\text{dark}} = 0\) and \(\Omega_{\text{DM}} = 0\)—no dark matter. If the phases have residual correlation from the carrier geometry, \(\Omega_{\text{DM}} > 0\). The observed value \(\Omega_{\text{DM}} \sim 0.27\) would then be a prediction, not a fit.