# Prior research constructs the adjoint reservoir but not its Xi characteristic

Date: 2026-09-08

## Constant channel is a port

The forced tail equation has the exact impedance balance

\[
\partial_q|G|^2+2\operatorname{Re}z|G|^2
=|a_{\rm in}|^2-|a_{\rm out}|^2.
\]

This correctly types the constant forcing amplitude as an external input, not a finite-energy autonomous state.  A two-state positive conservative augmentation cannot keep that amplitude constant: skew-adjoint completion forces a nontrivial response equation.

## Reverse incidence exists on the retained history carrier

A superseding result constructs the required response port.  The source incidence

\[
B:U\to H
\]

is Hilbert--Schmidt in the retained half-density history and seam metrics, with

\[
\|B\|_2^2
=
\sum_p\frac{\|b_p\|^2}{\log p}<\infty.
\]

Its bounded metric adjoint is

\[
(B^\dagger f)_p
=
\frac{\langle b_p,f\rangle}{\log p}.
\]

Hence the paired conservative candidate is defined:

\[
\mathcal D^{\rm pair}(s)
=
\begin{pmatrix}
D_H(s)&-B(s)\\
B(s)^\dagger&D_U(s)
\end{pmatrix}.
\]

The off-diagonal coupling is skew-adjoint in the declared direct-sum metric, so the local forcing cross term cancels vectorially.  The earlier claim that no adjoint reservoir exists is obsolete.

## Remaining divisor obstruction

Closing the port changes the triangular Evans system.  Its Schur characteristic contains

\[
D_U+B^\dagger D_H^{-1}B.
\]

No source theorem identifies the determinant of this paired pencil with `E(s)xi(s)` for a nowhere-zero `E`.  Equivalently, the natural Evans zero-state does not automatically satisfy

\[
B^\dagger u_z=0.
\]

Thus the conservative reservoir exists, but its spectral divisor may differ from Xi.  This is the same prime-shell adjoint residual found in the Evans audit.

## Disposition

Prior research closes construction and boundedness of the adjoint response port and the paired operator.  The remaining theorem is Xi-divisor compatibility of that independently constructed conservative pencil, including reciprocal covariance, complement invertibility, multiplicity preservation, and completed spectral exactness.  Defining the arithmetic law to force this characteristic would be fitted.

## Evidence

- `research/nima/theta-forcing-is-an-exact-impedance-port-and-wave-flux-difference.md`
- `research/grothendieck/adjoint-completion-makes-the-constant-source-channel-dynamical-and-forces-a-separate-response-port.md`
- `research/nima/theta-reciprocal-doubling-is-not-yet-adjoint-completion.md`
- `research/nima/the-retained-history-metric-now-constructs-the-adjoint-incidence-but-not-its-xi-characteristic.md`
