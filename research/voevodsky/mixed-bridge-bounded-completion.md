# Bounded completion of mixed bridge certificates

## Question

Can finite full-Gram bridge certificates converge to a closed infinite-dimensional bridge while preserving Schur composition and coercivity?

## Claim boundary

This packet constructs one bounded Hilbert-space completion and records sufficient uniform estimates. It does not construct the unbounded common-core intertwiner required by the radial \(R_\zeta\) sector.

## Infinite fixture

Let \(K=X=\ell^2(\mathbb N)\). On each coordinate define the block

\[
G_n=\begin{pmatrix}
2&c_n\\c_n&1
\end{pmatrix},
\qquad c_n=\frac1{n+2}.
\]

The direct-sum operator \(G\) is bounded and positive. Eliminating \(K\) gives the diagonal Schur operator on \(X\)

\[
S_n=1-\frac{c_n^2}{2}.
\]

Since \(c_n\le1/2\), every \(S_n\ge7/8\). Thus the quotient form is bounded, closed, has zero radical, and remains uniformly coercive.

## Finite-to-closed convergence

Let \(C^{(N)}\) retain the first \(N\) cross coefficients and set the tail to zero. Then

\[
\lVert C-C^{(N)}\rVert=\frac1{N+2},
\qquad
\lVert S-S^{(N)}\rVert=\frac1{2(N+2)^2}.
\]

Both tend to zero. Hence the finite bridge certificates converge in operator norm to the closed bridge. Schur composition, quotient-form equality, and the mixed square pass to the limit because inversion of the fixed pivot \(2I\), multiplication, and subtraction are operator-norm continuous.

The finitely supported sequences form a common dense core, but boundedness makes core choice inessential: all operators extend uniquely to the whole Hilbert space.

## Hostile limit

Replace the uniform pivot \(2I\) by diagonal entries \(a_n=1/(n+2)\) while keeping \(c_n=1/(n+2)\). Then \(A^{-1}\) is unbounded and the finite pivot lower bound tends to zero. Finite invertibility alone no longer supplies bounded Schur continuity. This separates finite theorem survival from unbounded completion.

## Unbounded source gate

The current radial sector lacks an independently derived common-core intertwiner \(R_\zeta\), domain invariance, graph-norm bounds, and a closure theorem identifying the target operator. The bounded model cannot manufacture these data.

## Disposition

Mixed bridge certificates admit a genuine bounded closed completion under uniform pivot coercivity and operator-norm convergence of the transported blocks. The unbounded source comparison remains unproved. The next executable branch is a sufficient-hypotheses theorem for closed semibounded forms using a common form domain and relatively bounded cross term, followed by comparison with the recorded \(R_\zeta\) gates.

## Verification

- `research/voevodsky/checkers/check_mixed_bridge_bounded_completion.py`
- `research/voevodsky/results/mixed_bridge_bounded_completion.json`
