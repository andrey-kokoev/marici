# Reciprocal-integer Weibull families resolve beta dependence but not its formula

## Question

What do exact generalized-gamma determinant families imply for the hard-edge logarithmic coefficient \(c(\beta)\)?

For \(\alpha=1\) and \(\beta=1/p\), exact moments reduce to factorial Hankel matrices. After subtracting

\[
\frac{\alpha}{\beta}\Delta^2(n\log n),
\]

the degree-twenty estimates of the coefficient multiplying \(\alpha^2\log n\) are

\[
\begin{array}{c|cccc}
\beta&1&1/2&1/3&1/4\\
\hline
c_{20}(\beta)&0.4923&0.5654&0.7597&0.9992.
\end{array}
\]

The endpoints agree with the exact Laguerre value \(c(1)=1/2\) and the quarter-Weibull candidate \(c(1/4)=1\). The intermediate sequences are distinct, but the \(\beta=1/2\) values still drift materially across degrees fourteen through twenty, so these data do not authorize a closed interpolation formula.

## Disposition

Resolve that \(c(\beta)\) is potential-dependent while retaining \(c(1/4)=1\) as a finite candidate. Reject the previously guessed formula \((1+\beta)/(4\beta)\), which fails the intermediate exact grids.

The next leaf is `half-weibull-log-limit`: extend or analytically solve the \(\beta=1/2\) family to discriminate its limiting coefficient before proposing a general law.

## Claim boundary

Finite reciprocal-integer families do not prove convergence or continuity in \(\beta\). Agreement at \(1/4\) remains diagnostic.
