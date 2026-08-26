# Coexistence fluctuation completion (WP358)

## Bounded question

WP357 found distinct normalized sextic source packets with the same classical
jump. Does the largest immediately source-derived complementary probe—the
broken-vacuum curvature—remove that ambiguity, and if so does identification
become selection?

On the coexistence surface,

\[
q=-\frac{3u}{4w},
\qquad
\kappa=V''(t_\star)=\frac{3u^2}{4w}=-uq.
\]

The pair \((q,\kappa)\) has response Jacobian

\[
\det\frac{\partial(q,\kappa)}{\partial(u,w)}
=-\frac{9u^2}{16w^3},
\]

which is nonzero for the admitted domain \(u<0,w>0\). Exact inversion gives

\[
u=-\frac{\kappa}{q},
\qquad
w=\frac{3\kappa}{4q^2},
\qquad
r=\frac{\kappa}{4}.
\]

Thus the classical jump plus a calibrated fluctuation scale is faithful on
the two-dimensional coexistence source family.

## Hostile pair and first nonfaithful arrow

The WP357 packets \((1,-4,3)\) and \((2,-8,6)\) share \(q=1\), but their
curvatures are respectively 4 and 8. The jump-only projection erases the
common action-scale direction; curvature restores it.

This completion is physical only after the kinetic normalization of \(t\) is
fixed. Under a field rescaling, a raw coordinate Hessian is not an invariant
mass. The admitted instrument must measure a pole mass or calibrated response
in the same source/readout frame, including wave-function normalization and
threshold corrections.

## Disposition

The complementary probe changes source identification, not flavor selection.
Every positive pair \((q,\kappa)\) reconstructs a coexistence packet, so the
probe family does not privilege a proper subfamily or a numerical point. It is
jointly faithful on the declared coexistence grammar and still neither a
numerical selector nor a full `physical16` selector.

The smallest exact falsifier of jump-only faithfulness is the two WP357 source
packets with common \(q=1\). The smallest instrument falsifier is an unfixed
kinetic normalization, under which the proposed curvature is coordinate data
rather than a calibrated physical mass.

Run `uv run --with sympy python
research/flavor/checkers/wp358_coexistence_fluctuation_completion.py` to
regenerate the result.
