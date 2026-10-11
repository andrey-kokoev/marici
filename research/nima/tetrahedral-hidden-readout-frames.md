# Hidden return depends on whether the comparison reference is fixed or transported

## Source-level test

The existing ordinary/twisted tetrahedral examples have the same marked Boolean vertex types. Their six edge-action matrices are related by a Boolean basis flip at vertex 1 alone:

    G1=X, G0=G2=G3=I,
    uij' = Gj uij Gi^-1.

This sends identity edges to X on 01,12,13, and leaves 02,23,03 unchanged, matching the stored twisted edge actions. This is an edge-action calculation. It is not a proof identifying the complete Agda tetrahedral packages or their higher fillers.

## Make the readout's endpoint and references explicit

The old two-edge port produces a map from vertex 0 to vertex 2. The existing diagonal d02 closes it back at the starting vertex. With the inserted comparison operators marked at their actual vertices, the closed hidden readout is

    b0(P;J1,J2) = (1/2) d02^-1 J2 u12 J1^-1 u01.

For the original fixtures d02=I, so this closing operation does not change their previously reported numerical values. It makes the endpoint typing explicit instead of relying on identical underlying Boolean vector spaces.

If local frame changes are presentation changes, the inserted operators must transform too:

    Ji' = Gi Ji Gi^-1.

Direct cancellation of successive G factors proves

    b0' = G0 b0 G0^-1.

The checker verifies this for all sixteen Boolean frame assignments, using exact rational matrices. Freezing J1=J2=J instead fails this covariance test on eight assignments.

## Consequence for the earlier +/- example

Under the vertex-1 flip, X J X=-J. Thus J1'=-J while J2'=J. With these transported references, both ordinary and twisted presentations give +I/2. The earlier +I/2 versus -I/2 result remains correct when J is held fixed in both matrices, but is not invariant under the candidate local-frame policy.

This distinguishes two different experiments:

- **Change the records relative to a fixed comparison reference:** the old sign-sensitive response remains a valid result of the declared law.
- **Change coordinates of the records and their reference together:** the closed response transforms covariantly and the sign distinction disappears.

It would be unjustified either to call the old result a physical gauge-invariant signal without a reference policy, or to declare the two full retained histories physically identical solely because these edge matrices transform this way.

## Disposition and next source obligation

The responsive quantity is not just a function of bare tetrahedral edge data. This adapter also needs a marked comparison reference and an explicit rule for transporting or physically holding it fixed. The source selection problem has therefore narrowed to that reference policy, rather than another arbitrary scalar gain.

Closing with the diagonal supplies a typed numerical return at the starting vertex, but does not by itself derive the original four-cycle gravitational proposal, a physical frame policy, or G. The selected exchange mechanism remains valid; its interpretation as physical back-reaction remains conditional.

## Verification

`python research/nima/checkers/check_tetrahedral_hidden_readout_frames.py` passed. Results: `results/tetrahedral-hidden-readout-frames.json`, including source digests, all sixteen frame tests, frozen-reference controls and the ordinary/twisted sign comparison.

This is an exact matrix audit of the declared edge actions, not a fresh Agda proof or code extraction. No prior dynamics implementation was modified. No ledger entry, commit or publication is claimed.
