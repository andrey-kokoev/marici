# Cosmology tau-lift constructor SCC audit

## Question

Does coning Benincasa's gradient-pivot normal-adapter Čech class against the ordered blow-up exceptional face currently construct the primitive integral column \((1,1)^T\) in rows \((\Xi_{\log},-\sigma_{123})\)?

## Claim boundary

This packet audits the exact constructor signature isolated in `research/nima/cosmology-tau-lift-prior-art-audit.md`. It does not construct the comparison map, a tau-p lift, a contour, a period, or an optical realization.

## Source pullback

Benincasa's source family supplies three gradient-pivot charts, pairwise Cartan primitives, and second-covariant Čech descent. The target blow-up supplies only the exceptional face column

\[
e_{\rm face}=(0,1)^T.
\]

The desired total lift requires

\[
e_{\rm total}=(1,1)^T.
\]

These packets do not yet provide the comparison of covers that transports the source-family Čech class to the ordered target wall, nor the strict transforms of the overlap primitives.

## Hostile audit

1. The face leg alone is linearly independent from the required column over \(\mathbf F_{101}\) and \(\mathbf F_{103}\), hence cannot equal it.
2. An ordinary Laurent Cartan contraction has double residue zero and cannot provide the required \(\Xi_{\log}\) residue one.
3. Raw columns \((s,1)^T\) vary across sampled Rees shears \(s=0,1,2\); a raw coefficient is not an invariant constructor.
4. Nonunit multiples \(k(1,1)^T\), with \(k=2,3\), are not primitive integral columns and cannot replace the required normalization.

## Disposition

The candidate is the strongest exact internal constructor signature, but it is not constructed. Voevodsky's subsequent unit gate and residue comparison sharpen the boundary: after orientation, the residue differential uniquely forces coefficient one, and the residue/Gysin shadow is monic on the one-dimensional \(\Xi_{\log}\) line. Integral normalization is therefore no longer an independent missing choice. The remaining cokernel is the primitive coordinate \((1,0)^T\).

The missing cells are:

- comparison of the gradient-pivot and ordered exceptional covers;
- strict transform of each Cartan overlap primitive;
- Rees-shear invariance of the resulting pre-residue map;
- the full total-square identity.

A further type audit closes the current internal candidate. The gradient-pivot source uses pivots \((a,b,c)\), but the target fixed fiber has coordinates \((a,b)\); the base-dependent \(c\) pivot disappears, leaving two charts and no triple Čech face. Retaining \(c\) in a relative total space restores three charts but introduces a projection-kernel direction. Its base covector \((-1,-1,-1)\) is independent from the \(p\)-normal covector \((1,1,3)\) over both audited fields, so it cannot be identified with the missing \(\Xi_{\log}\) leg.

The current source-domain census is therefore exhausted:

- the gradient-pivot adapter fails fixed-fiber typing;
- a native three-chart fiber cover is unsourced and would still need a unit logarithmic comparison;
- the relative base–fiber route lacks a source section of the invisible residue kernel;
- no Cayley–Menger face cone is sourced on this stratum.

That exhaustion statement is superseded by a newly materialized source candidate in the complete labelled rank-26 relation module. At \((x,y,z)=(3,6,-3)\), where \(p=0\) and total energy is nonzero, a degree-eight finite-cutoff Rees census finds support excess thirteen: seven length-one and six length-two elementary summands. The census agrees for the two unit normals \((1,0,0)\), \((0,1,0)\) and over \(\mathbf F_{101},\mathbf F_{103}\). Their difference is \(p\)-tangent.

The rank-26 route has now been pushed through the normal-derivative quotient at ambient degrees eight and ten. Let \(S\) be the special exact image and \(T\) the span of derivatives along the \(p\)-tangent difference \((1,-1,0)\). Over both \(\mathbf F_{32003}\) and \(\mathbf F_{32009}\), the quotient signatures are:

| degree | rank \(S\) | rank \((S+T)\) | \(T/S\) | normal increment |
|---:|---:|---:|---:|---:|
| 8 | 4276 | 4373 | 97 | 0 |
| 10 | 6298 | 6399 | 101 | 0 |

Thus both unit-normal derivative images are absorbed by \(S+T\) at both tested cutoffs. The thirteen raw \(p\)-supported summands do not produce a surviving normal line there, so no map to the ordered \(\tau_p\) column is applicable.

The same zero normal increment now holds at degrees twelve and fourteen over both primes. The tangent-derived increments are respectively 107 and 113, while both unit-normal increments remain zero. SCC therefore classifies the raw-row adapter as `raw_derivative_absorption_degrees_8_through_14_explicit_rees_connecting_map_open`.

This does not yet close the rank-26 route. The derivative-span calculation has not extracted the seven length-one Rees generators and therefore has not computed their connecting morphisms.

The extraction gate is now instrument-typed. The census streams sparse rows to `sparse_modular_rank_stream.exe`, whose returned payload contains only relation ranks. Neither the engine response nor the persisted census contains pivot transformations, Smith vectors, kernel representatives, or generator coordinates. Consequently the seven generators cannot be reconstructed from the existing receipts: dimensions do not determine representatives. A witness-producing sparse reducer must retain transformations for the special, dual, and triple Rees presentations and emit seven labelled length-one representatives before any connecting map can be evaluated.

The source audit localizes the information loss to `add_pivot` in `research/benincasa/sparse_modular_rank_stream.rs`. Each input row is reduced only as a column-coefficient map; the reducer does not carry a parallel sparse provenance vector indexed by source-row id. When a row reduces to zero, the dependency coefficients are therefore discarded. A suitable witness reducer must reduce pairs `(module_row, provenance_row)`, apply every subtraction and normalization to both components, and retain the provenance component of zero reductions. It should not dump all pivot state: after constructing the special, dual, and triple presentations, it should emit only candidates satisfying the length-one test, with source-row coefficients, labelled module coordinates, annihilation residual, and replay digest. Two-prime agreement must compare the reconstructed labelled supports, not only their count.

The alternative moving-relation/Euler route also lacks a source theorem. Under currently materialized data, both remaining routes are blocked rather than merely unexecuted.

## Reproducibility

- Contract: `research/aspect/contracts/cosmology-tau-lift-constructor-audit.v1.json`
- Checker: `research/aspect/checkers/check_cosmology_tau_lift_constructor_audit.py`
- Result: `research/aspect/results/cosmology_tau_lift_constructor_audit.json`
