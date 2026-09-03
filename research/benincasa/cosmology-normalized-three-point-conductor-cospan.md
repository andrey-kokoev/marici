# Minimal normalized three-point conductor cospan

Retaining the two central wall occurrences separately gives two chains,
\(0\to1\) and \(-1\to0\). In row order

1. central `b+x` at \(r=0\),
2. central `a+y` at \(r=0\),
3. moving `b+x-E` at \(r=1\),
4. moving `a+y-E` at \(r=-1\),

the boundary matrix is

\[
\begin{pmatrix}
-1&0\\
0&1\\
1&0\\
0&-1
\end{pmatrix}.
\]

Each column has zero augmentation, so the chain satisfies the required
boundary-of-boundary condition. Forgetting the distinct central labels recovers
the endpoint orientation \((1,-1)\).

This constructs the minimal combinatorial cospan, not its source geometry. The
existing endpoint chain uses coordinate `xi`; no source map identifies `xi`
with exceptional coordinate \(r\) while matching all four wall labels. Until
that map exists, the cospan cannot carry residues or Gauss–Manin transport.
