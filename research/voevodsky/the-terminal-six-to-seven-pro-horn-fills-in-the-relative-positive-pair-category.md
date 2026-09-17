# The terminal six-to-seven pro-horn fills in the relative positive-pair category

Use objects `(G_+,G_-)` with `G_+,G_- >= 0` and signed readout
`G_+-G_-`, modulo diagonal common rows

\[
(G_+,G_-)\sim(G_++C,G_-+C),\qquad C\succeq0.
\]

At a symmetric crossing the terminal boundary jump is

\[
\Delta T_{\nu,L}=-2P_{\gamma,L},
\qquad 2\Delta T_{I,L}=+2P_{\gamma,L}.
\]

Represent the two opposite boundary contributions by the positive pair

\[
\boxed{(2P_{\gamma,L},2P_{\gamma,L}).}
\]

Its signed readout is zero, exactly the affine clutching identity, and it is a
diagonal common row.  Hence its class is zero for every `L`, and the family
has the constant zero pro-class even though each representative has trace
`4L/pi`.  The divergent mass is retained rather than falsely bounded and is
removed only by the declared relative equivalence.

The construction is source-faithful levelwise because both legs use the unique
positive representative of the atomic evaluation form.  It is dagger
invariant under `gamma <-> -gamma`; admitted successors pull back both legs by
the same map; and translation transports both atoms together.  Thus these
operations descend to the relative quotient.

This resolves the terminal pro-horn **in the relative/pro-Hilbert target**
already required by the eight-leg source-volume analysis.  It does not produce
an ordinary uniformly trace-class positive row, which is impossible by the
uniqueness no-go theorem.  Nor does it prove Weil positivity: a relative
positive pair can have an indefinite signed readout away from this cancelling
terminal jump.

The executable algebraic receipt is
`results/terminal_relative_positive_pair_filler.json`.
