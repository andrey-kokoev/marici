# From retained field pairs to metric comparisons and typed shared-leg responses

## Objective and disposition

Construct numerical comparisons from the 36-component field, identify the information they erase, and test the actual shared-leg numerical/DG interface without fitting to its old matrix fixture.

This experiment provides three distinct outcomes:

1. **A concrete 137-scalar metric readout**, conditional on an explicit coframe-comparison policy.
2. **A demonstrated information-loss obstruction:** these scalars alone cannot recover the field or even its named L-projector energy.
3. **A typed rectangular shared-leg realization** satisfying the existing symbolic boundary-response identities, but not identical to the original fixed 2×2 numerical adapter.

No physical scale, direct reference d, reference-edge selection or preferred comparison policy is inferred from the count.

## The numerical comparison policy

Write x_e for the native spatial vector on arrow e and B_e for its existing invertible corner realization. Set

```
c_e = B_e^{-1} x_e,
K3 = B_e* B_e.
```

The exact classification already checked that K3 is the same for every patch. We use the supplied common corner metric to compare different arrows:

```
Q_arrow[i,j] = c_j* K3 c_i,    e_i,e_j != reference.
```

The orientation (j adjoint, then i) matches the existing chronological parent composition Y_j X_i. The block is the transpose of the usual column Gram convention; it is still Hermitian positive semidefinite and has rank at most three.

This pairing uses the actual coframes, not just the direct-sum metric. The direct-sum field metric alone does not identify distinct fibers for a cross-arrow comparison. Another possible policy is the common native spatial dot product x_j* x_i. The checker explicitly compares the two and finds differing values on the same field. Both must not be called the uniquely forced comparison merely because each uses existing geometry.

## Comparing the four state fibers without arbitrary neighbor ordering

For source vertex a, form a vector z_a in four destination-labelled slots, each of dimension three:

```
z_a[t] = c_(a,t) if t != a, otherwise 0.
```

Thus z_a belongs to C^4 tensor C^3, with metric I4 tensor K3. The zero diagonal slot records the absence of a self-arrow; it is not an additional field amplitude.

Define

```
Q_state[a,b] = z_b* (I4 tensor K3) z_a.
```

This matches fields by their actual target labels, rather than inventing an ordering identifying one source's three neighbors with another's. The diagonal is the total outgoing source-fiber norm. Off-diagonal entries sum comparisons at the two common destination labels. This is an explicit relational policy, not a derived physical state identification.

Together the 11×11 and 4×4 blocks supply **121 + 16 = 137 scalar slots**. They retain the original typed slot labels. Native proper rotations move the reference and endpoint labels while preserving these values covariantly; all twelve actions are checked against the independently sourced field matrices.

## Information loss is real, not only a possible caveat

A shared K3-unitary change T of all corner triples leaves both Gram blocks unchanged. The unrefined comparison rule therefore has at least a common U(3) ambiguity. It does not by itself enforce preservation of the named local projector P.

The checker constructs a K3-unitary Householder reflection that mixes the P line with its complement. For the original and reflected fields:

- all 137 scalar values agree exactly;
- the fields differ;
- total L-projector energy differs.

This is a concrete collision in a structure-sensitive quantity. It cannot simply be dismissed as harmless gauge freedom while the named L operation remains part of the retained structure. It proves that the scalar readout is not a lossless replacement for the pair-valued field package.

### A minimal structure-aware refinement

Use the already supplied complementary projectors P and I−P. Within each of the same 137 labels, retain two numbers: the P-sector pairing and the complementary-sector pairing. Orthogonality ensures their sum recovers the original scalar value.

This refinement distinguishes the exhibited collision and is invariant under the shared local U(1) × U(2) group. It is **137 labels with two scalar channels each**, not still only 137 scalar numbers. An explicit nontrivial sector phase leaves the refined data unchanged, so full field recovery is still not claimed. No complete classification of every readout collision is asserted.

## Rank obstruction for the old fixed 2×2 numerical identification

For the tested nondegenerate complex field, the scalar arrow Gram has rank 3 and the state Gram rank 4. These arise from vectors in dimensions 3 and 12, respectively; the latter four-vector Gram has rank at most 4.

Consider the direct candidate identifying every scalar q_ij with the old 2×2 response q_ij I2. Stacking such responses gives block matrices of ranks **6** and **8**. But responses of the old form Y_j X_i with a shared two-dimensional intermediate necessarily factor as a block column times a block row, hence have rank at most **2**.

Therefore that particular scalar-times-I2 identification is impossible on this fixture. The existing adapter also rejects the rectangular legs below because its multiplication is hard-coded to 2×2 matrices. This is a scoped obstruction, not a theorem excluding every matrix-valued or nonlinear adapter.

## Positive rectangular realization of the existing symbolic graph

Retain the actual owner graph and its source/target types, but state new object dimensions explicitly:

```
A = C,  B = C,
U = C^3,  V = C^12.
```

For the arrow branch, take X_i = c_i as a 3×1 column and Y_j = c_j* K3 as a 1×3 row. For the state branch, take X_a = z_a as a 12×1 column and Y_b = z_b* (I4 tensor K3) as a 1×12 row. Then each Y_j X_i equals the intended scalar comparison exactly.

The source graph's existing base-leg differences, two comparison routes and rectangle fillers retain their actual typed paths. Generic dimension-checked multiplication verifies:

- both witness-route responses equal Y_j X_i − d for all 137 slots;
- the two routes agree for two different base-root choices;
- filler responses give the corresponding mixed difference products;
- evaluated filler boundaries vanish;
- the existing retained-family promotions preserve all leaves and the weighted terminal response.

The calculation is a new rectangular **boundary-response realization** of the same symbolic construction. Degree-one witnesses are observed through their boundary differences, as in the original checker. It is not silently claimed to be a degree-preserving DG functor into ordinary vector spaces with zero differential, nor the identical old 2×2 realization.

The two tested d values, 0 and 2, are supplied controls. Changing d leaves the indirect comparison values unchanged and shifts the terminal residual by the expected amount. Thus neither 137 scalar slots nor the field pairing determines d.

## Tower consequences

The field-slot tower remains the lossless retained package. Metric comparisons are a **readout of that package**, not an erasure of its underlying field/history. The numerical shared-leg layer can now be populated at a rectangular candidate scope, with its object dimensions, pairing policy, witness response rule and supplied d explicitly recorded.

A full identification with the pinned numerical/DG carrier is still not established: the original numerical dimensions and assignment are different. Future work should compare these realizations as typed objects rather than replace one with the other on the basis of 137 matching labels.

The productive next questions are:

1. Is coframed pairing or native spatial pairing selected by the intended observation? What independently supplied comparison fixes this choice?
2. Should the readout retain the two named projector sectors separately, and what further observations are needed for the required reconstruction task?
3. Can the rectangular realization be related to the intended numerical carrier by an independently justified typed comparison, without rank collapse or discarded observables?
4. What source observation supplies d and its calibration?

## Reproduction

```
python research/strominger/checkers/check_field_metric_dg_binding.py
```

The checker uses exact algebraic arithmetic, the existing patch coframes, the owning symbolic shared-leg graph, and the owning retained-promotion routines. It writes `research/strominger/results/field-metric-dg-binding/verification.json` with explicit scope and direct source hashes. Generated receipts remain ignored runtime files. No viewer, website, production model or physical claim is changed.
