# Full native-pair dynamics do not linearly embed in the new coefficient law

## Result

The first source-comparison gate rejects a faithful, time-independent real-linear amplitude embedding of the full native spinor pair into Strominger's new coefficient dynamics. It does not reject a selected encounter-sector embedding, nonlinear or density-state representations, controlled/time-dependent maps, or a different dynamical law.

This is a new exact calculation using source constructors and pinned native receipts, not a comparison of note terminology or numerical energy fits. No owner source/result files were regenerated.

## Declared comparison

[Contract](contracts/scattering-generator-compatibility.v1.json) was written before execution. Active SCC obligation: source forward realization followed by generator intertwining, before energy-form and channel transport.

Strominger's coefficient state has137 rows and four real matrix-response columns. Vectorizing it gives548 real coordinates with generator A_c=I4 tensor A. This is larger than the200 real coordinates of the full100-complex-dimensional native pair, so the result is not a simple dimension-count objection.

The native branch is the existing optional cycle-defect energy H=L+2I-T-T^dagger and its declared conjugate pair:

    H_pair=H tensor I+I tensor conjugate(H).

Test whether an injective real-linear B satisfies

    A_c B=B realify(-i a(H_pair-bI)),

for a nonzero common real rate a and any common real offset b. Allowing b is deliberately generous; this does not physically select a vacuum or authorize dropping phase references relative to other sectors.

## Exact source reconstruction

The checker calls Strominger's S4 classification and native-generator constructors without running their artifact-writing mains. Direct exact matrix calculations verify

    p(A)=0,  p(x)=x(x^2+32)(x^2+128).

The three rational orthogonal projectors have ranks36,2,99 for squared frequencies32,128,0 respectively. Repeating A over four response columns changes multiplicities but not its at-most-five distinct complex eigenvalues.

For both native chiralities, reconstruct T from the recorded spin lift and L from the two retained low doublets and high-energy complement, using the same code and spectral convention as the existing native-pair adapter. The five nonempty single-object energy spaces are checked by exact Lagrange spectral projectors: Hermiticity, idempotence, eigenvalue equations, multiplicities and sum-to-identity. The reported zero-dimensional spectral row is excluded.

Tensor-sum spectral projectors imply100 total complex pair dimensions and **14 distinct pair energies** for each chirality. Complete exact energies and multiplicities are stored in the [result](results/scattering-generator-compatibility.json). Selected-doublet isometries and their existing scalar pair-energy compressions are also rechecked.

## Why this excludes the full-state map

If A_c B=B G and B is injective, then p(A_c)=0 gives B p(G)=0, hence p(G)=0. But G contains an eigenvalue -i a(e-b) for each distinct pair energy e. A nonzero affine change preserves14 distinct values, whereas p has only five roots. Contradiction.

This obstruction holds even allowing all548 coefficient coordinates, arbitrary response-column mixing in B, a common energy offset and a freely chosen nonzero rate. Storing the native complement as static provenance does not evolve it correctly and is not a counterexample to this test.

## What remains possible

The existing orbital vertex acts on a selected four-complex-dimensional scalar-energy encounter space and leaves96 native pair coordinates dark under that chosen vertex. That eight-real-dimensional encounter motion is not excluded by this spectrum test: the coefficient low-frequency space has36 real dimensions, enough for four rotation planes after a supplied rate choice. No particular embedding, energy-form preservation, discrete source-action compatibility or physical clock is established by that observation.

Therefore the next useful bridge test is encounter-restricted and source-constrained: require the existing spin/cycle action, metric, scalar/vector projectors and typed vertices to be carried by the same map. A successful match of one frequency is insufficient. The full native complement must remain on its own dynamical branch if no compatible full map is supplied.

The alternative is to keep the two conditional models distinct and use the already available native-pair/orbital scattering construction without claiming it is a realization of Strominger's coefficient law. This finite-source gate does not address an embedding of the orbital continuum, nor does it invalidate the conditional scattering amplitudes already computed there.

## Encounter follow-up

[Selected encounter operation gate](scattering-encounter-operation-gate.md) now constructs the abstract metric embedding but rejects native-cycle transport through the existing target relabellings/free flow. Source channel checks pass; target channel transport stops at that upstream operation mismatch. No new target symmetry or control is inferred from the embedding.

## Execution and limits

```text
uv run --with sympy python research/nima/checkers/check_scattering_generator_compatibility.py
```

Run through structured-command. The first two executions exposed integration defects: a legacy spin receipt has no own source_hashes field (its integrity is pinned by the adapter receipt), and the imported matrix-add function is binary. Both were corrected without changing source laws or the test criterion. The subsequent exact run passed, reporting14 energies for each chirality and the full-state obstruction.

A fresh SCC execution also passed (exit-code adapter; the detailed scientific verdict is in the retained JSON). Reports to Strominger and Voevodsky were admitted under proposal `ep_bd176123-86ef-4d3a-93a0-7efba9e1ccdc`; admission records communication provenance, not truth certification.

This is exact finite algebra with a written polynomial-intertwiner argument, not a new Agda/Rzk kernel proof. It supplies no channel map, calibration, physical scattering explanation or latest strained-model convergence result. Root outcome remains null; no commit/push authorized.
