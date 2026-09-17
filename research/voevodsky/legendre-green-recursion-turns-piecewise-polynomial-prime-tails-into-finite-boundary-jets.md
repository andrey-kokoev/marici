# Legendre Green recursion turns prime tails into finite boundary jets

Let

\[
\mathcal L=-\frac d{dt}\left((1-t^2)\frac d{dt}\right),
\qquad \mathcal LP_n=n(n+1)P_n.
\]

On any smooth piece `[a,b]`, Green's identity gives

\[
\int_a^b hP_n\,dt
=\frac{[(1-t^2)(hP_n'-h'P_n)]_a^b}
       {n(n+1)}
 +\frac1{n(n+1)}\int_a^b(\mathcal Lh)P_n\,dt.
\]

Iterating `r` times gives boundary jets of
`h,Lh,...,L^(r-1)h`, divided by

\[
[n(n+1)]^r,
\]

plus the integral of `L^r h`. For every translated dangerous vector, each
piece of `h` is a polynomial of degree at most 999. The Legendre operator does
not increase degree, and its action is diagonal on the Legendre-polynomial
basis. After decomposing each piece into Legendre polynomials, the remaining
integrals are elementary endpoint antiderivatives; equivalently one may stop
at any finite `r` and bound the last integral.

Summing pieces makes interior boundary terms depend only on jumps of the
corresponding jets. The first Green boundary term reproduces the observed
`n^-1` jump tail after using the Bernstein bounds for `P_n'`; the derivative
jump and bulk terms gain at least one additional inverse power.

This supplies a finite exact certificate format:

1. Arb-enclose the dangerous vectors;
2. translate their polynomial coefficients on the five source intervals;
3. compute jump jets at the four internal breakpoints;
4. evaluate the Green recursion for all `n>=5000` with a geometric/rational
   majorant after a fixed number of iterations.

It avoids absolute total variation and preserves the cancellation responsible
for the small residual scout.
