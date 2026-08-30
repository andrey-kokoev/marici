# Correlated mixture labels and zero-marginal conditioning

For two finite mixture label sets, arbitrary classical correlation is encoded
by one joint nonnegative table `pi_jk`.  The complete generator is the weighted
sum over the existing labelled pairs.  Marginals alone are insufficient.

For three blocks, the complete joint tensor `pi_jkl` is required.  The even-
and odd-parity distributions on three binary labels have identical pair
marginals but distinct joint laws.

If one marginal tends to zero as

\[
\pi_{jk}=\varepsilon r_k,
\]

the conditional row is

\[
\frac{\pi_{jk}}{\sum_l\pi_{jl}}
=\frac{r_k}{\sum_lr_l}.
\]

The limit depends on the projective approach direction `[r]`.  This is a
simplex-face Rees coefficient datum, not a new Cut incidence.
