# The common reservoir kernel requires a growing boundary-jet observer

Scope correction: the normal factor below is written on a real horizontal
slice.  Its full spectral-plane source is conjugate reciprocity, yielding
\(2\operatorname{Re}(s)-1\).

## The kernel left by reciprocal comparison

The direct-minus-reciprocal characteristic response is

\[
2\left(z-\frac12\right)R_X(P),
\qquad
R_X(P)=\prod_{j=1}^{N_X}(P+\lambda_j).
\]

Its common source kernel is

\[
E_X=\operatorname{span}
\{e^{-\lambda_1q},\ldots,e^{-\lambda_{N_X}q}\}.
\]

A seam observer must be faithful on \(E_X\); otherwise an off-seam state can
remain invisible to both sector observers.

## Canonical endpoint observer

Define the endpoint jet map

\[
J_Xu=\bigl(u(0),u'(0),\ldots,u^{(N_X-1)}(0)\bigr).
\]

For

\[
u(q)=\sum_{j=1}^{N_X}c_je^{-\lambda_jq},
\]

the jet matrix is

\[
(J_X)_{kj}=(-\lambda_j)^k,
\qquad 0\le k<N_X.
\]

This is a Vandermonde matrix.  Distinct labelled rates make it invertible, so
\(J_X\) is a canonical faithful observer of the common reservoir kernel.

## Minimality

Any linear observer with fewer than \(N_X\) scalar output coordinates has rank
strictly below \(N_X\) on \(E_X\).  It therefore has a nonzero invisible
reservoir state.  In particular, one endpoint value or one scalar seam trace
cannot resolve a cutoff containing two or more independent labelled modes.

The minimum seam-observer dimension grows exactly with the number of distinct
source rates.  Under arithmetic cutoff completion, the finite jet maps must
therefore assemble into an infinite boundary-jet object or an equivalent
label-resolved boundary carrier.

## What this does and does not prove

The combined finite observation

\[
u\longmapsto
\left(
2\left(z-\frac12\right)R_X(P)u,
J_Xu
\right)
\]

removes the false invisibility caused solely by the common reservoir kernel.
It does not prove RH.  A seam zero must remain possible through a separate
tangential boundary relation.  If the same jet observer were simply declared
injective on every admissible state at every \(z\), it would forbid seam zeros
as well and contradict the completed section.

This forces a further typing split:

1. kernel-resolution incidence records labelled source memory at the seam;
2. tangential spectral incidence determines which completed boundary states
   may have zero scalar readout on the seam.

Treating both as one scalar seam port conflates observability with spectral
selection.

## DPC verdict

The third observer is not one extra scalar.  Its minimal finite form is the
full endpoint jet of the source reservoir.  Completion must retain that growing
boundary object, while a separately authorized tangential relation carries the
actual seam spectrum.

The finite falsifier for an \(r\)-coordinate seam observer is any cutoff with
\(N_X>r\).  Rank-nullity produces a nonzero common-kernel state invisible to
both sectors and to the undersized seam observer.

## Verification

`check_rh_boundary_jet_observer.py` verifies exact Vandermonde faithfulness for
one through five labelled modes and constructs explicit null vectors for every
jet truncation of insufficient length.
