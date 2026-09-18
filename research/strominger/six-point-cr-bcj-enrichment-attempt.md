# Six-point source-derived CR-to-BCJ enrichment attempt

## Disposition

**Obstructed at six points.** The current source constructs the ordering-level BCJ quotient, but it does not lift that quotient to Jacobi numerator vectors on Coherent Resolution generators. The first chain-level defect has rank four.

## Candidate target and map

Let `V_DDM` be the 24-dimensional six-point DDM ordering module and `B6` its rank-18 fundamental-BCJ relation space. The exact sourced target

\[
Q_6=V_{\rm DDM}/B_6,
\qquad \dim Q_6=6,
\]

has the canonical quotient map `q`. This is a valid degree-zero/evaluated ordering map.

The worldsheet and inverse-pairing data can choose amplitude-level master coefficient representatives. They do not assign a numerator to every cubic graph over every CR generator, fix generalized gauge, or prove the kinematic Jacobi relations generatorwise. Consequently these representatives do not define maps `F_k` satisfying

\[
d_{\rm BCJ}F_k=F_{k-1}d_{\rm CR}.
\]

## Exact obstruction

All 24 fundamental BCJ combinations vanish after canonical-form evaluation. None vanishes as a raw CR chain, and none vanishes after Parke–Taylor dressing.

For permutation `(2,3,4,5)`, the first raw residual is

\[
\frac{17472}{5}[12345]
+\frac{6272}{5}[12356]
-\frac{6776}{5}[23456]
-\frac{16156}{5}[12456]
-1148[12346].
\]

Its Parke–Taylor-dressed residual is also nonzero:

\[
\frac{1113}{10}[12345]
+\frac{371}{5}[12356]
-\frac{1113}{20}[23456]
-\frac{392}{5}[12456]
-\frac{287}{20}[12346].
\]

Thus evaluation kills data that remain nonzero in the proposed chain carrier.

## Ranks, kernels, and repair

The exact ranks are:

| datum | rank/dimension |
|---|---:|
| DDM ordering module | 24 |
| BCJ relation space | 18 |
| quotient `Q6` | 6 |
| fundamental-BCJ CR top-chain span | 4 |
| residue-defect span | 4 |
| corrected-cycle span | 4 |

A minimal free mapping cone adds four degree-four defect lifts and four degree-five null-homotopies. This yields `H4=0` and formally kills all 24 relations.

However, **zero** of those eight added generators is forced by cubic-graph/Jacobi source data. They are selected as linear-algebraic bases of the defect and cycle spans. Therefore the repaired complex is an exact formal target, not a derived BCJ bridge.

## First missing datum

A successful construction must provide a source-derived assignment

\[
\text{CR generator}\longmapsto
\{n_g\}_{\text{cubic graphs}}
\]

such that:

1. every color Jacobi triple has the matching kinematic Jacobi identity;
2. generalized gauge is fixed or quotiented explicitly;
3. boundary images of the four independent defect directions are specified;
4. the resulting `F_k` commute with differentials;
5. all 24 fundamental combinations vanish before evaluation.

Because this first arrow fails, a second copy, state pairing, `Pi_grav`, and epsilon-soft/Bondi tests are not activated. No claim is made beyond six points.

## Verification

- `research/strominger/checkers/six_point_cr_bcj_enrichment_attempt.py`
- `research/strominger/results/six_point_cr_bcj_enrichment_attempt.json`
- freshly rerun source checks:
  - `research/nima/checkers/check_six_point_nmhv_bcj_chain_relation.py`
  - `research/nima/checkers/check_six_point_minimal_bcj_chain_repair.py`
