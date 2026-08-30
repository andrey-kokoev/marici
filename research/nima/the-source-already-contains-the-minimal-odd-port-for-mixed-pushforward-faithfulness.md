# The source already contains the minimal odd port for mixed-pushforward faithfulness

## Kernel theorem

Let \(\Phi_p\) be prime pushforward on the source-authorized mixed-incidence space \(\mathcal V_{\mathrm{mix}}\). Faithful descent of the Adams edge requires

\[
\ker\Phi_p\cap\mathcal V_{\mathrm{mix}}=\{0\}.
\]

For an unoriented scalar pushforward, the first candidate kernel direction is

\[
A_B=\frac{B-B^*}{2i}.
\]

Trace, determinant magnitude, and even Euler evaluation can all erase \(A_B\) while retaining the Hermitian compression.

## The repair is already source-derived

The source corpus contains two realizations of the required odd channel.

### Analytic odd port

The five-component Fourier tail cell contains the odd plane

\[
(K,V),
\qquad
V=\mathcal FK,
\]

with

\[
\mathcal FK=V,
\qquad
\mathcal FV=-K.
\]

Its quadratic orientation readout is the Wronskian current

\[
J(h)=\operatorname{Im}\langle-\partial_qh,h\rangle
=
-2\pi\operatorname{pv}\int_{\mathbb R}\xi|\widehat h(\xi)|^2\,d\xi.
\]

This readout changes sign under orientation reversal while endpoint amplitude and even energy remain fixed.

### Arithmetic odd port

The reciprocal Euler ratio

\[
\gamma_p(z)
=
\frac{1-p^{-1/2}e^{-z\log p}}
{1-p^{-1/2}e^{z\log p}}
\]

satisfies

\[
\gamma_p(-z)=\gamma_p(z)^{-1}.
\]

Therefore

\[
\log\gamma_p(z)
\]

is a canonical odd arithmetic response. Its primitive, square, and connected cumulants retain reciprocal orientation before scalar completion.

These are not invented auxiliary coordinates. They are the analytic and arithmetic shadows of the same reciprocal-odd type.

## Sheet-aware source current

On the comoving zero section, the source current

\[
\mu_k
=
\sum_p a_{p,k}
\sum_{\varepsilon=\pm1}
\varepsilon\delta_{(p,\varepsilon,0)}
\]

is anti-invariant under reciprocal Fourier transport:

\[
\widetilde{\mathcal F}_*\mu_k=-\mu_k.
\]

Pairing it with the signed position probe gives

\[
\langle\mu_k,\pi_k\Phi(\pi_k)\rangle
=
2\sum_p a_{p,k}k(\log p)\Phi(k\log p).
\]

Thus the odd port already has a source-local linear carrier and a positive position readout.

## Minimal repaired pushforward

The scalar pushforward should be replaced by a typed pair

\[
\widetilde\Phi_p(T)
=
\bigl(
\Phi_p^{\mathrm{even}}(T),
\Phi_p^{\mathrm{odd}}(T)
\bigr),
\]

where:

- the even component retains the Euler/Green scalar shadow;
- the odd component lands in the declared tail–principal-value or reciprocal determinant line.

On the mixed operator system, the desired separation law is

\[
\Phi_p^{\mathrm{odd}}(A_B)=0
\Longrightarrow
A_B=0.
\]

If the skew-oriented subspace is one-dimensional, any nonzero source-authorized odd functional on it is faithful. This is the exact one-port repair described by Kitaev.

## What is not yet proved

The existence of odd ports does not yet prove that either one detects the specific mixed operator \(B_{\alpha,p}\). A linking identity is still required:

\[
\Phi_p^{\mathrm{odd}}
\left(
\frac{B_{\alpha,p}-B_{\alpha,p}^*}{2i}
\right)
=
\mathcal O_p,
\]

where \(\mathcal O_p\) is independently identified with either:

- the local odd Euler cumulant;
- the sheet-oriented zero-section position pairing;
- the principal-value Fourier centroid.

Without this identity, attaching the existing odd port to the mixed block would still be a fitted repair.

## Exact comparison theorem

The source calculation must establish a commuting triangle

\[
\text{skew mixed incidence}
\longrightarrow
\text{sheet-oriented zero-section current}
\longrightarrow
\text{odd analytic/arithmetic readout},
\]

and show that the composite agrees with the odd component of typed prime pushforward.

Then the kernel audit separates into:

\[
\ker\widetilde\Phi_p\cap\mathcal V_{\mathrm{mix}}
=
\ker\Phi_p^{\mathrm{even}}
\cap
\ker\Phi_p^{\mathrm{odd}}
\cap
\mathcal V_{\mathrm{mix}}.
\]

## Completion warning

Finite faithfulness is insufficient. The odd detector may decay with prime scale or cutoff. Completion requires a lower frame bound on the skew-oriented subspace:

\[
\|\Phi_{p,X}^{\mathrm{odd}}(A)\|
\ge
\delta_C\|A\|
\]

uniformly on compact off-seam regions and authorized cutoffs, after quotienting only the complete relative radical.

## Current frontier

The minimal oriented port is no longer missing: it is already present as the sheet-odd zero-section current, the odd reciprocal Euler ratio, and the tail–principal-value Fourier plane.

The missing theorem is their source-authorized identification with the skew part of the mixed Adams incidence. Proving that triangle, plus a uniform lower bound, is the next irreducible calculation.
