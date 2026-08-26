# Feedback actuator reachability (WP277)

## Dual gate to observability

Retain WP276's fully observing sensor \(C=I_2\), but admit only one actuator

\[
B_1=\begin{pmatrix}1\\0\end{pmatrix}.
\]

For arbitrary feedback row \(K=(k_1,k_2)\), the closed-loop generator is

\[
A_{\mathrm{cl}}=-B_1KC
=\begin{pmatrix}-k_1&-k_2\\0&0\end{pmatrix}.
\]

The covector \((0,1)\) annihilates the actuator. Starting from
\(z=(0,1)^T\), feedback changes the first coordinate but leaves the second
derivative exactly zero. The controller knows the error and still cannot move
it to the target.

## Complementary actuator

With zero uncontrolled drift, the one-port controllability matrix has rank
one. Adjoining a second independent actuator gives \(B=I_2\); diagonal positive
feedback then has eigenvalues \(-k_1\) and \(-k_2\).

The added actuator must be source-derived. Algebraically completing the matrix
does not establish a physical operation on flavor couplings.

## Classification

Full observation without full actuator reachability is neither a complete
selector nor an executable preparation instrument. The first nonfaithful arrow
is from controller command to physical flavor-state displacement.

Nonzero source drift can enlarge controllability through repeated drift-action
commutators, but that possibility requires its own exact controllability audit.

Run `uv run --with sympy python
research/flavor/checkers/wp277_feedback_actuator_reachability.py` for the exact
rank-one obstruction, invariant covector, hostile initial state, and
complementary-actuator spectrum.
