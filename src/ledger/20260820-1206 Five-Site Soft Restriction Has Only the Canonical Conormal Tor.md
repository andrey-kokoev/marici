---
title: "Five-Site Soft Restriction Has Only the Canonical Conormal Tor"
date: 2026-08-20
entry: 1206
status: active-supported-base-change
sector: cosmology
---

# 1206 — Five-Site Soft Restriction Has Only the Canonical Conormal Tor

Sequence claim: `seqclaim-c8ce86e903d84c603fd192e6`.

## Supported calculation

Entry 1205 proves generic Koszul exactness for the first-Rees occurrence
symbols. Restrict now to their declared soft support rather than inferring
supported exactness.

For a regular soft ideal (I=(2X_A)) or (I=(2X_A,2X_B)), derived
self-intersection gives

\[
\operatorname{Tor}^R_\bullet(R/I,R/I)
\simeq
\Lambda^\bullet(I/I^2).
\]

Hence the conormal ranks are

\[
\boxed{
\begin{array}{c|c}
\operatorname{codim}I&\text{Tor ranks}\\
\hline
1&(1,1)\\
2&(1,2,1).
\end{array}}
\]

## Tensor with the geometric carrier

Tensor these conormal algebras termwise with Entry 1202's projective OS
cohomology. The resulting supported objects have seven profiles. Summed over
all 180 source terms, their ranks by conormal degree are

\[
\boxed{(12420,14670,3430).}
\]

Every rank is exactly the OS rank multiplied by the appropriate binomial
coefficient. There is no additional kernel, cokernel, or torsion:

\[
\boxed{\operatorname{Tor}_{\rm excess}=0.}
\]

## Meaning

The supported object is not zero. It is the canonical exterior conormal
layer required by the already declared soft embedding. No fitted support
summand and no new carrier stratum is needed.

This separates two valid statements:

\[
\text{generic positive Koszul homology}=0,
\]

while

\[
\text{supported derived self-intersection}
=\Lambda^\bullet(I/I^2).
\]

## Next falsifier

Attach the five-site Cayley--Menger coefficient variation to this supported
OS--conormal object. Determine its inertia along the (1|4) and (2|3)
soft divisors and their mixed intersections. A coefficient rank or monodromy
beyond the existing branch/Gram nearby cycles would refine H2; only an
undeclared incidence support would challenge the carrier.

## Artifacts

- `research/benincasa/checkers/five_site_qg_supported_conormal.py`
- `research/benincasa/results/five-site-qg-supported-conormal.json`
