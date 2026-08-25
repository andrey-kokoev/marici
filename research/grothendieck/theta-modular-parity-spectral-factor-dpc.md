# DPC: modular sewing supplies a source-derived parity spectral factor

## Problem situation

Packet 123 identifies each generalized Laguerre form as an indefinite
reflection-Krein norm. Packet 125 proves that its normalized reserve must tend
to zero at high spectral frequency. Uniform coercivity is therefore
impossible; a proof must prevent sign crossing without keeping the orbit a
fixed distance from its light cone.

## Deutsch--Popperian conjecture

Let `g_n(sigma)` be the density obtained by pushing

\[
 (u-v)^{2n}\Phi(u)\Phi(v)\,du\,dv
\]

along `sigma=u+v`.  Then

\[
 (2n)!\mathcal L_n[X](x)=\widehat g_n(x).
\]

The conjecture is:

> **Modular parity-factor conjecture.** For every `n`, the completed labelled
> theta construction supplies, before Fourier evaluation and compatibly with
> reciprocal sewing, a one-sector amplitude `h_n` such that
>
> \[
> g_n=h_n*\widetilde h_n,
> \qquad
> \widetilde h_n(s)=\overline{h_n(-s)}.
> \]

It would follow that

\[
 \boxed{
 (2n)!\mathcal L_n[X](x)=|\widehat h_n(x)|^2\ge0.}
\]

This permits arbitrarily small reserve and is therefore compatible with the
Riemann--Lebesgue boundary theorem.

## Explanatory content

The proposed mechanism is

\[
 \text{two reciprocal localizations}
 \xrightarrow{\text{modular sewing}}
 \text{one amplitude and its reflected adjoint}
 \xrightarrow{\text{relative product}}
 \text{nonnegative Laguerre readout}.
\]

The scalar zero of a factor is then destructive interference inside one
amplitude; the nonnegative completed readout is its modulus square.  The two
half-planes are shadows of the two adjoint localizations, not arbitrary halves
of a pre-existing scalar plane.

## Noncircularity requirements

The conjecture has force only if `h_n` is derived from source data.  The
following constructions are prohibited as circular:

1. define `h_hat_n=sqrt(L_n)` after assuming `L_n>=0`;
2. choose a Wiener--Hopf factor using the desired sign as input;
3. discard endpoint or cross-label terms that obstruct factorization;
4. change the factor separately on intervals selected by known zeros.

An admissible factor must arise from the integral winding labels, one
reciprocal chart, its moving seam current, and the modular transition law.

## Immediate attack at order one

For `n=1`, packet 119 gives

\[
 \widehat g_1(x)=4(B(x)^2+A(x)C(x)).
\]

The candidate factor must explain the signed `AC` polarization together with
the positive `B^2` repair as one modulus square.  A mere algebraic square root
of their sum is not source-derived.

The first calculation should keep the hyperbolically centered label pair of
packet 118 and attach its reciprocal moving-endpoint contribution.  If those
two pieces form an adjoint pair before integration over labels, their
convolution gives the required `h_1`.

## Sharp falsifiers

The conjecture fails if any of the following occurs:

1. the exact order-one sewn density has no source-local autocorrelation
   factor compatible with label transport;
2. different primes or winding labels require mutually incoherent phase
   choices for `h_1`;
3. the factor exists at order one but the first symmetric-power lift fails;
4. the same construction applies to a hostile self-Fourier carrier with
   off-critical zeros.

The first negative result must be retained as a typed obstruction; the factor
must not be repaired after inspecting the failed Fourier sign.

## Status

This is a conjecture and research programme, not a theorem. Its virtue is that
it explains both strict finite positivity and asymptotically vanishing reserve
with one source-level mechanism. The immediate target is the explicit
order-one one-chart amplitude and its modular adjoint.
