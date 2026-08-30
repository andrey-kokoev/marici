# The odd curvature carrier has a canonical quarter-gap Green energy

## Unitary half-density model

On one positive ray, define

\[
(\mathcal M_n f)(u)
=
\sqrt n,e^{u/2}f(ne^u).
\]

This is unitary from \(L^2(\mathbb R_+,dx)\) to
\(L^2(\mathbb R,du)\). For

\[
A=x\partial_x,
\qquad
P=A(A+1),
\]

the exact intertwining identity is

\[
\mathcal M_nP
=
\left(\partial_u^2-\frac14\right)\mathcal M_n.
\]

Hence the closure of \(P\) is unitarily equivalent to the constant
coefficient operator

\[
\mathcal C=\partial_u^2-\frac14.
\]

## Canonical positive energy

Define

\[
S=-P.
\]

Under \(\mathcal M_n\),

\[
S
\simeq
-\partial_u^2+\frac14.
\]

Therefore, on the standard Sobolev form domain,

\[
\langle f,Sf\rangle
=
\|\partial_u\mathcal M_nf\|^2
+
\frac14\|f\|^2.
\]

In particular,

\[
S\ge\frac14 I,
\qquad
\|S^{-1}\|\le4.
\]

The bound is independent of the label \(n\), the prime \(p\), and the
window length \(L=\log p\).

This is the absolute lower scale that the auxiliary shear analysis required.
It is not selected by a free regulator: it is fixed by the source
half-density completion operator.

## Restriction to the odd cyclic carrier

Let \(g_{\mathrm{odd}}\) be the curvature seed and let
\(\mathcal K_{\mathrm{odd}}\) be its closed spectral cyclic subspace for
\(P\). Because this subspace is reducing for the spectral calculus of
\(P\), the same estimate holds on it:

\[
S_{\mathrm o}
=
-S|_{\mathcal K_{\mathrm{odd}}}
\ge\frac14I.
\]

Thus the infinite odd tail does not create a soft auxiliary mode. Any
collapse of the enlarged Adams cell must come from the incidence loading or
from an additional odd perturbation, not from the bare theta-completion
energy.

## Resolvent consequence

For any endpoint-to-odd incidence map \(C_{\mathrm{oe}}\) that is bounded
in the source norm,

\[
\left\|
C_{\mathrm{eo}}S_{\mathrm o}^{-1}C_{\mathrm{oe}}
\right\|
\le
4\|C_{\mathrm{oe}}\|^2.
\]

More naturally,

\[
\|S_{\mathrm o}^{-1/2}C_{\mathrm{oe}}\|
\le
2\|C_{\mathrm{oe}}\|.
\]

Therefore the prior triangular shear gate becomes derived once the
even--odd incidence is uniformly bounded. The auxiliary inverse itself has a
source-uniform bound.

## What this does not prove

The actual oriented auxiliary block may be

\[
D_{\mathrm o}=S_{\mathrm o}+iT_{\mathrm{hist}},
\]

where \(T_{\mathrm{hist}}\) is the causal-minus-anticausal history
generator. Positivity of \(D_{\mathrm o}\) still requires

\[
\left\|
S_{\mathrm o}^{-1/2}
(iT_{\mathrm{hist}})
S_{\mathrm o}^{-1/2}
\right\|<1.
\]

The quarter-gap controls the denominator of this test but does not estimate
the odd history numerator. Nor does it construct the arithmetic endpoint
incidence.

## Domain qualification

The algebraic Gaussian-polynomial span is only a core candidate. The theorem
uses the self-adjoint Sobolev realization transported from the full
\(u\)-line. Finite polynomial truncations must not be mistaken for invariant
domains.

The odd carrier should be defined spectrally, not merely as the algebraic span
of \(P^ng_{\mathrm{odd}}\), so that restriction of the resolvent is
authorized.

## Frontier

One major analytic gate is now closed:

\[
\text{bare odd auxiliary energy}
\quad\Longrightarrow\quad
S_{\mathrm o}\ge\frac14I.
\]

The remaining local Adams gates are:

1. construct the causal odd perturbation on this Sobolev carrier;
2. prove its relative contraction;
3. construct the endpoint-to-odd incidence;
4. prove the Schur-return Green identity and radical descent;
5. match the returned orientation with the arithmetic odd port.
