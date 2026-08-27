# Protected threshold-port no-go: WP671

## Kinematic obstruction

For protected partners \(A,B\) and triplet excitation \(n\), define the two
directional threshold margins

\[
\Delta_{AB}=M_A-M_B-m_n,
\qquad
\Delta_{BA}=M_B-M_A-m_n.
\]

They satisfy

\[
\Delta_{AB}+\Delta_{BA}=-2m_n<0.
\]

Hence both reciprocal decays cannot be on shell in one positive-mass
experiment. The two formal vertices of WP670 do not automatically create two
directional width ports; only the heavier partner can decay to the lighter.

## Rank-one ordinary width

In the massless-daughter, unpolarized limit, the open total width is
proportional to

\[
W=y^2+z^2.
\]

Its Jacobian with respect to \((y,z)\) has rank one. The hostile vertex pairs

\[
(y,z)=(1,2),
\qquad
(y,z)=(11/5,2/5)
\]

both give \(W=5\), but their loop-erosion coordinates \(y^4+z^4\) are 17 and
\(14657/625\). Thus even an exact ordinary width does not determine the RG
backreaction.

## Minimal informational repair

Two separately calibrated chiral coordinates \((y^2,z^2)\) have response rank
two. They cannot be supplied by mutually opposite on-shell decays. A repair
requires a source-derived polarization or angular analyzer in the one open
channel, including its transfer function, acceptance, and covariance.

## Disposition

WP652's abstract two-width logic does not instantiate directly in the
protected pair. The remaining gate is a polarization-resolved physical
instrument, not another fitted scalar or a formal second pole coordinate.
Such an instrument would identify constructor magnitudes; it would not select
their values or a flavor point.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp671_protected_threshold_port_no_go.py

Generated result: results/wp671_protected_threshold_port_no_go.json.
