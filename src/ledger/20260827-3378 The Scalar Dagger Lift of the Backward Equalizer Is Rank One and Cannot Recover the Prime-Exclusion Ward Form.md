# The Scalar Dagger Lift of the Backward Equalizer Is Rank One and Cannot Recover the Prime-Exclusion Ward Form

The linear zero-state equalizer has the canonical positive lift

\[
|1+q|^2|R_p|^2=|q|^2|A_1+qB_2|^2.
\]

But a dagger square of one scalar covector has rank at most one. At the
smallest prime-two module on labels `(1,2,3)`, the native exclusion Ward form
is `diag(1,0,1)` and has rank two. No scalar weighting or seam coefficient can
remove this mismatch.

Therefore the backward witness must retain labelwise or pro-valued covectors
before forming its dagger or exterior square. Aggregating first and squaring
later cannot recover the arithmetic Ward tower. More generally, at least
`rank(P_{p-free})` independent backward observers are required on an
unrestricted cutoff module, so no fixed finite observer family suffices as
the cutoff grows.

Research packet:
`research/grothendieck/the-scalar-dagger-lift-of-the-backward-equalizer-is-rank-one-and-cannot-recover-the-prime-exclusion-ward-form.md`

Exact checker:
`research/grothendieck/checkers/check_scalar_dagger_ward_rank_obstruction.py`

The checker passes 5/5 gates.
