# Heterogeneous Gram/exact-sequence partial equipment

## Question

Can the sourced Green and gauge sectors coexist without coercing algebraic exactness into analytic form data?

## Claim boundary

This packet constructs a two-fiber finite model. It proves internal closure in each fiber and typed admission of mixed cells when a bridge certificate is supplied. It does not provide such a bridge for the sourced gauge sequence.

## Fibers

The analytic fiber \(\mathcal G\) contains positive full-Gram objects, principal-block under arrows, and Schur-complement over arrows.

The algebraic fiber \(\mathcal E\) contains finite vector spaces and exact sequences

\[
0\longrightarrow K\longrightarrow V\overset q\longrightarrow X\longrightarrow0.
\]

Its over reindexing is ordinary pullback. Kernel preservation and pullback associativity are strict up to the canonical tuple reassociation used by the checker.

The total representation is the typed disjoint union \(\mathcal G\sqcup\mathcal E\), augmented by partial mixed cells.

## Mixed bridge certificate

A bridge from an algebraic over-arrow to the Gram fiber contains:

1. a positive Gram form on \(V\);
2. the declared kernel coordinates \(K\);
3. the induced Schur form on \(X\);
4. comparison maps preserving tags and the quotient square;
5. equality between the target form and the computed Schur form.

Without all five fields, no mixed cell is constructed.

## Fixture

For \(V=\mathbb Q^{\{k,x\}}\), quotient \(q(k,x)=x\), and

\[
G_V=\begin{pmatrix}2&1/2\\1/2&1\end{pmatrix},
\]

the induced quotient form is \(7/8\). The bridge checker verifies the kernel, quotient square, positivity, and Schur equality. This fixture realizes a mixed cell.

The sourced gauge sequence has exactness and an identified kernel but lacks items 1 and 3. It remains valid in \(\mathcal E\) and is refused as a mixed cell. Refusal is not failure of the gauge quotient.

## Coherence

Composites entirely in \(\mathcal G\) use global Gram restriction and associative Schur elimination. Composites entirely in \(\mathcal E\) use pullbacks and kernel transport. Mixed pasting is defined only when each pasted edge carries a bridge and the intermediate Schur form agrees exactly. Under that predicate, pasting reduces to matrix equality and commuting linear squares.

## Disposition

A heterogeneous partial equipment realizes the currently sourced variance without adding a gauge metric. It has nonempty mixed cells, but none is source-authorized for the gauge fixture. The first remaining categorical theorem is closure and associativity of arbitrary mixed bridge pasting, beyond the checked finite fixture.

## Verification

- `research/voevodsky/checkers/check_heterogeneous_gram_exact_equipment.py`
- `research/voevodsky/results/heterogeneous_gram_exact_equipment.json`
