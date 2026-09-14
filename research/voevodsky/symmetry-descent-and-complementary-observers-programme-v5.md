# Symmetry descent and complementary observers programme v5

## Version relation

Version 5 supersedes programme v4 without rewriting it. It integrates the third cycle: graph-bounded unbounded weights, the full nonlocal reciprocal commutant, explicit Wilson constants, conditional physical metrics, a concrete rigged-radial model, and frozen Lean targets.

## Question

Which parts of the reconstruction calculus remain valid beyond bounded local multipliers and abstract boundary ladders, and where do physical calibration and formal verification introduce genuine authority boundaries?

## Claim boundary

The programme now covers pointwise-unbounded multipliers with uniform local upper square mass, arbitrary bounded nonlocal reciprocal operators, explicit finite-graph Wilson bounds, and a concrete doubled half-line rigged model. Physical metric formulas are conditional on a missing calibration packet. Lean statements are frozen but no Lean theorem is claimed checked. General operator-valued form criteria, singular-domain equivalence, graph-uniform constants, and sourced physical calibration remain outside scope.

## Hard core v5

1. Reconstruction objective fixes which distinctions must be recovered.
2. Coherent descent identifies erased vertical directions.
3. Essential observation is a lower-Gramian or Calkin property on a declared Hilbert rung.
4. Finite repair acts only on the exact residual kernel.
5. Relational moduli are observed on a separately constructed gauge quotient.
6. Covariance, locality, coercivity, and physical calibration are independent constructor roles.
7. Changing an operator domain changes the source object.
8. Nonunitary comparison preserves existence but changes numerical margins.
9. Distributional transpose, graph adjoint, and ambient adjoint remain distinct.
10. Formal verification certifies only frozen statements under explicit assumptions and toolchain provenance.

## Unbounded-weight extension

Let \(W:(0,\infty)\to B(K)\) be pointwise finite and weakly measurable. If for some \(\ell>0\),

\[
\sup_{|I|=\ell}\int_I\|W(r)\|^2dr=\Lambda<\infty,
\]

then \(M_W:H^1\to L^2\) is bounded even when \(W\notin L^\infty\). Within this class,

