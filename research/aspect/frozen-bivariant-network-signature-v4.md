# Frozen stratified metric network signature v4

## Status

Version 4 is a new frozen candidate. Version 3 remains unchanged and falsified.

v4 replaces pointwise metric route spaces with stratified metric route families. It adds specialization, radical quotient, and graded normal-crossing data. Cell creation during replay remains disabled, and maximum declared depth remains two.

## Singular fiber

For a Gram family \(G\) and a singular stratum \(Z\), v4 retains:

- the radical \(R=\ker G|_Z\);
- the nondegenerate quotient metric on \(V/R\);
- the specialization relation from nearby fibers;
- the determinant vanishing order;
- a filtration of \(R\) by first nonzero normal jet;
- the induced nondegenerate crossing form on every graded piece.

The radical is not discarded after passing to the quotient. It carries the memory of how rank returns away from the stratum.

## Graded crossing law

If radical directions first appear at orders \(k\) with graded dimensions \(d_k\), v4 requires

\[
\operatorname{ord}_Z\det G=\sum_k k d_k.
\]

Each leading crossing form must be nondegenerate on its graded piece. This prevents a first-jet test from silently accepting a higher-order tangency.

Associators and exchanges must preserve the radical filtration, descend to quotient isometries, and intertwine the graded crossing forms. Pentagon and hexagon laws must close both on open strata and after specialization.

## Completion law

Completed sewing must precede finite projection. Stratifying a finite cutoff does not repair Poisson leakage or authorize a projected global claim. This law is frozen independently from Nima's warning.

## Local gates

The v3 failure packet

\[
G(t)=\operatorname{diag}(1,t)
\]

passes: it has a one-dimensional radical and a nondegenerate first crossing form.

The first unused packet is

\[
G(t)=\operatorname{diag}(t,t^2).
\]

At \(t=0\), the radical is two-dimensional. One direction returns at first order and the other at second order. The determinant has order three, equal to

\[
1\cdot1+2\cdot1=3.
\]

This packet passes the frozen graded-filtration gate. It is still a local one-parameter test, not global admission.

## Next boundary

The decisive unused hostile is multiparameter: a singular packet whose limiting radical filtration depends on the normal direction. v4 currently carries a normal parameter or normal cone, but it has not yet earned path-independent gluing around such a discriminant intersection.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v4.py
```
