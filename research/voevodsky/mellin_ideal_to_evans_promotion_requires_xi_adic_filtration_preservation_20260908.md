# Mellin ideal to Evans promotion requires Xi-adic filtration preservation

Date: 2026-09-08

## Exact bridge condition

The Mellin theorem gives a source ideal

\[
I_E=(\Xi).
\]

The Evans theorem asks for

\[
r_U\in\tau\,\mathcal O(U_{\rm ar}),
\qquad \tau=\Xi
\]

in the centered spectral coordinate.  Equality of the scalar ideals does not by itself imply the second statement.
A comparison map from the Mellin source must preserve the Xi-adic filtration:

\[
L(I_E^m)\subseteq I_E^m\mathcal O(U_{\rm ar})
\qquad(m\ge1).
\]

For the distinguished source section, the `m=1` instance gives residual
divisibility.  At an order-`m` zero, preservation through level `m` gives the
complete residual-jet vanishing required for multiplicity.

## Sufficient mechanism

If the comparison is a morphism of modules over the spectral multiplier ring
on an ambient source module, then

\[
L(\Xi f)=\Xi L(f),
\]

so divisibility is automatic.  More generally an explicit filtered chain
homotopy can supply the same conclusion.  Merely being continuous,
holomorphic, Fourier-equivariant, or scalar-determinant preserving is not
enough.

## Derivative hostile

Parameter differentiation is the minimal counterexample:

\[
\partial_z((z-z_0)^mf)
=m f(z_0)(z-z_0)^{m-1}+\cdots.
\]

It lowers Xi-adic order by one.  This is directly relevant because the complete
five-port Green residual contains derivative, Wronskian, and first-jet
operations.  Their assembled comparison must exhibit cancellations restoring
filtration preservation; no componentwise ideal argument can be assumed.

A finite symbolic audit checked orders one through eight: multiplier maps
preserved all lower jets, while differentiation exposed the order-`m-1`
coefficient `m f(0)`.

## Sharpened construction target

The Mellin-to-Evans bridge consists of two noninterchangeable claims:

1. identify the entire split Evans source/history section as the image of the
   source-saturated Mellin module, retaining prime, grade, seam, and reciprocal
   ports;
2. prove that the complete five-port adjoint residual map is Xi-adically
   filtered, despite its derivative components.

If both hold, the source ideal theorem promotes directly to
`r_U=tau h_U` with multiplicities.  Without the second, the Mellin jet boundary
is only a divisor compiler and cannot be imported into the Green pencil.

## Evidence

- `check_marici_rh_xi_ideal_preservation_gate_20260908.py`
- `marici_rh_xi_ideal_preservation_gate_certificate_20260908.json`
