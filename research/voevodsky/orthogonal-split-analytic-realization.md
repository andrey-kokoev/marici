# Orthogonal-split analytic realization of the coherence pyramid

## Question

Is the integrated computad merely consistent syntax, or does at least one analytic model realize its composition and coherence obligations?

## Claim boundary

This packet constructs a finite-dimensional rational inner-product submodel. It proves realizability of the typed presentation in a restricted sector. It does not show that the enlarged Stieltjes Green form, radiative gauge quotient, or unbounded radial comparison belongs to this submodel.

## Objects

For a finite tagged set \(S\) with positive rational weights \(w_s\), define

\[
H(S)=\mathbb Q^S,
\qquad
G_S(x,y)=\sum_{s\in S}w_sx_sy_s.
\]

The radical is zero and the form domain is all of \(H(S)\).

## Under and over arrows

For \(S\subseteq T\), coordinate extension by zero gives an isometric under-embedding

\[
H(S)\hookrightarrow H(T).
\]

For disjoint tagged sets \(K,X\), coordinate projection gives an over-quotient

\[
p_{K,X}:H(K\sqcup X)\twoheadrightarrow H(X)
\]

with kernel exactly \(H(K)\).

This projection preserves the quotient form because the decomposition is orthogonal. The nonorthogonal Green projection rejected earlier is not admitted into this submodel.

## Partial composition

Under amalgamation is defined when added tag sets are disjoint; its joint Gram matrix is the diagonal form on their tagged union. Over pullback along a coordinate inclusion \(Y\subseteq X\) is

\[
H(K\sqcup Y)\twoheadrightarrow H(Y),
\]

with unchanged kernel \(H(K)\).

Sequential compositions normalize to tagged union and coordinate restriction. Positive minimum modulus equals the smallest retained weight.

## Coherence

Tagged union is normalized by sorted tags. Therefore both parenthesizations of three or four admitted under-amalgamations yield the same object and Gram form. Pentagon and unit laws are strict in this normalization.

For disjoint added tags \(U\) and a coordinate inclusion \(Y\subseteq X\), pullback and amalgamation both produce

\[
H(K\sqcup Y\sqcup U),
\]

with the same diagonal form, projection, and kernel. The Beck–Chevalley comparison is identity and preserves every certificate. Interchange is likewise strict for coordinate maps on disjoint tag blocks.

Finite-to-closed completion is identity: the domain is already complete, the radical is zero, and coercivity is the minimum positive weight. Completion pasting is therefore strict.

## Strongest falsification attempt

Insert a nonzero cross pairing between two added tags. The object may remain positive, but it exits the orthogonal-split constructor because the declared joint certificate no longer normalizes to tagged diagonal union. Thus the model is restrictive and does not absorb the earlier nonorthogonal counterexamples.

## Disposition

The candidate presentation has a genuine analytic realization as an orthogonal-split partial equipment. This proves consistency and nonemptiness, not adequacy for Marici's sourced sectors. The next branch must test whether actual Green, gauge, or closed-form source data admit a structure-preserving functor into or from this model, or require a broader analytic realization.

## Verification

- `research/voevodsky/checkers/check_orthogonal_split_analytic_realization.py`
- `research/voevodsky/results/orthogonal_split_analytic_realization.json`
- `research/voevodsky/coherence-pyramid-integrated-representation.json`
