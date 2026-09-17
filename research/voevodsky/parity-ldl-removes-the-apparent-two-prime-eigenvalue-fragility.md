# Parity LDL removes the apparent two-prime eigenvalue fragility

The completed rank-80 matrix has smallest ordinary eigenvalue about

\[
2.6582\times10^{-8}
\]

and condition number about `2.42e8`. Direct eigenvalue interval propagation
would therefore demand unnecessarily small global matrix errors.

After splitting into the exact even and odd Fourier-parity blocks, unpivoted
`LDL*` gives

\[
\min_j d_j^{\rm even}=0.00191378281745
\]

at zero-based pivot index 1, and

\[
\min_j d_j^{\rm odd}=0.0164957590677
\]

at index 2. Every pivot is positive.

The certification margin is therefore governed by pivots of size `1e-3`, not
by the `1e-8` smallest eigenvalue. Directed assembly should preserve the
parity blocks from the start and run interval `LDL*` separately. This also
prevents the even--odd cross-block implementation error found in the initial
scout.

The finite-range gamma quadrature, exact physical prime overlaps, endpoint
matrix, and 476-moment tail can each be enclosed entrywise before elimination.
The resulting pivot margins are comparable to the already certified
first-prime calculation.
