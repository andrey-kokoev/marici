# Explicit order-zero interval remainder audit

## Question

Does the archimedean source supply the bounded interval remainder required by the logarithmic Gårding criterion?

## Claim boundary

This packet verifies the explicit digamma-minus-log bound and its consequence conditional on the stated Carleman boundary identity and localization constants. It does not certify the finite low-block ground eigenvalue.

## Multiplier bound

For \(\Re z>0\),

\[
\log z-\psi(z)=
\int_0^\infty e^{-zt}
\left(\frac1{1-e^{-t}}-\frac1t\right)dt.
\]

The bracket lies strictly between zero and one. Therefore

\[
|\log z-\psi(z)|\le\frac1{\Re z}.
\]

At \(z=1/4+iu/2\), this gives a bound of four. Moreover,

\[
\max_{u\ge0}
\frac{1+u}{\sqrt{1/16+u^2/4}}
=\sqrt{20},
\]

attained at \(u=1/4\). Consequently,

\[
\left|
\Re\psi(1/4+iu/2)-\log(1+|u|)
\right|
\le4+\frac12\log20.
\]

No zero data or positivity hypothesis enters.

## Interval budget

Using the source-stated half-line comparison between zero-extension and spectral Dirichlet logarithms, whose Carleman norm is \(\pi\), the principal order-zero budget is

\[
C_0=\pi+4+\frac12\log20.
\]

The full interval constant is \(C_L=C_0+C_{\rm loc}(L)\), where the two-chart localization commutator remains to be inserted with the chosen Fourier normalization. Thus the relative coefficient is \(\eta=0\): no logarithmic principal reserve is lost.

For the synthetic choice \(C_{\rm loc}=0\), \(C_{\rm prime}=2\), and \(L=1\), the checker finds the first positive threshold among powers of two at \(M=32768\).

## Low-block gate

The natural logarithmic operator has a positive-growing high spectrum. If its local form is positive definite, the finite low-block pivot approaches a fixed ground eigenvalue, corresponding to \(p=0\), not compact-shadow decay. But a positive lower bound for that ground eigenvalue is the remaining local positivity problem and cannot be inferred from compact resolvent.

## Disposition

The archimedean interval remainder is order zero up to the explicit localization constant, so the strict-relative-bound gate is passed at \(\eta=0\). Remaining independent gates are:

1. source evaluation of \(C_{\rm loc}(L)\) and prime constants;
2. interval-enclosed positivity of the finite low block;
3. finite-tail coupling control.

## Verification

- `research/voevodsky/checkers/check_explicit_order_zero_interval_remainder.py`
- `research/voevodsky/results/explicit_order_zero_interval_remainder.json`
- `research/grothendieck/explicit-uniform-digamma-minus-log-bound.md`
