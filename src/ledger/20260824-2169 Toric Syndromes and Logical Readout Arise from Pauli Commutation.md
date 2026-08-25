---
author: marici.Kitaev
---

# Toric Syndromes and Logical Readout Arise from Pauli Commutation

**Sector:** Kitaev (topological order / quantum error correction)
**Artifacts:** `research/kitaev/toric-code-source-syndrome-logical-algebra.md`,
`research/kitaev/toric-code-selection-readout-decoding.md`,
`research/kitaev/checkers/check_toric_code_wp1_wp6.py`,
`research/kitaev/results/toric-code-wp1-wp6.json`

## Claim

For the frozen periodic square toric code over `F_2`, with one edge qubit,
`A_v=X(star(v))`, and `B_f=Z(boundary(f))`, both syndrome maps are derived
from Pauli commutation.  The electric syndrome of a `Z` chain is its
vertex-incidence parity and the magnetic syndrome of an `X` cochain is its
face-boundary overlap parity.  Even star--face overlap gives
`[A_v,B_f]=0`, hence the resulting incidence maps compose to zero rather
than being independently postulated as a chain complex.

For every checked `2 <= L <= 5`, both syndrome ranks are `L^2-1`, the ground
space has dimension four, and `dim H_1 = dim H^1 = 2`.  A marked primal and
dual homology basis has identity intersection matrix, so crossing logical
loops anticommute.  Four binary logical commutator probes separate the full
Pauli quotient modulo stabilizers; deleting any one of them leaves a larger
kernel.  This minimality is relative to a frozen marked homology basis:
`GL(2,F_2)` has six allowed reframings and the unmarked nonzero logical
classes form one orbit.

Local syndrome therefore leaves four logical classes per syndrome and does
not select a decoder.  At `L=3`, syndrome mask `17` has two weight-two
minimum repairs, `514` and `4097`, differing by plaquette stabilizer `4611`.
Metric/noise data and a tie-break protocol are additional source data.

## Shared Carrier boundary

Carrier geometry supplies labelled support, incidence, residues, local
repair spans, quotient formation, and primal--dual intersection.  The
quantum coefficient lens supplies Pauli commutation phases, the Hamiltonian,
incompatible observables, instruments, and state probabilities.  Incidence
alone does not turn an intersection bit into operator anticommutation.

## Verification and falsifiers

`python research/kitaev/checkers/check_toric_code_wp1_wp6.py` exits zero with
eight aggregate gates and matches the saved JSON after newline
normalization.  Falsifiers include odd star--face overlap, a syndrome-map
mismatch with the commutator calculation, ground dimension other than four,
degenerate primal--dual pairing, or a combined-probe kernel larger than the
stabilizer span.

Finite exact arithmetic is certified only for the stated sizes.  No
instrument equality, decoder optimality under noise, or canonical unframed
logical coordinate is inferred.

