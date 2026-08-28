# A nonclosed-range completion falsifies frozen v7

## Result

Version 7 is falsified. Every finite specialization cone can vanish while the completed operator develops a defect invisible to finite kernel and cokernel calculations.

## Hostile packet

On the Hilbert space of square-summable sequences, define

\[
D(e_n)=\frac{1}{n}e_n.
\]

Its cutoff at dimension (N) is

\[
D_N=\operatorname{diag}\left(1,\frac12,\ldots,\frac1N\right).
\]

Every (D_N) is invertible. Its kernel and cokernel vanish, so every finite mapping cone is acyclic.

But the smallest singular value is (1/N), and

\[
\lVert D_N^{-1}\rVert=N.
\]

There is no uniform inverse bound.

## Completed failure

The vector

\[
y=\left(1,\frac12,\frac13,\ldots\right)
\]

is square-summable because the sum of (1/n^2) converges. Its unique formal preimage under (D) is

\[
x=(1,1,1,\ldots),
\]

which is not square-summable. Thus (D) is not surjective.

Every finite-support vector lies in the range, so the range is dense. Since (y) is a limit of finite-support range vectors but is not itself in the range, the range is not closed.

## Exact defect in v7

v7 says that completed sewing precedes finite projection, but it does not declare:

- the ambient topological or stable category;
- which exact structure defines the specialization cone;
- whether cokernels use algebraic range or closed range;
- a derived completion functor;
- a spectral-gap or closed-range defect.

In algebraic vector spaces, the cokernel sees the missing vectors but leaves the Hilbert category. In Hilbert spaces with closed-range cokernels, the dense range has zero topological cokernel even though inversion is unstable. The same formal cone therefore has incompatible meanings.

An ordering slogan cannot resolve that ambiguity.

## Required successor

A successor must type completion itself. It needs:

- a declared ambient completed category and exact structure;
- derived completion rather than termwise finite completion;
- a closed-range or spectral defect object;
- uniform lower-bound data for any claimed inverse;
- a rule retaining zero-limit spectral channels even when every finite kernel and cokernel vanishes.

The next rung is analytic: vanishing cycles must include spectral mass approaching zero, not only vectors already in an algebraic kernel.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v7_nonclosed_range_completion_falsifier.py
```
