# Coherence tetrahedron simulated instrument

## Question

Can the newly exposed analytical faces be compiled into one finite coherent instrument fixture while preserving the distinction between canonical cancellation and transverse Evans response?

## Construction

The simulated instrument has four oriented complex-amplitude inputs

\[
(M_{0+},M_{0-},M_{1+},M_{1-})
\]

and the fixed two-output sewing matrix

\[
S=\frac{i}{2}
\begin{pmatrix}
-1&1&1&1\\
-1&1&-1&-1
\end{pmatrix}.
\]

On the source fixture

\[
(M_{0+},M_{0-},M_{1+},M_{1-})
=(iX,-iX,X',X'),
\]

its coherent outputs are exactly

\[
S M=(X+iX',X-iX')=(E,E^*).
\]

A separate three-input dark-port combiner receives

\[
(-R,-2E,R+2E).
\]

Its ideal output is zero. Adding an amplitude error \(\varepsilon\) to one input produces output \(\varepsilon\), so the channel exposes calibration leakage rather than treating the null as an Xi detector.

The reduced-pencil fixture uses

\[
D=\operatorname{diag}(0,2,3),
\qquad
\Psi=v=e_1,
\qquad
\ell=e_1^T.
\]

Although \(\det D=0\), the augmented matrix

\[
\mathcal G=
\begin{pmatrix}
D&v\\
\ell&0
\end{pmatrix}
\]

has determinant \(-6\). This tests the mechanics of removing one permanent kernel line; it does not identify the resulting determinant with Xi.

A passive Douglas-network fixture has singular values \(3/5\) and \(4/5\). Its defect operator is positive with diagonal \((16/25,9/25)\). A deliberate hostile with singular value \(6/5\) produces defect entry \(-11/25\) and must fail passivity.

## Claim boundary

This is an exact finite symbolic simulation. It compiles analytical formulas into coherent transfer, null-channel, kernel-reduction, and passivity tests. The reported transverse first-zero residual is metadata only because its interval certification remains open. The fixture does not realize the global coherence pyramid, prove Hardy positivity, establish a reduced Xi determinant, or imply RH.

## Disposition

The finite instrument is executable. Its next physical-binding requirements are calibrated phase-preserving four-port preparation, coherent two-output detection, an independently adjustable dark-port imbalance, and source-authorized realization of the reduced-pencil reference port.

## Verification

- Checker: `research/aspect/checkers/check_coherence_tetrahedron_instrument.py`
- Result: `research/aspect/results/coherence_tetrahedron_instrument.json`
- SCC state: `research/aspect/contracts/theta-rh-interaction-net-state.v18.json`
