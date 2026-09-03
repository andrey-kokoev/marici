# Certified tail error closes finite sector return bounds

## Question

When the physical sector constructor is available only through a finite wall/history/tail/PV approximation, what error certificate promotes a finite computation to strict return?

## Perturbative certificate

Let \(T_p\) be the exact normalized coupling and \(\widehat T_{p,N}\) a finite source-derived approximation. Suppose

\[
\|\widehat T_{p,N}\|\le q_N,
\qquad
\|T_p-\widehat T_{p,N}\|\le\varepsilon_N
\]

uniformly over primes. Then

\[
\|T_p\|\le q_N+\varepsilon_N.
\]

The finite calculation proves strict return exactly when

\[
q_N+\varepsilon_N<1.
\]

It supplies the explicit bounds

\[
\eta_N=1-q_N-\varepsilon_N
\]

for normalized block coercivity and

\[
1-\|K_p\|
\ge
1-(q_N+\varepsilon_N)^2
\]

for the return margin.

## Boundary and hostile alignment

A finite approximation with \(q_N<1\) proves nothing without an omitted-tail norm. At \(q_N=4/5\) and \(\varepsilon_N=1/5\), the certified margin is exactly zero. An omitted term aligned with the top singular direction saturates the triangle bound, so its sign, oscillation, or sector label cannot justify a smaller error.

For \(q_N=3/5\) and \(\varepsilon_N=1/10\), the exact coupling norm is at most \(7/10\), giving return margin at least \(51/100\).

## Sectorwise version

If

\[
\widehat T_{p,N}=\sum_s\widehat T_{p,s,N},
\]

then one may use

\[
q_N=\sum_s q_{s,N},
\qquad
\varepsilon_N=\sum_s\varepsilon_{s,N}.
\]

Orthogonal improvements remain valid only when the exact remainders obey the same proved cross-Gram relations. Orthogonality of the retained finite pieces does not control an untyped remainder.

## Uniformity gate

Pointwise convergence \(\varepsilon_{p,N}\to0\) is insufficient for one prime-uniform margin. The acceptance test requires either one \(N\) with

\[
\sup_p(q_{p,N}+\varepsilon_{p,N})<1
\]

or a separately proved prime-uniform asymptotic estimate. Cross-prime Markov composition cannot replace this supremum.

## Verification

`research/aspect/checkers/check_return_tail_error_certificate.py` checks strict, zero-margin, and failed certificates using exact rational bounds, including the aligned-error saturation.

## Disposition

A finite physical constructor can certify confinement without a closed form only if it carries a source-derived operator-norm error for every omitted sector and tail. A numerical cutoff below one without that error remains finite-cutoff evidence, not a uniform theorem.
