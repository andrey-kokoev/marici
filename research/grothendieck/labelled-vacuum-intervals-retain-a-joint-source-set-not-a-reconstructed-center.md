# Labelled vacuum intervals retain a joint source set, not a reconstructed center

## Delivered adapter

A standalone rational adapter now transports the seven-reading inverse to backgrounds 2, 3 and 4, and accepts labelled interval evidence rather than pretending that noisy values specify an exact source.

It returns:

- the complete input JSON value and its digest, recoverable without producer access;
- the labelled source/row model, including vertices, marks, normalization and filtration;
- the exact joint inverse image of the declared reading box within that model;
- derived coefficient and interaction marginals;
- conservative filtration certificates and inverse-norm error bounds;
- an explicit retention ledger and unresolved source-domain obligations.

This is a single-stage conditional inverse. It neither certifies source support nor reconstructs a history. Every generated example is synthetic.

## 1. Source and row transfer is explicit

The source consists only of the eight blockwise P/Q paths on (2,3), (5,7), (11,13), with all events forgotten and coefficient sum zero. At background A its outer corner is A->30030A.

The seven readings retain the owning decoder's exact IDs and seam masks. Arithmetic vertices are recomputed as A times the corresponding prime products. The independent checker compares the A=2 contract and exact inverses with Voevodsky's decoder, then audits the transferred arithmetic labels at A=3,4.

Actual ordered-cut enumeration supplies the forward matrix R. For the published inverse D the adapter checks

    R D = identity_7,
    D R = identity on the seven-dimensional ideal slice.

The canonical and reversed vacuum selectors are additionally checked on all 720 forgotten event orders at each background. The two-seam rows retain their SIX-event outer corner. They are new reading contracts, not readings assumed available from the old four-event receiver.

No norming factor involving a tiny retained-feature amplitude is introduced.

## 2. Preserve correlated uncertainty

Let the seven reading intervals have midpoint c and half-width vector r. The compatible reading values are

    y=c+diag(r)*epsilon,  epsilon in [-1,1]^7.

The compatible source set is exactly

    a=D*c + D*diag(r)*epsilon.

The serialized center and generator matrix retain this joint set. Cartesian bounds here make no statistical independence claim. Additional correlated evidence, if available, must be preserved and intersected separately; the adapter does not accept richer evidence and silently discard it.

The coefficient marginals are useful derived bounds, but their Cartesian product is generally larger than the joint set. In the noisy cubic example, simultaneously selecting every marginal upper endpoint violates sum(a)=0. Keeping only those marginals would lose an exact source correlation.

The error bounds are

    ||a-D*c||_1 <= 4*sum(r),
    ||a-D*c||_infinity <= 4*max(r).

These use the owning inverse's exact operator norms, both four. They concern unweighted path coefficients and unscaled readings, not the order-16 task moment prior or an independently certified physical acquisition error.

## 3. A center's filtration is not the source's filtration

Apply the interaction transform

    m_T=sum_(b contains T) a_b

to the joint set. Within the declared slice, I^k membership requires all coordinates of degree below k to vanish.

The adapter reports:

- `guaranteed`: every relevant affine interaction coordinate is identically zero;
- `ruled_out_by_a_coordinate`: one necessary coordinate interval excludes zero;
- `undetermined`: neither sufficient test applies.

The exclusion test is not a complete joint feasibility solver. It never calls a missing coordinate zero.

For the cubic center with reading half-width 1/100 in all seven coordinates, I membership is guaranteed, I^2 and I^3 membership are undetermined, and I^4 is ruled out. Reporting the center's exact cubic order as the unknown source's order would be incorrect.

## 4. Domain evidence cannot be manufactured by inversion

The input admits references to support evidence and an error contract. These are retained as uninterpreted references, not authenticated or promoted to proofs. The output remains explicitly conditional even when references are supplied.

At every audited background, the nonzero ideal source

    (5,2,3,7,11,13) - (5,3,2,7,11,13)

is outside the cube but has zero terminal value and all seven readings zero. Hence neither reading consistency nor a zero terminal check establishes the support restriction.

For the task lane, this adapter does not replace the original 271-direction-per-background source family with the larger forgotten ideal slice. In particular, a general ideal-slice canonical vacuum value is a mixture of interaction orders, not automatically the coefficient b_A of the pure cubic k_A. Retained-feature contributions and other out-of-domain source information must remain attached externally.

The retention guarantee is exact recovery of the adapter's incoming JSON evidence and model, not recovery of earlier raw acquisitions that were never supplied, original file formatting, or the complete unknown source.

## 5. History and noninvertible comparisons remain separate contracts

Nima's source-derived history and Voevodsky's noninvertible square explain why domain boundaries matter here:

- On the ambient seven-dimensional ideal slice, retaining only canonical and reversed vacuum readings loses five coordinates.
- Under the justified history of appending P-Q twice, the reachable image is two-dimensional and those two readings recover the compatible history.
- The five residual values in that history follow from the dynamics. They are not free values set to zero by an arbitrary section.

The present adapter imposes NO such dynamics. It must not discard five coordinates just because a history-relative inverse exists elsewhere. A future noisy-history adapter must retain the transition equations, earlier evidence and the joint cross-stage fiber, then pull the final constraint back through that justified history.

The optional terminal check here belongs to the FINAL six-event outer corner. It is not an earlier initial terminal fact. A nonzero initial terminal value may coexist with a final ideal source after appending ideal factors; those records must not be conflated.

Likewise, invertible observer coordinate comparisons do not turn lossy quotients into inverses, and the local finite-slice section does not split a globally nonsplit source-bimodule extension.

## 6. Reproduction and retention interface

Generate fixtures, audit labels and roundtrips, and run isolated decoding/recovery:

    uv run python research/grothendieck/checkers/check_uncertain_forgotten_slice.py

Inspect a model:

    python research/grothendieck/certificates/reconstruct_uncertain_forgotten_slice.py --model 3

Decode interval evidence:

    python research/grothendieck/certificates/reconstruct_uncertain_forgotten_slice.py research/grothendieck/results/uncertain-forgotten-slice/A3-readings.json

Recover and verify the exact incoming JSON value from a saved output:

    python research/grothendieck/certificates/reconstruct_uncertain_forgotten_slice.py --recover research/grothendieck/results/uncertain-forgotten-slice/A3-compatible-set.json

Only the Python file and input JSON are needed. Recovery recomputes the entire derived bundle and rejects inconsistent centers, generators or metadata; the digest is an integrity binding, not authentication.

The suite checks 69 exact roundtrips, 384 joint-noise vertices, A=2 agreement with the owning decoder, transferred row labels, out-of-domain collisions, fifteen malformed/corrupted inputs, and isolated execution plus evidence recovery. Existing task inputs and calibration hashes are preserved.

Artifacts are under `results/uncertain-forgotten-slice/`, with the audit in `results/uncertain-forgotten-slice-tests.json`.

No physical reading, justified support, noisy dynamics, calibration-gate resolution or full-source reconstruction is claimed.
