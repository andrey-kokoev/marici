# Finite Pfaffian no-go: Lean packet

Source: `research/grothendieck/finite-cutoff-pfaffian-lift-no-go.md`.

`scalarTransferDefect : ℝ[X]` is `1-X^2`, the determinant of the scalar
transfer defect `I-C*C` for `C=[X]`. The module proves:

- it is positive at every real `x` with `|x|<1`;
- it is not a square in `ℝ[X]`;
- the latter obstruction is witnessed by evaluation at `x=2`, where the
  polynomial is `-3` but every real polynomial square is nonnegative.

`scalarSkewDoubling` is the canonical matrix

\[
\begin{pmatrix}0&b\\-b&0\end{pmatrix}.
\]

It is skew-adjoint over `ℝ`, and its determinant is `b^2` over any commutative
ring. Inserting `scalarTransferDefect` therefore produces its square, not a
polynomial square root. This is the smallest executable falsifier for a
generic algebraic Pfaffian lift.

Typing boundary: the non-square hostile is over `ℝ[X]`; the scalar doubling
determinant is polymorphic over commutative rings. Mathlib currently supplies
no Pfaffian definition, so the general even-dimensional identity
`det A = Pf(A)^2` for skew matrices remains an external algebraic interface.
So do any source symmetry forcing even divisor multiplicities and compatibility
of such a factorization under cutoff inclusion. Adjoining an analytic square
root is a coefficient extension, not an algebraic construction from the
original transfer ring.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans were run; the module remains outside
`MariciFormal.lean`.
