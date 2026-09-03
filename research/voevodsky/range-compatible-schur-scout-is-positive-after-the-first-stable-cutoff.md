# The range-compatible Schur scout is positive after the first stable cutoff

## Problem

Does replacing the coarse factor-\(40\) correction by the truncated tail pseudoinverse restore positivity on the rank-\(25\) concentration block?

## Bold conjecture

The two negative directions in the coarse sufficient form are artifacts of replacing the exact tail resolvent by its worst uniform bound.

## Named rivals

1. The exact Schur complement also has a negative direction.
2. Numerical tail nullspaces violate range compatibility enough to invalidate the pseudoinverse.
3. Positivity at cutoff \(150\) disappears under spatial refinement or larger frequency cutoff.

## Risky consequences

The conjecture predicts a positive least generalized-Schur eigenvalue, small range residual, and agreement at fixed cutoff under quadrature refinement.

## Strongest falsification attempt

At cutoff \(150\), the runs \((n_x,n_u)=(320,1000)\) and \((400,1400)\) gave

\[
\lambda_{\min}(S_{150})
\approx0.00101578
\]

and

\[
\lambda_{\min}(S_{150})
\approx0.00102421.
\]

Both had zero negative Schur eigenvalues and range-compatibility residual approximately \(2.31\times10^{-6}\). At cutoff \(250\),

\[
\lambda_{\min}(S_{250})
\approx0.00656926,
\]

again with zero negative eigenvalues and residual \(8.25\times10^{-7}\).

The cutoff-\(100\) result was negative,

\[
\lambda_{\min}(S_{100})
\approx-0.00387889,
\]

and is retained as the strongest truncation rival. Its tail block had only eight numerically positive modes, compared with twenty at cutoff \(150\) and forty-four at cutoff \(250\).

## Exact residual

The positive values are not converged in frequency: the least eigenvalue changes from about \(0.00102\) to \(0.00657\). The pseudoinverse cutoff is fixed at a relative scale of \(10^{-10}\), and no tolerance sweep has been performed. The range residual is small but nonzero. The infinite positive frequency tail and interval enclosures are absent.

## Disposition

The conjecture survives the first fixed-cutoff refinement. The coarse factor-\(40\) certificate is rejected, while the range-compatible exact-Schur route remains viable and positive in every run with cutoff at least \(150\). This is a discovery-level numerical result, not a positivity certificate and not an RH implication.

The next discriminating test is a pseudoinverse-tolerance sweep at fixed cutoffs \(150\) and \(250\), followed by a frequency-cutoff sequence that does not confound spatial resolution.
