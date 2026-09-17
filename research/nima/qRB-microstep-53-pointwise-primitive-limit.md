# qRB microstep 53: pointwise primitive limit

For each fixed label `n`, the sieve coefficient is eventually constant:

- if `n=1`, every prime sieve retains it;
- if `n>1`, choose a prime divisor `p` of `n`; once `p` is included, the label is removed permanently.

Therefore the indicator of the retained label set converges pointwise to the indicator of `{1}`. Since each theta cell `phi_n` is positive,

$$
\prod_{p\in S}D_p\Phi
\longrightarrow
\phi_1
$$

pointwise as the finite prime sets exhaust the primes.

This proves the discrete pointwise spectral seed, but not convergence in a Hilbert or trace topology after summing over all labels.
