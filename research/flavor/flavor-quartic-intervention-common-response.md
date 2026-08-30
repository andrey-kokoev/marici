# Quartic-intervention common response (WP367)

## Bounded construction

WP359 identifies the canonical source ratio

\[
y=\frac{Q}{M^2}=-\frac1U,
\qquad U<0.
\]

Within the conditional WP361 portal grammar, the equilibrium flavor shell is

\[
x=J^2=\alpha y.
\]

Intervene on the canonical quartic coefficient through

\[
U(\epsilon)=U+h\epsilon,
\qquad h\ne0,
\]

on a neighborhood where \(U+h\epsilon<0\). The two equilibrium responses at
\(\epsilon=0\) are

\[
q=\frac{dy}{d\epsilon}=\frac{h}{U^2},
\qquad
p=\frac{dx}{d\epsilon}=\frac{\alpha h}{U^2}.
\]

Therefore

\[
\frac pq=\alpha.
\]

The intervention strength and background quartic cancel from the relational
response ratio. This supplies the conditional common causal perturbation
required by WP366.

## Deletion and contextual tests

If the portal is deleted while the source intervention remains, \(y\) still
responds but an uncoupled flavor coordinate has \(p=0\). The common response
is therefore a causal fingerprint of the portal rather than a cached readout.

However, all pairs \((U,h)\) with nonzero \(h/U^2\) give the same ratio at
fixed \(\alpha\). The ratio identifies the matching coefficient, not the
complete source packet. Its response Jacobian remains rank one.

Both \(U\) and \(J^2\) are quotient quantities, so the construction descends
under effective-field reparameterization and full flavor weak-basis
equivalence. It still factors through the CP-even coordinate \(J^2\) and
leaves fifteen `physical16` directions plus CP orientation unresolved.

## Instrument boundary

This is a source-side coefficient intervention inside an effective action. It
is not automatically a laboratory control. Experimental admission requires a
physical knob or threshold field whose calibrated displacement implements
\(h\epsilon\), equilibrium preparation or controlled dynamics, and joint
measurement of \(J^2\) and \(Q/M^2\) in one scheme.

The exact result is therefore a conditional causal constructor and response
instrument grammar, not a numerical selector. Its smallest falsifier is
portal deletion: \(q=h/U^2\ne0\) but \(p=0\). Its authority obstruction is
that the response ratio returns the already admitted coefficient \(\alpha\).

Run `uv run --with sympy python
research/flavor/checkers/wp367_quartic_intervention_common_response.py` to
regenerate the exact result.
