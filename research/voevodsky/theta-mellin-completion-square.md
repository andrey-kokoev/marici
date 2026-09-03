# Theta–Mellin completion square

## Question

What source object and map replace the invalid scalar embedding of theta coefficients into the Euler coefficient space?

## Claim boundary

This constructs the classical theta–Mellin comparison and reciprocal completion. It proves no statement about zero locations.

## Function-valued source

Let

\[
\psi(u)=\sum_{n\geq1}e^{-\pi n^2u}=\frac{\theta(u)-1}{2}.
\]

The source is the family of Gaussian coefficient functions of \(u\), not any fixed-\(u\) scalar coefficient sequence.

For \(\operatorname{Re}s>1\), termwise Mellin integration gives

\[
\int_0^\infty e^{-\pi n^2u}u^{s/2}\frac{du}{u}
=
\pi^{-s/2}\Gamma(s/2)n^{-s}.
\]

Therefore

\[
\int_0^\infty\psi(u)u^{s/2}\frac{du}{u}
=
\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The coefficient 1 appears only after integration; it is not the fixed-parameter Gaussian coefficient.

## Reciprocal completion

Using theta reciprocity and splitting at \(u=1\),

\[
\Lambda(s)=
\int_1^\infty\psi(u)
\left(u^{s/2}+u^{(1-s)/2}\right)\frac{du}{u}
+
\frac{1}{s-1}-\frac{1}{s}.
\]

Both the large-\(u\) kernel and the polar correction are invariant under \(s\mapsto1-s\). In centered coordinates \(s=1/2+w\), this is \(w\mapsto-w\).

Gaussian domination on \(u\geq1\) supplies the cutoff-limit interchange for compact spectral subsets. The small-\(u\) contribution is not discarded: reciprocity transports it to the large-\(u\) integral and leaves the explicit polar term.

## Disposition

The missing comparison is a Mellin square from function-valued theta coefficients to completed meromorphic functions. This square repairs the coefficient-space mismatch and gives reciprocal naturality with normalization retained. It does not put unsmoothed zeta coefficients in \(B_\epsilon\), and it supplies no RH implication.

## Verification

- `research/voevodsky/theta-mellin-completion-square-v1.json`
- `research/voevodsky/checkers/check_theta_mellin_completion_square.py`
- `research/voevodsky/results/theta_mellin_completion_square.json`
