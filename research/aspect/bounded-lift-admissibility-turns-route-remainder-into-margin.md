# Bounded-lift admissibility turns route remainder into margin

## Question

If exact route completeness is unavailable, can a small omitted-route action still certify confinement over the physically admissible absolute lifts?

## Bounded torsor certificate

Let admissible lifts of one relative class be

\[
c(t)=c_0+Vt,
\qquad
\|t\|\le M,
\]

where the radius \(M\) is source-derived. Let the complete route map split as retained and omitted components. Suppose the retained map kills the torsor directions, while the omitted remainder satisfies

\[
\|RV\|\le\varepsilon.
\]

If the complete route norm of the base lift is bounded by

\[
\|Bc_0\|\le q_0,
\]

then every admissible lift obeys

\[
\|Bc(t)\|
\le
q_0+\varepsilon M.
\]

Therefore the full admissible lift family has strict return whenever

\[
q_0+\varepsilon M<1,
\]

with return margin at least

\[
1-(q_0+\varepsilon M)^2.
\]

## Exact versus quantitative descent

Exact quotient descent requires \(RV=0\). The bounded certificate does not make the norm quotient-invariant; it proves only that every source-admissible lift remains inside the strict-return ball. Consequently the physical claim must retain unresolved lift multiplicity unless a selection or exact descent theorem is also supplied.

If the affine torsor is unrestricted, \(M=\infty\), and every nonzero remainder action defeats the certificate. Small operator norm alone cannot control arbitrary lift coefficients.

## Boundary

For \(q_0=1/2\), \(\varepsilon=1/10\), and \(M=2\), the total bound is \(7/10\) and the return margin is at least \(51/100\). For \(q_0=3/5\), \(\varepsilon=1/10\), and \(M=4\), the total reaches one exactly and terminal cancellation remains admissible.

## Source requirements

The radius must bound coefficients in a declared norm on the rank-seven torsor basis. A coordinate box, minimum-norm convention, or finite search range is not physical admissibility unless derived from the source constructor. The remainder estimate must hold on the entire torsor subspace, not only on the seven basis vectors separately unless their coefficient norm and induced operator bound are included.

## Verification

`research/aspect/checkers/check_bounded_lift_remainder.py` checks strict, boundary, and failed budgets with exact rational arithmetic.

## Disposition

There are now two distinct routes past incomplete physical maps: exact remainder annihilation gives quotient descent; source-bounded lift admissibility plus a quantitative remainder gives uniform confinement without descent. The current q_G12 source supplies neither a radius nor a remainder action bound.
