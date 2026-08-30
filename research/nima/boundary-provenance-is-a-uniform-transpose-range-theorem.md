# Boundary provenance is a uniform transpose-range theorem

## Question

Smooth prime synthesis is continuous into the Mellin–de Rham graph domain.
Does that automatically realize every arithmetic boundary current as an
analytic boundary functional?

## Transpose exists, provenance does not follow

Let

\[
K:\mathcal S_{\mathbb P}\longrightarrow\mathcal G_{QD}
\]

be the continuous smooth synthesis map. Continuity gives the transpose

\[
K':\mathcal G_{QD}'\longrightarrow\mathcal S_{\mathbb P}'.
\]

For \(g\in\mathcal G_{QD}'\), its arithmetic coefficient row is

\[
(K'g)_p=\langle g,\tau_{\log p}\Phi\rangle.
\]

A primitive, square, seam, or endpoint current \(a\) has analytic provenance
through this synthesis exactly when

\[
a\in\operatorname{Ran}K'.
\]

Membership in the codomain \(\mathcal S_{\mathbb P}'\) proves continuity as an
arithmetic current. It does not prove membership in the transpose range.

## Finite-cutoff trap

At cutoff \(X\), one may solve

\[
K_X'g_X=a_X.
\]

Even if every finite system is solvable, the minimum graph-dual norm of
\(g_X\) may diverge. Such solutions do not define a completed functional.

When the graph carrier is Hilbert, the exact finite cost is the least-norm
interpolation energy. If \(K_X) has full column rank, it is

\[
\lVert g_X^{\min}\rVert^2
=a_X^*(K_X^*K_X)^{-1}a_X.
\]

A cutoff-independent bound is the completion gate. Bounded least-norm
interpolants admit weakly convergent subnets; compatibility with cutoff
restriction then supplies a candidate element of the transpose range.

## Exact hostile

Let

\[
K_N=\operatorname{diag}(1,\ldots,1,N^{-1})
\]

and let \(a_N\) select the last coordinate. Every finite transpose equation is
solvable, but its unique least-norm solution has norm \(N\). Finite incidence
therefore gives false confidence while completed provenance fails.

This is the dual form of the earlier nonclosed-range and observability
obstructions.

## Consequence for the theta boundary currents

The next calculation is now finite and source-specific. For each declared
current, compute at every cutoff:

1. the smooth synthesis Gram matrix \(K_X^*K_X\) in the \(Q,D\) graph norm;
2. the labelled current vector \(a_X\);
3. the least-norm interpolation energy;
4. compatibility of minimizers under cutoff restriction;
5. reciprocal-sheet covariance of the resulting functional.

A single divergent current closes the claim that the common graph domain
realizes the full boundary packet. Different currents may require different
dual grades; no common Riesz identification is assumed.

## DPC verdict

Resolved: existence and continuity of the transpose map.

Withheld: source provenance of any specific boundary current not yet shown to
lie in its range.

Finite falsifier: solvable cutoff equations with unbounded least-norm
interpolation energy.

## Verification

The checker `check_uniform_transpose_range_gate.py` compares a stable family
with the diagonal hostile and verifies exact finite solvability together with
divergent minimum dual cost.

