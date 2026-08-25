# The global Tate integral is the legal joint theta completion operation

## Source-first global operation

Let `phi` be the standard factorizable Schwartz--Bruhat source on the adeles:
Gaussian at the real place and the unit-ball characteristic function at every
finite place.  Its global Tate zeta integral is

\[
 \boxed{
 Z(\phi,s)=\int_{\mathbb A^\times}
 \phi(x)|x|^s\,d^\times x.}
\]

This operation is defined from the completed source and multiplicative Haar
measure.  It does not begin with `zeta`, its logarithm, or its zero set.

## Euler-chart comparison

In the absolute-convergence chamber, factorization gives

\[
 Z(\phi,s)
 =Z_\infty(\phi_\infty,s)
 \prod_p Z_p(\mathbf1_{\mathbb Z_p},s),
\]

with

\[
 Z_p=(1-p^{-s})^{-1}.
\]

Thus the finite Euler determinant and its typed log-current expansion are a
local presentation of one global matrix coefficient.

## Continuation without a scalar logarithm

Split the adelic integral into reciprocal norm regions and apply Poisson
summation to one region.  The resulting identity supplies meromorphic
continuation and the functional equation, with explicit polar boundary terms.
After the standard endpoint polynomial removes those poles, the completed
readout is entire.

This derivation acts on `Z(phi,s)` itself.  It never analytically continues
the divergent scalar series

\[
 \int e^{-zq}\,d\mu_{\log}(q)
\]

through a region containing its divisor.  Hence it avoids the logarithmic
branch circularity of packet 170.

## Compiler typing

The legal completion operation is joint:

\[
 \boxed{
 A_{\rm Tate}:
 (\phi_\infty,\{\phi_p\}_p,
 \text{Haar data},\text{reciprocal sewing})
 \longmapsto Z(\phi,s).}
\]

Its fields are:

- `precedes`: scalar zero testing, determinant-section comparison, and the
  seam return map;
- `commutes_with`: Fourier transform only through the proved Poisson/Tate
  functional equation;
- `domain_after`: a meromorphic section, or an entire section after retaining
  the polar endpoint polynomial;
- `boundary_delta`: the explicit small/large-norm polar terms;
- `completion_scope`: the whole adelic source, not separate prime grades;
- `residual_capability`: retains the completed scalar section but does not by
  itself retain every Euler-chart log-current as an independent global
  scalar.

## Relation to `P,Q,T>=3`

In the Euler chamber, logarithmic expansion of the finite-place factors
recovers

\[
 \mu_{\log}=P+Q+T_{\ge3}.
\]

After leaving that chamber, `P`, `Q`, and `T>=3` remain typed provenance of
the factorization chart, but they cannot each be pushed independently through
`A_Tate` as scalar functions.  Their authorized comparison is

\[
 \exp\left(\int e^{-zq}d\mu_{\log}\right)
 =\prod_p(1-p^{-1/2-z})^{-1}
\]

where both sides converge, followed by continuation of the **global** Tate
section.

Therefore the compiler relation is not three commuting gradewise braids.  It
is one many-to-one normalization:

\[
 (P,Q,T_{\ge3},\phi_\infty)
 \longrightarrow A_{\rm Tate}.
\]

## Durable gain and remaining gap

The joint completion operation is source-derived and noncircular.  What is
still absent is an operator-valued lift

\[
 A_{\rm Tate}
 \longrightarrow
 (B_s,C_s)
\]

from the global scalar matrix coefficient to the seam incidence maps of the
return operator.  Reconstructing such maps backward from the scalar completed
function would be tautological.

Thus global analytic continuation is no longer the missing operation.  The
missing theorem is a functorial lift of Tate--Poisson sewing from scalar zeta
integrals to the full tail--seam boundary module.
