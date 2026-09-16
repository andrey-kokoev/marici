# The completed-zeta divisor supplies the canonical local meromorphic target but not the operator comparison

## Question

Can the local numerator/denominator frames required by the determinant compiler be constructed without assuming a global holomorphic direct-Euler product?

## Claim boundary

Yes for the canonical scalar target determined by the completed zeta divisor. This constructs the meromorphic line and preserves divisor multiplicities. It does not prove that the retained operator determinant continues to, or equals, this target; using the target cannot substitute for that comparison.

## Local frames

Let \(Z(s)\) denote the source-normalized completed zeta section, with its explicitly removed elementary poles if required by convention. The direct Sonin target is the meromorphic section

$$
M_{\rm comp}(s)=E(s)Z(s)^{-1},
$$

where \(E\) is the declared elementary endpoint/archimedean factor.

For any point \(\rho\), choose a disc \(U_\rho\) containing no other divisor point. If \(Z\) has order \(m_\rho\) at \(\rho\), write

$$
Z(s)=(s-\rho)^{m_\rho}u_\rho(s),
\qquad
u_\rho(\rho)\ne0.
$$

Then on \(U_\rho\),

$$
M_{\rm comp}(s)
=
\frac{N_\rho(s)}{Q_\rho(s)},
\qquad
N_\rho(s)=E(s)u_\rho(s)^{-1},
\qquad
Q_\rho(s)=(s-\rho)^{m_\rho}.
$$

Away from the divisor take \(Q=1\). On overlaps, two frame pairs differ by multiplication by one nowhere-zero holomorphic function, so they define one meromorphic line section.

## Reflection

Sharp reflection sends a local frame at \(\rho\) to a local frame at \(\bar\rho\):

$$
(N_\rho,Q_\rho)
\longmapsto
(N_\rho^\#,Q_\rho^\#).
$$

After including the completed functional-equation involution, the reciprocal chart at \(1-\bar\rho\) has the same order. Thus the local line construction preserves multiplicity without choosing zero locations or assuming they lie on the critical line.

## Uniqueness of comparison

Suppose an operator determinant compiler \(D_{\rm op}\) is independently continued as a meromorphic section on a connected domain and agrees with \(M_{\rm comp}\) on a nonempty open subset of \(\operatorname{Re}s>1\). The meromorphic identity theorem then forces

$$
D_{\rm op}=M_{\rm comp}
$$

throughout that domain, including equality of zero and pole orders.

Therefore no second normalization calculation is needed after existence of the operator continuation. But the identity theorem does not construct that continuation.

## Circularity boundary

Defining \(D_{\rm op}:=M_{\rm comp}\) would fit the operator characteristic to the desired arithmetic divisor. The admissible proof must first construct \(D_{\rm op}\) from the retained return operators and then compare it on the Euler half-plane.

## Disposition

The canonical completed meromorphic target and its reflected local frames are constructed, with multiplicities retained. Operator-to-target equality is unique if it exists, but existence of the independent meromorphic operator determinant remains the decisive comparison gate.