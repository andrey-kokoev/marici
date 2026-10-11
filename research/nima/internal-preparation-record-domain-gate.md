# Admission test rejects internal preparation on the existing record domain

## Actual contract being tested

The twelve-mode memory lift stores discarded contrast. With P the mean
projector and Q=I-P, its natural minimal bank is

    r in ker(P), initialized at r=0.

The original return preserves this 23-dimensional carrier-plus-bank domain.
The 24-coordinate formula also defines a larger mathematical extension, but
its additional bank common coordinate is not part of that minimal storage
contract. The preceding preparation used precisely this extra coordinate.

## Exact gate

Let A=diag(I,Q) be the admissible-state projector. The checker proves

    U A = A U,
    A(u,0)=(u,0).

All simultaneous carrier/bank coordinate permutations also preserve this
domain and fix that baseline. Adjacent transpositions generate all of them;
the property therefore persists under compositions with U.

For the proposed internal preparation E_t, however,

    P r_after = [2t²/(3+2t²)] u.

Over real t this is zero only at t=0, the trivial preparation. Every nonzero
member of the proposed family leaves the existing record domain.

At t=1 the unauthorized bank mean is 2u/5. Projecting it away would change
the decoded payload from u to 3u/5 and discard model budget 64/5. That is
not a valid normalization or a lossless implementation of the old law.

## Disposition

Reject `internal-history-preparation.md` as an implementation ON THE OLD
minimal bank. Its full-space isometry calculation remains correct, but it
is an explicitly enlarged model requiring additional admitted storage and
write operations. A mathematically available coordinate is not evidence
that the source has that operational degree of freedom.

This is a bounded numerical-domain gate, not a theorem that every native
retained object has a zero-mean bank. Generic source retention does not by
itself supply the missing correspondence to this extra numerical mode.
The tetrahedral source still admits nontrivial history swaps; those swaps
do not automatically perform this common-mode conversion.

The external-reservoir construction remains a conditional resource-accounted
option because its final encoded bank is mean-zero. It still requires the
reservoir, control and physical realization as supplied inputs. There is no
currently checked autonomous preparation from the old baseline.

## Verification

    uv run --with sympy python research/nima/checkers/check_internal_preparation_record_domain.py

32 exact checks pass, with the previous internal-isometry checks rerun.
Receipt: `results/internal-preparation-record-domain.json`.
