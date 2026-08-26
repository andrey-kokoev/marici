# Rank-one incidence faithfulness packet

## Grothendieck sources

This formalizes the finite core shared by:

- `research/grothendieck/theta-anomaly-line-incidence-closes-but-rank-one-detection-is-unfaithful.md`;
- `research/grothendieck/theta-overlap-projective-incidence-no-go.md`.

## Formal objects

- `rankOneIncidence vacuum trace c=(trace c)•vacuum` is the anomaly-line
  aggregation.
- `rankOneIncidence_transport` proves exact commutation from compatible trace
  and vacuum transport.
- `nonzero_scalar_trace_surjective` and
  `compatible_trace_composite_surjective` type the one-dimensional endpoint
  quotient-surjectivity statement.
- `twoLabelKernelWitness=(weight_1,-weight_0)` is the explicit detector
  kernel.
- `twoLabelTrace_not_injective` proves scalar unfaithfulness as soon as the
  second label is visible.
- `rankOneIncidence_eq_zero_iff` identifies rank-one incidence loss with the
  ordinary trace kernel when the vacuum is nonzero.

## Assumptions and coefficient types

Transport coherence needs semimodules over a semiring. Quotient surjectivity
and the kernel hostile use vector spaces over a field. The explicit witness
only needs one nonzero visible weight; the source packet assumes both labels
visible, which is stronger.

## Category boundary

The theorem proves projective hyperplane incidence and transport coherence.
It does not produce a symmetric bulk operator, deficiency solutions, a Green
trace, a maximal self-adjoint arithmetic Lagrangian, or a Fredholm comparison.
Calling the scalar overlap a determinant does not turn its zeros into
self-adjoint spectral incidence.

The proposed full Cauchy-jet/seam-germ detector still requires finite
translate independence and completion stability. Those are separate from
the degree-zero scalar trace and remain gated. No RH conclusion follows.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
