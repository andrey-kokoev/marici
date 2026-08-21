# 1539 — The Source Exponent Forces the Integrated Boundary Vertex

## Problem

Equation (17) of arXiv:1408.4801 contains

\[
\exp\left[-i\int V+iS_0^{(3)}\right],
\qquad
V=\bar H_I^+-\bar H_I^-.
\]

At second order this gives

\[
-\frac12\left(\int V-S_0^{(3)}\right)^2.
\]

Equation (18), however, rewrites the same term with

\[
H_0^{(3)}(t)=-\frac12\delta(t-t_0)S_0^{(3)}.
\]

## Unique effective convention

Let

\[
d=\int_{t_0}^{t}\delta(t'-t_0)dt'.
\]

Then the Eq. (18) presentation produces

\[
-\frac12\left(\int V-\frac d2S_0^{(3)}\right)^2.
\]

Matching the bulk--bulk, mixed, and boundary--boundary coefficients to the
source exponent requires

\[
\boxed{d=2},
\qquad
\boxed{\int H_0^{(3)}=-S_0^{(3)}}.
\]

Neither the ordinary full-weight endpoint convention \(d=1\) nor the common
half-weight convention \(d=1/2\) matches Eq. (17).

## Interpretation

The contraction engine must use the integrated insertion

\[
\int H_0^{(3)}=-S_0^{(3)}
\]

as the authoritative source datum.  The local notation
\(-\tfrac12\delta S_0^{(3)}\) is insufficient without a nonstandard endpoint
normalization and must not be interpreted using a default distribution rule.

This is a presentation ambiguity, not evidence for a physical factor of two.
Equation (17) fixes the effective vertex uniquely.

## Verification

`research/benincasa/checkers/boundary_delta_insertion_contract.rs` compares
the three quadratic coefficients.  In a common normalization they are

\[
(-4,4d,-d^2)
\]

versus the required \((-4,8,-4)\), with unique solution \(d=2\).

The machine-readable output is
`research/benincasa/results/boundary-delta-insertion-contract.json`.

## Next falsifier

Reproduce Eq. (19) using the effective integrated insertion.  Retain ordinary
full-weight and half-weight endpoint interpretations as negative controls.
