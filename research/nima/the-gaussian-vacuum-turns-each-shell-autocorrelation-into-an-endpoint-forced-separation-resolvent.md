# The Gaussian vacuum turns each shell autocorrelation into an endpoint-forced separation resolvent

## Question

Does the Gaussian source equation produce a nonlocal response law for the
explicit ordered-pair shell kernels?

## Claim boundary

Yes. Each ordered-pair correlation satisfies an exact first-order equation in
the separation coordinate. Its forcing is the difference of two endpoint
products, and its homogeneous coefficient is fixed by the pair labels. This
constructs a canonical source-derived resolvent from endpoint forcing to the
bulk correlation density. It does not identify that resolvent with the
reciprocal or linking port of the G4 Green complex.

## Pair kernel

Let

\[
 g_{nm}(x,t)=\phi_n(x)\phi_m(x+t),
\]

where

\[
 \phi_n(x)=e^{-\pi n^2x^2}.
\]

Define

\[
 \rho_{nm}^{[a,b]}(t)=\int_a^b g_{nm}(x,t)\,dx.
\]

Set

\[
 A_{nm}=n^2+m^2,
 \qquad
 \alpha_{nm}=\frac{m^2}{A_{nm}},
 \qquad
 \kappa_{nm}=\frac{n^2m^2}{A_{nm}}.
\]

## Vacuum transport identity

Direct differentiation gives

\[
 \partial_x g_{nm}
 =-2\pi\bigl(A_{nm}x+m^2t\bigr)g_{nm},
\]

and

\[
 \partial_t g_{nm}
 =-2\pi m^2(x+t)g_{nm}.
\]

Eliminating the interior coordinate \(x\) yields

\[
 \left(\partial_t+2\pi\kappa_{nm}t\right)g_{nm}
 =\alpha_{nm}\partial_x g_{nm}.
\]

This is a direct consequence of the two Gaussian vacuum equations; no zero or
asymptotic fitting enters.

## Shell Green identity

Integrating over \([a,b]\) gives

\[
 \left(\partial_t+2\pi\kappa_{nm}t\right)
 \rho_{nm}^{[a,b]}(t)
 =\alpha_{nm}
 \left[g_{nm}(b,t)-g_{nm}(a,t)\right].
\]

Thus the shell-interior correlation is the response of the separation
operator

\[
 \mathcal A_{nm}=\partial_t+2\pi\kappa_{nm}t
\]

to a source-fixed endpoint difference.

The coordinate \(t\) is relative separation, not physical time.

## Exact resolvent formula

Multiplication by the integrating factor

\[
 e^{\pi\kappa_{nm}t^2}
\]

gives

\[
 \rho_{nm}^{[a,b]}(t)
 =e^{-\pi\kappa_{nm}t^2}
 \left[
 \rho_{nm}^{[a,b]}(0)
 +\alpha_{nm}\int_0^t
 e^{\pi\kappa_{nm}s^2}
 \bigl(g_{nm}(b,s)-g_{nm}(a,s)\bigr)\,ds
 \right].
\]

The initial value is also source-fixed:

\[
 \rho_{nm}^{[a,b]}(0)
 =\int_a^b e^{-\pi(n^2+m^2)x^2}\,dx.
\]

Hence the bulk density is not a free extra coefficient. It is the unique
solution selected by the Gaussian vacuum and its shell initial value.

## Ordered orientation

Swapping \(n\) and \(m\) preserves \(\kappa_{nm}\) but replaces

\[
 \alpha_{nm}=\frac{m^2}{n^2+m^2}
\]

by

\[
 \alpha_{mn}=\frac{n^2}{n^2+m^2}.
\]

The separation operator has a symmetric confining coefficient, while the
endpoint forcing retains ordered ratio orientation. The pair labels therefore
cannot be codiagonalized before this response is formed.

## Candidate-one consequence

The previous endpoint-only obstruction concerned finite algebraic combinations
of boundary traces. The Gaussian vacuum supplies a different object: a
nonlocal separation resolvent of an endpoint difference. It exactly recovers
the shell autocorrelation density on every ordered Gaussian pair.

A viable linking constructor may therefore be sought as the transported
resolvent

\[
 \mathcal A_{nm}^{-1}
 \alpha_{nm}(\operatorname{ev}_b-\operatorname{ev}_a)
\]

with the source initial condition retained. This candidate is fixed before any
Xi zero is inspected.

## Required comparison

To enter G4, one must still prove that the declared ordered Stokes/Wronskian
linking port is the image of this pairwise separation resolvent under the
retained boundary comparison. Required checks are:

1. preservation of ordered pair labels and ratio orientation;
2. continuity on the projective arithmetic rigging;
3. compatibility with reciprocal sewing;
4. equality of analytic-transpose signs;
5. recovery of the full shell density, not only its endpoint asymptotic;
6. commutation with parameter differentiation for every Xi multiplicity jet.

## Disposition

The missing nonlocal source law is no longer abstract at the Gaussian-pair
level. It is an endpoint-forced separation resolvent with an explicit initial
condition. The unresolved step is its typed identification with the existing
G4 linking port. No RH conclusion is authorized.
