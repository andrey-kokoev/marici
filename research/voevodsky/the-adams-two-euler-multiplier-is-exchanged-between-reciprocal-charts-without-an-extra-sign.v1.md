# The Adams-two Euler multiplier is exchanged between reciprocal charts without an extra sign

## Question

How does the Adams-two Euler multiplier transform under reciprocal parameter reflection?

## Claim boundary

Use the analytic reciprocal involution \(\rho(s)=1-s\) and the centered coordinate \(z=s-1/2\), so \(\rho(z)=-z\).

The positive-chart Adams-two multiplier is \(\lambda_{p,+}(s)=1-p^{-2s}\), equivalently \(\lambda_{p,+}(z)=1-p^{-1}e^{-2z\log p}\).

The reciprocal-chart multiplier is \(\lambda_{p,-}(s)=1-p^{-2(1-s)}\), equivalently \(\lambda_{p,-}(z)=1-p^{-1}e^{2z\log p}\).

Therefore \(\lambda_{p,-}(z)=\lambda_{p,+}(-z)\) and \(\lambda_{p,-}(s)=\lambda_{p,+}(1-s)\). Reciprocal transport exchanges the two chart functions exactly and introduces no scalar minus sign.

Let \(R_U\) exchange the positive and negative prime sectors. On the doubled Euler carrier, define \(\Lambda_p(z)=\operatorname{diag}(\lambda_{p,+}(z),\lambda_{p,-}(z))\). Then \(R_U\Lambda_p(z)R_U=\Lambda_p(-z)\).

The fixed-parameter anticommutation formula \(R_U\Lambda_p(z)R_U=-\Lambda_p(z)\) fails generically because \(1-p^{-1}e^{2z\log p}\) is not the negative of \(1-p^{-1}e^{-2z\log p}\).

In the Hermitian reciprocal lane, \(s\mapsto1-\overline s\) gives the corresponding conjugate relation \(\lambda_{p,-}(s)=\overline{\lambda_{p,+}(1-\overline s)}\) under the real prime coefficients.

## Disposition

The Euler subobject transforms by reciprocal chart exchange rather than Clifford anticommutation. The remaining extension calculation must choose the Euler-coordinate sign so that the even endpoint entry and odd jet shift assemble with this sign-free diagonal chart exchange.
