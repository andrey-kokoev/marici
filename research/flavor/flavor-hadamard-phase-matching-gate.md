# Hadamard phase-matching gate: WP1124

## Question

Can boundary \(C_3\) and endpoint \(\mathbb Z_2\) invariants select an \(H_6\)
Hadamard representative?

## DPC resolution

- **Conjecture:** the source-shaped Kronecker Hadamard
  \(H=F_3\otimes F_2\) is selected by \(C_3\) history and endpoint
  \(\mathbb Z_2\).
- **Rivals:** \(C_6\) Fourier Hadamard; \(C_3\times\mathbb Z_2\) Kronecker
  Hadamard; generic \(H_6\); no sourced phase matching.
- **Risky consequences:** \(H\) must be unitary, every squared magnitude must
  be \(1/6\), and both factors must preserve the selected packet and six event
  channels.
- **Falsification attempt:** the Kronecker algebra passes exactly, but endpoint
  \(\mathbb Z_2\) maps the selected quartet to a different coset and zero
  physical16 event channels are sourced.
- **Residual:** a boundary defect with endpoint symmetry or anomaly phases
  could select an \(H_6\) representative.
- **Disposition:** retain the Kronecker \(H_6\) algebra; reject current
  \(C_3\times\mathbb Z_2\) source matching.

## Exact algebra

Let \(\zeta_3^2+\zeta_3+1=0\). Then \(F_3\) and \(F_2\) are Fourier Hadamards,
and \(F_3\otimes F_2\) is a six-state Hadamard:

\[
|F_3\otimes F_2|^2q=\Bigl(\frac16\Bigr)^6,
\qquad
\frac32|F_3\otimes F_2|^2q=\Bigl(\frac14\Bigr)^6.
\]

## Source gate

Kronecker form, \(C_3\) history, endpoint signs, and Hadamard symmetry are not
source authority. A sourced phase observable still has to preserve the selected
packet and supply six physical16 channels.

Checker: `research/flavor/checkers/wp1124_hadamard_phase_matching_gate.py`

Result: `results/wp1124_hadamard_phase_matching_gate.json`
