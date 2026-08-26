# The Two-Sided Schur Incidence Test Beats the Global Square Sum

Let the normalized core–tail coupling have entries

\[
r_{ij}=\langle e_i,A^{-1/2}BC^{-1/2}f_j\rangle.
\]

Define the absolute incidence loads

\[
\alpha=\sup_i\sum_j|r_{ij}|,
\qquad
\gamma=\sup_j\sum_i|r_{ij}|.
\]

The matrix Schur test gives

\[
\|A^{-1/2}BC^{-1/2}\|
\le \sqrt{\alpha\gamma}.
\]

Therefore \(\alpha_N\gamma_N\le(1-\delta)^2\) uniformly in the cutoff,
together with uniform diagonal coercivity, proves completion-stable source
coercivity. More precisely,

\[
G_N\ge
\left(1-\sqrt{\alpha_N\gamma_N}\right)
\min(a,c)I.
\]

This compiler is stronger than the global Hilbert–Schmidt budget for diffuse
incidence. For \(R=\frac12I_5\), the squared Hilbert–Schmidt norm is \(5/4\),
so the preceding scalar budget fails, whereas

\[
\alpha=\gamma=\frac12
\]

certifies an operator-norm gap of \(1/2\).

## Why both incidence directions are mandatory

A row bound alone does not control accumulation onto a tail mode. For

\[
R=\begin{pmatrix}1/2\\1/2\\1/2\\1/2\end{pmatrix},
\]

every row load is \(1/2\), but the sole column load is \(2\) and \(\|R\|=1\).
The associated block Gram reaches the cancellation threshold. The dual
failure occurs when a single core mode accumulates many tail incidences.

## Scope and loss

The absolute-value Schur test is sufficient, not necessary, because it erases
phase cancellation. A normalized Hadamard pattern can have row and column
absolute sums at the threshold while its operator norm remains strictly below
one. Failure of this test therefore requests a sharper operator estimate; it
does not produce an invisible state.

Weighted Schur tests may improve the certificate. A weight used only as an
auxiliary proof multiplier does not change the source frame and may vary with
cutoff, provided it proves one uniform bound for the unchanged native
incidence matrices. Uniform conditioning is required only if the weights are
instead used to redefine the source topology or norm.

## Theta/Tate consequence

The next arithmetic estimate can be organized as two bounded incidence
questions:

1. How much normalized tail mass can couple to any fixed core atom?
2. How much normalized core mass can accumulate on any fixed tail atom?

Uniform bounds whose product is below one prove the required no-invisibility
theorem. Pointwise Euler decay answers neither question without uniform
summation in both directions.

## Falsifiers

- Only row sums or only column sums are bounded.
- Signed sums replace sums of absolute incidences.
- Auxiliary proof weights are silently promoted into a retyped source norm.
- Failure of the sufficient Schur test is reported as an actual kernel.
- Incidences are computed after adding an unauthorized constructor row.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
9/10. The target was a local certificate that survives diffuse high rank.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The square-sum false negative is repaired by a two-sided incidence
compiler, and the exact one-sided accumulation obstruction is isolated.
