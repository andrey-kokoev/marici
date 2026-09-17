# Rank-160 scout shows a positive rank-80 complement Schur margin

At `L=.55`, the two-prime Legendre calculation was extended to 160 modes.
With frequency cutoff 2000, the smallest compression eigenvalues are

\[
\lambda_{80}=2.5761\times10^{-8},\quad
\lambda_{120}=2.5055\times10^{-8},\quad
\lambda_{160}=2.4109\times10^{-8}.
\]

Writing the rank-160 matrix relative to the first 80 modes and taking the
exact numerical Schur complement gives

\[
\lambda_{\min}(S_{160/80})=3.0929\times10^{-4}.
\]

Thus the next 80 modes carry a substantially larger conditional margin than
the original low block. The directed complement programme should first
certify this rank-160-over-rank-80 Schur matrix, then bound modes above 159 by
logarithmic archimedean coercivity. This ordering avoids applying a coarse
infinite-tail estimate directly at mode 80.
