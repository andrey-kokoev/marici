# Positive Gaussian mediation has the wrong curvature and a free center

Work package: WP621  
Owner: marici.Figueiredo

## Process and optionality snapshot

Pre-objective activation:

- excitement: 8/10;
- confidence that mediator multiplicity leaves a free source center: 9/10;
- expected information gain: 8/10;
- immediate reason: Gaussian mediation is the most economical proposed
  origin of WP620's rational coefficient ratio;
- confounds: loop signs, non-Gaussian sectors, direct contacts, and constrained
  auxiliary fields.

Frozen optionality space:

- one stable positive-mass mediator;
- an arbitrary finite stable mediator tower;
- zero offsets;
- target-proportional offsets;
- identical mediator replication;
- one hostile common offset deformation;
- one deliberate wrong-sign mass rival;
- ten exact checks declared.

## Bounded question

Can a finite positive Gaussian mediator grammar derive WP620's positive
curvature and target center from masses or representation multiplicities?

## General elimination theorem

Let \(\sigma\) be a finite vector of real mediators with positive mass-squared
matrix \(M^2\). Couple it linearly to the relational coordinate \(z\):

\[
V(\sigma,z)
=
\frac12\sigma^TM^2\sigma
+\sigma^T(gz-J).
\]

Eliminating \(\sigma\) gives

\[
V_{\mathrm{eff}}(z)
=
-\frac12(gz-J)^T(M^2)^{-1}(gz-J).
\]

Since \((M^2)^{-1}\) is positive, the induced quadratic coefficient is

\[
\kappa_{\mathrm{ind}}
=
-\frac12g^T(M^2)^{-1}g
\leq0.
\]

WP620 instead requires \(\kappa>0\). A stable positive Gaussian tower
therefore has the wrong curvature sign. Increasing the number of mediators
makes the negative-semidefinite Gram contribution larger; it does not create
the bounded square.

## The center is transported source data

The stationary coordinate of the induced square is

\[
z_*=
\frac{g^T(M^2)^{-1}J}
{g^T(M^2)^{-1}g}.
\]

It is a maximum before another stabilizing sector is added. With \(J=0\), the
only stationary center is \(z_*=0\). To obtain the WP620 target

\[
z_0=\frac{576}{25},
\]

one may choose \(J_a=z_0g_a\), but this inserts the desired center directly
into the mediator offsets.

Replicating an identical mediator packet multiplies numerator and denominator
by the same multiplicity, leaving \(z_*\) unchanged. Representation count can
fix overall response strength but not the center.

The smallest hostile deformation is

\[
J_a\longmapsto J_a+\delta g_a.
\]

It preserves mediator masses, couplings, and multiplicities while shifting

\[
z_*\longmapsto z_*+\delta.
\]

Thus the center is continuously variable source data.

## Exact finite example

For

\[
g=(1,2,3),
\qquad
M^2=\operatorname{diag}(1,2,3),
\]

the Gram coefficient is six and the induced quadratic coefficient is
\(-3\). Target-proportional offsets reproduce \(576/25\), but only because
that value was placed in every \(J_a/g_a\).

A mediator mass matrix with a negative eigenvalue can reverse the induced
curvature in the deliberate-failure example. That mediator sector is itself
unstable, so it is not an admissible repair.

## Physical criticism

The relevant source-calibrated experiment must resolve:

1. every mediator pole mass;
2. residues determining the couplings \(g_a\);
3. independently calibrated one-point offsets \(J_a\);
4. finite widths and mediator mixing;
5. the WP618 root-vector masses and referenced interference in the same
   source lineage.

These records reconstruct both the induced curvature sign and \(z_*\) before
flavor data are used. A positive reconstructed curvature from a supposedly
tree-level positive Gaussian tower, or an offset center different from the
flavor-inferred target, falsifies the declared architecture.

## Disposition

Finite positive Gaussian mediation is closed as the origin of WP620's bounded
target square. It remains a legitimate relational interaction and
presentation rigidifier, but it supplies negative curvature and transports a
free offset-to-coupling ratio.

A progressive successor requires a source-derived positive direct contact,
loop effect, constrained auxiliary sector, or stable non-Gaussian completion.
Its center must be calculated independently; adding stabilization while
retaining target-proportional offsets only relocates the fitted datum.

## Post-objective process report

- excitement: 9/10;
- confidence in the finite positive-Gaussian theorem: 10/10;
- realized information gain: 9/10;
- immediate reason: the curvature-sign obstruction is stronger than the
  anticipated center-freedom result;
- surviving confounds: loop-induced signs, constrained auxiliaries, and
  non-Gaussian stable completions.

Raw optionality delta:

- every finite stable positive-Gaussian branch is eliminated as the source of
  positive curvature;
- mediator replication is proved neutral on the selected center;
- the center is reconstructed as one continuously movable offset ratio;
- zero-offset mediation selects only zero;
- one deliberate wrong-sign repair is rejected by source instability;
- all ten declared exact checks pass;
- positive non-Gaussian completion and independent center selection remain
  open.

These process ratings are non-evidential.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp621_positive_gaussian_center_migration.py

The generated result is
`research/flavor/results/wp621_positive_gaussian_center_migration.json`.
