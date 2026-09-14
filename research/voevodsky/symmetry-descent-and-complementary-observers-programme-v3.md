# Symmetry descent and complementary observers programme v3

## Version relation

This version supersedes `symmetry-descent-and-complementary-observers-programme-v2.md` without rewriting it. Version 3 incorporates the closed-operator, graph-metric, non-arithmetic transfer, bulk-observer, and executable-checker cycle.

## Question

Can enriched symmetry comparisons and stable observer factorizations be specified and checked on both Hilbert and graph-domain rungs without confusing boundary coherence with bulk observability?

## Claim boundary

The programme now has exact Hilbert and graph-domain observer theorems, an enriched Green--Real comparison groupoid, constructive finite-interval and half-line examples, a machine-readable constructor-role contract, and two passing checkers. It does not yet classify all coercive half-line weights, extend the theory to general Banach or rigged-dual categories, or construct a physical realization of the abstract observers.

## Hard core v3

1. Symmetry transfer is typed as restriction, comparison, genuine quotient descent, ordinary lift, or projective lift.
2. Stable observation is a lower-Gramian condition on a declared metric rung.
3. The complementary observer supplies the essential Calkin margin; compact channels repair only finite-dimensional defects.
4. Boundary conditions, boundary traces, coherence mates, and bulk observers have independent constructor roles.
5. Green and differential orientation signs are compositional degrees.
6. Real, reciprocal, and phase-gauge cells must be checked separately from observer coercivity.
7. Graph and ambient adjoints differ by the graph metric operator.
8. Infinite-domain stability requires a bulk confinement or thickness mechanism not implied by sewing.

## Enriched category established

A Green--Real boundary object is

\[
(H,\mathcal E,D,B,\gamma,J_B,\Lambda,J_H).
\]

Unitary comparison morphisms carry differential and Green degrees

\[
(\sigma,\varepsilon)\in\{\pm1\}^2.
\]

Under the normalized Green identity,

\[
\sigma=\varepsilon.
\]

The phase gauges are degree \((+,+)\); reciprocal swaps are degree \((-,-)\). Observer Gramians and their Calkin classes transport by unitary conjugation.

## Graph-domain observer theorem

For closed \(D\), the domain \(\mathcal E_D\) is Hilbert under

\[
\|x\|_D^2=\|x\|^2+\|Dx\|^2.
\]

Every graph-continuous observer is bounded on this rung. For graph-bounded \(A,Q\), stability is

\[
A^{*D}A+Q^{*D}Q\ge\delta^2I_{\mathcal E_D}.
\]

If \(A\) is graph-compact, then

\[
q_D(A^{*D}A+Q^{*D}Q)=q_D(Q^{*D}Q).
\]

Finite-dimensional boundary traces are finite rank and cannot provide the essential graph margin.

## Metric-rung correction

For the inclusion

\[
i:\mathcal E_D\hookrightarrow H,
\]

we have

\[
i^*=(I+D^*D)^{-1}.
\]

If \(U:V\to\mathcal E_D\) and \(\bar U=iU\), then

\[
\bar U^*=U^{*D}(I+D^*D)^{-1}.
\]

Graph and ambient transpose--adjoint squares are separately Real-compatible but cannot be identified across metrics.

## Non-arithmetic transfer established

On \(H^1(0,L)\),

