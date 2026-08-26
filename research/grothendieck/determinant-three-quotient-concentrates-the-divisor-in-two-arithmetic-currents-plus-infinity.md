# Determinant-three quotient concentrates the divisor in two arithmetic currents plus infinity

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact section normal form and boundary-current reduction

## Nowhere-zero carrier quotient

On the plus Euler chart, let

\[
 L_s e_p=p^{-s}e_p,
 \qquad
 \Re s>\frac13.
\]

The regularized determinant

\[
 u_3(s)=\det_3(I-L_s)
\]

is holomorphic and nowhere zero on this chart.  Define the carrier-normalized
completed section

\[
 R_+(s)=\Xi(s)u_3(s).
\]

Because (u_3\) is a unit,

\[
 \operatorname{div}R_+=\operatorname{div}\Xi
\]

throughout the chart.  The normalization changes presentation but moves no
zero.

## Exact Euler-chamber factorization

In the ordinary Euler chamber, write

\[
 \tau_k(s)=\frac1k\operatorname{Tr}(L_s^k)
 =\frac1k\sum_p p^{-ks}.
\]

Then

\[
 \zeta(s)=\exp\left(\sum_{k\ge1}\tau_k(s)\right),
\]

while

\[
 u_3(s)=\exp\left(-\sum_{k\ge3}\tau_k(s)\right).
\]

If (B_\infty(s)\) denotes the completed archimedean factor, the normalized
section has the exact form

\[
 R_+(s)
 =B_\infty(s)
 \exp\left(\tau_1(s)+\tau_2(s)\right).
\]

Thus every connected prime-power contribution of length at least three has
been absorbed into a nowhere-zero carrier.  The divisor remains entirely in
the holomorphic continuation of a section whose source coordinates are:

1. the primitive current;
2. the prime-square current;
3. the archimedean line.

No higher cyclic channel remains in its logarithmic connection.

## Residual connection

Where the Euler sums converge absolutely,

\[
 \frac{R_+'(s)}{R_+(s)}
 =\frac{B_\infty'(s)}{B_\infty(s)}
 -\sum_p(\log p)p^{-s}
 -\sum_p(\log p)p^{-2s}.
\]

The first prime sum is the primitive boundary current.  The second is the
prime-square current.  All (k\ge3\) terms cancel identically against the
determinant-three connection.

This is a source-derived gauge normalization, not a fitted subtraction: the
coefficient (1/k\) and the cutoff at three are forced by the relative
determinant functor.

## Meaning and limitation

The result does not prove that the primitive or square current is positive,
nor that either separately admits scalar continuation.  Indeed:

- the primitive series converges only for (\Re s>1\);
- the square series converges for (\Re s>1/2\) and reaches its divergence at
  the seam;
- separate continuation of the primitive current imports the zeta divisor by
  Möbius inversion.

Therefore (R_+\) must be retained as a completed section derived from
\(\Xi\) and the unit carrier.  The displayed Euler formula types its source
coordinates in the convergence chamber; it does not authorize their separate
continuation.

The reduction nevertheless has real force.  Any global conservation law for
the divisor can be sought on a three-component residual packet rather than on
the full infinite prime-power tower.  The connected tail is proved
divisor-neutral.

## Reciprocal chart

The minus chart has the analogous unit

\[
 u_3^-(s)=\det_3(I-L_-(s)),
 \qquad
 L_-(s)e_p=p^{s-1}e_p,
\]

and residual section

\[
 R_-(s)=\Xi(s)u_3^-(s).
\]

On the overlap, the ratio (R_+/R_-\) is the inverse of the nowhere-zero
carrier transition.  Hence the two residual presentations carry the same
divisor and exchange their primitive and square boundary data through the
reciprocal sewing law.

## Sharp next theorem

The remaining target is a source-local connection or Green identity for the
residual packet

\[
 \left(B_\infty,\tau_1,\tau_2\right)
\]

whose two reciprocal presentations glue without separately continuing
\(\tau_1\) or (\tau_2\).  An off-seam zero must then be tested as a failure of
this three-component boundary conservation, not as a defect of the connected
Euler carrier.

The falsifier is any surviving (k\ge3\) coefficient in the normalized
logarithmic connection.  In the Euler chamber that residual is exactly zero.

## Result

Quotienting by the determinant-three unit preserves every Riemann zero while
removing the entire connected prime-power tail from the section connection.
The RH-bearing boundary packet is reduced exactly to primitive current,
prime-square current, and the archimedean line.
