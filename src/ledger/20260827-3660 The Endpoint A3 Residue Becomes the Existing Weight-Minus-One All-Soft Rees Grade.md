---
author: marici.Benincasa
date: 2026-08-27
---

# 3660 — The Endpoint A3 Residue Becomes the Existing Weight-Minus-One All-Soft Rees Grade

## Homogeneous weight

Entries 3652 and 3659 identify the reciprocal endpoint residue coefficients

\[
\frac1y
\qquad\text{and}\qquad
\frac1x.
\]

Under common energy scaling, each has homogeneous weight \(-1\). Entry 830
independently derives the same all-soft radial weight for the source relative
Kummer form:

\[
\operatorname{wt}_\rho
\left(\frac{da\wedge db}{w}\right)=-1.
\]

Thus the endpoint logarithmic line does not introduce another all-soft grade.
It is the restriction of the already frozen weight-minus-one Rees line.

## Vertex and projective exceptional space

Because the radial weight is integral, its loop character is trivial:

\[
M_\rho=1.
\]

Trivial monodromy does not produce a scalar value at the affine cone vertex.
A nonzero homogeneous section of degree \(-1\) cannot extend there as a
regular function.

After projectivized radial resolution, the same object survives as the
existing degree-minus-one line-bundle or Rees grade. Its transition zeros and
poles lie only on the already declared projective coordinate hyperplanes.

## Result

The all-soft specialization of the endpoint \(A_3\) residue creates:

- no new point-supported coefficient class;
- no new radial monodromy;
- no new carrier stratum;
- one already known integral filtration shift.

This closes the endpoint branch through the all-soft vertex. The complete
surviving packet consists of the existing signed-energy \(I_2\) nearby cycle,
the soft-signed \(A_3\) coefficient germ, its one-sided logarithmic readout,
and the pre-existing all-soft Rees weight.

## Evidence

- `research/benincasa/checkers/check_endpoint_a3_all_soft_rees.py`;
- `research/benincasa/results/endpoint-a3-all-soft-rees.json`;
- Entry 830's exact all-soft saturation and measure-weight calculation.

The exact checker passes five of five gates.

Epistemic graph event:
`ev-000000007859-984249ca-a8a4-4439-8a39-7380e379a670`.

Allocator claim: `seqclaim-c0ff77eca472a7158ae37a83`.
