# Wall subtraction places the four-grade theta packet in every finite Sobolev rung

## Refined Mellin-wall expansion

For \(r>-1\),

\[
\Theta_r(u)
=
e^{ru}
\sum_{n\ge1}n^re^{-\pi n^2e^{2u}}.
\]

The Mellin or Euler--Maclaurin expansion at \(u=-\infty\) begins

\[
\Theta_r(u)
=
C_re^{-u}
+
\zeta(-r)e^{ru}
+
O\!\left(e^{(r+2)u}\right),
\]

where

\[
C_r
=
\frac12
\pi^{-(r+1)/2}
\Gamma\!\left(\frac{r+1}{2}\right).
\]

The same expansion may be differentiated termwise to every fixed order.

## Relative representative

For the synthesized four-grade packet, define the canonical global
representative

\[
\Psi_p^{\mathrm{rel}}(u)
=
\Psi_p(u)-\rho_pe^{-u},
\]

where \(\rho_p\) is the source-computed coefficient-wall residue. The
subtracted term grows only at the negative Mellin end, exactly where it
cancels the packet wall, and decays at the positive end.

## Decay at the negative end

The four exponents are

\[
r_j=j+\frac12,
\qquad
j=0,1,2,3.
\]

After the common \(e^{-u}\) residue is removed, the slowest surviving term is
the \(j=0\) Euler--Maclaurin correction,

\[
c_{0,p}\zeta\!\left(-\frac12\right)e^{u/2}.
\]

Therefore, for every \(m\ge0\),

\[
\partial_u^m\Psi_p^{\mathrm{rel}}(u)
=
O(e^{u/2})
\qquad
(u\to-\infty).
\]

Possible cancellation of this coefficient only improves the estimate.

## Decay at the positive end

As \(u\to+\infty\), every label term contains

\[
e^{-\pi n^2e^{2u}}.
\]

After any finite number of derivatives, this dominates all polynomial and
exponential prefactors. Hence

\[
\partial_u^m\Psi_p^{\mathrm{rel}}(u)
\]

decays faster than every ordinary exponential at \(+\infty\).

## Sobolev conclusion

Both ends are square integrable after every finite number of derivatives.
Consequently,

\[
\Psi_p^{\mathrm{rel}}
\in
H^m(\mathbb R)
\qquad
\text{for every }m\ge0.
\]

Indeed the relative representative is Schwartz in the logarithmic coordinate.
In particular it belongs to every finite-order differential Green graph built
from \(\partial_u\), including the graph of

\[
\mathcal C=\partial_u^2-\frac14.
\]

This proves analytic regularity of the wall-subtracted label synthesis. It
does not by itself prove radical descent or identify its Green class with the
raw Stieltjes window difference.

## Constructor consequence

The first Adams-edge comparison has now separated into:

1. one explicit coefficient-wall incidence \(\rho_p\);
2. one rapidly controlled relative bulk vector
   \(\Psi_p^{\mathrm{rel}}\);
3. the remaining source identity comparing that bulk vector with the
   relative Green class of
   \[
   d_p=W_{2\log p}-W_{\log p}.
   \]

Thus failure of the final comparison can no longer be attributed to an
undefined theta sum or insufficient differential regularity.

## Hostile

Use a fixed cutoff-localized wall representative at every finite label
truncation. Sharp truncations carry a wall profile centered near
\(u=-\log N\), so a fixed cutoff does not cancel their moving transition
layer. The global limiting subtraction is analytically valid, but
finite-cutoff Green convergence requires the source-derived moving wall.
