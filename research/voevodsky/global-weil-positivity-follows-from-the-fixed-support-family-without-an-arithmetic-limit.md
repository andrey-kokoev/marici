# Global Weil positivity follows from the fixed-support family without an arithmetic limit

Let `Q` be the coded Weil form on `C_c^infty(R)`, and let `Q_L` be its
restriction to functions supported in `[-L,L]`. Assume:

1. every prime-power coefficient, endpoint term, and Fourier normalization in
   `Q_L` agrees with the source Weil criterion;
2. `Q_L(f)>=0` for every `L` and every `f in C_c^infty([-L,L])`.

Then `Q(f)>=0` for every `f in C_c^infty(R)`: choose any `L` containing the
support of `f`. The arithmetic sum has already stabilized exactly at
`n<=e^{2L}`, so no interchange of an infinite signed sum with a limit occurs.

Since `C_c^infty` is a core for the logarithmically weighted archimedean form,
this positivity extends to the closed form domain wherever the source
criterion requires that closure. Therefore, once the fixed-support family is
certified and the source normalization is audited, the support-limit step is
formal and introduces no additional analytic or numerical error.

At present this implication cannot be invoked to assert global positivity:
the all-`L` premise remains open, and the exact source-identity audit has not
been completed. In particular, a conditional asymptotic Hankel discrepancy
criterion is not a proof of the premise.
