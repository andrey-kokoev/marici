# Eight-axis words have a faithful history homomorphism

Let

\[
\mathsf A=\{H,V,D,q,L,C,O,R\}
\]

and let `A*` be the free monoid of finite sequential words. On the history-Fock carrier

\[
\mathbb F_{\mathsf A}
=\ell^2(\mathsf A^*)\otimes\mathbb X,
\]

define right-creation operators

\[
S_a(e_w\otimes x)=e_{wa}\otimes x.
\]

For a word `w=a_1...a_k`, put

\[
\rho(w)=S_{a_k}\cdots S_{a_1}
\]

under the convention that operations are appended from left to right. Then

\[
\rho(uv)=\rho(v)\rho(u),
\]

or, after choosing the opposite composition convention, an ordinary monoid homomorphism. Distinct words act differently on the vacuum, so the representation is faithful. This represents formal combinations of arbitrary finite length.

## Local binary cube

For one traversal of the eight binary directions, restrict to words with no repeated generator. The history ranks are

\[
1,8,56,336,1680,6720,20160,40320,40320,
\]

for lengths zero through eight, totaling

\[
109601
\]

history states. There are exactly

\[
8!=40320
\]

maximal histories.

Every generator appends its label when unused and acts by zero when the local binary type forbids repetition. The exhaustive checker verifies the composition law at every split of every one-use history.

Endpoint-only representation is not faithful: all maximal histories have the same Boolean endpoint. The history carrier retains all 40320 orders.

## Lax and coherent relations

The words `qR` and `Rq` remain distinct basis histories although they have the same endpoint. Their relation is represented by the nonzero 2-cell

\[
A_X=P_X\mathcal F(I-P_X),
\]

not by equality. Similarly, Beck--Chevalley, dagger, successor, and graph-completion relations should be imposed as 2-cells. The result is a 2-representation of the typed path 2-category.

Passing to a homotopy category may identify 2-isomorphic words. Keeping the enriched history carrier retains route effects.

## Semantic boundary

This proves the universal combinatorial representation theorem. It does not yet prove that every formal word has a nonzero analytic realization. To obtain that stronger theorem one must supply:

1. a source and target object for each generator occurrence;
2. a typing automaton for repetitions and graded successors;
3. realification for anti-linear dagger;
4. Fock/tensor linearization for multi-ary `H,V`;
5. graph correspondences for directed `C,O,R`;
6. all required coherence 2-cells;
7. the unresolved arithmetic joint-closability gate.

Untyped words may consistently act by zero, but that is a typed disposition rather than a nonzero analytical homomorphism.

Hence the conjecture is proved formally and locally, while its faithful nonzero analytic realization remains a separate, sharply specified problem.
