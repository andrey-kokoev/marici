# Entry 1611 — The Source Endpoint Weights Reject a Naive Scalar Cut Square

## Criticism of Entry 1608

Entry 1608 established a finite Cut-norm mechanism and conjectured its
cosmological realization.  The first source-level falsifier rejects the naïve
realization as the modulus square of one scalar endpoint amplitude.

## Frozen source coefficients

In the direct oscillatory basis, the bulk, combined mixed, and
boundary--boundary sectors are

\[
J_1,qquad -2J_2,qquad -J_0.
\]

The published source normalization is

\[
J_1-4J_2-2J_0
\]

before the \(c_3\) response.  Matching the mixed coefficient would require an
endpoint amplitude weight two.  Its scalar square would then give weight four
to the boundary--boundary term, whereas the source requires weight two:

\[
2^2=4\neq2.
\]

Therefore

\[
\boxed{
\text{no single scalar endpoint amplitude has the source sector weights.}
}
\]

## Surviving conjecture

The finite positivity mechanism is not falsified.  Its source realization
must retain occurrence labels, perturbative symmetry factors, and the
bulk/boundary incidence complex.  The candidate is an occurrence-resolved
quadratic Cut pairing, not \(|A_{\rm bulk}+wA_{\partial}|^2\) for one scalar
\(w\).

## Next falsifier

Construct the two-vertex labelled production complex before quotienting the
two endpoint occurrences.  Derive its quadratic pairing and test whether the
source coefficients \((1,-4,-2)\) arise from incidence multiplicities and the
boundary--boundary \(-1/2\) symmetry factor.  Do not fit a scalar weight.

## Prior artifact reused

`research/benincasa/checkers/finite_time_endpoint_multiplicativity_obstruction.rs`

Allocator claim: `seqclaim-2761985105bf3788221f0c91`.
