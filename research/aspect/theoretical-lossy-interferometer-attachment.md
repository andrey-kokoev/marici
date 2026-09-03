# Theoretical lossy-interferometer attachment

## Question

Can the attachment gates be instantiated in an explicit optical model without claiming access to laboratory hardware or experimental validation?

## Claim boundary

This is an idealized two-path, single-photon calculation. The beam splitter, phase, mismatch, and loss laws are declared assumptions. The result is mathematical, not experimental.

## Model

Use the path basis \(|0\rangle,|1\rangle\). Let

\[
B=\frac{1}{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P_\phi=\begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix},
\qquad
U_\phi=BP_\phi B.
\]

A detector of efficiency \(\eta\in[0,1]\) has three effects on the one-photon path space:

\[
E_0=\eta|0\rangle\langle0|,
\quad
E_1=\eta|1\rangle\langle1|,
\quad
E_\varnothing=(1-\eta)I.
\]

The attached input effects are

\[
F_j=U_\phi^\dagger E_jU_\phi.
\]

They form a POVM because \(F_0+F_1+F_\varnothing=I\).

For input \(|0\rangle\), the probabilities are

\[
p_0=\eta\cos^2(\phi/2),
\qquad
p_1=\eta\sin^2(\phi/2),
\qquad
p_\varnothing=1-\eta.
\]

Mode mismatch is represented by a declared dephasing channel with visibility \(v\in[0,1]\). It changes the click probabilities to

\[
p_0=\frac{\eta}{2}(1+v\cos\phi),
\qquad
p_1=\frac{\eta}{2}(1-v\cos\phi),
\qquad
p_\varnothing=1-\eta.
\]

The parameter \(v\) is part of the model; it is not inferred from the word “mismatch.”

## Attachment gates

1. **Existence:** all three pulled-back effects are defined on the same input path space.
2. **Completeness:** retaining only click effects gives \(F_0+F_1=\eta I\), not \(I\), when \(\eta<1\). The no-click attachment is required.
3. **Composition:** applying dephasing, the interferometer, and detector effects in stages gives the same probabilities as pulling the effects back through the composed channel.
4. **Typing:** visibility and efficiency are distinct parameters. Renormalizing on clicks deletes information about \(\eta\).

## DPC cycle

### Governing conjecture

Explicit channel composition plus a no-click effect gives a coherent theoretical attachment semantics for loss and mismatch. The mechanism is hard to vary because channel duals determine the pulled-back effects and POVM normalization fixes the missing record.

### Rivals

1. Two click effects alone form a complete detector attachment under loss.
2. Conditioning on a click preserves all information relevant to detector efficiency.
3. A scalar visibility can be inserted without declaring the channel that it summarizes.

### Risky consequences

The click-only effect sum must equal \(\eta I\), the full three-effect sum must equal \(I\), click conditioning must remove \(\eta\), and the staged and direct mismatch formulas must agree exactly.

### Falsification attempt

The checker uses exact Gaussian-rational matrices at four phase roots and an exact 27-point rational parameter grid. It verifies unitarity, normalization, nonnegativity on that grid, and the efficiency cancellation under click conditioning. Deliberately removing the no-click effect leaves the exact nonzero residual \((1-\eta)I\). The displayed general formulas are established by the packet’s direct algebra, not promoted from the finite checker.

### Residual

No hardware data, calibration record, or publication source is used. The assumptions require separate justification before any experimental claim.

### Disposition

Rivals 1 and 2 are rejected by exact symbolic residuals. Rival 3 is rejected as an untyped model move. The governing conjecture is provisionally retained for this declared idealized model.

## Disposition

The attachment machinery has a concrete theoretical optical instance. Physical possession and experimental validation are neither assumed nor required for this result.
