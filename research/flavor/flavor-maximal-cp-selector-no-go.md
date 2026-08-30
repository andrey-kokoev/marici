# Coefficient-free maximal CP is an exact but false selector: WP1023

## Question

Can the oriented-volume magnitude be selected without a fitted coefficient by
extremizing the normalized physical invariant (J^2)?

## Admitted quotient

Take the unitary three-generation mixing quotient with nondegenerate quark
spectra. The Jarlskog invariant is

\[
J=c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta.
\]

Its square descends under the full weak-basis group and does not distinguish
the two CP-conjugate signs.

## Exact coefficient-free extremum

The factors separate:

\[
(s_{12}c_{12})^2\le\frac14,qquad
(s_{23}c_{23})^2\le\frac14,
\]

and, with (x=s_{13}^2),

\[
x(1-x)^2\le\frac4{27}.
\]

Together with (sin^2\delta\le1), this gives

\[
J^2\le\frac1{108}.
\]

Equality requires

\[
s_{12}^2=s_{23}^2=\frac12,qquad
s_{13}^2=\frac13,qquad
\sin^2\delta=1.
\]

Thus maximal CP is a genuine coefficient-free proper selector on the mixing
quotient. It is not texture-chart data.

## Ensemble falsification

Every one of the 1,210 fitted sheets has (|J|<1/1000), whereas maximal CP
requires (J^2=1/108). No fitted sheet survives. The existing CKM/Jarlskog
instrument directly falsifies the selected orbit.

This is a stronger failure than WP1022: selecting the invariant volume itself
is mathematically possible without an inserted target value, but the simplest
coefficient-free rule predicts the wrong physical magnitude.

## Source and instrument boundary

The extremization is a mathematical operation, not a declared source action.
No local renormalizable flavor potential, conditional expectation, threshold
constructor, or calibrated preparation apparatus has been derived whose
stationary locus is maximal (J^2). The readout instrument exists; the source
operation does not.

## Smallest exact falsifier

The exact comparison

\[
J^2_{\mathrm{fit}}<10^{-6}<1/108
\]

already makes the selected and fitted families disjoint.

## Claim boundary

This closes global maximization of (J^2), not all coefficient-free invariant
actions. It does not infer an implicit time evolution or causal relaxation
toward the extremum.

## Disposition

Reject maximal CP as a flavor explanation. The next candidate must derive a
source-local invariant action whose stationary locus gives a small nonzero
oriented volume without inserting the observed (J) scale, and must survive
the complete fitted ensemble.

Verification: uv run --with sympy python
research/flavor/checkers/wp1023_maximal_cp_selector_no_go.py.
