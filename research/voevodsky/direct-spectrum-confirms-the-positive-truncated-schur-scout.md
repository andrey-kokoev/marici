# The direct spectrum confirms the positive truncated Schur scout

## Question

Is the positive generalized-Schur result at cutoffs \(250\) and \(350\) an artifact of pseudoinverse block elimination?

## Claim boundary

No artifact is visible. Direct diagonalization of the full discretized truncated operator finds no eigenvalue below \(-10^{-10}\) at either cutoff or either fixed-cutoff resolution. This independently matches the positive generalized-Schur result. The continuum operator remains uncertified.

## Direct spectral test

At cutoff \(250\), the \((480,1800)\) discretization gave

\[
\lambda_{\min}(A_{250}^{\rm disc})
\approx-7.75\times10^{-16},
\]

and the refined \((560,2200)\) discretization gave

\[
\lambda_{\min}(A_{250}^{\rm disc})
\approx-1.09\times10^{-15}.
\]

Both values are at roundoff scale, with zero eigenvalues below the declared threshold \(-10^{-10}\). Their smallest reported positive eigenvalues agree at

\[
2.402244\times10^{-10}.
\]

At cutoff \(350\),

\[
\lambda_{\min}(A_{350}^{\rm disc})
\approx-8.96\times10^{-16},
\]

again with no eigenvalue below \(-10^{-10}\).

At cutoff \(150\), one eigenvalue barely crosses the threshold,

\[
\lambda_{\min}(A_{150}^{\rm disc})
\approx-1.02\times10^{-10},
\]

consistent with the previously identified low-cutoff instability.

## Relation to the Schur test

For cutoffs \(250\) and \(350\), two independent numerical projections agree:

1. direct full-matrix diagonalization is positive semidefinite to roundoff;
2. the rank-\(25\) range-compatible Schur complement is positive across three pseudoinverse tolerances.

The coarse form using \(40BB^*\) remains negative in two directions and is therefore too lossy.

## Residual

The smallest full-matrix positive eigenvalues are around \(2.4\times10^{-10}\), so direct spectral positivity has no usable numerical margin for interval promotion. These tiny values arise in the large discretized near-nullspace, not in the rank-\(25\) Schur block, whose observed margins are between \(0.0044\) and \(0.0138\) in the stable runs.

The first missing certification object is an interval enclosure of the rank-\(25\) full-tail Schur complement. It must include:

- certified concentration projection and threshold separation;
- full-frequency tail contribution or a monotone remainder bound;
- range compatibility;
- quadrature and spatial discretization errors;
- an interval lower bound for the least Schur eigenvalue.

## Disposition

The direct-spectrum rival is eliminated numerically at cutoffs at least \(250\). The first-prime local form has stable discovery-level positive evidence, but no continuum positivity theorem and no RH implication.
