# The Tate character and logarithmic current have different continuity thresholds

## Adjacent-label test

Let \(u_n\) denote the analytic tail–seam atom at logarithmic label \(\log n\),
with Gram kernel

\[
\langle u_n,u_m\rangle=
A\!\left(\left|\log(n/m)\right|\right).
\]

For \(n=p^k\), compare the arithmetic atom with its adjacent nonmatching
label \(n-1\). Their analytic distance is

\[
\lVert u_n-u_{n-1}\rVert^2=
2\left[A(0)-A\!\left(\log\frac{n}{n-1}\right)\right].
\]

This is the sharp local continuity denominator for any typed prime-power
functional.

## Cusp threshold

Suppose the kernel has a nonzero one-sided cusp at the origin:

\[
A(0)-A(h)=c h+o(h),
\qquad
c>0.
\]

Since

\[
\log\frac{p^k}{p^k-1}\sim p^{-k},
\]

the adjacent-atom norm is asymptotic to

\[
\sqrt{2c}\,p^{-k/2}.
\]

The undifferentiated local Tate logarithm has coefficient proportional to

\[
\frac1k p^{-k/2}.
\]

It is therefore exactly at the cusp continuity scale. Adjacent collapse alone
does not disprove continuity of the determinant character.

## Differentiation changes the verdict

Differentiating with respect to spectral height inserts \(\log p\). The
coefficient scale becomes

\[
\frac{\log p}{k}p^{-k/2}.
\]

Its ratio to the cusp norm grows like \(\log p\). Thus the logarithmic current
cannot be continuous in the same bare analytic Gram topology when the cusp
asymptotic holds with a finite nonzero coefficient.

This separates two objects:

- the multiplicative Tate anomaly character may sit at the analytic
  continuity threshold;
- its spectral logarithmic derivative requires an additional graph-norm,
  boundary-jet, or arithmetic valuation port.

The distinction is structural. Differentiation is an extra constructor and
cannot be transported through completion without its own continuity proof.

## Exact prototype

For the cusp kernel \(A(h)=e^{-h}\) and \(n=p^k\),

\[
\lVert u_n-u_{n-1}\rVert=
\sqrt2\,p^{-k/2}.
\]

The undifferentiated coefficient-to-norm ratio is exactly

\[
\frac1{k\sqrt2},
\]

while the differentiated ratio is

\[
\frac{\log p}{k\sqrt2}.
\]

The first is uniform in \(p\); the second diverges.

## Theta gate

The prototype does not establish the theta kernel cusp coefficient. The next
source calculation is to derive the exact small-shift asymptotic of the native
tail–seam Gram kernel, with endpoint orientation retained. Three outcomes are
possible:

1. a linear cusp, giving the borderline character and divergent current split;
2. smoother than linear decay, already excluding the character on the bare
   analytic carrier;
3. rougher decay, leaving room for both functionals.

## DPC verdict

Prime-power type jumps do not by themselves exclude the Tate determinant
character from the analytic completion. Under the natural cusp scaling, they
exclude its differentiated logarithmic current. Any proof that treats those
two continuity questions as identical is invalid.

## Verification

`check_rh_tate_character_current_threshold.py` verifies the exact exponential
cusp prototype for multiple prime powers and confirms uniform character ratios
and divergent differentiated-current ratios.
