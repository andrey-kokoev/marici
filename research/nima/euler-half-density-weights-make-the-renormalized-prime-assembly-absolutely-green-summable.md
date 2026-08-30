# Euler half-density weights make the renormalized prime assembly absolutely Green summable

## Mixed Euler weight

The primitive and square endpoint coefficients are

\[
p^{-1/2-\sigma}
\]

and

\[
\frac12p^{-1},
\]

respectively. Their mixed coefficient is

\[
w_p(\sigma)
=
\frac12p^{-3/2-\sigma},
\qquad
\sigma\ge0.
\]

This is the weight attached to the completed primitive--square Adams block.

## Prime growth of the local packet

All coefficients in the four-grade packet, its five-grade covariant
derivative, the base completion channel, and the wall residue are polynomial
of degree at most two in

\[
L=\log p.
\]

The Gaussian grade norms and the quarter-gap resolvent are independent of
\(p\). Therefore, for each fixed finite graph order \(m\),

\[
\|\Psi_p^{\mathrm{rel}}\|_{\operatorname{graph}_m}
+
\|\mathcal C^{-1}\Psi_p^{\mathrm{rel}}\|_{\operatorname{graph}_m}
\le
C_m
\left(
1+(\log p)^2
\right).
\]

The same type of bound holds for the covariantly differentiated five-grade
packet and the complete base-plus-curvature source.

## Absolute prime summability

Hence

\[
\sum_p
|w_p(\sigma)|
\left(
1+(\log p)^2
\right)
\le
\frac12
\sum_{n\ge2}
\frac{1+(\log n)^2}{n^{3/2}}
<
\infty.
\]

Because

\[
p^{-\sigma}\le1,
\]

the bound is uniform for every \(\sigma\ge0\), including the seam value
\(\sigma=0\).

Thus the renormalized mixed packets are absolutely summable in every declared
finite-order Green graph rung.

## Hilbert direct-sum bound

If prime fibers are kept orthogonal before scalar readout, then

\[
\sum_p
|w_p(\sigma)|^2
\left(
1+(\log p)^2
\right)^2
\le
\frac14
\sum_{n\ge2}
\frac{(1+(\log n)^2)^2}{n^3}
<
\infty.
\]

Therefore the prime-labeled source belongs to the Hilbert direct sum, again
uniformly through \(\sigma=0\).

This direct-sum statement does not require scalar prime cancellation.

## Wall assembly

The exact wall coefficient satisfies

\[
|\rho_p|
\le
C\left(
\log p+(\log p)^2
\right).
\]

Consequently,

\[
\sum_p
|w_p(\sigma)\rho_p|
<
\infty
\]

uniformly for \(\sigma\ge0\). The coefficient-wall channel itself therefore
assembles absolutely; it is not merely a weak distribution after the mixed
primitive--square weight is applied.

## Cutoff convergence

Let \(X\) be the prime cutoff and \(N\) the theta-label cutoff. With the
Euler--Maclaurin wall packet retained at every \(N\),

\[
\sum_{p\le X}
w_p(\sigma)\Psi_{p,N}^{\mathrm{ren}}
\]

is Cauchy as \(N\to\infty\) in the Green graph, uniformly in \(X\) and
\(\sigma\ge0\). The prime tail then tends to zero as \(X\to\infty\) by the
absolute majorant above.

Thus the \(N\)- and \(X\)-completion limits may be interchanged by dominated
convergence.

## What remains conditional

The analytic summability theorem does not prove that the scalar assembly is
source-faithful on prime labels. For operator-valued prime diagonality one
still needs the valuation idempotents or the twisted Fourier--Bohr
intertwining theorem.

However, cross-prime estimates are no longer needed for existence if the
constructor uses the direct-sum prime carrier followed by the absolutely
convergent mixed readout.

## Consequence

The completion chain now closes analytically:

\[
\text{label renormalization}
\longrightarrow
\text{quarter-gap Green limit}
\longrightarrow
\text{Euler-weighted prime direct sum}
\longrightarrow
\text{absolute scalar readout}.
\]

The earliest unresolved issue returns to typing: prove that this assembled
normal form is the source-authorized Adams edge and preserves prime labels,
wall incidence, and reciprocal orientation.

## Hostile

Use only the primitive coefficient \(p^{-1/2}\). The packet growth is merely
polylogarithmic, but

\[
\sum_p p^{-1/2}(\log p)^2
\]

diverges. The seam-safe summability is a property of the mixed
primitive--square channel, not of the primitive self-channel.
