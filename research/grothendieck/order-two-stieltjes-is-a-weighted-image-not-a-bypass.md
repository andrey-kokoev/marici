# Order-two Stieltjes is a weighted image, not a bypass

## Question

Does the promising order-two Stieltjes branch avoid the heat complete-monotonicity gate, or only repackage it?

## Distinguish the two scalar functions

The heat scalar is

\[
H_{\rm heat}(t)=\mathcal K(t,0).
\]

The prior outer-ray current, written here as `H_out(x)`, uses the squared coordinate `x=(s-1/2)^2`. Reusing the letter `H` obscured that these live on different parameter spaces.

Prior research proves the exact transform between their candidate measures. If

\[
F(t)=e^{-t/4}H_{\rm heat}(t),
\]

then the Bernstein density for `H_out'` is

\[
m_{\rm out}(t)=-tF'(t).
\]

Under a positive squared-spectral measure,

\[
H_{\rm heat}(t)=
\int e^{-\lambda t}\,d\rho(\lambda),
\]

so

\[
\frac{m_{\rm out}(t)}t
=
\int(\lambda+1/4)
 e^{-(\lambda+1/4)t}\,d\rho(\lambda).
\]

Thus the order-two Stieltjes measure is the heat measure shifted by `1/4` and weighted by the shifted spectral rate.

## Equivalence with a boundary condition

If `H_heat` is completely monotone, then `m_out(t)/t` is completely monotone and has support beginning at `1/4`.

Conversely, if `m_out(t)/t=-F'(t)` is completely monotone and the source boundary condition

\[
F(t)\longrightarrow0
\qquad(t\to\infty)
\]

holds, then

\[
F(t)=
\int_t^\infty\frac{m_{\rm out}(r)}r\,dr
\]

is completely monotone. Multiplying back by `e^(t/4)` recovers the heat measure after undoing the support shift. Hence the order-two branch does not evade RH-strength positivity; it is an invertible weighted image once the boundary and support data are retained.

## What the branch genuinely improves

The value of the order-two presentation is structural:

- compact Hausdorff support after the resolvent change;
- three explicit Hankel/localizing matrix families;
- determinate Jacobi approximants;
- double-pole and residue constraints;
- a divided-difference kernel replacing independent derivative tests.

These provide an induction and factorization surface unavailable in raw heat coordinates.

## Finite-difference interaction

The finite-difference criterion for `H_heat` avoids derivative-amplified arithmetic tails. It should be used for certified approximation. The order-two Hausdorff/Jacobi presentation should be used for the exact positive factorization target. They are complementary charts, not separate proofs.

## Disposition

Do not report order-two Stieltjes positivity as an escape from complete monotonicity. Use it as the preferred coordinate for a source-derived J-fraction or divided-difference Gram factor, while finite heat differences control arithmetic approximation. The missing sign theorem remains one and the same.