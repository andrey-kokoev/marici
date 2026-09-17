# qRB microstep 54: sieve convergence in source L1

Assume the completed source satisfies

$$
\Phi=\sum_{n\ge1}\phi_n\in L^1,
\qquad
\phi_n\ge0.
$$

The finite sieve remainders `S_S` decrease pointwise to `phi_1`, and

$$
0\le S_S-\phi_1\le\Phi-\phi_1\in L^1.
$$

Dominated convergence therefore gives

$$
\|S_S-\phi_1\|_{L^1}\longrightarrow0.
$$

Thus prime-sieve exhaustion is not merely pointwise: it converges in the source L1 topology under the natural integrability hypothesis.

This still does not imply convergence of differentiated observers, boundary traces, or relative Hilbert norms; those require graph-norm estimates.
