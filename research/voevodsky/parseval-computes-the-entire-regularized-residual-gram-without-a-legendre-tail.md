# Parseval computes the entire residual Gram without a Legendre tail

The mode-by-mode residual extension is unnecessary. Let `P` be the retained
92-dimensional concentration-plus-endpoint space, let `Z=P-D` be the
regularized trial map, and let `A` denote the gamma-floor lower operator. The
full residual is

\[
R=(I-PP^*)AZ.
\]

Therefore its complete Gram matrix is the finite matrix

\[
R^*R=Z^*A^2Z-(P^*AZ)^*(P^*AZ).
\]

No Legendre cutoff appears in this identity.

For the present lower operator,

\[
A=q_R I+M_{\mathbf1_{[-R,R]}(q-q_R)}+P_{2,3}+E,
\]

where `P_{2,3}` is the finite translation operator and `E` is rank two.
Every term in `Z^*A^2Z` is directly computable:

- multiplier--multiplier terms by one frequency integral;
- translation--translation terms by exact finite overlap integrals;
- multiplier--translation terms by Fourier phase multiplication;
- endpoint terms from the two endpoint vectors.

Equivalently, evaluate the complete piecewise Fourier symbol before squaring,
then add the endpoint cross terms. This is exactly the global residual-Gram
mechanism already used in the prior regularized polynomial pipeline.

Disposition: stop extending residual Legendre blocks beyond 4999. Assemble
and interval-certify the `92 by 92` Parseval residual Gram instead. The
finite-mode scouts remain useful cross-checks of its partial sums.
