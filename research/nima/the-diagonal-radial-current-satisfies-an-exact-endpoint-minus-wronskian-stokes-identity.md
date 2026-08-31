# The diagonal radial current satisfies an exact endpoint-minus-Wronskian Stokes identity

## Question

Can the interior radial derivative isolated by hyperbolic centering be identified
with an already typed ordered linking density?

## Claim boundary

Yes at the source-density level. The interior centered derivative is exactly a
shell integral of the analytic-transpose Wronskian between the two separated
completed-theta copies. Therefore the diagonal autocorrelation obeys an exact
endpoint-minus-Wronskian transport law. What remains open is representation of
this function-valued Wronskian current by the retained G4 wall/incidence linking
port with its frozen metric and arithmetic loading.

## Diagonal pair density

Fix one theta label \(n\) and a shell \([a,b]\). Write

\[
 \rho_n(t)
 =\int_a^b\Phi_n(u)\Phi_n(u+t)\,du.
\]

The centered pair density is

\[
 H_n(S,\delta)
 =\Phi_n\!\left(\frac{S+\delta}{2}\right)
  \Phi_n\!\left(\frac{S-\delta}{2}\right).
\]

Its centered derivative is

\[
 \partial_\delta H_n(S,\delta)
 =\frac12\left[
 \Phi_n'\!\left(\frac{S+\delta}{2}\right)
 \Phi_n\!\left(\frac{S-\delta}{2}\right)
 -
 \Phi_n\!\left(\frac{S+\delta}{2}\right)
 \Phi_n'\!\left(\frac{S-\delta}{2}\right)
 \right].
\]

This is the analytic-transpose Wronskian density of the two ordered copies.

## Shell Wronskian current

Define

\[
 \mathcal W_n^{[a,b]}(t)
 =\int_a^b
 \left[
 \Phi_n'(u)\Phi_n(u+t)
 -\Phi_n(u)\Phi_n'(u+t)
 \right]du.
\]

It is odd under reversal of the separated slots and vanishes at \(t=0\).
It retains the whole shell interior and is not a finite endpoint scalar.

## Exact radial Stokes identity

Direct differentiation gives

\[
 \rho_n'(t)
 =\int_a^b\Phi_n(u)\Phi_n'(u+t)\,du.
\]

Integration by parts in \(u\) yields

\[
 \int_a^b\Phi_n'(u)\Phi_n(u+t)\,du
 +\rho_n'(t)
 =\Phi_n(b)\Phi_n(b+t)
 -\Phi_n(a)\Phi_n(a+t).
\]

Subtract the definition of \(\mathcal W_n^{[a,b]}\). The result is

\[
 \rho_n'(t)
 =\frac12\left[
 \Phi_n(b)\Phi_n(b+t)
 -\Phi_n(a)\Phi_n(a+t)
 \right]
 -\frac12\mathcal W_n^{[a,b]}(t).
\]

This is exactly the moving-window identity obtained from hyperbolic centering:
the interior radial derivative is the ordered Wronskian current.

## Initial value

At \(t=0\),

\[
 \mathcal W_n^{[a,b]}(0)=0,
\]

and hence

\[
 \rho_n'(0)
 =\frac12\left[\Phi_n(b)^2-\Phi_n(a)^2\right].
\]

The zero ratio-cocycle value is therefore compatible with a nonzero radial
endpoint derivative.

## Laplace-domain identity

Let

\[
 R_n(z)=\int_0^\infty e^{-zt}\rho_n(t)\,dt,
\]

\[
 E_n(z)=\frac12\int_0^\infty e^{-zt}
 \left[
 \Phi_n(b)\Phi_n(b+t)-\Phi_n(a)\Phi_n(a+t)
 \right]dt,
\]

and

\[
 W_n(z)=\int_0^\infty e^{-zt}\mathcal W_n^{[a,b]}(t)\,dt.
\]

On a right half-plane, integration by parts gives

\[
 zR_n(z)-\rho_n(0)
 =E_n(z)-\frac12W_n(z).
\]

Equivalently,

\[
 R_n(z)
 =\frac{\rho_n(0)+E_n(z)-\frac12W_n(z)}{z}.
\]

The apparent singularity at \(z=0\) is removable because the numerator
vanishes there by the density identity. This formula transports all parameter
jets at once.

## Transfer to candidate one

The diagonal ordinary Evans shell is \(-R_n(z)\). Its source decomposition now
has three explicit typed pieces:

1. shell initial autocorrelation \(\rho_n(0)\);
2. two-endpoint response \(E_n(z)\);
3. ordered interior Wronskian response \(W_n(z)\).

Thus an independently invented diagonal linking section is unnecessary at the
density level: the needed candidate is the Wronskian current already forced by
radial differentiation.

## Remaining G4 comparison

The retained G4 linking form uses wall trace and incidence coordinates with a
source arithmetic coefficient. To import the radial identity, one must prove a
map from the function-valued shell current \(\mathcal W_n^{[a,b]}(t)\) into
that graph which preserves:

- theta label and shell;
- slot reversal and analytic-transpose sign;
- adjacent-shell concatenation;
- the Laplace readout;
- the frozen endpoint metric and arithmetic loading.

Boundedness of the scalar wall/incidence form does not prove this representation.

## Hostile

A proposed diagonal response fails if it includes only the endpoint term or
only the Wronskian term. The exact source law requires their fixed relative
coefficient \(-1/2\) and the initial value \(\rho_n(0)\).

## Disposition

The missing diagonal density is no longer an unspecified nonlocal response. It
is canonically decomposed by an exact radial Stokes identity into initial,
endpoint, and ordered-Wronskian data. Candidate one remains open only at the
representation of this Wronskian shell current in the retained G4 linking
carrier and its source-normalized arithmetic codiagonal. No RH conclusion is
authorized.
