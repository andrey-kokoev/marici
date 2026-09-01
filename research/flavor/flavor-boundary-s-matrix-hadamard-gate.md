# Boundary S-matrix Hadamard gate: WP1122

## Question

Can a boundary S-matrix supply the physical16 event kernel?

## DPC resolution

- **Conjecture:** a sourced \(C_6\) boundary S-matrix is the six-state Fourier
  Hadamard \(F_6\) and produces the physical16 event weights.
- **Rivals:** \(C_6\) Fourier S-matrix; \(C_3\) history times endpoint
  \(\mathbb Z_2\); a generic unitary S-matrix; no sourced S-matrix.
- **Risky consequences:** \(F_6\) must be unitary, every squared magnitude
  must be \(1/6\), and the source must supply a \(C_6\) generator preserving
  the selected packet plus six asymptotic physical16 channels.
- **Falsification attempt:** the \(F_6\) algebra passes exactly, but current
  Krylov history has order \(3\), endpoint \(\mathbb Z_2\) maps the selected
  quartet to a different coset, and zero asymptotic physical16 channels are
  sourced.
- **Residual:** a future defect could source a \(C_6\) or equivalent Hadamard
  boundary S-matrix with event-channel provenance.
- **Disposition:** provisionally retain \(F_6\) as target-compatible algebra;
  reject it as a current-source construction.

## Exact algebra

Let \(\omega=(1+i\sqrt3)/2\), so \(\omega^6=1\). The unnormalized Fourier
entries \(\omega^{jk}\) all have squared norm \(1\), and the row inner
products are \(6\delta_{j\ell}\). Thus \(F_6\) is unitary and

\[
|F_6|^2q=\Bigl(\frac16\Bigr)^6,
\qquad
\frac32|F_6|^2q=\Bigl(\frac14\Bigr)^6
\]

for \(q=(6,8,1,4,2,2)/23\).

## Source gate

The algebra does not supply a \(C_6\) generator, physical16 asymptotic
channels, or event provenance. Unitarity alone is not a production law.

Checker: `research/flavor/checkers/wp1122_boundary_s_matrix_hadamard_gate.py`

Result: `results/wp1122_boundary_s_matrix_hadamard_gate.json`
