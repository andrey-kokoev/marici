# Oriented two-thimble coupled positivity theorem

## Universal identity

Let an oriented contour block decompose as

\[
I=I_1+I_2,\qquad J=J_1+J_2,
\]

where \(I_j\) is a thimble denominator integral and \(J_j\) its logarithmic
moment. Put

\[
\lambda=\beta-i\alpha.
\]

Then the cone numerator of the paired logarithmic barycenter is

\[
\boxed{
\mathcal N
=\Re\left[\lambda(J_1+J_2)\overline{(I_1+I_2)}\right].
}
\]

Expanding gives

\[
\mathcal N=N_{11}+N_{22}+N_{12},
\]

where

\[
N_{jj}=\Re(\lambda J_j\overline{I_j}),
\]

and

\[
N_{12}
=\Re\left[\lambda
\left(J_1\overline{I_2}+J_2\overline{I_1}\right)\right].
\]

If \(I\ne0\), then

\[
\beta\Re(J/I)+\alpha\Im(J/I)
=\frac{\mathcal N}{|I|^2}.
\]

This identity retains the oriented complex phases. It requires neither
componentwise positivity nor a common thimble phase.

## Coupled dominance theorem

If

\[
N_{11}>0
\]

and

\[
\boxed{N_{11}>-\left(N_{22}+N_{12}\right),}
\]

then the exact oriented two-thimble block lies strictly inside the required
cone.

More conservatively, it is sufficient that

\[
N_{11}>|N_{22}|+|N_{12}|.
\]

The proof is the displayed expansion. Although algebraically elementary, the
statement identifies the correct source quantities after a Stokes jump:
self terms and oriented cross interference must be bounded only after the
Picard--Lefschetz block is assembled.

## First theta block

For the post-jump block at

\[
(a,b)=(0.5,6.03),
\]

the traced thimble quadrature gives

\[
\begin{aligned}
N_{11}&\approx 0.1258518801083633,\\
N_{22}&\approx-0.0546477184742985,\\
N_{12}&\approx-0.0146538473394111.
\end{aligned}
\]

Therefore

\[
\boxed{\mathcal N\approx0.0565503142946537>0,}
\]

and

\[
\frac{\mathcal N}{|I_1+I_2|^2}
\approx1.2796779867852124.
\]

The conservative defect is

\[
|N_{22}|+|N_{12}|\approx0.0693015658137096,
\]

so the principal dominance safety factor is approximately

\[
\frac{N_{11}}{|N_{22}|+|N_{12}|}\approx1.816.
\]

The competitor self term and cross term are both negative. Positivity is not
being hidden in favorable interference; the principal thimble dominates the
entire oriented defect.

These numbers are non-certified path quadrature. The theorem itself is exact.

## Global target

For each Stokes chamber, form the source-canonical Picard--Lefschetz blocks.
Within a two-thimble chamber, prove a uniform bound

\[
\frac{-(N_{22}+N_{12})}{N_{11}}<1.
\]

At later walls, replace the two-term formula by the corresponding finite
oriented block matrix

\[
\mathcal N=\sum_{j,k}\Re(\lambda J_j\overline{I_k}).
\]

The sharp falsifier is the first parameter at which the oriented defect ratio
reaches one. This falsifier is local to a canonical Stokes chamber and does
not inspect Xi zeros.

The full matrix expression is basis-independent: simultaneous
Picard--Lefschetz mutation of the thimble periods and contragredient mutation
of the physical-cycle coefficients leave \(I\), \(J\), and \(\mathcal N\)
unchanged. Consequently a wall is a change of coordinates, not a new scalar
positivity event, provided the relative class is reconstructed correctly.
See `theta-relative-cycle-mutation-invariance.md`.

On the ray \(a=1/2\), upward-flow tracing places the first two-thimble chamber
between \(b=5.98828529\ldots\) and \(b=9.64392578\ldots\). Exact-path samples
at \(b=7,8,9,9.6\) all pass; the defect ratio decreases from \(0.4344\) to
\(0.2444\), while the paired cone increases. See
`theta-first-two-thimble-chamber-reconnaissance.md`.

Artifacts:

- checkers/theta_stokes_upward_thimble_trace.py
- results/theta-stokes-upward-thimble-trace.json
- checkers/theta_stokes_paired_cycle_crosscheck.py
- results/theta-stokes-paired-cycle-crosscheck.json
- checkers/theta_oriented_two_thimble_identity.py
- results/theta-oriented-two-thimble-identity.json
