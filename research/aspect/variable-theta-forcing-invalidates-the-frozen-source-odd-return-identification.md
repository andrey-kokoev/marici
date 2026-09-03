# Variable theta forcing invalidates the frozen-source odd-return identification

## Question

Does the co-moving odd return row identify the complete Schur first jet with the physical theta endpoint current on the source-varying carrier?

## Frozen-source identity

For a constant forcing, the co-moving row

\[
C_\ell=(1,-1)D_\ell
\]

cancels the explicit return-frame and transport derivatives. The remaining Schur derivative equals the endpoint current. The existing Aspect checker verifies exactly this frozen-source calculation.

## Source-varying residual

The physical theta forcing varies along the endpoint coordinate. For

\[
f(u)=f_0+gu
\]

and

\[
\mathbf r_\ell=\int_0^\ell D_{\ell-u}\mathbf1 f(u)\,du,
\]

the source calculation gives

\[
(1,-1)\mathbf r_\ell'+Q_\ell
=zg\ell^2+O(\ell^3).
\]

For the theta source,

\[
f'(x)=-4\pi e^{2x}e^{-\pi e^{2x}},
\]

which is generically nonzero. Therefore the frozen-source equality does not identify the physical source-varying odd return. The exact stored checker passes because its model omits the forcing-jet port.

## Exact source connection

Writing

\[
y=e^{2x},\qquad f=2e^{-\pi y},
\]

the source closes nonlinearly:

\[
\partial_xy=2y,
\qquad
\partial_xf=-2\pi yf.
\]

Equivalently, \(f\) is horizontal for

\[
\nabla_x=\partial_x+2\pi y.
\]

The natural linear observables \(h_k=y^kf\) satisfy

\[
\partial_xh_k=2kh_k-2\pi h_{k+1}.
\]

Every finite truncation leaks through \(h_{N+1}\). Thus exact moving-source transport requires either the finite nonlinear pair \((y,f)\) or a completed infinite graded jet module; no finite transport-complete linear block on \(h_0,\ldots,h_N\) exists.

## Consequence for the recovery-kernel test

The proposed physical auxiliary subspace cannot yet be tested against \(\ker R\), because its source-varying forcing component is absent from the frozen finite Schur carrier. Testing inclusion on that truncation would certify the wrong object. The first missing typed object is the forcing connection or full jet completion on the same carrier as incidence, recovery, and Schur elimination.

## Correction

The prior graph disposition that the odd return equals the endpoint/Wronskian current must be restricted to constant forcing. It does not establish the physical theta-source identification.

## Disposition

Defer the physical auxiliary-in-recovery-kernel test. First extend the Schur/recovery carrier by the nonlinear forcing connection or completed infinite jet tower, reproduce the \(zf'(x)\ell^2\) residual, and only then type the physical auxiliary subspace and evaluate recovery on it.
