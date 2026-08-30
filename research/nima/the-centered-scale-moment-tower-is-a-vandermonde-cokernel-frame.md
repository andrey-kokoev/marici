# The centered scale-moment tower is a Vandermonde cokernel frame

## Source construction

On one conductor fiber with \(r\) labels, let \(E\) average the fiber and let

\[
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_r),
\qquad
\lambda_i=\log n_i.
\]

Differentiating the scale-conjugated averaging operator gives the first
off-diagonal current

\[
C_1=(1-E)\Lambda E.
\]

The full centered moment tower is

\[
C_k=(1-E)\Lambda^kE,
\qquad
1\le k\le r-1.
\]

Since \(E\) has a one-dimensional image on the fiber, each \(C_k\) supplies
the centered vector

\[
v_k=(1-E)(\lambda_1^k,\ldots,\lambda_r^k)^T.
\]

## Exact theorem

If the \(\lambda_i\) are pairwise distinct, then

\[
v_1,\ldots,v_{r-1}
\]

form a basis of the mean-zero fiber complement.

Proof: adjoining the constant vector gives the evaluation matrix of
\(1,x,\ldots,x^{r-1}\) at the \(r\) values \(\lambda_i\). Its determinant
is the Vandermonde product

\[
\prod_{i<j}(\lambda_j-\lambda_i),
\]

which is nonzero exactly for distinct labels. Centering changes each nonconstant
column by a multiple of the constant column and therefore preserves this
determinant.

## Orientation consequence

The absolute Vandermonde determinant is a canonical cyclicity certificate. Its
sign becomes source-derived if the scale values themselves authorize the order

\[
\lambda_1<\cdots<\lambda_r.
\]

For arithmetic labels, strict monotonicity of \(\log n\) supplies that order
without inspecting zeros or fitting a scalar kernel.

This is stronger than choosing an arbitrary basis order: the same source
operator \(\Lambda\) both generates the missing directions and orders their
evaluation points.

The determinant-functor gate remains necessary under refinement. Adding labels
changes the ordered wedge by the parity of the induced shuffle, and the cutoff
comparison must carry that sign coherently.

## Finite falsifiers

The route fails on a fiber if:

- two distinct source states have the same scale value;
- an admitted constructor identifies labels while forgetting their scale;
- the moment operations are not source-authorized;
- refinement maps do not intertwine \(E\) and \(\Lambda\);
- completion destroys the moment-domain or its determinant comparison.

## Cross-sector consequence

Benincasa's globally connected integral relation graph need not be split into
connected components. A source-derived conductor filtration followed by the
centered moment filtration can make the global sparse problem block-triangular
without pretending the blocks are disconnected.

The next calculation is therefore finite and exact: compute the conductor-fiber
moment ranks and the determinant-functor shuffle signs before attempting global
Smith reduction.

