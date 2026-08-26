# Pointwise Strong Closure Does Not Control Normalized Moving States

Let

\[
P_N=|e_N\rangle\langle e_N|
\]

on (\ell^2). For every fixed state (x),

\[
\|P_Nx\|=|x_N|\to0,
\]

so (P_N\to0) strongly. The Gram operators also converge strongly:

\[
P_N^*P_N=P_N\to0.
\]

Nevertheless

\[
\|P_N\|=1
\]

for every (N), witnessed by the moving normalized state (x_N=e_N).

Thus weak transport plus pointwise source-Gram convergence gives pointwise
strong closure, but not operator-norm closure or a theorem uniform over all
normalized cutoff states.

This matters because the RH-facing claim has the form

\[
\inf_{\|x\|=1}\|J_Nx\|\ge c>0
\]

or excludes every normalized state from becoming invisible. Such a statement
is governed by smallest singular values and operator norms, not convergence on
each fixed vector.

## Uniform upgrade

To pass from pointwise strong closure to uniform state control, one needs an
additional source theorem such as:

- operator-norm convergence;
- collective compactness plus a uniqueness/no-tail theorem;
- a uniform finite-rank or tightness estimate;
- direct cutoff-independent lower and upper frame bounds.

Compactness of the admissible normalized state family can also make pointwise
convergence uniform when the operator family is equicontinuous. The full unit
sphere of an infinite-dimensional Hilbert space is not norm compact.

## Falsifiers

- Strong convergence holds but operator norms remain nonzero.
- A moving normalized state saturates the residual.
- Pointwise Gram convergence is used to claim a uniform eigenvalue bound.
- Compactness of the infinite-dimensional unit sphere is assumed.
- Uniformity is obtained only after excluding tail states without source
  authority.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. Fixed-state strong convergence, operator norm, moving witnesses, and
uniform lower bounds were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The positive Gram-closure theorem was sharply bounded to fixed states.
The RH-strength quantifier remains a separate norm/tightness theorem excluding
moving normalized tail witnesses.
