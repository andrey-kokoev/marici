# Phases 1--4 information-preserving factorization closure

## Question

Have the first four phases produced a typed architecture, a source-reconstruction theorem, separate reconstruction objectives, and a stable bulk--moduli product construction with hostile verification?

## Claim boundary

This packet closes only Phases 1--4. It does not claim an orthogonal or Quillen factorization system, a canonical physical product metric, a Banach or rigged-dual extension, or stability under nonunitary comparison. All files remain uncommitted.

## Phase 1: typed architecture

Authority:

`research/voevodsky/information-preserving-factorization-system-v1.md`

Established:

- context \((X,V,p,Y,\mathcal G,M)\);
- quotient, source, and product reconstruction objectives;
- coherent descent;
- relative essential bulk observation;
- finite-defect repair;
- moduli observation;
- admitted compositions and forbidden promotions;
- complete Green--Real radial role assignment.

The phrase “factorization system” is explicitly bounded to an observation-design architecture.

## Phase 2: master source-reconstruction theorem

Authority:

`research/voevodsky/quotient_vertical_and_finite_repair_observers_form_a_stable_block_row_20260910.md`

For closed \(V\subseteq X\), quotient control

\[
\|Bpx\|\ge a\operatorname{dist}(x,V)
\]

and vertical control

\[
\|Ev\|\ge d\|v\|
\]

imply that \((Bp,E)^\top\) is bounded below. One proved constant is

\[
\delta_X=
\frac{d}{\sqrt{1+((d+\|E\|)/a)^2}}.
\]

No block-diagonal observer hypothesis is used. If \(E=(D,K)^\top\), a positive invertible vertical Calkin Gramian for \(D\) leaves finite defect, and injectivity of \(K\) on that exact defect completes the lower bound. With compact \(K|_V\), the Calkin converse forces essential vertical margin to come from \(D\).

## Phase 3: objective typing

Authority:

`research/voevodsky/contracts/reconstruction-objectives.v1.json`

Established types:

- `reconstruct_quotient`;
- `reconstruct_source`;
- `reconstruct_product`.

A quotient result promotes to source reconstruction only through vertical essential observation, finite repair, and the stable block-row theorem. Source reconstruction promotes to product reconstruction only after a moduli object, moduli metric, stable moduli observer, and product theorem are supplied.

## Phase 4: bulk--moduli product

Authority:

`research/voevodsky/product_bulk_and_holonomy_moduli_observers_are_stable_in_the_explicit_product_metric_20260910.md`

For the declared product metric, independently stable factors with constants \(\delta_X\) and \(\delta_M\) combine with

\[
\delta_\times=\min(\delta_X,\delta_M).
\]

A mixed Lipschitz perturbation with constant \(\rho<\delta_\times\) leaves margin \(\delta_\times-\rho\).

For finite sewing graphs, real and imaginary holonomy quadratures are isometric for the chord product metric, so \(\delta_M=1\). The radial product observer consequently has lower constant \(\min(\delta_X,1)\).

## Constructor-role pullback

The four phases compose only because the interfaces agree:

| Interface | Required agreement |
|---|---|
| descent to quotient theorem | same \(X,V,p\) and quotient metric |
| quotient theorem to vertical observer | same Hilbert or graph metric rung |
| essential observer to finite repair | repair tested on the exact kernel of \(D|_V\) |
| source theorem to product theorem | source lower bound uses the same \(X\)-metric appearing in the product metric |
| sewing quotient to moduli observer | same cycle coordinates and gauge equivalence |
| Real comparison to quadratures | conjugation acts evenly on real and oddly on imaginary coordinates |

Equal dimensions alone would not establish any of these pullbacks.

## Hostile verification inventory

### Constructor roles

Checker:

`research/voevodsky/checkers/check_constructor_role_calculus.py`

Result:

`research/voevodsky/results/constructor_role_calculus.json`

Expected status: 14 gates pass and four deliberate substitutions have nonzero residuals.

### Green--Real comparisons

Checker:

`research/voevodsky/checkers/check_green_real_radial_comparisons.py`

Result:

`research/voevodsky/results/green_real_radial_comparisons.json`

Expected status: 10 identities pass and three deliberate failures have nonzero residuals.

### Reconstruction objectives and product observer

Checker:

`research/voevodsky/checkers/check_reconstruction_objectives_and_product_observer.py`

Result:

`research/voevodsky/results/reconstruction_objectives_and_product_observer.json`

Expected status: 16 checks pass and five omissions are detected.

The finite-model checker does not replace the general proofs. It tests exact representative models, countermodels, and interface gates.

## Defects repaired during the cycle

1. The constructor-role hostile test originally expected the arity gate before the source/target gate; the expected first failure was corrected.
2. Symbolic conjugation of \(1/u\) was incomplete in the first Green--Real checker implementation; an explicit conjugate matrix repaired it.
3. The wrong-phase Real test incorrectly targeted involutivity; it was replaced by the nonzero wall-preservation residual.
4. A control character entered the product-observer packet during formula transport; it was removed and clean text readback passed.
5. SymPy integers initially failed JSON serialization in the reconstruction checker; result fields were converted to strings.
6. The first quotient-omission witness was contaminated by hostile horizontal cross terms; a separate vertical-only omission model repaired the test.

No defect was reclassified as a scientific residual.

## Residuals and next boundary

Phases 1--4 leave five explicit research fronts:

1. condition-number transport under boundedly invertible nonunitary comparisons;
2. multiplicity-valued reciprocal and Real bulk weights;
3. rigged-dual boundary typing without invalid Calkin classes;
4. sharper necessity criteria for half-line weight coercivity;
5. basis-independent quantitative metrics on sewing moduli.

These belong to later phases and are not required for the Phase 1--4 closure.

## Disposition

Phases 1--4 are complete at their declared strength. The architecture is typed, the source block-row theorem is proved, reconstruction objectives are separated, the product bulk--moduli theorem is proved in an explicit metric, and hostile executable models cover the main forbidden promotions. Fresh closure passed: 14 constructor-role gates, 10 Green--Real identities with three nonzero hostile residuals, and 16 reconstruction/product checks with five omission witnesses.
