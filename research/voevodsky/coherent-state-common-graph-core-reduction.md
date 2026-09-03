# Coherent-state common graph-core reduction

## Question

Can the Segal--Bargmann topology repair close the categorical arrow from finite Gaussian packet positivity to positivity of the completed Weil form?

## Claim boundary

The graph-core theorem is reduced to an explicit source-row identification. A polynomially weighted finite-difference fixture is verified. The actual completed row model and positivity remain open.

## Closed multiplier model

Let the unbounded gamma contribution be represented after unitary transport by a multiplication operator

\[
M_mf(u)=m(u)f(u)
\]

with logarithmic growth. Its maximal domain is

\[
D(M_m)=
\left\{f\in L^2:
\int |m(u)|^2|f(u)|^2du<\infty
\right\},
\]

and its graph norm is exactly

\[
\|f\|_{M_m}^2
=
\int(1+|m(u)|^2)|f(u)|^2du.
\]

Thus the abstract form-core question becomes weighted \(L^2\) density.

## Stability under bounded rows

Suppose endpoint evaluation becomes bounded under Segal--Bargmann transport and the completed fixed-width labelled prime row is a bounded operator \(B\). Then

\[
\|f\|_{M_m}^2
\leq
\|f\|_{M_m,B}^2
\leq
(1+\|B\|^2)\|f\|_{M_m}^2.
\]

Equivalent graph norms have the same dense subspaces. Therefore a core for the gamma multiplier remains a common core after adjoining bounded endpoint and prime rows.

The crucial source condition is boundedness of the completed infinite labelled prime row, not merely boundedness of each finite prime adjacency.

## Coherent states generate the candidate core

Gaussian translates are coherent states under Segal--Bargmann transport. Finite differences of translates remain finite coherent-state combinations. For

\[
g_h(x)=e^{-(x-h)^2/2},
\]

the central difference satisfies

\[
\frac{g_h-g_{-h}}{2h}
\longrightarrow
xe^{-x^2/2}.
\]

The checker verifies this convergence in the stronger norm weighted by \(1+x^2\), not only pointwise or in unweighted \(L^2\). Higher finite differences analogously generate polynomial--Gaussian derivatives.

For a logarithmic multiplier, Gaussian domination makes these finite-difference limits compatible with the weighted graph norm. Hermite functions are then the proposed intermediate core:

\[
\operatorname{span}\{\text{coherent states}\}
\ 	ext{graph-dense in}\ 
\operatorname{span}\{\text{Hermite functions}\}
\ 	ext{graph-dense in}\ D(M_m).
\]

The second density uses the closed multiplication realization and must be stated for the actual transported measure and multiplier.

## Categorical consequence

Let \(j:\mathcal V\to D(Q)\) include finite coherent-state spans. Under the source-row model above, \(j\) is a form-core inclusion. Hence restriction

\[
j^*:\operatorname{Form}(D(Q))
\longrightarrow
\operatorname{Form}(\mathcal V)
\]

reflects nonnegativity for the closed form:

\[
j^*Q\geq0
\Longrightarrow
Q\geq0.
\]

This closes the topology-sensitive conservativity arrow identified in the categorical proof bracket. It does not establish the premise \(j^*Q\geq0\).

## Remaining source verification

The actual completed explicit formula must be shown to admit one common realization in which:

1. gamma is the stated closed logarithmic multiplier;
2. endpoint rows are bounded kernel-vector evaluations;
3. the infinite labelled prime row converges in operator or row norm at fixed width;
4. the resulting \(A,B\) reproduce the completed Weil form exactly;
5. differentiated tail estimates justify every jet cell.

If any row is unbounded beyond the gamma graph norm, the common-core argument must be redone with the enlarged graph norm.

## Proof bracket after reduction

The form-core gate is no longer an unspecified density demand. Conditional on exact row identification and bounded prime completion, coherent states provide the required common core. The unresolved mathematical core is then concentrated in:

- source identification of those rows;
- arithmetic positivity on the coherent-state packets, equivalently a global Douglas contraction.

## Disposition

The Segal--Bargmann route is viable as a topology repair but has not proved RH. It converts endpoint discontinuity into bounded evaluation and reduces the common-core theorem to weighted multiplier density plus bounded perturbation stability. The first missing typed object is the actual completed closed \(A/B\) row realization with a norm-controlled infinite prime component.

## Verification

- `research/voevodsky/coherent-state-common-graph-core-reduction-v1.json`
- `research/voevodsky/checkers/check_coherent_state_graph_core_fixture.py`
- `research/voevodsky/results/coherent_state_graph_core_fixture.json`
