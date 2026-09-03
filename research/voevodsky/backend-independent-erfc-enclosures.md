# Backend-independent erfc enclosures

## Question

Can the accelerated gamma series be enclosed without relying on the failing `mpmath.iv.erfc` implementation or installing a new interval package?

## Claim boundary

Two analytic enclosure formulas cover the required erfc range. High-precision fixtures confirm containment, but directed enclosures for elementary constants and functions remain unimplemented.

## Taylor enclosure

For nonnegative \(x\),

\[
\operatorname{erf}(x)
=
\frac2{\sqrt\pi}
\sum_{k\geq0}
\frac{(-1)^kx^{2k+1}}{k!(2k+1)}.
\]

Let

\[
t_k(x)=\frac{x^{2k+1}}{k!(2k+1)}.
\]

The consecutive absolute-term ratio is

\[
\frac{t_{k+1}(x)}{t_k(x)}
=
\frac{x^2(2k+1)}{(k+1)(2k+3)}.
\]

Choose \(K\) so that this ratio at the interval upper endpoint is at most \(r<1\) for all subsequent terms. Then the omitted absolute tail obeys

\[
\left|
\sum_{k\geq K}(-1)^kt_k(x)
\right|
\leq
\frac{t_K(x)}{1-r}.
\]

Consequently a finite rational-polynomial sum plus this absolute remainder encloses

\[
\operatorname{erfc}(x)=1-\operatorname{erf}(x).
\]

Unlike a bare alternating-series assertion, this remains valid in the middle range where the initial term magnitudes increase.

## Large-argument enclosure

Repeated integration by parts gives

\[
\operatorname{erfc}(x)
=
\frac{e^{-x^2}}{\sqrt\pi x}
\left[
\sum_{k=0}^{K-1}
(-1)^k
\frac{(2k-1)!!}{(2x^2)^k}
+R_K(x)
\right].
\]

The remainder has the next alternating sign and satisfies

\[
|R_K(x)|
\leq
\frac{(2K-1)!!}{(2x^2)^K}.
\]

This gives one-sided upper and lower bounds rather than an asymptotic decimal approximation.

## Hybrid split

The tested split is:

- Taylor plus absolute-tail bound for \(0\leq x\leq4\);
- integration-by-parts bound for \(x\geq4\).

At \(x=4\), both enclosures overlap. Fixtures covered

\[
0.02,1,3,4,6,12.
\]

The largest observed high-precision enclosure widths were approximately

\[
2.04\times10^{-14}
\]

for the Taylor branch and

\[
2.93\times10^{-14}
\]

for the asymptotic branch. These are containment checks against high-precision `mpmath`, not certified interval output.

Increasing \(K\) can reduce these widths below the rank-two error allocation.

## Directed elementary layer still required

The finite sums can use exact rationals once the argument interval is enclosed. A complete implementation must still outward-enclose:

- \(\pi\) and \(\sqrt\pi\);
- \(x^2\) and interval powers;
- \(e^{-x^2}\);
- multiplication and division endpoints.

These can be implemented with rational range reduction and Taylor remainders, but doing so is a separate arithmetic kernel. High-precision decimal padding is not a substitute.

## Gamma-series application

For each accelerated gamma term:

1. outward-enclose its erfc argument;
2. choose the Taylor or large-argument branch from the entire argument interval;
3. enclose the erfc value;
4. combine it with the exact finite coefficient;
5. sum all terms outward;
6. add the proved omitted-series and \(R=40\) integral tails;
7. propagate four sample intervals through the rank-two error budget.

No package installation is required for this route.

## Disposition

The failed interval erfc primitive is not a mathematical blocker. Explicit Taylor and integration-by-parts enclosures replace it. The remaining implementation boundary is a small directed-rounding elementary kernel, followed by gamma-series accumulation and determinant propagation.

## Verification

- `research/voevodsky/backend-independent-erfc-enclosures-v1.json`
- `research/voevodsky/checkers/check_backend_independent_erfc_enclosures.py`
- `research/voevodsky/results/backend_independent_erfc_enclosures.json`
