# Boundary S-matrix phase matching gate: WP1150

## Question

Can boundary S-matrix or Hadamard phase data distinguish the three quotient
matching classes?

## DPC resolution

- **Problem:** test whether boundary phase data select a production matching.
- **Conjecture:** S-matrix phase data select one quotient matching class.
- **Rivals:** universal Hadamard modulus; fixed-\(q\) rank-three matching;
  phase-gauge representative; no phase discrimination.
- **Risky consequences:** an \(H_6\) modulus maps every basis vector to
  \(u=(1/6)^6\); a matching maps only source \(q\) to \(u\); phase changes
  preserve moduli; physical16 channels are required.
- **Falsification attempt:** Hadamard phase data are class-independent, every
  rank-three matching is nonuniversal on basis vectors, and zero physical16
  asymptotic channels are sourced.
- **Residual:** a fixed-\(q\) nonuniversal S-matrix may be compared to the
  matching polytope.
- **Disposition:** reject boundary phase selection and keep the matching
  classes open.

Checker: `research/flavor/checkers/wp1150_smatrix_phase_matching_gate.py`

Result: `results/wp1150_smatrix_phase_matching_gate.json`
