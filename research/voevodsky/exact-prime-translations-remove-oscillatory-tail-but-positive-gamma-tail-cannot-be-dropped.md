# Exact prime translations remove the oscillatory tail, but the positive gamma tail cannot be dropped

The finite prime cosine terms need not be certified by integrating to a large
frequency cutoff. Plancherel converts each complete cosine multiplier into the
physical overlap

\[
\int_{\mathbb R}\cos(au)|\widehat f(u)|^2\frac{du}{2\pi}
=
\int f(t)f(t+a)dt.
\]

For compactly supported polynomial basis vectors this is a finite-interval
polynomial integral and can be enclosed directly. This removes the prime
oscillatory-tail problem entirely.

A hostile test then retained the gamma multiplier only through its first
positive crossing

\[
U_\Gamma\approx6.28983598884
\]

and dropped the pointwise-positive gamma tail. The resulting 80-dimensional
lower form is strongly indefinite, with smallest eigenvalue approximately

\[
-0.3001.
\]

This does not indicate a violation of the full form. Comparison with the
cutoff-convergence calculation shows that the positive high-frequency gamma
tail contributes essential coercivity to high polynomial modes; discarding it
throws away the mechanism that repairs the finite prime translations.

Therefore the corrected certification architecture is:

1. evaluate every prime translation exactly in physical coordinates;
2. retain, rather than discard, a quantitative positive lower form for the
   gamma tail;
3. combine that lower form with the endpoint and translation matrices before
   interval `LDL*`;
4. use the same gamma-tail coercivity to control the infinite-dimensional
   complement.

The remaining analytic object is a matrix/operator lower bound for the
positive multiplier

\[
\mathbf1_{|u|\ge U_\Gamma}
\bigl(\Re\psi(1/4+iu/2)-\log\pi\bigr),
\]

not an oscillatory prime-tail estimate.
