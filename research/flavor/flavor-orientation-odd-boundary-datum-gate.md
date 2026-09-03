# Orientation-odd boundary-datum gate: WP1252

## Question

Can the current source construct an orientation-odd boundary datum?

## DPC resolution

- **Problem:** construct an independent orientation-odd UV boundary datum
  selecting the local split and clock orientation, then derive \(\rho\),
  source kernel, gain, and Physical16 descent.
- **Bold conjecture:** boundary S-matrix or phase data may construct the
  orientation-odd UV datum selecting the split, clock orientation, and
  production algebra.
- **Named rivals:** complete-mixing source; irreversible boundary
  generator; \(C_6\) Fourier Hadamard; \(C_3\times\mathbb Z_2\) Kronecker
  Hadamard; anomaly-sector phases; Green-residue channels.
- **Risky consequences:** complete mixing needs \(x=0\) and irreversible
  six-state rates; the required unitary class is \(H_6\) with all moduli
  squared \(1/6\); \(F_3\otimes F_2\) is target compatible; anomaly or
  Green residues must source phases and six event channels.
- **Strongest falsification attempt:** history has three isometric slots,
  zero dissipative rates and event-time maps, no \(C_6\) generator,
  endpoint \(\mathbb Z_2\) fails packet symmetry, anomaly coefficients are
  not phase characters, and the Green residue has rank one.
- **Exact residual:** derive a sourced boundary character with a
  selected-packet-preserving six-channel map and event-time interface.
- **Disposition:** retain \(H_6\)/\(F_3\otimes F_2\) as target algebra;
  reject current-source orientation-odd datum.

Checker: `research/flavor/checkers/wp1252_orientation_odd_boundary_datum_gate.py`

Result: `results/wp1252_orientation_odd_boundary_datum_gate.json`
