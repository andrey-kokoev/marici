# Fixed-point threshold readout factorization: WP720

## Question

If WP719 supplies an isolated interacting fixed point, does that source object
already fix the low-energy asymmetric portal and its physical readout?

## Typed pipeline

Let the fixed-point portal be

\[
p_*=
\begin{pmatrix}g_{n*}\\g_{m*}\end{pmatrix}.
\]

Relevant deformations introduce dimensionless threshold coordinates \(\rho\).
To first order, the matched low-energy portal is

\[
p_{\mathrm{low}}=p_*+A\rho.
\]

The physical portal contrast is evaluated by

\[
d=\begin{pmatrix}1&-1\end{pmatrix},
\qquad
\Delta_{\mathrm{low}}=dp_*+dA\rho.
\]

Therefore an isolated fixed point selects the low-energy contrast only if

\[
dA=0
\]

or if the same source theory uniquely fixes every threshold coordinate seen by
\(dA\). This is the exact threshold-survival condition.

## Smallest hostile pair

Take a threshold response that shifts only the first portal:

\[
A=
\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The two relevant deformations \(\rho_a=(0,0)\) and \(\rho_b=(1,0)\) begin at
the same fixed point but yield low-energy contrasts differing by one. The
fixed point has selected a source coordinate without selecting its threshold
descendant.

A common-mode threshold response has equal rows and obeys \(dA=0\). It can
change both portals while protecting their contrast. This distinction must be
derived from source representations; it cannot be imposed after inspecting
the desired low-energy answer.

## Instrument factor

After matching, an unlabelled total response

\[
R_{\mathrm{total}}=\begin{pmatrix}1&1\end{pmatrix}
\]

annihilates the contrast direction \((1,-1)^T\). Two independently calibrated,
representation-labelled channels have the ideal response \(R_{\mathrm{lab}}=I_2\)
and preserve it. Algebraic availability of representation labels is not enough;
the physical production, decay, timing, and detector model must retain them.

## Deutschian consequence

The source principle must be stronger than an interacting fixed point. It must
select an entire trajectory through the following data:

1. an anomaly-free representation packet fixing Clebsches and beta functions;
2. an isolated interacting fixed point with the required attractive basin;
3. a source-normalized relevant deformation fixing dimensionless mass ratios;
4. threshold matching satisfying \(dA=0\) or using those fixed ratios; and
5. two calibrated, incidence-preserving representation channels.

Only this composed object makes the low-energy portal hard to vary. Changing
the sign, magnitude, threshold value, or readout would then require changing
the source representation, fixed point, relevant trajectory, or instrument.

## Claim boundary and disposition

WP720 establishes necessary and sufficient first-order conditions for contrast
survival through affine thresholds and linear readout. It does not construct
the required matter packet or prove nonlinear survival. The next bounded task
is to find a source-fixed relevant ray and compute its threshold Jacobian,
rather than treating the fixed point alone as the selector.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp720_fixed_point_threshold_readout_factorization.py`

Generated result: `results/wp720_fixed_point_threshold_readout_factorization.json`.
