# 1635 — The Trace-Balanced Cut Generator Strictly Descends on the Full Weyl Moment Tower

## Remaining gate

Entry 1634 proves strict degree preservation on number moments.  Test every Weyl monomial through degree eight and verify that ordering/CCR reduction introduces no degree-raising obstruction.

## Exact Weyl generator

Use

\[
[Q,P]=2i,
\qquad
L=a^\dagger=\frac{Q-iP}{2}.
\]

For the trace-balanced adjoint channel

\[
\mathcal L^\dagger(O)
=
L^\dagger O L
-\frac12\{L^\dagger L,O\},
\]

the exact Weyl-symbol operator is

\[
\boxed{
\mathcal L^\dagger
=
\frac12(Q\partial_Q+P\partial_P)
+\frac12(\partial_Q^2+\partial_P^2).
}
\]

Therefore

\[
2\mathcal L^\dagger(Q^mP^n)
=(m+n)Q^mP^n
+m(m-1)Q^{m-2}P^n
+n(n-1)Q^mP^{n-2}.
\]

The first term preserves total degree; the diffusion terms lower it by two.  No positive degree shift survives.

The unit maps to zero:

\[
\mathcal L^\dagger(1)=0,
\]

which is the trace-preserving condition.

## CCR compatibility

Weyl symbols are the canonical ordering quotient of the CCR algebra.  The displayed differential operator is defined directly on that quotient, so two operator representatives related by \([Q,P]=2i\) have the same image.  No ordering-dependent coherence cell is required.

The checker verifies all 45 monomials through total degree eight and 56 degree-lowering terms.

## Narrow result

\[
\boxed{
\text{The complete trace-balanced cubic Cut generator is a strict filtration-preserving endomorphism of the full Weyl moment tower.}
}
\]

The degree-two shift belongs to the positive production cell in isolation.  Source virtual-Cut coherence cancels it globally.

## Qualifications

The local generator uses one observed creation jump.  Momentum-dependent amplitudes and sums over occurrence labels preserve the degree statement when they commute with the observed canonical variables.  Mode-mixing Kraus tensors require the corresponding multi-mode Weyl audit.

## Architectural consequence

The cosmological state coefficient object can be taken as an infinite filtered positive Weyl-moment tower carrying:

- Hamiltonian symplectic derivations;
- completely positive labelled production cells;
- virtual normalization cells;
- a strict trace-balanced channel generator;
- cumulant grades constrained by higher moment positivity.

This is a concrete sector-specific coefficient architecture over the unchanged occurrence/Cut carrier.

## Durable artifacts

- `research/benincasa/checkers/weyl_gain_moment_generator.rs`
- `research/benincasa/results/weyl-gain-moment-generator.json`
- `research/benincasa/weyl-gain-moment-generator.md`

## Next falsifier

Perform the multi-mode occurrence-resolved Weyl audit for the actual cubic momentum kernel \(C_{p;qk}\).  Verify complete positivity, strict total-degree preservation after virtual balance, and naturality under \((q,k)\leftrightarrow(k,q)\) before continuum trace.  A cross-mode ordering defect would be the first failure of the one-mode coefficient architecture.
