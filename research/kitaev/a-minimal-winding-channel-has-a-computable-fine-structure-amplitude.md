# A Minimal Winding Channel Has a Computable Fine-Structure Amplitude

The distance theorem identifies the first allowed perturbative order but not
its coefficient. The smallest exact coefficient model has two degenerate
logical endpoints and one virtual path of length (L) between them.

Let the logical subspace (P\mathcal H) be spanned by

\[
|0\rangle,|1\rangle.
\]

Let the excited subspace contain (L-1) intermediate states, each with
unperturbed energy \(\Delta>0\), with nearest-neighbor virtual coupling
\(\lambda\). Couple \(|0\rangle\) to the first intermediate state and the last
intermediate state to \(|1\rangle\), also with amplitude \(\lambda\).

At spectral parameter (E=0), the Feshbach effective operator is

\[
H_{\mathrm{eff}}(0)
=
PHP
+
PHQ(-QHQ)^{-1}QHP.
\]

The off-diagonal logical amplitude is

\[
t_L(\lambda)
=
\lambda^2
\left[(-QHQ)^{-1}\right]_{1,L-1}.
\]

Expanding at \(\lambda=0\) gives

\[
t_L(\lambda)
=
(-1)^{L-1}
\frac{\lambda^L}{\Delta^{L-1}}
+O(\lambda^{L+2}).
\]

The sign counts the (L-1) negative virtual denominators. The leading power is
exactly the distance-selected path length.

## Exact Schur-complement audit

For path lengths (L=2,3,4,5,6), symbolic inversion verifies

\[
\lim_{\lambda\to0}
\frac{t_L(\lambda)}{\lambda^L}
=
\frac{(-1)^{L-1}}{\Delta^{L-1}}.
\]

This is the simplest fine-structure coefficient that distance permits. It is
not yet the coefficient of a toric Hamiltonian, because a torus has many
ordered winding paths with source-specific matrix elements and denominators.

## Paired-path cancellation

Now add two disjoint virtual paths with identical excitation energies. Give
their endpoint products opposite signs. Each path individually contributes an
allowed order-(L) logical amplitude, but their Schur-complement off-diagonal
entries cancel exactly:

\[
t_L^{(1)}+t_L^{(2)}=0.
\]

For the symmetric paired model, the diagonal self-energies agree as well, so
the full effective operator remains scalar on the logical doublet.

This is the mandatory hostile fixture for the claim that distance determines
splitting. Distance determines the earliest possible order. Interference and
selection rules determine whether that order is present.

## Path-sum compiler

For an actual stabilizer Hamiltonian, the leading logical coefficient must be
assembled from typed virtual paths:

\[
t_\gamma
=
\sum_{p\in\mathcal P_\gamma}
\frac{
\prod_{j=1}^{L_p}\langle s_j|V_{e_j}|s_{j-1}\rangle
}{
\prod_{j=1}^{L_p-1}(E_0-E_{s_j})
}.
\]

The source must supply:

- which ordered paths are admitted;
- intermediate syndrome energies;
- matrix-element signs and phases;
- multiplicities and automorphisms;
- whether paths in different homology classes mix;
- the perturbative regime in which the expansion is controlled.

No scalar logical readout contains this path data by itself.

## Uniform suppression criterion

Suppose the number of length-(L) winding paths is at most (C\mu^L), each
matrix element has magnitude at most \(|\lambda|\), and every virtual
denominator has magnitude at least \(\Delta\). Then

\[
|t_\gamma|
\le
C\Delta
\left(\frac{\mu|\lambda|}{\Delta}\right)^L.
\]

Exponential suppression follows only in the regime

\[
\mu|\lambda|<\Delta.
\]

This exposes the missing completion constant: distance growth must beat path
entropy. A growing first allowed order is not enough when the number of paths
or inverse denominators grows too quickly.

## Readout and connection boundary

Grothendieck's flat jet connection transports multiplicity but cannot locate
zeros; a scalar connection containing (F'/F) imports the divisor
circularly. The finite analogue is that a logical-sector label does not supply
the virtual path sum that splits it. Comparison must be derived before
compression.

The analogy identifies a constructor requirement, not a theta winding-path
formula.

## Falsifiers

- Claiming distance alone makes the leading coefficient nonzero.
- Summing path magnitudes while ignoring phase cancellation.
- Using a scalar sector label to reconstruct virtual denominators.
- Inferring exponential suppression without controlling path entropy.
- Treating the minimal chain model as the toric Hamiltonian coefficient.
- Importing the path formula into the theta/Fock sector without a source
  spectral comparison.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to compute the first allowed fine-structure coefficient and
its sharp cancellation mechanism.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The minimal coefficient is explicit, paired paths can cancel it, and
uniform suppression is reduced to distance beating path entropy.