\[
f\mapsto(f',Wf)
\]

is graph-bounded below exactly when

\[
\int_IW(r)^*W(r)dr\ge\beta I_K
\]

uniformly on intervals of one fixed length.

More singular weights define

\[
H^1\cap\operatorname{Dom}M_W.
\]

Coercivity on that intersection is reconstruction on a changed source. The endpoint weight \(1/r\) exhibits the distinction by forcing vanishing trace behavior.

Authority:

`research/voevodsky/unbounded_weights_split_into_graph_bounded_observers_and_domain_changing_closed_rows_20260911.md`

## Full nonlocal reciprocal classification

For \(\mathcal H=H_0\oplus H_0\),

\[
\{W_u\}'\cong B(H_0)\oplus B(H_0).
\]

In channel coordinates, commuting and anticommuting operators retain the block forms

\[
\begin{pmatrix}A&C\\u^2C&A\end{pmatrix},
\qquad
\begin{pmatrix}A&C\\-u^2C&-A\end{pmatrix},
\]

with arbitrary bounded nonlocal \(A,C\). Their ungraded Gramians agree. Stability and essential observation reduce to both parity operators

\[
A+uC,
\qquad
A-uC.
\]

Local-mass criteria apply only to the decomposable multiplier subalgebra. General nonlocal operators require parity-sector Gramians and Calkin classes.

Authority:

`research/voevodsky/the_full_nonlocal_reciprocal_commutant_splits_over_the_two_parity_sectors_20260911.md`

## Explicit Wilson constants

For edge weights \(\lambda_e>0\), define

\[
\Lambda_{\mathrm{cot}}
=
\min_{T\text{ spanning tree}}
\max_{e\notin T}\lambda_e.
\]

Tree gauge identifies chord coordinates with fundamental holonomies and gives

\[
\alpha_\Gamma
\ge
\Lambda_{\mathrm{cot}}^{-1/2}.
\]

The all-cycle upper constant satisfies

\[
L_\Gamma^2
\le
\sum_{c\in\mathscr C(\Gamma)}
\sum_{e\in c}\lambda_e^{-1}.
\]

Thus the stable bulk--moduli margin has the explicit bound

\[
\min(\delta_X,\Lambda_{\mathrm{cot}}^{-1/2}).
\]

A tree is a proof certificate, not a moduli coordinate.

Authority:

`research/voevodsky/spanning_tree_gauge_gives_explicit_combinatorial_bounds_for_wilson_observer_stability_20260911.md`

## Conditional physical metric

A sector-derived metric requires a calibrated record map and positive covariance:

\[
d_{\mathrm{rec}}(z,z')^2
=
\langle\Delta\mathcal R,
\Sigma^{-1}\Delta\mathcal R\rangle.
\]

It is a direct product exactly when response and covariance are block separable. If the normalized cross block has norm \(\eta<1\), the coupled metric is bounded relative to the product metric by factors \(1-\eta\) and \(1+\eta\).

The current radial interface lacks

\[
(\mathcal R,\Sigma,\text{units},
\text{physical quotient},\text{provenance}).
\]

Therefore the algebraic transport formulas are verified, but no numerical physical metric is asserted.

Authority:

`research/voevodsky/sector_derived_product_metrics_are_noise_whitened_readout_metrics_not_arbitrary_direct_sums_20260911.md`

## Concrete rigged-radial model

Use

\[
\Phi=\mathcal S_+^2,
\qquad
\mathcal E=H^1(0,\infty)^2,
\qquad
H=L^2(0,\infty)^2,
\]

and

\[
D=\operatorname{diag}(\partial_r,-\partial_r).
\]

The trace and Green form are

\[
\gamma(f)=(f_+(0),f_-(0)),
\qquad
J_\partial=\operatorname{diag}(-1,1).
\]

The transpose maps boundary coefficients to endpoint deltas in \(\Phi'\). The graph adjoint maps them to the Riesz representative \(e^{-r}\). No bounded ambient \(L^2\) trace exists.

Bulk reciprocal comparison anticommutes with \(D\), fixed-fiber Real comparison commutes with it, and

\[
\Lambda_u=\{(c,uc):c\in\mathbb C\}
\]

is Green-isotropic and invariant under both comparisons. This realizes the full rigged constructor ladder while leaving essential bulk observation to a separate thick multiplier.

Authority:

`research/voevodsky/the_doubled_half_line_derivative_realizes_the_full_rigged_green_real_boundary_ladder_20260911.md`

## Frozen Lean targets

Six statements are frozen:

1. nonunitary lower-bound transport;
2. quotient--vertical block-row stability;
3. finite residual repair;
4. product lower-Lipschitz stability;
5. reciprocal block classification;
6. tree-gauge Wilson lower bound.

Authority:

`research/voevodsky/frozen_lean_formalization_targets_for_information_preserving_reconstruction_20260911.md`

Implementation belongs to `marici.Buzzard`. A typed request has been sent. No standard Lean project marker was found at the four candidate paths inspected, and no Lean theorem is claimed checked.

## Verification added in this cycle

### Unbounded graph multipliers

`research/voevodsky/results/unbounded_graph_multiplier_weights.json`

Status: 14 checks pass; five hostile failures detected.

### Nonlocal commutant and rigged radial model

`research/voevodsky/results/nonlocal_commutant_and_rigged_radial_model.json`

Status: 20 checks pass; six hostile failures detected.

### Weighted graph Wilson bounds

`research/voevodsky/results/weighted_graph_wilson_bounds.json`

Status: nine checks pass; \(\Lambda_{\mathrm{cot}}=9\) for the weighted test graph; five hostile failures detected.

### Conditional noise-whitened metrics

`research/voevodsky/results/noise_whitened_product_metrics.json`

Status: 16 checks pass; six hostile failures detected. This verifies conditional algebra only and preserves the calibration blocker.

## Integrated Green--Real observer

The mathematical reconstruction package is

\[
\mathcal O(x,m)
=
(Bpx,Dx,Kx,\Psi_\Gamma(m)).
\]

Its extensions now admit:

- graph-bounded pointwise-unbounded local \(D\);
- arbitrary bounded nonlocal reciprocal \(D\), tested sectorwise;
- explicit Wilson moduli constants;
- rigged distributional boundary rows outside the Gramian;
- nonunitary transport with condition-number loss.

A physical version additionally requires the missing calibration packet. A formally certified version additionally requires a checked Lean project and theorem.

## Constructor prohibitions added in v5

1. Closed-row coercivity on a proper intersection domain is not observation of the old graph source.
2. Full reciprocal covariance does not imply radial locality.
3. Sector Gramian positivity does not imply a local-mass representation.
4. A spanning tree certificate is not canonical moduli data.
5. An analytic product norm is not a physical metric.
6. Conditional whitening algebra is not calibration evidence.
7. Endpoint delta is not an ambient Hilbert adjoint vector.
8. A frozen Lean target is not a checked theorem.
9. A handoff or graph admission is not formal verification.

## Residual scope

1. Necessary-and-sufficient form criteria beyond uniform local operator-norm upper mass.
2. Coercivity criteria for structured nonlocal kernels.
3. Sharp or graph-family-uniform Wilson constants under bounded geometry hypotheses.
4. Acquisition of a sector-authorized calibration packet.
5. Discovery of the admitted Lean project and completion of F1 by the formalization owner.

## Disposition

Five mathematical fronts are developed and representative hostile checks pass. The physical-metric front stops at a precisely typed missing calibration object. The Lean front stops at owner and toolchain authority after freezing assumption-complete targets and sending a directed request. Programme v5 therefore separates proved mathematical portability, conditional physical transport, and pending formal certification instead of merging their evidence modalities.
