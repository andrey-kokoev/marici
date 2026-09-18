# The first-zero unchanged-Evans Hilbert residual is strictly negative

## Question

Does the unchanged Evans state satisfy the tested Hilbert membership condition at the first nontrivial zeta zero?

## Certified zero and regularization

Arb encloses the first zero at

\[
\rho_1=\frac12+iT,
\]

where

\[
T=14.13472514173469379045725198356247027078425711569924317568556746014996342981
\pm8.84\times10^{-76}.
\]

For

\[
H(T)=\int_0^\infty |\xi(1/2+ix)|^2\frac{2T}{x^2-T^2}\,dx,
\]

the singularity is removable. On the central cell, write

\[
\xi(1/2+ix)=(x-T)g_T(x).
\]

A radius-\(0.1\) Cauchy enclosure gives \(|g_T|\le0.202\). Excluding a central half-width \(10^{-5}\) therefore costs at most \(1.63\times10^{-11}\).

## Validated finite integral

A 160-bit interval subdivision with 30,001 cells gives

\[
\int_0^{30}|\xi(1/2+ix)|^2\frac{2T}{x^2-T^2}\,dx
\le-0.14339124473816492.
\]

The interval extension is evaluated separately on every cell; no point-sample quadrature error estimate is used.

## Tail envelope

For \(s=1/2+ix\), \(x\ge60\), and \(N=\lceil x\rceil\), the one-term Euler--Maclaurin formula gives

\[
\zeta(s)=\sum_{n=1}^{N}n^{-s}+\frac{N^{1-s}}{s-1}-\frac12N^{-s}
+s\int_N^\infty(\{u\}-\tfrac12)u^{-s-1}\,du.
\]

The four absolute-value bounds are respectively

\[
2\sqrt N-1,
\qquad \frac{\sqrt N}{|s-1|},
\qquad\frac1{2\sqrt N},
\qquad\frac{|s|}{\sqrt N}.
\]

Using \(x\le N\le x+1\) shows their sum is at most \(4\sqrt{x+1}\). Thus

\[
|\zeta(1/2+ix)|\le4\sqrt{x+1}.
\]

For \(z=1/4+ix/2\), first-term complex Stirling with

\[
|R_1(z)|\le\frac{1}{12|z|\cos^2(\arg z/2)}\le\frac1{3x}
\]

gives

\[
|\xi(1/2+ix)|^2
\le25x^{9/2}e^{-\pi x/2}.
\]

Directed evaluation sharpens the required constant to at most

\[
20.617895.
\]

Also

\[
\frac{2T}{x^2-T^2}\le\frac{31}{x^2},
\]

with directed constant at most \(29.930515\). Hence

\[
\left|\int_{60}^{\infty}\cdots\,dx\right|
\le775\int_{60}^{\infty}x^{5/2}e^{-\pi x/2}\,dx
\le1.656\times10^{-34}.
\]

Validated interval subdivision on \([30,60]\) contributes at most \(6.02\times10^{-18}\) in absolute value.

## Result

Combining the three ranges yields

The composed Arb upper endpoint is

\[
H(T)\le
-0.14339124473816490429329282952152519454697140312
+4.77\times10^{-48}<0.
\]

Therefore the unchanged Evans state fails this necessary Hilbert membership condition at the first certified zeta zero.

## Claim boundary

This rejects the unchanged Evans state as the filler of the existing source-generated positive response graph under the tested membership criterion. It does not reject a divisor-preserving modified-history state, construct `U_G4`, prove or disprove RH, or identify the arithmetic crossing defect.

## Disposition

The unchanged-Evans membership branch is falsified. The remaining constructive programme must change the state or expose an independent authoritative `U_G4`; it may not reuse unchanged membership as an assumption.

Verification:

- `research/voevodsky/checkers/check_first_zeta_zero_arb_enclosure.py`
- `research/voevodsky/checkers/check_first_zero_evans_arb_finite_integral.py`
- `research/voevodsky/checkers/check_evans_tail_envelope_constants.py`
- `research/voevodsky/checkers/check_first_zero_evans_arb_tail.py`
