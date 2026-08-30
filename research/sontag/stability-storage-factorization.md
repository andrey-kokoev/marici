# Stability and storage factorization

Owner: `marici.Sontag`

## Bounded question

When does a quadratic storage law factor a transition into certified strict
decay rather than mere energy nonincrease?

## Typed constructor

For `x+=Ax` and `V(x)=x^T P x`, the exact coherence law is
`A^T P A-P=-Q`. The storage port is coercive when `P` is positive definite;
strict decay requires `Q` positive definite.

With `A=diag(1/2,1/3)` and `P=I`, one obtains
`Q=diag(3/4,8/9)`. Both forms are positive definite, so the finite system has
a strict Lyapunov certificate.

## Hostile falsifier

Take `A=diag(1,1/2)` and `P=I`. Then
`Q=diag(0,3/4)` is only semidefinite. Storage never increases, but the nonzero
mode `e_1` is fixed forever. Energy monotonicity alone therefore does not
factor through asymptotic stability.

## Completion gate and verdict

The finite-dimensional gate is uniform coercivity of `P` and strict positivity
of `Q`. Verdict: exact strict-storage factorization for the witness; obstruction
to promoting semidefinite dissipation to asymptotic stability in the hostile.
