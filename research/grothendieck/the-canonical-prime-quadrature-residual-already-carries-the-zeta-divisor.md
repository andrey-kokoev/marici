# The canonical prime quadrature residual already carries the zeta divisor

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact circularity boundary

## Canonical arithmetic sampling measure

The prime-power constructor does not permit arbitrary quadrature weights. Its
natural incidence measure on logarithmic scale is

\[
d\nu_{\mathrm{arith}}(L)
=\sum_{n\ge2}\frac{\Lambda(n)}{n}\,\delta_{\log n}(dL).
\]

The factor (Lambda(p^k)=\log p) records the primitive prime attached to each
valuation depth, while (1/n) is the multiplicative Haar normalization after
the change (n=e^L).

For (operatorname{Re}s>0), its Laplace transform is

\[
\int_0^\infty e^{-sL}\,d\nu_{\mathrm{arith}}(L)
=\sum_{n\ge2}\frac{\Lambda(n)}{n^{s+1}}
=-\frac{\zeta'}{\zeta}(s+1).
\]

The continuous scale measure has transform

\[
\int_0^\infty e^{-sL}\,dL=\frac1s.
\]

Hence the canonical quadrature defect is

\[
\widehat\mu(s)
=-\frac{\zeta'}{\zeta}(s+1)-\frac1s,
\]

where

\[
d\mu=d\nu_{\mathrm{arith}}-dL.
\]

## Divisor content

The subtraction removes the pole contributed by the pole of (zeta) at one.
It does not remove the nontrivial zero poles. If (ho) is a simple
nontrivial zero, then (widehat\mu) has a pole at

\[
s=\rho-1
\]

with residue (-1). Multiplicity changes the residue accordingly.

Archimedean completion supplies the gamma and endpoint terms of the explicit
formula, but it does not erase the nontrivial divisor. It relocates the same
global spectral information into the completed logarithmic derivative.

## Consequence for the seam-current programme

Ledger 3044 reduced the forcing to a continuous scale integral and asked for
an arithmetic quadrature from prime-power samples. The canonical quadrature
exists as a measure, but its error is exactly the prime-counting fluctuation
whose transform carries the zeta zeros.

Therefore proving the required cancellation by asserting that this residual
vanishes, has a favorable sign, or has support confined to the seam would be
circular unless derived from an independent source operator or conservation
law. The arithmetic quadrature is essentially the explicit formula in another
coordinate system.

## What remains admissible

This does not close the moving-seam programme. It rules out one shortcut. A
noncircular proof must do one of the following:

1. pair the residual with the special theta forcing density and prove
   cancellation without separately controlling its full transform;
2. derive a local operator identity whose spectral theorem subsequently
   explains the residual poles;
3. find a source coboundary before prime aggregation, so the divisor-bearing
   scalar residual never appears;
4. use a quadrature on a sharply restricted theta-generated function class
   whose exactness follows independently of zeta zeros.

The sharp hostile test for option four is to add the smallest source function
outside that class while retaining all claimed local prime recursions.

## Verification

The checker verifies the local prime-power geometric expansion, the continuous
Laplace transform, and the surviving residue at a generic shifted nontrivial
zero.
