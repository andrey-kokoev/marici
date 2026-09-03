# Near-null direction separates gamma log-log growth from prime exponential rank cost

## Question

What do the first gamma correction and prime error do on the explicit near-null polynomial `p_m(y)=(1-y)^m`?

## Claim boundary

The first gamma correction is structurally aligned with the leading moment measure and grows only logarithmically in the saddle location, hence as `log log m` at fixed mesh ratio. A coefficientwise prime bound instead pays `4^m`. This identifies the prime term, not the first gamma correction, as the obstruction to a growing-rank small-heat theorem based on this direction. No sign for the exact prime quadratic form is proved.

## Alpha family

For `alpha>0`, define

\[
d_n^{(\alpha)}(\kappa)
=(1+n\kappa)^{-\alpha}-(1+(n+1)\kappa)^{-\alpha}.
\]

Its moment measure is

\[
d_n^{(\alpha)}(\kappa)
=\frac1{\Gamma(\alpha)}
\int_0^\infty
r^{\alpha-1}e^{-r}(1-e^{-\kappa r})e^{-n\kappa r}\,dr.
\]

For `p_m(y)=(1-y)^m`, its energy is

\[
E_m(\alpha,\kappa)
=\frac1{\Gamma(\alpha)}
\int_0^\infty
r^{\alpha-1}e^{-r}(1-e^{-\kappa r})^{2m+1}\,dr.
\]

The leading gamma matrix is `alpha=1/2`.

## First gamma correction

The scaled small-heat expansion contains

\[
c^{-1/2}\bigl(\log(1/t)-\log c+C_\Gamma\bigr).
\]

Because

\[
\left.\partial_\alpha c^{-\alpha}\right|_{\alpha=1/2}
=-c^{-1/2}\log c,
\]

the first correction energy on `p_m` is

\[
\left.\partial_\alpha E_m(\alpha,\kappa)
\right|_{\alpha=1/2}
+C_\Gamma E_m(1/2,\kappa).
\]

Moreover,

\[
\partial_\alpha\log E_m
=-\psi(\alpha)+\mathbb E_{m,\alpha,\kappa}[\log r],
\]

where the expectation uses the normalized positive density in the integral above. The saddle satisfies

\[
e^{-\kappa r_m}\asymp m^{-1},
\qquad
r_m\asymp \kappa^{-1}\log m.
\]

Standard two-sided localization around this saddle gives, for fixed `kappa` in a compact subinterval of `(0,infinity)`,

\[
\partial_\alpha\log E_m(1/2,\kappa)
=\log\log m+O_\kappa(1).
\]

Thus the correction-to-leading ratio is

\[
\frac{\text{first gamma correction}}
{\log(1/t)E_m(1/2,\kappa)}
=O_\kappa\!\left(
\frac{1+\log\log m}{\log(1/t)}
\right).
\]

It remains perturbative whenever `log log m=o(log(1/t))`.

## Prime bound on the same direction

The coefficient `l1` norm of `(1-y)^m` is `2^m`. If every relevant prime-error matrix entry is bounded by

\[
C t^{-A}e^{-c/t},
\]

then its unnormalized quadratic form is bounded by

\[
C t^{-A}4^m e^{-c/t}.
\]

The gamma energy `E_m(1/2,kappa)` decays only polynomially in `m`, up to powers of `log m`, because its saddle is at `r_m` and `e^{-r_m}\asymp m^{-1/\kappa}`. Hence the coarse prime estimate becomes nonperturbative only when `m` reaches order `1/t`. Below a sufficiently small constant multiple of `1/t`, exponential prime suppression defeats the coefficient growth.

This is only a magnitude estimate. Cancellation in the exact prime quadratic form may improve it, while adverse alignment may make the bound relevant.

## Strongest falsification attempt

The calculation treats one explicit near-null family, not all polynomial directions. It also uses saddle localization at fixed mesh ratio; confluent and large-ratio limits require separate uniform estimates. Therefore it cannot establish a rank window for the full matrix without a minimax theorem showing that all near-null directions have comparable localization.

## Disposition

The first gamma correction does not explain loss of rank-uniformity. The next source-level target is the exact prime quadratic form on polynomial amplitudes, preserving its translation phases rather than replacing it by the coefficientwise `4^m` bound.