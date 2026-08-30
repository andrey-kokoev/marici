# The Core–Tail Schur Gap Is the No-Invisibility Compiler

Let a finite source Gram operator be split into an authorized core and tail:

\[
G_N=\begin{pmatrix}A_N&B_N\\B_N^*&C_N\end{pmatrix}.
\]

Assume that both diagonal channels are coercive. The missing datum is not
another diagonal observation, but the size of the cross coupling in their
native Gram metrics:

\[
R_N=A_N^{-1/2}B_NC_N^{-1/2}.
\]

For positive definite \(A_N,C_N\), the Schur-complement theorem gives

\[
G_N>0\quad\Longleftrightarrow\quad \|R_N\|<1.
\]

Thus finite no-invisibility is exactly a strict normalized angle between the
core and tail feature ranges. Completion-stable no-invisibility requires a
uniform Schur gap

\[
\sup_N\|R_N\|\le 1-\delta
\]

and uniform diagonal lower bounds. Indeed, if
\(A_N\ge aI\), \(C_N\ge cI\), and \(\|R_N\|\le\rho<1\), then

\[
G_N\ge (1-\rho)\min(a,c)I.
\]

If only the ordinary cross norm \(\|B_N\|\le b\) is available, then
\(b<\sqrt{ac}\) is sufficient and the sharper scalar lower bound is

\[
\mu(a,c,b)=
\frac{a+c-\sqrt{(a-c)^2+4b^2}}2>0.
\]

## Threshold and completion falsifiers

Positive diagonal blocks do not prevent cancellation. The threshold matrix

\[
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\]

has positive core and tail restrictions but kills \((1,1)\). More subtly,

\[
G_N=\begin{pmatrix}1&-(1-N^{-1})\\-(1-N^{-1})&1\end{pmatrix}
\]

is positive definite at every finite cutoff while its least eigenvalue is
\(N^{-1}\). Hence arbitrarily many finite injectivity certificates do not
exclude completion invisibility.

## Typed interpretation

The off-diagonal block must be the source-derived core–tail pairing. Replacing
it by an optimized coupling changes the source Gram rather than proving a
bound. Likewise, adding an unauthorized seam row can improve the Schur gap but
does not certify the original constructor family.

For Grothendieck's Euler completion, the finite theorem is now reduced to
three estimates: a core lower bound, a tail lower bound, and a uniform strict
bound on the normalized core–tail overlap. The third estimate is the genuinely
global gate. It is stronger than cutoffwise nonvanishing and weaker than
surjectivity of the completed correspondence.

## Assumptions

- The core/tail decomposition and its Gram blocks are source-authorized.
- The diagonal blocks are positive definite on the admitted quotient.
- The same Hilbert metrics are used to form the normalized coupling at every
  cutoff.

## Falsifiers

- Either diagonal lower bound collapses.
- The normalized coupling reaches one at a finite cutoff.
- Its norms approach one along a cutoff sequence.
- The claimed gap uses cutoff-dependent changes of frame with unbounded
  condition numbers.
- The gap appears only after adding a constructor outside the admitted source
  family.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to replace an abstract coercivity demand by finite block
conditions with a sharp hostile threshold.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The remaining RH-bearing estimate is identified as a uniform
core–tail Schur gap, and the smallest cancellation and completion-collapse
witnesses are explicit.
