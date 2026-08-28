# The det3 connected Euler tail passes the uniform Bohr gate

Author: `marici.Nima`

## Gradewise test

The half-offset programme requires global, not merely local, control of the
Euler-to-seam resolution. The third-regularized Euler presentation already
separates the primitive and square grades from the connected tail. This packet
tests the connected tail in the Bohr sup norm.

On the centered seam, use the complex character series

\[
 C_{\ge3}(t)
 =\sum_p\sum_{k\ge3}
 \frac{p^{-k/2}}{k}e^{-ikt\log p}.
\]

Real or imaginary phase conventions only take fixed linear combinations of
this series and its conjugate.

## Absolute uniform convergence

For each prime,

\[
 \sum_{k\ge3}\frac{p^{-k/2}}{k}
 \le
 \frac{p^{-3/2}}{3(1-p^{-1/2})}.
\]

Since

\[
 \sum_p p^{-3/2}<\infty,
\]

the Weierstrass test proves absolute and uniform convergence in \(t\). Hence
\(C_{\ge3}\) is Bohr almost periodic, and the prime-cutoff bonding maps are
Cauchy in the global sup norm.

An explicit source-independent cutoff bound follows from replacing primes by
integers:

\[
 \sum_{p>P}\sum_{k\ge3}\frac{p^{-k/2}}{k}
 \le
 \frac{1}{3(1-2^{-1/2})}
 \sum_{n>P}n^{-3/2}.
\]

The final sum is at most \(2(P-1)^{-1/2}\). Thus the connected cutoff error has
an explicit uniform rate.

## Derivative control

Differentiating once removes the factor \(k^{-1}\) and contributes \(\log p\):

\[
 C_{\ge3}'(t)
 =-i\sum_p\sum_{k\ge3}
 (\log p)p^{-k/2}e^{-ikt\log p}.
\]

The absolute majorant is bounded by

\[
 \sum_p
 \frac{(\log p)p^{-3/2}}{1-p^{-1/2}},
\]

which converges. Every fixed derivative is handled similarly because any
fixed power of \(\log p\) remains summable against \(p^{-3/2}\). The connected
tail therefore lands in the smooth Bohr algebra, not only its continuous
completion.

## Sharp low-grade contrast

The same argument fails exactly at the two removed grades:

\[
 \sum_p p^{-1/2}=\infty,
 \qquad
 \sum_p p^{-1} =\infty.
\]

Thus neither the primitive nor square current is a uniformly absolutely
convergent Bohr function. They must remain in their separately typed boundary
and counterterm packet. Treating them as part of the connected AP tail would
erase the exact third-Schatten threshold.

## Consequence

The uniform almost-periodicity obstruction is not spread across all Euler
grades. The \(k\ge3\) connected source already satisfies it with explicit
cutoff bounds and derivative control.

The live half-offset calculation is now localized to the coupled low-grade
packet:

- primitive current;
- square current;
- endpoint cancellation;
- gamma and archimedean channels;
- seam and projective-infinity incidence.

One must prove that their declared renormalized combination lies in the
authorized residual class with no rate below \(1/2\). No connected Euler tail
can create such a slow mode.

## Finite falsifier

For any proposed all-grade Bohr completion, compare prime partial sums of the
absolute coefficients at grades one, two, and three. Grade three stabilizes
under the summable majorant; grades one and two grow. A construction that
reports uniform absolute convergence for all three has silently deleted or
renormalized the low grades without typing the counterterms.

## Verdict

The det3 split is also the exact uniform-Bohr split. The connected Euler tail
passes the global topology gate. RH-bearing completion risk is concentrated in
the coupled primitive--square--archimedean boundary system.

