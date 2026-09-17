# Support-limit form-core convergence preserves the signed prime sum

Let

\[
\mathcal D= C_c^\infty(\mathbb R),\qquad
\mathcal D_L=\{f\in\mathcal D:\operatorname{supp}f\subset[-L,L]\}.
\]

The global Weil form is determined on the strict inductive limit
`D=union_L D_L`. No absolute majorization of the finite-prime contribution is
needed in passing to this limit.

## Exact stabilization of the arithmetic part

For `f,g in D_L`, a translated overlap

\[
\int \overline{f(x)}g(x+\log n)\,dx
\]

vanishes whenever `log n>2L`. Consequently

\[
Q_{\rm fin}(f,g)
=-\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}
  \operatorname{Re}\int\overline{f(x)}g(x+\log n)\,dx
\]

is a finite, signed sum. Every arithmetic cutoff `X>=e^{2L}` gives exactly the
same value. Thus arithmetic-cutoff convergence is eventual equality on every
core vector, and all cancellation between prime powers is retained.

## Archimedean form core

The archimedean multiplier has growth `O(log(2+|u|))`. Its closed-form domain
is the weighted Fourier space

\[
\mathcal H_{\log}=
\{f\in L^2:\int\log(2+|u|)|\widehat f(u)|^2du<\infty\}.
\]

Smooth frequency truncation followed by physical cutoff and mollification
shows that `C_c^infty` is dense in this norm: frequency truncation controls the
weighted tail by monotone convergence; physical cutoffs converge after the
frequency truncation because the resulting function is Schwartz; mollifiers
then give compactly supported smooth approximants.

The two endpoint functionals are continuous on every fixed-support core and
pass through this approximation. The finite arithmetic sum is also continuous
on `D_L`, since each translation is an `L2` contraction.

## Consequence

If every fixed-support form `Q_L` is nonnegative on `D_L`, then the global Weil
form is nonnegative on `D`: each test vector belongs to one `D_L`, where its
prime sum has already stabilized exactly. Closure in `H_log` extends the
archimedean part without replacing the signed arithmetic sum by an absolute
bound.

Therefore support-limit convergence is not an additional numerical gate. The
remaining substantive gate is positivity for every finite `L` (including all
successive prime-power thresholds).
