# Norm Closure Preserves Invertibility Only with a Uniform Inverse Bound

Let (T_N:X\to X) be invertible bounded operators and suppose

\[
\|T_N-T\|\to0.
\]

Finite invertibility alone does not imply that (T) is invertible. The exact
hostile is

\[
T_N=\operatorname{diag}(1,N^{-1})
\longrightarrow
T=\operatorname{diag}(1,0)
\]

in operator norm. Every finite stage is invertible, but

\[
\|T_N^{-1}\|=N
\]

and the limit has a kernel.

The positive theorem is standard but decisive: if

\[
\sup_N\|T_N^{-1}\|\le M<\infty,
\]

then (T) is invertible. For sufficiently large (N),

\[
\|T_N^{-1}(T-T_N)\|<1,
\]

so

\[
T=T_N\bigl(I+T_N^{-1}(T-T_N)\bigr)
\]

is invertible by the Neumann series. Moreover the limiting lower bound is at
least (1/M).

Thus source tightness and operator-norm closure solve the moving-forward-tail
problem, but RH-strength strict nonvanishing still requires uniform inverse
control. These are independent gates.

## Passing fixture

For

\[
S_N=\operatorname{diag}(1,1+N^{-1}),
\]

one has (S_N\to I) in norm and (\|S_N^{-1}\|\le1). The limit remains
invertible.

## Source-facing conclusion

Grothendieck's finite Euler transitions being invertible and source-tight can
establish a well-defined completed operator. They do not exclude a completed
kernel unless one additionally proves a cutoff-independent inverse bound, or
directly proves the completed operator bounded below. This is precisely the
isolated RH theorem, not a technical afterthought.

## Falsifiers

- Forward operators converge in norm while inverse norms diverge.
- Every finite determinant is nonzero but the smallest singular value tends to
  zero.
- A compact or tight limit is mistaken for a bounded-below limit.
- Uniform inverse control holds only after scalar normalization by the desired
  divisor.
- Invertibility is checked on a finite core without a tail lower bound.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. Forward norm error, smallest singular value, inverse norm, and limiting
invertibility were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The positive tightness theorem was placed at its exact boundary:
operator-norm closure constructs the limit, while a uniform inverse bound is
the independent condition preserving zero-freeness. This matches
Grothendieck's stated RH obstacle exactly.
