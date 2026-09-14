# Symmetry descent and complementary observers programme v4

## Version relation

Version 4 supersedes `symmetry-descent-and-complementary-observers-programme-v3.md` without rewriting it. It integrates the information-preserving factorization architecture, its quotient/source/product reconstruction theorems, and the five-extension portability cycle.

## Question

Does the symmetry-descent programme define a portable reconstruction calculus across nonunitary presentation changes, multiplicity-valued radial channels, rigged boundary ladders, unbounded half-line geometry, and basis-independent sewing moduli?

## Claim boundary

The answer is affirmative for Hilbert and graph Hilbert observers, boundedly invertible graph-rung comparisons, bounded operator-valued half-line multipliers, finite sewing graphs with declared edge weights, and rigged ladders whose continuity data are supplied. The programme does not yet cover general Banach sources, unbounded multiplier fields, arbitrary nonlocal reciprocal commutants, graph-uniform moduli constants, or a sector-derived physical product metric. RH remains peripheral.

## Hard core v4

1. Symmetry transfer is typed as restriction, comparison, quotient descent, lift, or gauge quotient.
2. Reconstruction objective is typed as quotient, source, or source--moduli product.
3. Coherent descent determines which distinctions are erased; it supplies no lower margin by itself.
4. A descended channel controls quotient directions.
5. An essential observer controls required infinite-dimensional vertical directions modulo compact error.
6. A finite channel may repair only the exact finite residual kernel.
7. A moduli observer acts on a separately constructed relational quotient.
8. Graph, ambient, test, and dual rungs have different adjoints or transposes.
9. Green, Real, reciprocal, and gauge covariance are independent of coercivity.
10. Numerical stability is metric-dependent and degrades under nonunitary comparison.

## Four-role factorization architecture

The observation context is

\[
\mathfrak X=(X,V,p,Y,\mathcal G,M).
\]

The four roles are:

1. coherent descent \(p:X\to Y\);
2. essential vertical observer \(D\);
3. finite-defect repair \(K\);
4. relational-moduli observer \(\Psi:M\to R\).

Authority:

`research/voevodsky/information-preserving-factorization-system-v1.md`

The term “factorization system” denotes this typed observation architecture, not an orthogonal or Quillen factorization system.

## Master source-reconstruction theorem

For closed \(V\subseteq X\), suppose

\[
\|Bpx\|\ge a\operatorname{dist}(x,V)
\]

and

\[
\|Ev\|\ge d\|v\|
\quad(v\in V).
\]

Then

\[
T=(Bp,E)^\top
\]

is bounded below. One explicit constant is

\[
\delta_X=
\frac{d}{\sqrt{1+((d+\|E\|)/a)^2}}.
\]

If \(E=(D,K)^\top\), positive invertible Calkin Gramian for \(D|_V\) leaves finite kernel, and injectivity of \(K\) on that kernel completes source reconstruction. When \(K|_V\) is compact, it cannot supply the essential margin.

Authority:

`research/voevodsky/quotient_vertical_and_finite_repair_observers_form_a_stable_block_row_20260910.md`

## Product bulk--moduli theorem

For the explicit product metric, a source observer with lower constant \(\delta_X\) and a moduli observer with lower-Lipschitz constant \(\delta_M\) combine with

\[
\delta_\times=\min(\delta_X,\delta_M).
\]

A Lipschitz mixed perturbation of size \(\rho<\delta_\times\) leaves margin \(\delta_\times-\rho\).

Authority:

`research/voevodsky/product_bulk_and_holonomy_moduli_observers_are_stable_in_the_explicit_product_metric_20260910.md`

## Extension 1: boundedly invertible comparison

For \(C:X\to X'\) boundedly invertible and \(T'=TC^{-1}\),

\[
\frac{\delta}{\|C\|}\|x'\|
\le
\|T'x'\|
\le
L\|C^{-1}\|\|x'\|.
\]

Thus observer condition number grows by at most

\[
\kappa(C)=\|C\|\|C^{-1}\|.
\]

Gramian and Calkin margins transport by congruence. Compactness, closed range, kernel dimension, and finite repair transport exactly. The whole typed package must transport:

