# Filtered cubic nonvanishing has a portable source certificate and independent verifier

## Deliverable

The finite obstruction supporting the 270-row filtered nonvanishing theorem now has an exported exact certificate and a separate verifier.

The verifier uses only Python's standard library. It imports no producer, discovery checker, project recorder, SymPy, or numerical integration code. A portability test runs it in isolated Python outside the repository with only the verifier and the two JSON files.

It verifies the finite source assertion

    P_y(N I)=0, P_y(f(v_y))=1,

conditional on the explicitly declared owning observer/analytical hypotheses. This is the obstruction used by the exact filtration-level-two functor. The independent program does not purport to re-prove the entire completed filtered-category construction or the theta calibration.

## 1. Files and evidence contract

Producer:

`checkers/export_filtered_obstruction_certificate.py`

Independent verifier:

`certificates/verify_filtered_obstruction.py`

Portable evidence:

- `results/filtered-obstruction-problem.json`;
- `results/filtered-obstruction-certificate.json`.

The versioned problem freezes the six labelled events, the old and cubic outer corners, the two old seam rows, the target private row, the original unchanged stage-two protocol, and the source/target filtration flags. It also records the pushout graph signs (1,-1).

A SHA-256 digest binds the certificate to this problem. The verifier independently checks that the problem is the supported mathematical protocol; accepting a new digest does not authorize changed endpoints or a changed filtration. The digest is input integrity, not authentication.

Structural labels are integers. Coefficients and asserted scalar values are rational strings. Floating-point values, boolean labels, duplicate JSON keys, duplicate path terms and unrecognized certificate fields are rejected.

The certificate contains actual expanded source vectors and projected right-action values, rather than just a passed flag or an advertised rank.

## 2. Independently verify the local relation kernels

For all 240 typed two-event corners in the six-cube, the verifier rebuilds the terminal recorder from its defining rule:

- forgotten edges contribute the empty word;
- a retained x->y edge contributes the noncommutative potential difference u_y-u_x;
- u_root=0;
- successive retained contributions concatenate in order.

It uses its own rational elimination to verify rank six on the eight marked paths in each corner. It checks the supplied forgotten and mixed relation vectors, their zero recorder images and their independence. Therefore these two vectors span the ENTIRE two-event kernel, including the absence of an additional two-retained relation.

It also verifies injectivity at zero and one event. Thus every nonzero ideal factor needs at least two events. No global assertion that every relation is quadratically generated is needed for the minimal-length argument below.

## 3. Verify spanning, not only the displayed witness

A contributing right product has the form x c with x in I^2 and c in I. The target row has six events and fixed outer endpoints. Minimal lengths force x to have exactly four events and c exactly two. Longer sources or contexts cannot contribute, and right multiplication cannot change the initial vertex.

Every four-event I^2 source is a linear combination of products of two of the verified minimal two-event relations. The verifier independently enumerates all possibilities:

    15 four-event prefix endpoints,
    6 ordered pair partitions per endpoint,
    4 retained/forgotten factor choices,

for a total of 360 prefix generators. Their expanded path supports are disjoint within each endpoint corner, proving independence as well as spanning there.

Appending either of the two verified ideal relations on the remaining pair gives 720 right-action generators. The certificate cannot omit a troublesome prefix or action: the verifier constructs the complete expected index sets itself.

On a four-event I^2 input, saturation of the old observer cannot add nonidentity contexts: those would exceed its four-event support. The lower detector kills I^2. Thus only the two old depth-two sector coefficients matter, and only when the outer endpoint is exactly the old endpoint 420, mask 15.

Both coefficients equal one common prefix coefficient. The old physical functional is d_2 times this coefficient, with d_2 nonzero. Exactly one prefix has nonzero coefficient: the mixed (2,3), forgotten (5,7) product v_2. Therefore the other 359 prefix generators are a COMPLETE relevant source-preimage generating set for N under right multiplication.

This is a source-preimage certificate. It need not materialize a huge basis of the observer quotient N itself. Surjective compatible source evaluation supplies that passage, as stated in the input contract.

## 4. Verify the action and the private witness independently

The verifier computes ordered cuts directly on marked paths. For a vacuum-buffer row it requires every retained mark to be one of the selected cuts. Positive-degree buffer words cannot contribute to vacuum. It then matches the actual seam vertices and marks, retaining outer endpoints explicitly.

This implementation is separate from the producer's recorder and derivative routines.

For every prefix it checks both final-diamond actions and the identity

    P_y(x c_1)=ell_2(x)/d_2,

in exact source coefficients. The forgotten final relation contributes zero to the retained final slot. The result is zero on every relevant N-prefix action and one on

    v_y=mixed(2,3) forgotten(5,7) mixed(11,13).

The same independent cut enumeration also verifies the full 270-by-270 private coefficient matrix is the identity on the two-feature minimal cubic products. This confirms that the distinguishing row belongs to the declared separating family; it is not a newly fitted coordinate.

Actual scalar responses multiply those source coefficients by their nonzero physical factors. The verifier checks the exact combinatorics, not those numerical amplitudes.

## 5. Filtration and the explicit verification boundary

The problem retains the flags

    B: (B,B,B,0), A: (A,A,B,0), G: (G,G,0,0),
    K: (K,N,L,0),

and the pushout relation (f(b),-i(b)). At level two, a splitting of the observed extension would yield H:A->N with H i=f. Right equivariance would then imply

    f(v_y)=H(v_2)c_1 in N I,

contradicting the independently verified values.

The owning theorem proves that evaluation at filtration level two is exact and therefore detects nonvanishing after every admissible filtered refinement. This categorical implication is a mathematical input, not a claim that a rational program has reconstructed the complete filtered derived category.

The other explicit external inputs are:

- the actual old gap d_2 is nonzero;
- the actual target response factor E_y is positive;
- the observer is the declared surjective compatible source-bimodule evaluation;
- the ideal and source recorder are the stated ones.

No response noise tolerance, all-depth bound, theta enclosure or physical acquisition claim is added by this certificate. In particular exact coefficient one is not confused with an unnormalized measured amplitude of one.

## 6. Adversarial and portability checks

`checkers/check_filtered_obstruction_verifier.py` loads only the verifier and saved evidence, never the producer or the discovery scripts.

The test run verifies:

- the original bundle;
- a benign reordering of all evidence lists and source terms;
- rejection of 34 semantic corruptions, including missing generators, wrong actions, wrong relations, altered endpoints, false kernel membership and an altered filtration even with a recomputed digest;
- rejection of duplicate-key and floating-point JSON inputs;
- isolated three-file execution outside the repository.

The tests exercise certificate checking, not experimental reliability or proof of the external hypotheses.

## Reproduction

Generate or regenerate evidence:

    uv run --with sympy python research/voevodsky/checkers/export_filtered_obstruction_certificate.py

Verify the saved evidence independently:

    python research/voevodsky/certificates/verify_filtered_obstruction.py research/voevodsky/results/filtered-obstruction-problem.json research/voevodsky/results/filtered-obstruction-certificate.json

Run verifier tests:

    python research/voevodsky/checkers/check_filtered_obstruction_verifier.py

All pass. The certificate is approximately 1.3 MB; independent verification requires no project imports or optional Python packages.
