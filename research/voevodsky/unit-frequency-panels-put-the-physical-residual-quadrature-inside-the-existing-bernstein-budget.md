# Unit frequency panels put the residual quadrature inside the existing Bernstein budget

The corrected physical residual scout was rerun with 250 unit frequency
panels and Gauss order 48 on each panel. It agrees with the higher-order
geometric-panel calculation in the lower-form minimum to `1.6e-15` relative
scale.

This panelization is important because the previously proved Bernstein ellipse
has absolute imaginary semiminor `0.2` on every unit panel. The same bounds
used for the directed finite-gamma matrix apply to the synthesis integrand

\[
e^{ixu}(q(u)-q(250))\widehat Z(u).
\]

Here `|e^{ixu}|<=e^{L/5}`, and Cauchy--Schwarz gives
`|Zhat(u)|<=sqrt(2L)||Z||`. Thus the frequency-synthesis error is controlled by
the same order-48 geometric factor as the established `2.544e-13` gamma-entry
budget, with only the explicitly computable `||Z||` scaling.

The physical panels have maximum length below `0.406`. Their order-900 rule
is exact on the polynomial--polynomial part through degree 1799, covering the
degree-1338 products. Terms containing exponentials or the bandlimited
synthesis are entire and admit a much smaller Bernstein remainder.

This closes the choice-of-panel obstruction. Final promotion must still carry
these bounds through exact-decimal retained/tail maps and recompute the
`92 by 92` lower form in Arb; floating orthogonalization cannot be treated as
exact.