\[
(X,V,p,J,R,T)
\mapsto
(X',C(V),pC^{-1},C^{-*}JC^{-1},CRC^{-1},TC^{-1}).
\]

Compatibility with independently fixed target Green or Real structures remains a separate cell.

Authority:

`research/voevodsky/boundedly_invertible_comparisons_transport_observer_margins_with_condition_number_loss_20260910.md`

## Extension 2: multiplicity-valued reciprocal observers

On the doubled radial carrier with multiplicity space \(K\), all reciprocal-even and reciprocal-odd operator-valued block multipliers are

\[
\mathcal M_+(A,C)=
\begin{pmatrix}A&C\\u^2C&A\end{pmatrix},
\qquad
\mathcal M_-(A,C)=
\begin{pmatrix}A&C\\-u^2C&-A\end{pmatrix}.
\]

For conjugation \(\kappa\) on \(K\), fixed-fiber Real covariance requires

\[
A=\kappa A\kappa,
\qquad
\kappa C\kappa=u^2C.
\]

Since

\[
\mathcal M_-=
\operatorname{diag}(I,-I)\mathcal M_+,
\]

the parity families have equal ungraded Gramians but opposite reciprocal variance. This is a full classification inside the multiplication algebra, not inside the full nonlocal commutant.

Authority:

`research/voevodsky/multiplicity_valued_reciprocal_and_real_bulk_multipliers_admit_full_block_classification_20260910.md`

## Extension 3: rigged-dual boundary ladder

The declared ladder is

\[
\Phi_D\hookrightarrow\mathcal E_D\hookrightarrow H
\hookrightarrow\mathcal E_D'\hookrightarrow\Phi_D'.
\]

Four constructors remain distinct:

- test trace \(\gamma:\Phi_D\to B\);
- transpose \(\gamma':B'\to\Phi_D'\);
- graph adjoint \(\gamma_D^{*D}:B_H\to\mathcal E_D\);
- ambient adjoint \(\gamma_H^*\), only when ambient boundedness holds.

When a graph-Hilbert trace exists,

\[
\gamma_D'R_B=R_D\gamma_D^{*D}.
\]

Ambient-unbounded traces and boundary distributions have no Hilbert Calkin class. A finite-dimensional graph trace has finite-rank Gramian and zero graph Calkin class.

Authority:

`research/voevodsky/rigged_dual_boundary_rows_require_transposes_not_ambient_adjoints_or_calkin_classes_20260910.md`

Contract:

`research/voevodsky/contracts/rigged-boundary-constructor-ladder.v1.json`

## Extension 4: exact half-line criterion

For bounded weakly measurable

\[
W:(0,\infty)\to B(K),
\]

the observer

\[
f\longmapsto(f',Wf)
\]

is bounded below on \(H^1(0,\infty;K)\) if and only if there are \(\ell,\beta>0\) such that every interval \(I\) of length \(\ell\) satisfies

\[
\int_IW(r)^*W(r)\,dr\ge\beta I_K.
\]

Necessity follows from sine packets and permits

\[
\beta=
\frac{\delta^2\ell}{2}-\frac{\pi^2}{2\ell}>0
\]

when \(\ell>\pi/\delta\). Sufficiency follows from dimension-independent Bochner variation control. This upgrades the earlier scalar sufficient condition to an exact scalar and multiplicity-valued characterization.

Authority:

`research/voevodsky/uniform_local_mass_exactly_characterizes_bounded_multiplier_completion_of_half_line_derivative_observation_20260911.md`

## Extension 5: basis-independent sewing moduli

The weighted edge chord metric descends through compact vertex gauge:

\[
d_\Gamma([z],[z'])
=
\inf_{g\in\mathbb T^V}d_E(z,g\cdot z').
\]

It is independent of edge orientation and cycle-basis presentation once positive edge weights are declared. All-simple-cycle Wilson characters separate gauge orbits. Their real and imaginary quadratures give a finite redundant Real-graded embedding with graph-dependent constants

\[
\alpha_\Gamma d_\Gamma(m,m')
\le
\|\Psi_\Gamma(m)-\Psi_\Gamma(m')\|
\le
L_\Gamma d_\Gamma(m,m').
\]

The product bulk--moduli margin is therefore

\[
\min(\delta_X,\alpha_\Gamma).
\]

Authority:

`research/voevodsky/edge_torus_quotient_gives_a_basis_independent_metric_and_all_cycle_observer_for_sewing_moduli_20260911.md`

## Green--Real radial worked example

The principal coherence data remain

\[
C_uF^2=W_uC_u,
\qquad
W_u^*J_\partial W_u=-J_\partial,
\qquad
J_u=\operatorname{diag}(1,u^2)K.
\]

The completed observer architecture is now:

\[
\mathcal O_{\mathrm{rad}}(x,m)
=
\bigl(Bpx,Dx,Kx,\Psi_\Gamma(m)\bigr).
\]

Here:

- boundary sewing declares the coherent domain and comparison cells;
- \(Bp\) controls descended directions;
- a thick reciprocal/Real block multiplier \(D\) controls essential vertical bulk directions;
- compact analytic \(K\) repairs only the exact finite kernel;
- \(\Psi_\Gamma\) observes gauge-invariant sewing holonomy;
- nonunitary comparison transports all components with condition-number loss;
- rigged boundary distributions remain outside the bulk Gramian.

## Verification inventory

### Prior-cycle closure

- constructor roles: 14 checks, four hostile residuals;
- Green--Real radial identities: 10 checks, three hostile residuals;
- reconstruction/product observer: 16 checks, five omission witnesses.

### Extension-cycle checks

- multiplicity block covariance: 15 checks, five hostile residuals;
- nonunitary condition numbers: 17 checks, six hostile residuals;
- rigged-ladder contract: eight rungs, nine constructors, six forbidden promotions; structural validation passed;
- half-line interval thickness: 12 checks, five deliberate failures;
- finite graph quotient/Wilson shadow: 14 checks on 16 gauge orbits, five hostile failures.

Finite and discrete checkers test exact representative models and deliberate failures. They do not replace the infinite-dimensional or continuous proofs.

## Constructor-role consequences

The integrated calculus now rejects these promotions before scalar comparison:

1. quotient reconstruction to source reconstruction without vertical control;
2. unitary or invertible comparison to observer margin;
3. covariance to coercivity;
4. transpose to graph or ambient adjoint without Riesz and boundedness data;
5. boundary distribution to Hilbert Calkin class;
6. operator-norm local mass to weak-operator thickness;
7. cycle-coordinate metric to basis-independent moduli metric;
8. finite gauge shadow to continuous-torus theorem;
9. redundant all-cycle observations to increased moduli dimension.

## Surviving theorem

For the declared Hilbert or graph-Hilbert source and finite sewing graph, stable product reconstruction consists of:

1. quotient lower control;
2. essential vertical Calkin margin;
3. injective finite repair on the exact residual kernel;
4. basis-independent stable moduli observation;
5. coherent Green, Real, reciprocal, gauge, and metric-rung comparison cells.

Under boundedly invertible comparison, existence of this structure is invariant and its numerical constants change by explicit norm bounds. In the half-line multiplier realization, essential bulk stability is exactly equivalent to fixed-scale uniform weak-operator local mass.

## Remaining fronts

1. Extend the interval characterization to unbounded or form-bounded weights.
2. Classify nonlocal operators in the full reciprocal commutant and determine which admit local-mass analogues.
3. Quantify \(\alpha_\Gamma\) from graph combinatorics and edge weights.
4. Construct sector-derived product metrics rather than merely declared ones.
5. Test rigged-ladder continuity in a concrete distributional radial model.
6. Formalize stable reconstruction and forbidden promotions in Lean after theorem statements are frozen.

## Disposition

Version 4 establishes portability across all five selected extensions at their stated scope. Symmetry descent remains the conceptual spine; complementary observation supplies the operational lower bounds; constructor-role typing prevents cross-rung and cross-objective promotion; and Green--Real radial sewing remains the worked example. The programme is now an integrated reconstruction calculus rather than a collection of analogies. Fresh full-suite execution and a closure packet remain before this cycle is closed.
