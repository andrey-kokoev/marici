# The canonical seam jet restores orientation to the linear moment tower

## Bounded question

Can the one-sided theta compression acquire a source-derived second
orientation factor without replacing the physical readout by its square?

## Seam jet ports

On the arithmetic circle, the cut distribution has winding coefficients

\[
 \langle e_n,\delta_0\rangle=1.
\]

Applying the circle Laplacian generates the canonical jet

\[
 \delta_0,A\delta_0,A^2\delta_0,\ldots,
\]

whose coefficient matrix is

\[
 V(n,k)=n^{2k},
 \qquad n\ge1,quad k\ge0.
\]

For ordered labels `n_1<...<n_r` and consecutive ports
`k=0,...,r-1`,

\[
 \det[n_i^{2(k-1)}]_{i,k=1}^r
 =\prod_{1\le i<j\le r}(n_j^2-n_i^2)>0.
\]

The seam jet is therefore a source-derived totally positive observation
system on the winding labels.

## Linear moment tower

Compose the completed labelled kernel `K(t,n)=b(t,n^2)` with these ports:

\[
 M_k(t)=\sum_{n\ge1}n^{2k}K(t,n).
\]

These are not arbitrary extra observables.  Since multiplication by `n^2` is
the spectral action of `A`, they are the energy moments of the same completed
seam state.  They belong to the joint heat--energy jet of the theta source.
They are **not** asserted to be reconstructible from derivatives of the single
scalar `Phi`: differentiating the completion polynomial opens an additional
raw heat channel, and discarding it would assume the faithfulness at issue.

For ordered scales `t_1<...<t_r`, infinite Cauchy--Binet gives

\[
\begin{aligned}
 \det[M_{k-1}(t_i)]_{i,k=1}^r
 =\sum_{n_1<\cdots<n_r}
 &\det[K(t_i,n_j)]\\
 &\times\det[n_j^{2(k-1)}].
\end{aligned}
\]

The first determinant has the fixed sign `epsilon_r` by packet 112; the
Vandermonde factor is positive.  Absolute Gaussian convergence justifies the
limit from finite label truncations.  Hence

\[
 \boxed{
 \operatorname{sgn}det[M_{k-1}(t_i)]
 =\varepsilon_r
 \quad\text{for every }r.}
\]

The complete linear moment tower is strictly sign-regular at all finite
orders.

## What was hiding the theorem

Scalar trace compression retains only the zeroth seam port `delta_0`.  A
single port has no higher minors, so it necessarily erases the orientation
certificate.  The certificate reappears when the entire source-generated jet
is retained:

\[
 \boxed{
 \text{one scalar port forgets orientation; the seam jet remembers it}.}
\]

This is exactly analogous to the jointly faithful score towers and multiple
endpoint ports found in other Marici sectors.  Higher observations are not
independent fitted measurements; they are the transport closure of the
original cut distribution under the source Laplacian.

## Relation to the generalized Laguerre tower

The moment functions `M_k`, together with the raw heat channel opened by
differentiating the completion polynomial, control derivatives of the
positive Riemann kernel with respect to heat scale. They therefore provide a
strictly richer labelled input from which generalized Laguerre and Hankel
expressions may be assembled. But a sign-regular moment tower on the positive
scale axis is not yet the
statement that the cosine transform `Xi` has only real zeros.

The remaining bridge must show that modular sewing transports this real-scale
Chebyshev orientation into coefficientwise positivity of the vertical
self-comparison of `Xi`.  Without that theorem, identifying the two towers
would be circular.

## Next gate

Write the generalized Laguerre form of `Xi` explicitly as a quadratic
contraction of the seam-jet moment matrix.  Then ask whether the contraction
is a Schur complement or Gram minor with a source-fixed positive metric.

The falsifier is a hostile positive integral-spectrum kernel whose seam-jet
moment tower is sign-regular by the theorem above but whose Fourier transform
has a negative generalized Laguerre coefficient.  Such an example would show
that even complete jet closure is insufficient without modular sewing.
