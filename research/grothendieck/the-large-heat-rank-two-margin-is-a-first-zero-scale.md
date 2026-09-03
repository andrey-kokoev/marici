# The large-heat rank-two margin is a first-zero scale

## Question

What controls the shrinking positive margin of the gamma-plus-prime rank-two determinant at larger heat scale?

## Conditional atomic form

Under RH, the remainder-localizer measure at fixed `t,h` is

\[
\mu_R
=c_h(t)\delta_{y_E}
+
\sum_{j\ge1}w_j(t,h)\delta_{y_j},
\]

where

\[
y_E=e^{h/4},
\qquad
c_h(t)=(e^{h/4}-1)e^{t/4},
\]

and

\[
y_j=e^{-h\gamma_j^2},
\qquad
w_j(t,h)=m_j e^{-t\gamma_j^2}(1-e^{-h\gamma_j^2}).
\]

The rank-two determinant is

\[
D_2
=\sum_{j<k}w_jw_k(y_j-y_k)^2,
\]

including the endpoint atom as one index.

## Leading asymptotic

Let `gamma_1` be the least positive zero ordinate and `m_1` its multiplicity. As `t` grows, the leading term is the endpoint--first-zero pair:

\[
D_2(t,h)
\sim
c_h(t)m_1e^{-t\gamma_1^2}
(1-e^{-h\gamma_1^2})
(e^{h/4}-e^{-h\gamma_1^2})^2.
\]

Since `c_h(t)` carries `e^(t/4)`, the net exponential scale is

\[
D_2(t,h)
\asymp
\exp[-t(\gamma_1^2-1/4)].
\]

Pairs involving two nontrivial zeros decay faster, and endpoint pairs with later zeros are suppressed by their larger ordinates.

## Consequence for source estimates

The positive determinant margin is exponentially smaller than the order-one endpoint, gamma, and prime components. A uniform large-heat proof based on separate absolute bounds must resolve cancellation down to the first-zero scale `exp[-t(gamma_1^2-1/4)]`.

Ordinary PNT error estimates do not reach that scale at the moving prime saddle. This is the determinant analogue of the earlier pointwise large-heat warning.

## Interpretation of the scan

The collapse from robust short-heat determinants to the `7.55e-8` margin at `t=0.05` is consistent with the onset of endpoint--first-zero dominance. Increasing rank introduces products involving further zero atoms and causes still sharper conditioning.

## Falsifier

Any proposed all-heat determinant proof whose residual error decays only algebraically, or at a zero-free-region PNT scale, cannot certify the asymptotic sign. A successful source identity must preserve the completed cancellation symbolically or encode spectral information of first-zero strength.

## Boundary

The asymptotic is conditional on RH, isolation of the least ordinate, and the exact atomic expansion. It explains the required scale but cannot be used as source evidence for positivity.

## Disposition

Use finite interval certificates only as local diagnostics. Do not extrapolate them into a uniform proof. The large-heat determinant gate requires a symbolic completed identity or arithmetic estimate already carrying RH-scale information.