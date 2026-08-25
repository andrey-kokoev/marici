# Convex flux accessibility-selector audit (WP143)

Owner: `marici.Figueiredo`.

## Bounded question

Can a stable nonlinear sector energy select one oriented, detector-accessible
flux without the non-normalizability obstruction of WP142, and is its selected
integer independently predicted?

Pre-objective process report: excitement `9/10`, confidence `9/10` that convex
energy closes stability/accessibility but relocates the answer into a
coefficient ratio, expected information gain `9/10`. Confounds are the
quadratic source ansatz and lack of a microscopic coefficient derivation.
These reports are non-evidential.

Freeze the full-lattice source

\[
E(n)=\alpha n^2-hn,
\qquad \alpha>0,quad n\in\mathbb Z.
\]

Positive `alpha` makes the finite-temperature sector sum normalizable for
every finite `h`. The continuous minimum lies at

\[
n_*=\frac{h}{2\alpha}.
\]

For `alpha=1,h=8`, the neighboring energies are

\[
E(3)=-15,qquad E(4)=-16,qquad E(5)=-15.
\]

Thus the unique integer ground sector is `n=4`. WP140 maps it to threshold
`1/2`, below reach `3/4`. This is the first stable source architecture in the
flux branch that simultaneously selects orientation and an accessible scale.

The selection is robust rather than isolated. Sector `4` remains the unique
integer minimum throughout

\[
7\alpha<h<9\alpha;
\]

the exact perturbation `h=15/2` stays inside that interval.

## Authority attack

The numerical sector has not been explained. It is encoded directly in
`h/(2alpha)=4`. The equally stable source `(alpha,h)=(1,2)` selects `n=1`
instead and returns WP142's inaccessible threshold. Both descend, are
normalizable, and obey the same source grammar.

A topological construction might write `h=2alpha N`, but then the desired
integer is carried by the new boundary label `N`. Unless a separate theorem or
preparation law fixes `N`, this is transport of sector authority rather than
its derivation. Choosing the coefficient interval after inspecting detector
reach is target fitting.

Classification: **conditional stable accessible-sector selector; numerical
sector encoded in an unsourced coefficient ratio**. It is a selector, not a
rigidifier, and it needs no reference port for descent. The detector comparison
still defines a relational experiment, and no executable multi-point
instrument is supplied.

The smallest authority falsifier is the stable pair `h=8,2`, selecting
accessible `n=4` and inaccessible `n=1`. The remaining gate is a microscopic
source relation fixing `h/alpha` independently of threshold and flavor data,
followed by WP133-style open-rival instrument verification.

Post-objective process report: excitement `9/10`, confidence `10/10`, realized
information gain `10/10`. Raw delta: one stable accessible sector is selected;
the selection persists on an open coefficient interval; one stable hostile
coefficient packet selects a different sector; twelve of twelve checks pass;
the numerical coefficient authority and physical instrument remain absent.
These reports are non-evidential.
