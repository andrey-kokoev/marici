# The minimal active theta reservoir is one source-aligned mode

## Construction

In the overdriven region \(\rho>1\), a passive port extension cannot repair the positive lossless balance. There is, however, an exact smallest active repair.

Let

\[
Q=I+2r\sigma_x,
\qquad
b=-f(1,0)^T,
\qquad
\rho=b^*Q^{-1}b.
\]

Allow a positive reservoir to change the dissipative balance from \(Q\) to \(Q+\Delta\), with \(\Delta\geq0\). The forced input becomes contractive exactly when

\[
b^*(Q+\Delta)^{-1}b\leq1.
\]

The source-aligned rank-one update

\[
\Delta_*=rac{\rho-1}{\rho}bb^*
\]

saturates the boundary:

\[
b^*(Q+\Delta_*)^{-1}b=1.
\]

It vanishes continuously on \(\rho=1\) and adds only one active balance mode.

## Minimality

Whiten the original balance by writing \(q=Q^{-1/2}b\) and \(X=Q^{-1/2}\Delta Q^{-1/2}\). Then \(\lVert q\rVert^2=\rho\). Among positive updates making

\[
q^*(I+X)^{-1}q\leq1,
\]

the normalized reservoir cost obeys

\[
\operatorname{Tr}X\geq\rho-1.
\]

Indeed, the inverse Cauchy inequality gives

\[
q^*(I+X)^{-1}q
\geq
\frac{\rho^2}{\rho+q^*Xq},
\]

so feasibility requires \(q^*Xq\geq\rho(\rho-1)\). Positivity gives \(q^*Xq\leq\rho\operatorname{Tr}X\). Equality throughout is attained by

\[
X_*=(\rho-1)uu^*,
\qquad
u=q/\sqrt\rho,
\]

which maps back to \(\Delta_*\). Thus the active repair has minimum normalized trace cost \(\rho-1\), and the optimum is a single mode aligned with the whitened source direction.

## Optical instrument

This specifies the missing component: a tunable dissipative coupling aligned with the calibrated theta forcing quadrature. It is not an unused detector or an additional incident channel. It must alter the measured state-decay matrix by the rank-one increment \(\Delta_*\).

At \(r=0\) and \(y=\log 2/(2\pi)\), one has \(f=\sqrt2\), \(\rho=2\), and

\[
Q=I,
\qquad
\Delta_*=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
Q+\Delta_*=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\]

The falsifiable signature is therefore anisotropic: the source-aligned decay rate doubles while the orthogonal response rate remains unchanged. Any claimed minimal repair that perturbs both eigenchannels, fails to saturate the contractive boundary, or costs more than \(\rho-1\) in the whitened trace is not the canonical rank-one completion.

## Sector transfer

Strominger's relative connection is now given a quantitative target. To act as this reservoir, its source-derived coupling must induce precisely a positive rank-one change in the balance along the forcing direction, while its defect attachment supplies the required global regularity. Nima's global theta construction can test whether a canonical boundary operation generates this update. Flavor can use the same theorem: a new source equation must change the portal balance transversely, not append another measurement channel.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_minimal_active_theta_reservoir.py
```
