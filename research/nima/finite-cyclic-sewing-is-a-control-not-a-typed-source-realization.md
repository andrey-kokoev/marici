# Finite cyclic sewing is a control, not a typed source realization

## Question

Does Aspect’s exact \(Z/6Z\) Fourier construction supply the missing finite
typed sewing matrix?

## Claim boundary

It supplies an exact phase-framed finite control and simulator threshold. It
does not derive the incidence between cyclic residues and the six declared
source channels. All \(6!=720\) assignments preserve the same Fourier
unitarity.

## What the cyclic model constructs

The finite source is the function space on \(Z/6Z\) with delta basis
\(\delta_0,\ldots,\delta_5\). The trace is the identity and the normalized
Fourier matrix is

\[
J_{kj}=\frac{\omega^{kj}}{\sqrt6}.
\]

Its Gram metric is the identity, \(J^\dagger J=I\), \(J^2\) is inversion, and
\(J^4=I\). These statements make it a valid finite source-derived control
inside the cyclic model.

## Missing typed incidence

The six target labels are:

1. primitive;
2. prime-square;
3. seam;
4. endpoint;
5. connected tail;
6. archimedean.

The cyclic source provides no map assigning these types to
\(\delta_0,\ldots,\delta_5\). Equal cardinality supplies bijections but selects
none.

For every permutation matrix \(P\),

\[
(PJ)^\dagger(PJ)=I.
\]

Hence all 720 output assignments pass unitarity, inverse composition, norm,
and singular-value tests. Matrix quality cannot authorize the arithmetic or
physical meaning of a row.

## Controlled compilation status

Because the cyclic \(J\) is an actual phase-framed operator, its algebraic
controlled block is defined. A finite optical multiport may use it as a
calibration or compiler fixture.

That controlled cyclic experiment tests:

- coherent-control plumbing;
- route-marker erasure;
- map tomography;
- uncertainty thresholds;
- port-label preservation inside the declared cyclic source.

It does not test:

- the completed adelic trace basis;
- the six theta boundary incidences;
- a source-derived left/right associator;
- physical arithmetic channel labels.

## Source identity gate

A typed replacement requires six labelled source vectors
\(\phi_i\in\mathcal S(\mathbb A)\) and proofs that:

1. each declared channel is derived from \(\phi_i\);
2. the trace coordinates are injective on their span;
3. Fourier images close in the declared finite carrier or have an explicitly
   typed residual;
4. the Gram metric is source-derived;
5. cutoff refinement preserves the incidence;
6. every allowed basis change preserves the channel labels or carries an
   explicit transport cell.

No permutation may be selected because it makes the matrix look symmetric,
unitary, sparse, or experimentally convenient.

## DPC verdict

Current type: exact finite cyclic control realization.

Withheld type: finite completed source realization with the six declared
boundary channels.

Finite falsifier: two different residue-to-channel permutations give equally
unitary matrices and different typed incidence. The complete ambiguity has 720
elements.

## Disposition

The cyclic construction should be retained as the controlled-apparatus
calibration model. It cannot cross into the completed source programme until a
labelled source incidence map replaces the provisional ordering.

## Verification

The checker check_z6_typed_incidence_ambiguity.py verifies exact Fourier
orthogonality in the cyclotomic ring, enumerates all 720 assignments, and
confirms that every assignment preserves the same Gram matrix while carrying a
distinct type signature.

Source artifacts audited:

- research/aspect/completed-sewing-finite-cyclic-realization.md
- research/aspect/contracts/completed-sewing-finite-cyclic-source.v1.json
- research/aspect/checkers/check_completed_sewing_finite_cyclic_realization.py
