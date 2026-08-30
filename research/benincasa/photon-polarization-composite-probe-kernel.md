# Photon Polarization Composite-Probe Kernel

## Bounded question

Does the source-authorized two-photon polarization probe family distinguish the real and complex quantum coefficient lenses?

This packet derives the exact algebraic map and a hostile two-point fiber.  Source authorization of the circular-polarization probe remains a separate gate pending the optical audit.

## Conventions

Let

\[
\sigma_0=I,
\qquad
\sigma_1=X,
\qquad
\sigma_2=Y,
\qquad
\sigma_3=Z.
\]

For a two-polarization density operator (ho), define the labelled product-probe map

\[
\mathcal P(\rho)_{\mu\nu}
=
\operatorname{Tr}
\left[
\rho(\sigma_\mu\otimes\sigma_\nu)
\right],
\qquad
\mu,\nu\in\{0,1,2,3\}.
\]

Pauli orthogonality gives

\[
\operatorname{Tr}(\sigma_\mu\sigma_\alpha)
=2\delta_{\mu\alpha},
\]

and therefore

\[
\rho
=
\frac14
\sum_{\mu,\nu=0}^3
\mathcal P(\rho)_{\mu\nu}
\sigma_\mu\otimes\sigma_\nu.
\]

Thus the complete sixteen-probe map is injective.

## Real-probe restriction

The local real-symmetric one-rebit observables are spanned by

\[
I,
\quad X,
\quad Z.
\]

Restrict (mathcal P) to the nine products with (mu,\nu\in\{0,1,3\}).  Then

\[
\operatorname{Tr}
\left[
(Y\otimes Y)(\sigma_\mu\otimes\sigma_\nu)
\right]
=0
\]

for every retained pair.  The direction (Y\otimes Y) lies in the restricted kernel.

## Positive hostile fiber

Take

\[
\rho_\pm
=
\frac14
\left(
I\otimes I
\pm\frac12Y\otimes Y
\right).
\]

Since (Y\otimes Y) has eigenvalues (+1,+1,-1,-1), each state has eigenvalues

\[
\frac38,
\quad
\frac38,
\quad
\frac18,
\quad
\frac18.
\]

Both states are therefore positive and normalized.

Every retained real product probe has the same value on (ho_+) and (ho_-).  The omitted probe gives

\[
\operatorname{Tr}
\left[
\rho_\pm(Y\otimes Y)
\right]
=\pm\frac12.
\]

Hence the restricted probe map has a physical two-point fiber, while the complete map separates it.

## Optical typing gate

In a polarization qubit realization:

- (Z) distinguishes horizontal from vertical polarization;
- (X) distinguishes diagonal from anti-diagonal polarization;
- (Y) distinguishes right- from left-circular polarization.

The complete probe theorem becomes a physical source theorem only if the frozen instrument admits the phase-sensitive (Y) analyzer independently on each labelled photon.  Algebraic availability of (Y) is insufficient.

The primary optical-tomography literature derives complete two-photon reconstruction from local polarization analyzers.  The remaining Marici gate is to match those analyzers to the frozen photon source and readout packet without enlarging its instrument post hoc.

## Decision table

| Source probe family | Kernel status | Interpretation |
|---|---:|---|
| (I,X,Z) locally | contains (Y\otimes Y) | real/rebit composite; local tomography fails |
| (I,X,Y,Z) locally | zero | complex two-qubit tomography passes |
| (Y) only after fitted instrument extension | unauthorized | no complex-lens conclusion |

## Falsifier

If the frozen optical source/readout lacks an independent local circular-polarization analyzer, then the current Marici packet does not derive complex local tomography.  The real-versus-complex ambiguity remains.

## Primary source

D. F. V. James, P. G. Kwiat, W. J. Munro, and A. G. White, *On the Measurement of Qubits*, arXiv:quant-ph/0103121, derives tomographic reconstruction for two photon-polarization qubits.
