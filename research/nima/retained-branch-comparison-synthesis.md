# Branch comparisons beyond the inherited spectral image

## Interface extension

`RetainedSuccessorLedger` now provides `split_payload(stage, values)` and `reassemble_payload(stage, parent_values, remainder)`.

For a non-root successor with extension J and averaging decoder D, the split is

    parent_values = D y,
    remainder = (I-J D)y,
    y = J(parent_values) + remainder.

The remainder lies in ker(D), the zero-mean sibling-comparison space. Reassembly rejects a remainder with a nonzero mean in any sibling family. Strict `decode()` is unchanged: it still rejects off-image payloads instead of silently projecting them.

This is an analysis/reconstruction interface for an arbitrary supplied path payload, not a constructor that prepares its coefficients physically.

## First successor: four sibling comparisons

The ten-word carrier splits into six copied primitive coordinates and four detail coordinates. In the checker's retained sibling-order convention, a basis of ker(D) is

    c_AB = [AB BA]-[AB BC],
    c_CA = [CA AB]-[CA AD],
    c_BA = [BA AB]-[BA AD],
    c_DB = [DB BA]-[DB BC].

Each bracket is a separate complete word. Basis signs depend on the chosen sibling order; dimension and coarse visibility do not.

With A the final-occurrence summary,

    A c_AB = A c_DB = BA-BC,
    A c_CA = A c_BA = AB-AD.

Thus this four-dimensional detail space has coarse-visible rank TWO and a two-dimensional coarse kernel, spanned by

    c_AB-c_DB, c_CA-c_BA.

The new hidden details are NOT the original K-zero contrasts CA-BA and AB-DB. The old contrasts are in the copied six-dimensional image, have nonzero decoded parent coefficients, and zero sibling detail. The new hidden contrasts have zero decoded parent coefficients and nonzero sibling detail. Both kinds can be invisible to the same coarse summary without being the same retained information.

At each tested extension, the summary of copied parent payloads has rank four and the summary of new sibling detail has rank two; their combined rank is six. This is a statement about this particular observation map, not a new spectral decomposition into physical modes. No preferred complement to the detail's coarse kernel is inferred from the rank count alone.

## Scope of the split

The already selected equal-sibling decoder makes J D the counting-metric orthogonal projector onto the unchanged-copy image. Consequently the one-step inherited/detail split is orthogonal in that metric. This does NOT make J an isometry, nor choose a physical norm or probability law. Injective extension still replicates coefficients according to available continuations.

The comparison space ker(D) consists of zero sibling means. Another decoding convention would need its own explicitly checked complementary space. None is substituted here.

## Later stages retain the new distinctions

Checks extend the ledger through word length six. The current-step detail dimensions are:

| Word length | Parent words | Child words | New detail dimension | Coarse-visible rank | Coarse-hidden dimension |
|---|---:|---:|---:|---:|---:|
|2|6|10|4|2|2|
|3|10|16|6|2|4|
|4|16|26|10|2|8|
|5|26|42|16|2|14|
|6|42|68|26|2|24|

Every detail basis is transported injectively to every later tested stage. Its full retained rank is preserved, while its coarse rank remains two; coarse-hidden combinations remain hidden. The transported detail remains outside the original six-input image, with zero origin decoder reading.

Different introduction stages need not remain distinguishable after coarse aggregation. Full path records, not the coarse ranks, carry that ancestry distinction.

## Complete ancestry reconstruction

Repeated splitting of an arbitrary length-six path payload gives

- six origin coefficients;
- four detail coordinates introduced at length two;
- six at length three;
- ten at length four;
- sixteen at length five;
- twenty-six at length six.

The resulting dimension partition is

    68 = 6 + 4 + 6 + 10 + 16 + 26.

The checker concatenates the transported origin and sibling-detail bases and verifies full rank at every stage. This proves directness and coverage of the finite coordinate decomposition, not merely recovery of a selected numerical example. Splitting/reassembly is also checked on rational payload fixtures.

No orthogonality of all transported introduction-stage subspaces is assumed; the one-step orthogonal split and the multi-step direct decomposition are different statements.

For unchanged-copy inputs, the newly introduced detail is exactly ZERO at every step. The growth of the ambient carrier therefore describes available comparison coordinates, not spontaneous creation of independent amplitudes. Nonzero detail requires an additional supplied payload/preparation rule, which remains outside this construction.

## Verification

    python research/nima/checkers/check_retained_branch_comparisons.py
    python research/nima/checkers/check_retained_path_successor.py

Both fresh runs pass. The latter includes the preceding spectral, observation and retained-path closure checks. Negative tests reject root splits, forged stages, incorrect dimensions, inexact float coefficients, nonzero-mean remainders and strict decoding of pure branch detail.

Report: `results/retained-branch-comparisons.json`.

## Synthesis

The inherited spectral interface covers one well-defined subspace. The rest of the path carrier is now organized by retained sibling comparisons and their introduction stages, without assigning an unsupported ambient spectrum.

The preparation question was made explicit: what operation supplies nonzero coefficients in these branch-comparison spaces? The follow-up `bilinear-branch-preparation-synthesis.md` now shows that the already declared bilinear path rule B(x,y) reaches all four first-stage detail coordinates with a single supplied input pair. Complete ten-word outputs remain constrained to rank-one interface blocks, and physical preparation of those inputs is still not supplied by the algebra.
