# Source ray, real structure, and augmentation select the theta output frame

## The residual gauge is exactly one phase

The repaired theta Gramian determines a minimal two-output realization only up to \(U(2)\). The source direct-feedthrough supplies the first reduction.

Choose the source ray as

\[
D=e_1.
\]

Source duality fixes the first response row. Every remaining lossless factor has the form

\[
C_\phi=
\begin{pmatrix}
f&0\\
e^{i\phi}2r&e^{i\phi}
\end{pmatrix}.
\]

All values of \(\phi\) produce the same Gramian and source duality. Thus source incidence reduces the output gauge from \(U(2)\) to the stabilizer of \(D\), which is one residual \(U(1)\) acting on \(D^\perp\).

## The selection ladder

The triangular frame is selected through four typed stages:

1. Lossless Gram data determine the two-output realization modulo \(U(2)\).
2. The source-derived unit feedthrough ray \(D\) fixes the driven output direction, leaving \(U(1)\).
3. A compatible real structure on the orthogonal output line reduces the allowed phase to the two real orientations, leaving a sign.
4. Augmentation orients that real line and selects the positive representative.

The result is

\[
C_0=
\begin{pmatrix}f&0\\2r&1\end{pmatrix}.
\]

This is the precise condition under which the earlier triangular normal form becomes canonical. Neither the Gram determinant nor source incidence alone is enough.

## Mixed-exchange gate

Nima's mixed-exchange theorem supplies the compatibility test for stage three. A linear exchange and an antilinear dagger comparison define the required real line only when their composite has trivial square. If that coherence scalar is nontrivial, the output phase cannot legitimately be reduced to sign. Augmentation applied before this test is mistyped.

The hostile packet is immediate: choose \(\phi=\pi/2\). It obeys every positive lossless identity and has the same source ray and response volume as \(\phi=0\), but it is not in the declared real output frame. Any detector assignment inferred before a real-structure comparison confuses a phase convention with physical orientation.

## Optical implementation

The necessary augmentation is a phase reference on the output line orthogonal to the direct source ray. A balanced homodyne reference can implement the comparison, provided its phase is independently source-authorized rather than estimated from the same response. The sequence is operational:

1. calibrate the direct source ray;
2. null it to isolate the orthogonal response;
3. compare that response with an independent real local oscillator;
4. use the augmentation convention to choose its positive orientation.

This adds no new dynamical selector. It makes the invariant two-port class into a reproducible instrument frame.

## Cross-sector consequence

The same ladder explains Figueiredo's mass audit. Existence of mass coordinates is analogous to existence of a response line; it does not orient or numerically select a point on that line. Completion A still needs a transverse scale law. Completion B fails earlier because it lacks the source constructor for the line itself.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_theta_output_frame_augmentation_ladder.py
```
