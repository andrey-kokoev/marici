# Critical-to-threshold selector disposition (WP377)

## Question resolved

Does the WP356--WP376 continuation establish a genuine source-generated
selector on the faithful flavor quotient, or only conditional shell selectors
and increasingly faithful source instruments?

The answer is negative at the current authority boundary.

## Admitted state domains

The chain contains three nested conditional domains:

1. stationary vacua of a canonical even scalar source potential;
2. a heavy singlet mediator with finite-width threshold matching and controlled
   mass settings;
3. a nondegenerate local `physical16` chart with fifteen CP-even coordinates
   and signed Jarlskog coordinate \(J\).

The source and flavor quotients remain distinct. The canonical source quotient
is represented by \((Q,M^2)\), or equivalently its reconstructed coexistence
coefficients. The faithful flavor quotient is the full `physical16` tuple, not
\(J\), \(J^2\), or measured ten.

## What genuinely descends

The canonical source quantities

\[
Q=Zq,
\qquad
M^2=\kappa/Z
\]

descend under effective-field reparameterization. The conditional portal

\[
V_{\mathrm{int}}=\lambda(J^2-\alpha Q/M^2)^2
\]

descends under the full weak-basis groupoid because \(J^2\) is a physical
invariant and the source ratio is a singlet. It selects the codimension-one
shell

\[
J^2=\alpha Q/M^2.
\]

This is a genuine selector only conditional on the portal action and its
matching coefficient being source-derived before flavor readout.

## Why numerical selector authority still fails

The portal constraint has rank one. It leaves fifteen CP-even directions and
the CP-conjugate orientation pair. Its magnitude responds to both the source
vacuum and the matching coefficient. Dimensional analysis leaves a free
dimensionless \(\alpha\).

A proposed exchange Ward identity fixes only the relational quotient
\(\alpha/s=1\), where \(s\) is the relative port scale. Unit normalization is
a common-unit presentation unless a microscopic common representation derives
that scale. Positive pairing alone does not do so: every positive \(s\) admits
an invariant positive Gram metric.

Therefore the current operation is:

- a conditional codimension-one selector;
- a shell and port-presentation rigidifier;
- not a numerical selector;
- not a full `physical16` selector;
- not yet independently source-authorized.

The smallest exact physical16 falsifier is a pair of points differing in one
CP-even coordinate but sharing the same \(J\). Both satisfy every portal and
threshold readout. The smallest authority falsifier is the nonzero response of
the selected shell to \(\alpha\).

## What the threshold programme achieved

The mediator continuation is progressive on identification and instrumentation:

- tree matching supplies a causal quartic intervention with deletion and
  decoupling tests;
- the finite-width absorptive channel repairs the dispersive blind point;
- calibrated detector contrast and likelihood give exact faithfulness margins;
- two scan contexts remove fixed differential nuisance;
- three contexts remove one shared common nuisance plus arbitrary differential
  drift;
- the three-setting spacing has a unique source-calibrated D-optimum for every
  positive width ratio.

These operations identify source pole and nuisance coordinates. None reduces
the fifteen-dimensional CP-even flavor fiber or derives \(\alpha\). A faithful
source instrument is not a flavor selector.

## Report for marici.Nima

- Admitted state domain: the conditional canonical scalar, mediator, portal,
  and calibrated threshold-scan grammar described above.
- Faithful quotient coordinate: full `physical16`; source coordinates and
  threshold records are separate upstream quotients.
- Source-authorized probe family: conditionally, canonical vacuum and pole
  responses, invariant portal residual, finite-width dispersive and absorptive
  channels, and predeclared multi-setting scans.
- Contextual partition: threshold scans locally separate their declared source
  and nuisance packet; the flavor portal partitions `physical16` only by
  \(J^2\), leaving fifteen CP-even directions and orientation.
- Classification: conditional selector and rigidifier on a CP shell; threshold
  branch is identifier only; overall neither a numerical nor full
  `physical16` selector.
- Smallest exact falsifier: two `physical16` points with identical \(J\) and a
  different CP-even coordinate; for normalization authority, nonzero shell
  response to \(\alpha\).
- Remaining physical-instrument gate: derive the portal, relative port scale,
  and mediator control from one microscopic source action; realize the
  calibrated finite-width scan; then test the selected numerical shell across
  the complete fitted ensemble without fitting \(\alpha\).

Run `uv run --with sympy python
research/flavor/checkers/wp377_critical_to_threshold_selector_disposition.py`
to verify the dependency chain and exact claim boundary.
