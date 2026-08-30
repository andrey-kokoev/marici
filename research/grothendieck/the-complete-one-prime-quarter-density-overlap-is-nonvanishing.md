# The complete one-prime quarter-density overlap is nonvanishing

## Bounded question

Does the normalized reciprocal cross overlap vanish inside one complete
prime-power depth tower before archimedean boundary amplitudes are attached?

## Logarithmic-derivative tower

Fix a prime \(p\), put

\[
r=p^{-1/2},
\]

and let \(\theta\) be the local Mellin phase. The quarter-density feature at
depth \(k\geq1\) is

\[
u_k=\sqrt{\log p}\,r^{k/2}e^{ik\theta}.
\]

The diagonal norm is

\[
\sum_{k\geq1}|u_k|^2
=(\log p)\frac{r}{1-r}.
\]

The reciprocal bilinear overlap is

\[
\sum_{k\geq1}u_k^2
=(\log p)\frac{re^{2i\theta}}{1-re^{2i\theta}}.
\]

Hence the normalized overlap is

\[
\rho_p^{\rm LD}(\theta)
=\frac{(1-r)e^{2i\theta}}{1-re^{2i\theta}}.
\]

It is never zero. Moreover,

\[
\frac{1-r}{1+r}
\leq
|\rho_p^{\rm LD}(\theta)|
\leq1.
\]

Thus the complete local depth tower occupies a strict acute sector in the
normalized reciprocal comparison.

## Euler-log tower

For Euler-log normalization the feature is

\[
u_k=\frac1{\sqrt{k}}r^{k/2}e^{ik\theta}.
\]

Its diagonal norm is

\[
-\log(1-r),
\]

and its reciprocal overlap is

\[
-\log(1-re^{2i\theta}).
\]

Because \(|r|<1\), the latter cannot vanish: the analytic logarithm is zero
only when its argument is one, which would require \(re^{2i\theta}=0\).
Continuity on the phase circle therefore gives a positive prime-dependent
lower bound for the normalized overlap.

## Aggregation boundary

At any finite prime cutoff, tensor-product aggregation multiplies the local
normalized overlaps and remains nonzero. Direct-sum aggregation instead adds
cross entries and can cancel.

An infinite tensor product may still lose its overlap if the product of local
reserves tends to zero. The logarithmic-derivative lower bounds already permit
this because

\[
\prod_p\frac{1-p^{-1/2}}{1+p^{-1/2}}
=0.
\]

Thus local nonvanishing does not supply a uniform global reserve.

## Source boundary

This theorem concerns the pure arithmetic depth features. The actual staircase
features also contain the interval amplitudes \(B_{p,k}[A](z)\). Those amplitudes
need not preserve the geometric depth progression. Their archimedean coupling
is the first place the local acute law can fail.

## Result

Reciprocal cancellation is not generated within a single coherent arithmetic
prime tower. It can enter only through:

- additive mixing of distinct primes;
- collapse of an infinite tensor-product reserve;
- source-dependent archimedean interval amplitudes;
- completion and seam currents.

The next audit should therefore compare tensor-product Euler aggregation with
the actual additive staircase/archimedean compression. Confusing these two
aggregations would manufacture or erase cancellations.
