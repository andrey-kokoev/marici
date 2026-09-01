# Green-residue event-basis no-go: WP1126

## Question

Can localized Green-function residues supply a six-channel event basis and
\(H_6\) phases?

## DPC resolution

- **Conjecture:** localized physical16 Green residues decompose into six event
  channels carrying \(H_6\) phases.
- **Rivals:** rank-one common Green residue; factorized brane-coupling
  residue; six independent residue channels; no residue event basis.
- **Risky consequences:** six independent physical16 residue channels, a
  six-channel bijection, 36 unit-modulus phases up to the common
  \(1/\sqrt6\) scale, and packet-preserving event-index observables.
- **Falsification attempt:** the sourced residue is \(vv^T\) with rank one and
  every \(2\times2\) minor zero; it supplies one channel, not six, and no
  phase observables.
- **Residual:** a future boundary Green function could supply six independent
  residues and phases.
- **Disposition:** reject Green-residue \(H_6\) provenance for the current
  source.

## Exact obstruction

For \(g=(2,1,1,1)\), the factorized residue is proportional to \(gg^T\).
Every \(2\times2\) minor vanishes, so the residue rank is one. A rank-one
matrix cannot provide the six independent channels required by an \(H_6\)
event basis.

Checker: `research/flavor/checkers/wp1126_green_residue_event_basis_no_go.py`

Result: `results/wp1126_green_residue_event_basis_no_go.json`
