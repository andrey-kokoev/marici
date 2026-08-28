# Flavor double-commutator gradient audit

Work package: WP929

## Question

Does the first Hermitian double-commutator candidate provide genuine motion on
the faithful flavor quotient, and if so does it select a physical point?

The source-authority gate is applied first.  The declared Spin5 packet does not
derive this term, its coefficient, its sign, its normalization, or a detector
instrument.  The calculation below is therefore a conditional audit of a
candidate operation, not admission of new flavor dynamics.

## Candidate

For positive Hermitian Gram matrices (H_u,H_d), put

\[
C=[H_u,H_d],\qquad F=-\frac12\operatorname{tr}(C^2)\geq 0.
\]

The negative Euclidean gradient is

\[
\dot H_u=-[C,H_d],\qquad
\dot H_d=-[H_u,C].
\]

Both velocities are Hermitian and are equivariant under simultaneous weak-basis
conjugation.  Consequently the operation descends to `physical16`; it is not
texture-chart data.

Its Lyapunov identity is exact:

\[
\dot F=-\lVert[C,H_d]\rVert_F^2-\lVert[H_u,C]\rVert_F^2\leq0.
\]

For Hermitian (H_u,H_d), equality forces (C=0).  Thus the fixed set is the
whole commuting locus, not an isolated point.  Unlike WP928's Lax transport,
the hostile exact witness has nonzero derivatives of higher spectral traces.
The candidate therefore produces genuine quotient-level contraction, but it
also changes mass spectra and supplies no numerical choice inside the commuting
family.

## Classification

Conditionally, the operation selects a proper commuting subspace.  It is not a
point selector and is not merely a presentation rigidifier.  Physically, it is
not yet an admitted selector because no declared source operation generates its
coefficient and dissipative sign, and no calibrated instrument realizes the
flow.

This distinction is decisive: algebraic availability of a descending gradient
does not establish executable flavor dynamics.

## Exact falsifier and acceptance boundary

The checker uses an exact rational two-generation mixing block embedded in
three generations.  It verifies strict decrease of (F), preservation of the
linear traces, change of higher spectral traces, and simultaneous-conjugation
equivariance.  This falsifies the claim that every commutator-dependent
higher-order candidate is another isospectral reparameterization.

It does not authorize the candidate.  Admission requires an independently
derived source term with fixed positive coefficient and a typed physical
instrument.  Without those, WP929 is a conditional mathematical constructor
and the source-selector branch remains open-negative.

## Reproduction

Run:

```powershell
uv run --with sympy python research/flavor/checkers/wp929_double_commutator_gradient_audit.py
```

The generated result is
`research/flavor/results/wp929_double_commutator_gradient_audit.json`.
