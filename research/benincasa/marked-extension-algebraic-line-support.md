# Marked extension support on the split algebraic plane

## Frozen data

The four fixed final coordinates of the rank-twelve marked-relative source
reduction are ordered as

\[
(e_6,e_7,e_8,e_9).
\]

Entry 867 gives the source-defined algebraic frame

\[
k_0=(1,0,0,0),\qquad
k_1=(0,\alpha,\beta,\gamma),
\]

where

\[
\alpha=(1-y^2)(y^2-u^4),\quad
\beta=2(u^2+y^2),\quad
\gamma=-2y^2(u^2+1),
\]

and its exact splitting gauge

\[
h=\frac{u(u+v)(u+v-4)P_6}{4}.
\]

Thus a fixed final column (b=(b_0,b_1,b_2,b_3)^T) has split-line
coordinates

\[
c_1=\frac{b_1}{\alpha},\qquad
c_0=b_0-hc_1,
\]

provided

\[
b_2=\beta c_1,\qquad b_3=\gamma c_1.
\]

## Exact finite-specialization test

The checker runs the complete 132-equation source reduction and retains the
full primitive exact-lift space.  It accepts a solve only when

\[
\operatorname{rank}=117,qquad
\text{fixed mask}=3847,
\]

so the four final coordinates are canonical across primitive lifts.

For each of the three labelled quotient generators, both base derivatives,
and five generic kinematic points, the algebraic-plane residual vanishes
exactly.  At each of two independent 61-bit primes, both (c_0) and (c_1)
are nonzero in all thirty columns.

Because a characteristic-zero rational function that vanished identically
would vanish at every good modular specialization, these good-rank exact
specializations prove that none of the twelve labelled line projections is
identically zero.  Equivalently, in each derivative direction the generic
source support graph is the complete bipartite graph

\[
K_{3,2}.
\]

This is a support theorem.  It does not reconstruct the rational extension
entries, determine their divisors, or certify a preferred affine
normalization.

## Reproduction

From `research/benincasa/marici-gm`:

```powershell
cargo run --release --bin marked_extension_algebraic_line_support -- ../results/marked-extension-algebraic-line-support-p1.json
cargo run --release --features replication-prime --bin marked_extension_algebraic_line_support -- ../results/marked-extension-algebraic-line-support-p2.json
```

