# The exact theta forcing connection extends the local Schur jet

## Question

What is the smallest source extension that restores the forcing derivative omitted by the frozen-source Schur block?

## Source carrier

Use the nonlinear source coordinates

\[
y=e^{2x},\qquad f=2e^{-\pi y}.
\]

They satisfy the autonomous connection

\[
y'=2y,
\qquad
f'=-2\pi yf.
\]

The exact transport over a displacement \(\ell\) is

\[
y(x+\ell)=e^{2\ell}y(x),
\qquad
f(x+\ell)=f(x)\exp[-\pi y(x)(e^{2\ell}-1)].
\]

This carrier is finite and transport-complete, but nonlinear.

## Coupled Schur jet

For the local affine forcing \(f(u)=f_0+gu\), exact formal expansion gives

\[
(1,-1)\mathbf r_\ell'
=-2zf_0\ell+z(f_0-g)\ell^2+O(\ell^3),
\]

while the moving endpoint current is

\[
Q_\ell
=2zf_0\ell+z(2g-f_0)\ell^2+O(\ell^3).
\]

Therefore

\[
(1,-1)\mathbf r_\ell'+Q_\ell
=zg\ell^2+O(\ell^3).
\]

The connection supplies \(g=f'=-2\pi yf\); the quadratic residual is a determined source port, not a tunable counterterm.

## Linear alternative

For \(h_k=y^kf\),

\[
h_k'=2kh_k-2\pi h_{k+1}.
\]

The completed sequence \((h_k)_{k\ge0}\) is a linear representation of the same connection. Every finite truncation fails transport closure because the top equation contains \(h_{N+1}\).

## Interface extension

The smallest lawful finite extension of the local Schur system is therefore a nonlinear skew-product carrier consisting of:

1. the two Green route coordinates;
2. the endpoint source coordinate \(y\);
3. the forcing amplitude \(f\);
4. the co-moving odd return row;
5. a forcing-jet output carrying \(f'\).

Incidence and recovery may now be redefined over this skew product. A determinant-line linearization requires the completed infinite jet module instead.

## Verification

`research/aspect/checkers/check_variable_theta_forcing_connection.py` verifies the formal coefficients exactly and records the nonzero omitted-jet hostile.

## Claim boundary

This constructs the source forcing extension and its first-jet residual. It does not yet define the completed Green metric, physical auxiliary subspace, recovery action on forcing jets, or a determinant functor on the nonlinear carrier.

## Disposition

The nonlinear forcing carrier resolves the missing local source transport. The next gate is to lift incidence and recovery to this skew product and test whether the forcing-jet directions are annihilated or retained by recovery before any Schur quotient is formed.
