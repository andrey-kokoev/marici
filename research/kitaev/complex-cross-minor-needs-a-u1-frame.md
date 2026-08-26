# A Complex Cross Minor Needs a U(1) Frame

Let

\[
M=\begin{pmatrix}a&z\\\overline z&d\end{pmatrix}>0
\]

be a labelled Hermitian two-channel coefficient block. Put

\[
t=a+d,\qquad \Delta=ad-|z|^2,\qquad q=a-d,
\qquad x=2\Re z,\qquad y=-2\Im z.
\]

Then

\[
q^2+x^2+y^2=t^2-4\Delta,
\qquad
|z|^2=\frac{x^2+y^2}{4}
=\frac{t^2-4\Delta-q^2}{4}.
\]

Thus the spectrum and one labelled longitudinal quadrature magnitude recover
the positive cross minor \(|z|^2\). They do not recover the phase of (z).
The residual frame is the diagonal rephasing action

\[
D_\alpha=\operatorname{diag}(e^{i\alpha/2},e^{-i\alpha/2}),
\qquad
M\longmapsto D_\alpha M D_\alpha^*,
\qquad
z\longmapsto e^{i\alpha}z.
\]

Away from (z=0), the compatible incidence frames therefore form a
(U(1))-torsor. A single bit is sufficient only after source structure has
reduced the coefficient lens to a real form. In that real locus, the allowed
phases are (0) and \(\pi\), so the residual action contracts to (C_2).

## Exact witness

The blocks

\[
M_0=\begin{pmatrix}2&1/2\\1/2&1\end{pmatrix},
\qquad
M_{\pi/2}=\begin{pmatrix}2&-i/2\\i/2&1\end{pmatrix}
\]

are positive definite and have the same trace (3), determinant (7/4),
longitudinal coordinate (q=1), and cross minor (1/4). Their off-diagonal
phases differ by \(-\pi/2\). No (C_2) sign port distinguishes all such
complex frames.

## Compiler consequence

There are three separately typed targets:

- spectral control needs (t) and \(\Delta\);
- cross-minor magnitude additionally needs the labelled value (q^2);
- coherent off-diagonal reconstruction additionally needs a phase reference.

The phase reference is not demanded when the downstream readout uses only
\(|z|^2\). Conversely, a scalar determinant or positive Gram certificate
cannot authorize coherent reconstruction of (z).

## Authority boundary and falsifiers

This is an abstract coefficient-lens theorem. It does not identify the
Fourier--Tate coefficient block, its labelled basis, or an authorized phase
reference. The theta-specific seam/resistance instantiation remains frozen.

The packet is falsified by any of the following:

- a claimed (C_2) frame theorem without a source-derived real structure;
- reconstruction of the phase of (z) from trace, determinant, and (q^2);
- treating a phase torsor as an additional amplitude coordinate;
- demanding a phase port when only the invariant cross minor is operative;
- importing this Hermitian formula into a nonsymmetric block.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to test whether the real-symmetric (C_2) conclusion
survives the quantum coefficient lens.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The invariant magnitude theorem survives, while the residual frame
enlarges from (C_2) to (U(1)) unless a real structure is source-derived.
