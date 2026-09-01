# Unitary S-matrix Hadamard classification: WP1123

## Question

Which unitary S-matrices produce uniform physical16 events for every six-state
branch distribution?

## DPC resolution

- **Conjecture:** a generic unitary S-matrix can produce the target event law
  without six-state Hadamard moduli.
- **Rivals:** generic non-Hadamard unitary; complex Hadamard \(H_6\);
  row/column phase-equivalent Hadamard; fixed-\(q\) nonuniversal S-matrix.
- **Risky consequences:** evaluate \(P=|S|^2\) on every basis vector \(e_b\),
  forcing every column \(Pe_b=(1/6)^6\) and hence every squared modulus
  \(1/6\).
- **Falsification attempt:** the basis-vector evaluation proves every
  qualifying unitary is a complex Hadamard; no non-Hadamard unitary survives.
- **Residual:** the full \(H_6\) phase-parameter space and source-phase
  matching remain open.
- **Disposition:** reject generic non-Hadamard S-matrices; classify the
  required algebra as \(H_6\) modulo row/column phases and permutations.

## Exact theorem

A q-independent production law requires \(Pq=(1/6)^6\) for every probability
vector \(q\). Taking \(q=e_b\) gives \(Pe_b=(1/6)^6\). Therefore

\[
|S_{eb}|^2=\frac16
\]

for every event and branch. A unitary matrix with constant modulus
\(1/\sqrt6\) is exactly a complex Hadamard matrix. Conversely, every
\(6\times6\) complex Hadamard has \(|S|^2=J_6/6\) and produces the target.

Row phases, column phases, and row/column permutations do not alter the event
kernel and are gauge equivalences, not source provenance.

Checker: `research/flavor/checkers/wp1123_unitary_s_matrix_hadamard_classification.py`

Result: `results/wp1123_unitary_s_matrix_hadamard_classification.json`
