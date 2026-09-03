# The limit-circle hard edge does not select the minus-one branch

## Question

Does square summability or minimal-solution theory select the \(p=-1\) solution of the parabolic hard-edge recurrence?

No. With \(a_n\asymp n^4\) and defect limit two, the indicial roots are \(-1\) and \(-2\). Both model solutions satisfy

\[
\sum_{n\ge1}|n^{-1}|^2<\infty,
\qquad
\sum_{n\ge1}|n^{-2}|^2<\infty.
\]

Moreover,

\[
\sum_{n\ge1}\frac1{a_n}<\infty.
\]

Thus the Jacobi endpoint is in the non-Carleman regime compatible with limit-circle behavior. The \(p=-2\) solution is minimal relative to \(p=-1\), but both are square summable. Neither Hilbert-space membership nor positivity at the exterior point determines the coefficient of the slower \(p=-1\) branch.

The selected continuous Weibull measure therefore carries additional boundary data at the limit-circle endpoint. Branch selection must be expressed through its Weyl boundary functional, Nevanlinna parameter, or an equivalent source-derived condition. A generic boundary condition can cancel the \(p=-1\) coefficient and leave \(p=-2\).

## Disposition

Reject unconditional recessive-branch selection from the indicial equation and square summability. The next leaf is `weibull-weyl-boundary-coefficient`: identify the boundary functional of the selected continuous measure and prove that its \(p=-1\) connection coefficient is nonzero.

## Claim boundary

This does not show that the selected measure chooses \(p=-2\). It shows that the existing asymptotic and Hilbert-space data do not decide between the two branches.