\[
f\mapsto(f',f(0))
\]

is bounded below by an endpoint Poincare estimate. On \(H^1(0,\infty)\), broad packets produce an essential approximate kernel.

A bounded weight repairs the half-line if it has either:

- a pointwise tail lower bound; or
- uniform local mass

  \[
  \int_I|w|^2\ge\beta
  \]

  on every interval of one fixed length.

Then derivative plus weighted bulk observation is graph-coercive. Weight-poor intervals of unbounded length reproduce the broad-packet obstruction.

## Reciprocal and Real bulk classification

Within diagonal multipliers, reciprocal-even and Real covariance force

\[
D_w^+=\operatorname{diag}(M_w,M_w)
\]

with real \(w\). Reciprocal-odd covariance gives

\[
D_w^-=\operatorname{diag}(M_w,-M_w).
\]

The two have identical ungraded lower modulus but different symmetry variance. A thick even multiplier is the canonical essential bulk complement for the worked example.

## Phase layer retained

Isolated wall phases are gauge-equivalent. Sewing-network phases modulo vertex gauge are classified by

\[
H^1(\Gamma;U(1)).
\]

Cycle holonomy is finite relational information. Its Real-even and Real-odd quadratures give exact stable reconstruction of each oriented \(U(1)\) phase, but this finite-dimensional observer does not supply an infinite-carrier essential margin.

## Constructor-role contract

Machine-readable role authority is now materialized at

`research/voevodsky/contracts/constructor-role-calculus.v1.json`.

It declares 16 roles, eight signature fields, substitution order, admitted compositions, forbidden promotions, and deliberate failures.

The first-failure rule is:

1. source and target;
2. arity and variance;
3. support and labels;
4. required cells;
5. numeric equality.

## Verification

### Constructor-role checker

`research/voevodsky/checkers/check_constructor_role_calculus.py`

Result:

`research/voevodsky/results/constructor_role_calculus.json`

Status: 14 checks pass; four deliberate failures have nonzero residuals.

### Green--Real radial checker

`research/voevodsky/checkers/check_green_real_radial_comparisons.py`

Result:

`research/voevodsky/results/green_real_radial_comparisons.json`

Status: 10 exact symbolic identities pass; three deliberate failures have nonzero residuals.

The checker cycle corrected two test defects: incomplete symbolic conjugation substitution and an invalid claim that a wrong phase power fails involutivity rather than wall preservation.

## Principal worked-example status

Constructed and checked:

\[
C_uF^2=W_uC_u,
\]

\[
W_u^*J_\partial W_u=-J_\partial,
\]

\[
J_u=\operatorname{diag}(1,u^2)K,
\qquad
J_uW_u=W_uJ_u,
\]

phase-gauge naturality, two-sewing holonomy, graph/ambient metric separation, and reciprocal-even thick bulk complements.

The worked example now distinguishes:

- conservative domain sewing;
- finite boundary readout;
- finite relational phase reconstruction;
- essential bulk observation;
- compact analytic finite-defect repair.

## Surviving conjecture

For enriched Green--Real systems, stable joint reconstruction should be equivalent to:

1. an essential observer with positive Calkin Gramian on the declared graph rung;
2. compact analytic injectivity on its finite residual kernel;
3. compatible graded symmetry and Real cells;
4. separate finite relational observers for gauge-holonomy moduli not represented in the bulk Gramian.

Items 1 and 2 are proved in Hilbert graph spaces. Item 3 is proved for unitary comparisons and the radial multiplier family. Item 4 is constructed for finite \(U(1)\) sewing graphs but not yet integrated into a general moduli-observer theorem.

## Remaining rivals

1. **Banach transfer:** Hilbert Gramian arguments extend without replacement to Banach graph spaces.
2. **Rigged-dual transfer:** distributional boundary rows admit the same Calkin classification.
3. **Thickness completeness:** uniform local weight mass is necessary, not only sufficient.
4. **Nonunitary comparison invariance:** Fredholm and observer margins survive arbitrary bounded enriched comparisons.
5. **Moduli/bulk unification:** one observer Gramian naturally combines finite holonomy moduli and infinite bulk states without choosing a product metric.

None is established.

## Next executable frontier

1. Formulate the product observer on bulk graph states and finite holonomy moduli with an explicit product metric.
2. Determine stability under nonunitary but boundedly invertible enriched comparisons, tracking condition numbers.
3. Test a vector-valued or matrix-valued weight where reciprocal symmetry acts nontrivially on multiplicity space.
4. State a rigged-dual boundary theorem without assigning Calkin classes to unbounded traces.
5. Compare uniform local mass with sharper one-dimensional coercivity criteria.

## Disposition

Version 3 completes the first two programme cycles: bounded and graph-domain observer theory, followed by enriched Green--Real realization and executable role checking. The conceptual spine now separates genuine quotient descent from subgroup restriction and gauge quotient; the operational theorem separates essential bulk margin from finite repair; the error language is machine-readable; and the worked example has both exact coherence and explicit stable complements. The remaining work concerns product moduli/bulk observers, nonunitary comparison bounds, and extension beyond Hilbert graph spaces.
