# Source-Gram Coercivity Proves No Invisibility, Not Full Surjectivity

For a bounded Hilbert-space operator (T:X\to Y), the source-Gram bound

\[
T^*T\ge c^2I_X
\]

is equivalent to

\[
\|Tx\|\ge c\|x\|.
\]

It proves that no normalized source state becomes invisible. Consequently
(T) is injective, has closed range, and has a bounded inverse on its range
with norm at most (c^{-1}).

It does not prove surjectivity onto (Y). The smallest finite typed hostile is
the isometric embedding

\[
T=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}:
\mathbb R^2\to\mathbb R^3.
\]

Here

\[
T^*T=I_2,
\qquad
TT^*=\operatorname{diag}(1,1,0).
\]

Every source state is faithfully transported, while the third target direction
is unreachable.

## Two-sided theorem

Full Hilbert-space invertibility requires both source and target coercivity:

\[
T^*T\ge c^2I_X,
\qquad
TT^*\ge d^2I_Y.
\]

The first gives injective closed range. The second makes (T^*) injective, so
(\operatorname{ran}T) is dense. Closed plus dense gives surjectivity.

For Grothendieck's stated theorem—no normalized source state becomes invisible
during completion—the source-Gram lower bound is exactly sufficient. Calling
this full invertibility overstates the required result and introduces an
unnecessary target-coverage obligation. If a reciprocal or two-sided
correspondence is claimed, then the target Gram must be audited independently.

## Finite-stage warning

Square finite matrices conflate injectivity and surjectivity. Restricted-product
completion may change the effective source and target spaces, so the limit must
retain the arrow type (X\to Y). A positive determinant at each square cutoff
does not decide which one-sided property survives.

## Falsifiers

- Source coercivity is reported as surjectivity.
- Finite square typing is silently retained after source and target completions
  diverge.
- Target coverage is inferred without a bound on (TT^*).
- A target cokernel is mistaken for an invisible source state.
- Full invertibility is demanded when the theorem needs only bounded-below
  transport.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. Source injectivity, closed range, target surjectivity, and two-sided
invertibility were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The RH-bearing condition was weakened to its exact necessary type:
source-Gram coercivity excludes invisibility. Full invertibility was separated
as a two-sided theorem requiring the target Gram.
