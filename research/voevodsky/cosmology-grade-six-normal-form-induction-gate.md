# Grade-six normal-form induction gate

## Question

Do the finite ranks `4, 8, 12, 16, 20` define a proof that the four grade-six seeds generate a free module over `Q[x²,y²]`?

## Exact conditional reduction

At transport degree `d`, freeness is equivalent to linear independence of the `4(d+1)` classes

\[
x^{2i}y^{2(d-i)}c_j,
\qquad 0\leq i\leq d,\quad 1\leq j\leq4.
\]

A sufficient induction datum is a compatible family of dual quotient probes `L[d,j,i]` that:

1. vanish on the grade-six relation image at ambient index `12+2d`;
2. evaluate to one on the indexed orbit class;
3. vanish on every other degree-`d` orbit class;
4. commute with the `x²` and `y²` embeddings under the index shift.

These conditions give a Kronecker evaluation matrix at every degree and therefore independence. They also separate the required restricted statement from false global injectivity.

## Disposition

The current row-echelon computations verify the Kronecker-rank consequence only for degrees zero through four. Their pivot coordinates depend on the ambient quotient basis, so they do not construct compatible probes. The induction is therefore not established. It is not falsified: no relation among the grade-six orbit classes has appeared through degree four, and the known global kernels avoid this span at the tested degrees.

The next gate is to construct source-labelled dual probes or exhibit a degree where probe compatibility fails. Further finite rank checks alone do not close the induction.

## Evidence

- `research/voevodsky/results/cosmology_grade_six_truncated_free_module.json`
- `research/voevodsky/results/cosmology_grade_six_A18_degree_three.json`
- `research/voevodsky/results/cosmology_grade_six_A20_degree_four.json`
