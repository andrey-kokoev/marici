# The order port is faithful on every finite mean-zero fiber

## Ordered-fiber operator

For an ordered fiber of size \(r\), define

\[
S_r(i,j)=\operatorname{sgn}(i-j).
\]

This is the finite matrix of the order kernel. It is real and skew-symmetric.

## Kernel theorem

If \(S_rx=0\), subtracting consecutive row equations gives

\[
x_i+x_{i+1}=0.
\]

Hence every kernel vector is alternating.

- If \(r\) is even, the boundary row equation forces the alternating
  coefficient to vanish. Thus \(S_r\) is invertible.
- If \(r\) is odd, the kernel is spanned by

\[
(1,-1,1,-1,\ldots,1)^T.
\]

This vector has coordinate sum one. It is not in the mean-zero subspace.

Therefore

\[
\ker S_r\cap\ker E_r=\{0\},
\]

where \(E_r\) denotes the sum or averaging readout. The order port is
injective on every finite mean-zero fiber, regardless of parity.

## Meaning

The two-label quarter-turn was not an accidental low-dimensional feature.
Source order detects the entire finite contrast sector that scalar averaging
forgets.

The parity distinction remains typed:

- even fibers have a nondegenerate skew form;
- odd fibers have a one-dimensional order-kernel line;
- the averaging port detects that odd kernel line.

Thus the pair consisting of averaging and order is jointly faithful on every
finite ordered fiber.

## What remains open

Finite joint faithfulness does not imply a cutoff-independent lower bound as
\(r\) grows. The next calculation is the smallest singular value of

\[
\begin{pmatrix}
E_r\\
S_r
\end{pmatrix}
\]

in the source coefficient topology and after conductor refinement.

The finite theorem also does not identify the theta/Tate boundary residual.
The source must still derive:

- the order kernel on the actual carrier;
- its old/new conductor block;
- its compatibility with Mellin transport;
- the primitive, square, seam, and archimedean defect produced by the coupling.

## Falsifier

Any proposed finite order port fails if it has a nonzero mean-zero kernel
vector. This is a direct rank test requiring no scalar zero information.

