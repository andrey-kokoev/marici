# 1632 — The Labelled Cubic Cut Is Completely Positive with a Forced Moment-Filtration Shift

## Objective

Entry 1631 requires an infinite non-flat moment tower.  Test whether the source cubic labelled Cut defines a positive map on that tower and determine its exact filtration variance.

## Kraus form

After retaining and then tracing the internal occurrence label \(r=(q,k)\), the production contribution has the form

\[
\boxed{
\Phi_{\rm Cut}(\rho)
=
\sum_r C_r\rho C_r^\dagger.
}
\]

For every auxiliary system and every \(X\succeq0\),

\[
(\Phi_{\rm Cut}\otimes\operatorname{id})(X)
=
\sum_r(C_r\otimes I)X(C_r^\dagger\otimes I)
\succeq0.
\]

Thus the occurrence-resolved Cut map is completely positive before forgetting labels.  Positive integration over the symmetric finite-EFT measure of Entry 1618 preserves this property.

## Filtration variance

For cubic vacuum production, each \(C_r\) contains one observed creation operator.  The adjoint map is

\[
\Phi_{\rm Cut}^\dagger(O)
=
\sum_r C_r^\dagger O C_r.
\]

If \(O\) has observed polynomial degree \(D\), then \(C_r^\dagger O C_r\) has degree \(D+2\).  Therefore the finite truncation is typed as

\[
\boxed{
\Phi_D:
\mathbb M_{\leq D+2}
\longrightarrow
\mathbb M_{\leq D}.
}
\]

It is not a same-level endomorphism of \(\mathbb M_{\leq D}\).

## Finite check

The checker realizes the observed creation incidence on a finite occupation basis and verifies positive quadratic forms for rank-one input states and probes.  It also verifies the forced degree-two shift.

## Narrow result

\[
\boxed{
\text{The labelled cubic Cut is completely positive and filtration-preserving only as a degree-two shifted tower map.}
}
\]

This corrects the tempting but mistyped same-level formulation.

The map need not be trace-preserving by itself: it is the positive production contribution, not the complete normalized time-evolution channel.  Source normalization and virtual terms belong to the full Dyson comparison.

## Architectural consequence

The state coefficient tower and Cut calculus fit naturally as a filtered pro-object:

\[
\cdots
\to\mathbb M_{\leq D+2}
\xrightarrow{\Phi_D}
\mathbb M_{\leq D}
\to\cdots.
\]

Occurrence labels index Kraus legs; forgetting them performs the physical partial trace.  This supplies a concrete quantum-information realization of the existing labelled Cut carrier without changing its incidence geometry.

## Durable artifacts

- `research/benincasa/checkers/cut_kraus_shifted_moment_tower.rs`
- `research/benincasa/results/cut-kraus-shifted-moment-tower.json`
- `research/benincasa/cut-kraus-shifted-moment-tower.md`

## Next falsifier

Add the source virtual/Hamiltonian Dyson term and normalization cell.  Test the trace-preserving identity

\[
\sum_r C_r^\dagger C_r
-i(H_{\rm eff}-H_{\rm eff}^\dagger)
=0
\]

at the same shifted filtration degree.  The production Cut alone is CP; the complete finite-time channel must satisfy the optical-theorem normalization without a fitted anti-Hermitian term.
