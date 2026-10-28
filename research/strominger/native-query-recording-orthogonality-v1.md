# Does native query retention derive physical orthogonality?

## Verdict

Native retention does not itself supply a norm-preserving measurement interaction. However, an explicit isometric nondemolition recording contract forces orthogonality of the query sectors WITHOUT assuming orthogonal pointer states. Combined with the previous triangle transport condition, it selects the uniform pairing on the declared amplitude carrier.

This replaces the algebraic self-adjointness premise by an operationally meaningful sufficient premise. It does not derive that premise from the seed.

## 1. What the inspected native implementation supplies

`NativeSeedTransitionProbe.agda` proves that evaluating a supplied vertex equivalence through the native table or retained filler gives the same Boolean query. Its `retention-preserves-query` is a definitional equality.

`BoundaryGeneratedQuestions.agda` implements `retain-filler` by remembering the boundary packages and storing the filler itself. `filler-recovered` recovers that value definitionally. This is actual native data retention, not an amplitude interaction with a blank pointer.

Neither inspected signature provides an amplitude pairing, tensor-product metric, prepared pointer, isometry or physical apparatus. This bounded source audit does not assert a universal absence theorem for the repository.

## 2. Conjecture R1 and reversible counterexample

Conjecture R1: because a native query can be evaluated and its input retained reversibly, its nondestructive recording lift automatically preserves the attached joint norm.

On labelled states define the controlled recording permutation

    T_e(g,b)=(g,b xor f_e(g)), b in {0,1}.

It is an involution, leaves the group label unchanged, and writes the exact query answer into a blank bit. It preserves every classical input through its inverse. This is a finite semantic replay of query recording, not a proved native amplitude compiler.

Use the previously admitted positive carrier pairings

    H_lambda=(I+lambda J)/(3+9lambda).

Both lambda=0 and lambda=1/9 admit the native triangle left actions as isometries. Give the pointer a Gram matrix

    R_eta=[[1,eta],[eta,1]], eta=0 or 1/2.

Both pointer pairings are strictly positive. At eta=1/2 the two unit pointer states are distinct but NOT orthogonal. They can encode some distinguishing information in a quantum realization, not a perfectly distinguishable classical bit.

Extend T_e linearly to the joint amplitude carrier with product pairing H_lambda tensor R_eta. All six maps remain reversible permutations. They are isometries for lambda=0 and fail for lambda=1/9, for BOTH pointer overlaps.

For the AB query, choose one group-coordinate vector from each answer sector and add them, with blank pointer. At lambda=1/9 and eta=1/2, squared norm changes from

    11/18 -> 7/12.

The recording retains the classical label and computes the right answer, but violates the proposed joint norm. R1 is therefore false. Logical reversibility cannot be substituted for physical isometry.

## 3. Repair R2: isometric nondemolition recording forces orthogonality

Let X_0 and X_1 be the linear subspaces selected by the false and true query answers. Assume a positive carrier inner product, a product pairing with a pointer, a fixed unit blank r, and a linear isometry V satisfying

    V(x tensor r)=x tensor r_0, x in X_0,
    V(y tensor r)=y tensor r_1, y in X_1,

where r_0 and r_1 are unit pointer vectors with eta=<r_0,r_1> != 1.

Preservation of inner products gives

    <x,y>=<x,y><r_0,r_1>,
    (1-eta)<x,y>=0.

Hence X_0 is orthogonal to X_1. The query projection is therefore self-adjoint. In the real finite model, distinct unit pointer vectors suffice to ensure eta!=1. For a physical record one should require genuinely different pointer states, not merely different representatives of the same quantum ray; the explicit eta=1/2 example satisfies that stronger distinction.

No orthogonality of r_0 and r_1 was assumed. Perfect classical readability would be a stronger requirement than this theorem needs.

### Complete finite selector

If each of the six native queries admits this recording contract for the SAME carrier pairing, and the two native triangle left actions preserve that pairing, the preceding translated-query separation theorem applies:

- query recording forces cross-sector pairing entries to vanish;
- translated queries separate all 132 distinct ordered group pairs;
- triangle transport equates the remaining diagonal entries;
- therefore H=cI, c>0;
- unit feature normalization removes c.

With the previously declared local exchange law and common preparation, the AB;BA record response is consequently 1/3, and all typed finite-word responses are fixed.

This remains a theorem on the declared finite carrier and interaction grammar, not uniqueness of all physical realizations.

## 4. Hostile controls and limits

- Identical pointer states have eta=1. They preserve overlaps without forcing orthogonality, but carry no answer distinction. Two syntactic labels do not establish two physical records.
- If the carrier can change during recording, the displayed nondemolition equation no longer holds. General informative measurements need not make their input alternatives orthogonal.
- The product pairing and isometry are assumptions. We have not derived tensor-product quantum kinematics from WG.
- The proposed controlled recording is a different operation from the earlier exchange. Existence of an exchange apparatus does not automatically authorize these nondemolition recorders.
- Retaining a native package is not preparing a blank pointer, implementing its coupling, or resetting it for another run.
- The theorem concerns coherent linear amplitudes and pure pointer preparations. It is not a classification of arbitrary mixed-state instruments.

## 5. Next source obligation

The sought interface is now an explicit recording dilation:

    retained native query
      -> prepared pointer and specified joint pairing
      -> source-authorized isometric interaction
      -> unchanged carrier on each answer sector
      -> distinct pointer states.

A source construction proving that interface would derive query-sector orthogonality operationally. The currently inspected retention functions prove only the first item. This is the precise frontier; renaming retention as measurement would skip the central obligation.

## Verification

    python research/strominger/checkers/check_native_query_recording_orthogonality.py

The exact Fraction checker replays the preceding pairing construction, tests all controlled recording permutations, blank-input correctness and inverse recovery, both pointer metrics, full-domain isometry or its failure, the explicit norm witness, the complete recording Gram-defect identity, and translated-query separation. The general recording implication above is a written proof, not a new Agda theorem.

Receipt: `results/native-query-pairing-selection/recording-orthogonality.json`.

Prior mechanism: `research/kitaev/broadcastability-is-the-algebraic-record-boundary.md`. No physical experiment, fresh Agda closure, native amplitude compiler, or resource-return theorem is claimed.
