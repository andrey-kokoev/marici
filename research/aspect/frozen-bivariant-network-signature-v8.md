# Frozen analytic-completion network signature v8

## Status

Version 8 is a new frozen local candidate. Version 7 remains unchanged and falsified.

v8 types the completed analytic category and retains defects that appear only as finite-section singular values approach zero.

## Ambient category

Route objects are separable Hilbert complexes with declared norms. Transport maps are bounded, or are declared closed densely-defined operators equipped with graph norms. Specialization uses topological mapping cones, reduced cohomology, and an explicit nonclosed-range defect.

Finite sections form a pro-object. Their derived completion carries a comparison map to the declared completed route complex. Finite data promote only when the comparison cone vanishes.

## Repair of the v7 hostile

For

\[
D(e_n)=\frac1n e_n,
\]

every finite section is invertible. But its reduced minimum modulus is

\[
\gamma(D_N)=\frac1N,
\]

so no uniform positive lower bound survives. The unit vectors (e_N) form an approximate-kernel sequence because

\[
\lVert e_N\rVert=1,
\qquad
\lVert De_N\rVert=\frac1N\longrightarrow0.
\]

v8 retains this sequence as a zero-limit spectral pro-object. It also records the dense nonclosed range rather than identifying dense range with surjectivity.

## Three analytic gates

Strict descent requires all three defects to vanish:

1. reduced topological cohomology of the completed cone;
2. the nonclosed-range defect;
3. the zero-limit spectral germ represented by approximate-kernel sequences.

Finite invertibility promotes only with a uniform inverse bound.

## First unused hostile

The unilateral shift on square-summable sequences has

\[
S(e_n)=e_{n+1}.
\]

It is an isometry, so its reduced minimum modulus is one and it has no approximate kernel. Its range is closed. Nevertheless, its cokernel is the line spanned by the first basis vector.

Therefore the spectral and nonclosed-range gates cannot replace the ordinary completed mapping cone. v8 retains both.

## Frozen exclusions

v8 forbids:

- promoting finite invertibility without a uniform inverse bound;
- promoting dense range to surjectivity;
- inferring absence of approximate kernels from zero finite kernels;
- switching between algebraic and topological cokernels without declaring the category;
- discarding zero-limit spectral mass because zero is not an eigenvalue;
- using a spectral gap as a substitute for kernel or cokernel accounting;
- promoting termwise completion to derived completion.

## Next falsifier

Attack non-normality or domains. A non-normal completed operator can have a large pseudospectrum even when the tested point has no eigenvector, while an unbounded specialization can change its domain under completion. Either may require a resolvent or graph-domain defect beyond v8's zero-limit singular channel.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v8.py
```
