# All separated rank-two bounds do not imply Gram positivity

## Exact hostile kernel

Consider the continuous even periodic difference kernel

\[
k(d)=1-\sin^4(d/2).
\]

Since `0<=sin^4(d/2)<=1`,

\[
0\le k(d)\le k(0)=1
\]

for every real `d`. Therefore every two-translate matrix

\[
\begin{pmatrix}
1&k(d)\\
k(d)&1
\end{pmatrix}
\]

is positive semidefinite. The separated rank-two inequality holds globally.

## Rank-four failure

Use the four translates

\[
0,\quad\frac\pi2,\quad\pi,\quad\frac{3\pi}2.
\]

Their circulant Gram matrix has first row

\[
(1,3/4,0,3/4).
\]

Its exact Fourier eigenvalues are

\[
\frac52,\quad1,\quad-\frac12,\quad1.
\]

Thus the matrix has a negative direction despite passing every two-point test.

Equivalently,

\[
k(d)=\frac58+rac12\cos d-rac18\cos2d,
\]

so its Fourier coefficient at frequency two is negative.

## Consequence for the Weil kernel

A proof of

\[
|K_\sigma(d)|\le K_\sigma(0)
\]

for every separation would establish all rank-two Toeplitz minors but would not imply positive definiteness. Likewise, complete monotonicity information corresponding only to low confluent orders cannot replace higher translate ranks.

The first genuinely faithful spatial theorem remains PSD of every finite Toeplitz matrix. Bochner positivity is a statement about the entire Fourier measure, not pairwise correlation bounds.

## Disposition

Treat the global rank-two source inequality as a valid intermediate theorem and falsifier, not an RH proof. Any promotion to full Weil positivity must add all ranks or directly produce a positive Fourier measure.
