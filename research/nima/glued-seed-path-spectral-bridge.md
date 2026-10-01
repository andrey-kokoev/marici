# Actual glued path composition admits cross-triangle continuations

## Source operation reused

Use the existing `check_indexed_path_synthesis.py` pullback composer: concatenate retained words exactly when the first target equals the second source. Instantiate it on the actual six labelled primitive arrows, without keeping triangle context as a restriction on allowed continuation.

This differs from the preceding product-category pilot, where both triangle components continued separately. No new coupling matrix or weight is added to create additional paths.

## Glued versus unglued domain

With the shared A and B vertex identities retained, there are ten composable two-step words. With separate vertex copies per triangle, there are six. The difference is precisely

| New cross-context word | Source | Target |
|---|---|---|
|AB BA|A|A|
|BA AB|B|B|
|CA AD|C|D|
|DB BC|D|C|

The two return words are nonempty histories, not identities. The C->D and D->C composites do not insert CD or DC as primitive edges. Parent labels, word order and actual endpoint records remain recoverable.

The source determines availability of these concatenations. It does not determine which path is executed, its frequency, amplitude, energy or probability.

For bounded structural controls, the complete path-language counts are:

| Length | Glued | Unglued |
|---|---:|---:|
|1|6|6|
|2|10|6|
|3|16|6|
|4|26|6|
|5|42|6|
|6|68|6|

No physical interpretation of those counts or recurrence is asserted. Set composition is checked to be associative, and complete words rather than endpoint pairs are retained.

## Correct carrier change

The primitive coefficient carrier is now the DIRECT SUM of the two local three-occurrence spaces: complex dimension SIX. This is not the earlier nine-dimensional tensor space of paired occurrences.

The six local rank-one projectors (three for each triangle) extend blockwise to the six-dimensional carrier, are pairwise orthogonal, and sum to identity. Each remains tied to its own registered spectral record and history window.

Declare the usual free bilinear extension of endpoint path composition:

    coefficient of word (a,b) = x_a y_b, if target(a)=source(b).

Its output carrier is the TEN labelled length-two paths. Incompatible primitive pairs are absent from that path domain. The linear extension from the 36 formal primitive tensor basis pairs onto this ten-path space has rank ten. This does not imply that a single separable input pair x,y independently prepares ten arbitrary output amplitudes.

## What local spectral records can and cannot do

Keeping ALL six input modes and composing their components with the actual endpoint rule gives

    B(x,y)=sum_(alpha,beta) B(P_alpha x,P_beta y).

All 36 input basis pairs pass this reconstruction square, as does a complex coefficient fixture. Local spectral coordinates are therefore sufficient to REPRESENT the primitive inputs without information loss, provided actual endpoint composition and provenance are retained separately.

But two restrictions fail:

1. **Same-context spectral operand pairs only.** This preserves the six local continuations but deletes the four new cross-context words. For example, x=e_AB and y=e_BA produce the retained word AB BA, while this restriction gives zero coefficient in the enlarged output space.
2. **Same-mode pairs only.** This also fails exact reconstruction. Cross-mode contributions are needed; matching eigenvalues is not implied by endpoint composability.

These zeros are results of explicit coefficient truncation in a common comparison space, not claims that an unavailable physical experiment was executed with zero response.

Finally, the three-packet triangle adapter does not accept ANY two-step output word: all such attempts are rejected by its existing arity check. No next-level spectral identity is fabricated. Thus complete local spectra provide a coordinate bridge into the enlarged path domain, NOT a closed successor output format.

## Structural synthesis

Unlike the context-separated product algebra, full glued endpoint composition genuinely depends on the shared source incidence. It adds available cross-context histories without inventing a numerical force. This corrects the operation domain before asking about a response.

The remaining spectral question is downstream: how should the complete retained family of mixed-length/branched path records be promoted under an admitted constructor? Reusing the local three-slot projector routine is not enough, and the old nine-dimensional tensor algebra must not be silently substituted for this six-to-ten bridge.

No physical preparation, traversal schedule, calibrated reader or native pointed-equivalence witness is supplied by this finite coefficient construction.

## Verification

    python research/nima/checkers/check_glued_seed_path_spectral_bridge.py

Fresh exact checks pass for the four added words, glued/unglued language comparison through length six, local spectral completeness, all 36 input basis-pair products, complex reconstruction, context/mode restriction failures, output parent recovery and rejection by the three-slot adapter. Importing the existing composer reruns its original path-indexing and associativity regressions.

Report: `results/glued-seed-path-spectral-bridge.json`.
