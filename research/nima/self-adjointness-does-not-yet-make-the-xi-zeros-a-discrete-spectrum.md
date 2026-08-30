# Self-adjointness does not yet make the xi zeros a discrete spectrum

The conditional operator
\[
H_{\Lambda}=iJ\mathcal A_{\Lambda}
\]
would solve seam confinement, but it does not automatically supply the desired spectral determinant.

The theta-tail generator lives on a half-line and contains a first-order transport component. The unforced translation generator on a half-line has noncompact resolvent and continuous essential spectrum. A decaying theta coupling or finite-dimensional boundary sewing will generally not make its resolvent compact.

This creates three distinct Hilbert--Pólya regimes:

1. Compact resolvent:
   the spectrum is discrete with finite multiplicities, and an operator determinant may encode it after ideal-class control.
2. Continuous essential spectrum with isolated gap eigenvalues:
   a relative determinant may encode the isolated part.
3. Zeros represented as embedded eigenvalues, scattering phase crossings, or resonances:
   ordinary characteristic determinants are unavailable and multiplicity requires scattering theory.

The present tail-flow geometry appears provisionally closer to the third regime than the first.

A finite-rank change of boundary condition does not normally remove essential spectrum. If two self-adjoint extensions have finite-rank resolvent difference, then their essential spectra agree. Thus maximal reciprocal sewing can enforce self-adjointness without discretizing the transport continuum.

Likewise, a rapidly decaying multiplication or integral coupling may be relatively compact. Such a perturbation can create discrete eigenvalues off the essential spectrum but does not erase the essential background.

Therefore the next theorem cannot simply state
\[
\xi\left(\frac12+it\right)
=
\det(t-H_{\Lambda}).
\]
The determinant on the right is undefined for a generic unbounded operator with continuous spectrum.

There are two viable source outcomes.

## Outcome A: hidden compactification

The complete wall, theta, archimedean, and reciprocal graph norm may compactly embed into the state Hilbert space:
\[
\operatorname{dom}H_{\Lambda}
\hookrightarrow
\mathcal H
\quad\text{compactly}.
\]
Then \(H_{\Lambda}\) has compact resolvent. This must be proved from a source coercive estimate; no finite boundary argument supplies it.

The sharp hostile is a sequence translated toward infinity with bounded graph norm and no convergent Hilbert subsequence.

## Outcome B: relative scattering determinant

Retain a reference self-adjoint transport operator \(H_0\). If
\[
(H_{\Lambda}-z)^{-1}-(H_0-z)^{-1}
\]
is trace class or determinant-class, define a perturbation determinant
\[
D_{\Lambda/0}(z).
\]
Its boundary values encode the scattering matrix, and zeros/poles encode the relative discrete or resonant data.

The finite boundary determinant
\[
\det(I-CG(z))
\]
is naturally such a perturbation determinant. This is compatible with continuous bulk spectrum: the zero-free Euler/transport carrier is the reference, while wall and reciprocal sewing produce the relative divisor.

In this regime, RH zeros are more naturally phase crossings or spectral singularities of the relative system than the entire spectrum of \(H_{\Lambda}\).

The exact source audit is:

1. determine the essential spectrum of the uncoupled doubled tail operator;
2. prove whether theta forcing is relatively compact, trace class, or neither;
3. compute the resolvent difference induced by \(\Lambda\);
4. decide compact-resolvent versus relative-scattering regime;
5. select the authorized determinant class;
6. prove zero multiplicity equals the appropriate eigenvalue, resonance, or crossing multiplicity.

A major no-go follows. If the essential spectrum already fills the real seam, merely showing every zeta zero corresponds to a point in
\[
\sigma(H_{\Lambda})\subset\mathbb R
\]
is vacuous: every real ordinate may belong to the spectrum. One must show that zeros correspond to a distinguished relative spectral event.

The smallest hostile constructs a self-adjoint half-line operator with spectrum \(\mathbb R\) and observes that every critical-line ordinate lies in its spectrum. It “proves” seam placement but explains no zero set.

A second hostile uses a formal Fredholm determinant despite a non-trace-class resolvent difference. The resulting scalar regularization can hide arbitrary divisor data.

Thus the next categorical fork is unavoidable:

\[
\text{self-adjoint doubled source operator}
\to
\begin{cases}
\text{prove compact resolvent},\\
\text{or construct a relative scattering determinant}.
\end{cases}
\]

Given the current half-line theta-tail geometry, the relative boundary/scattering determinant is the conservative default until compactness is genuinely established.
