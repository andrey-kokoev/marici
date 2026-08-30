# The Bordered Prime Transfer Has an Exact Order-Three Determinant Split

## Finite valuation chain

For the depth-\(N\) bordered prime colligation, the transfer readout is

\[
g_N(q)=1+q+\cdots+q^N.
\]

Its doubled determinant section has the exact factorization

\[
g_N(q)^2
=e^{2q}e^{q^2}R_N(q),
\]

where

\[
R_N(q)=g_N(q)^2e^{-2q-q^2}.
\]

This normalization is fixed by the source jets:

\[
(\log g_N^2)'(0)=2,
\qquad
(\log g_N^2)''(0)=2
\]

for \(N\ge2\). Therefore

\[
(\log R_N)'(0)=0,
\qquad
(\log R_N)''(0)=0.
\]

The factors \(e^{2q}\) and \(e^{q^2}\) are respectively the primitive and
prime-square currents already derived from the valuation chain. They are not
counterterms fitted to the final scalar section.

## Infinite local chain

For \(|q|<1\), passage to the full valuation chain gives

\[
g(q)^2=(1-q)^{-2}
\]

and

\[
R(q)=(1-q)^{-2}e^{-2q-q^2}.
\]

Its logarithm is

\[
\log R(q)=\sum_{k\ge3}\frac{2q^k}{k}.
\]

This is exactly the order-three regularized determinant split: linear and
quadratic cumulants remain explicit boundary channels, while the connected
tail begins at cubic order.

## Finite terminal current

At finite depth,

\[
\log g_N(q)^2
=2\sum_{k\ge1}\frac{q^k}{k}
-2\sum_{j\ge1}\frac{q^{(N+1)j}}{j}.
\]

The second sum is the terminal cutoff current. It begins at degree \(N+1\)
and must remain inside \(R_N\). Dropping it would falsely identify a finite
chain with the completed local factor.

## Completion contract

For a global source-derived operator \(K_X(z)\), the corresponding statement
would require:

- compact-local boundedness and convergence in Schatten class three;
- uniform bounded invertibility of \(I+K_X(z)\);
- explicit primitive, square, seam, and archimedean boundary blocks;
- no definition of \(K_X\) from a scalar determinant ratio.

This entry proves only the local bordered-transfer factorization. It does not
construct the global \(K_X\) or the determinant–Evans comparison unit.

