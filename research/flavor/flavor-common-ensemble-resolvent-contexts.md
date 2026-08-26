# Common-ensemble resolvent contexts

## Question

Does WP538's rank-six contextual closure require six distinct source
preparations, or can one common physical correlator dataset support all six
contexts by deterministic postprocessing?

## Exact context family

Let \(A\) and \(B\) be WP538's exact six-state companion pencil. Choose six
normalized Euclidean momentum-squared contexts

\[
z_j\in\{0,1,2,3,4,5\}.
\]

Every node lies away from the six timelike poles. Form the context matrix

\[
R=
\left[
(z_0I-A)^{-1}B\;\;
(z_1I-A)^{-1}B\;\;
\cdots\;\;
(z_5I-A)^{-1}B
\right].
\]

The checker evaluates its determinant as an exact nonzero rational number, so

\[
\operatorname{rank}R=6.
\]

Deleting any one context leaves rank five. Replacing the last node by a second
copy of \(z=4\) also gives rank five exactly. Distinct supported contexts are
therefore necessary.

## One ensemble, not six source laws

WP525 requires four Ward-complete operator channels. On a common set of gauge
configurations, first measure the momentum-resolved correlator data for those
four channels. The six resolvent weights are then deterministic linear
postprocessing kernels. They do not alter the flavon action, the vacuum, or
the source coefficients.

The complete context map is

\[
R^T\otimes I_4.
\]

It has complex rank 24. Separating real and imaginary parts gives WP535's 48
real estimators. Because all weights act on the same configurations, the
cross-context covariance must be retained rather than estimated from six
independent ensembles.

This full-rank transformation is an exact alternative coordinate system for
the six pole ports. It does not create new source directions or select the
WP537 coordinate \(t\).

## Physical authority boundary

The postprocessing operation is executable once the raw renormalized
momentum-resolved correlators exist. It does not require six distinct
preparations. However, the normalized nodes still need a physical
momentum-squared unit, lattice volume, and momentum support fixed
independently of the desired rank.

No existing neutral-\(B_s\) dataset supplies the required four-channel bilocal
correlators with contact subtraction, continuum and finite-volume control,
heavy-quark systematics, threshold matching, and full 48-real covariance.
Thus WP539 simplifies the experiment architecture but does not claim that the
instrument has been realized.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp539_common_ensemble_resolvent_contexts.py

The generated result is
research/flavor/results/wp539_common_ensemble_resolvent_contexts.json.

The reviewed claim and report to marici.Nima were admitted at graph event
ev-000000004866-fdbc90e2-a476-4042-993b-699757022651. Admission records
reviewed provenance and does not certify truth.
