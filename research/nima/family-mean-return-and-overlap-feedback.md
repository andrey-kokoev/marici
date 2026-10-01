# Feedback from editable family records

## Return contract

Start with the137 labelled slot records and their32 source-indexed and32
target-indexed families from the fibration audit. Retain every member. In
addition to membership, expose each family's arithmetic mean as an editable
readout. Member values form x in R137. The mean is a selected interface
observable, not the complete promoted record.

For a family F, define get_F(x)=sum_(i in F) x_i/|F|. Returning a requested
mean y uses the smallest Euclidean member change:

    put_F(x,y)_i = x_i + (y-get_F(x)) for i in F,
    put_F(x,y)_i = x_i otherwise.

This follows by minimizing squared change subject to the mean constraint.
It satisfies get-after-put=y, put-back-current-mean=x, and last-put-wins for
the same family. Internal deviations from the family mean are preserved.
Euclidean cost, mean readout, full correction, and the update schedule are
explicit choices. Different metrics or readouts define different returns.

## Gain determined by incidence

A source-family edit delta changes every member in that family by delta.
The change read by target family T is

    delta_y_T = (|F intersection T|/|T|) delta.

This is an actual cross-interface gain computed from retained membership.
It requires no coefficient inferred from rung numbers. For the full family
mean map A and compatible requested readouts y, simultaneous least-change
return is

    x_next = x + A^+ (y-Ax).

A request is compatible iff y belongs to the image of A. Retained member data
make hidden directions available; they are not overwritten by this return.

## Overlapping-family feedback

Within each source partition the normalized group indicators are orthonormal;
let P_s project onto their span, and similarly P_t for target families. A
source correction followed by target correction has residual map

    e_next = (I-P_t)(I-P_s)e,
    feedback operator = P_s+P_t-P_t P_s.

The projectors generally do not commute. A target correction can reopen a
source mean, making further reconciliation necessary. For compatible desired
means, alternating projections converge to the joint least-change solution.
The common invisible subspace is preserved pointwise.

## Concrete137-slot outcome

The64 family mean rows have rank47. Thus90 member directions are invisible
to these means; full member records retain those details. The residual operator
has spectral radius0.290892665417 on the47-dimensional visible subspace and
acts as identity on the90-dimensional invisible subspace.

| Source-target cycles | Mean residual norm in seeded test |
|---:|---:|
| 1 | 0.385311503223 |
| 2 | 0.0682087070713 |
| 5 | 0.00144717760989 |
| 10 | 0.00000301220431348 |
| 30 | 2.05518979885e-16 |

A request changing one source arrow-family mean while demanding zero target
arrow means is incompatible: the weighted source and target totals disagree.
The joint image test detects it. Repeated alternating enforcement of such a
request should not be reported as convergence to an agreed state; a conflict
policy or explicit approximation objective is required.

## Incremental structural result

The indexed-family architecture now has a concrete read/return contract and
a feedback operator derived from its membership incidence under that contract.
This model stays at the137 member level and the first source/target indexes;
it does not yet implement persistent identity/version semantics or two levels
of recursively promoted family endpoints. Its gain is a software response
coefficient, with no current identification as alpha or physical energy.

The next useful test is whether the return contract remains consistent through
promotion to families of families, preserving weights and provenance, and
whether different grouping routes give the same reconstructed member update.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_family_record_return.py

Checks all cross-family gains against intersection counts, readout rank,
residual spectrum, preservation of hidden detail, convergence to the joint
pseudoinverse solution, and rejection of one incompatible request. Uses NumPy
with explicit tolerances and a fixed seed. No measured constants enter.
