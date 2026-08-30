# Clifford teleportation and the magic-resource boundary

Owner: `marici.Kitaev`

Status: component Clifford gates constructed by encoded teleportation;
controlled inversion and two record phases obstructed in the frozen
stabilizer resource theory.

## Noncircular encoded Clifford teleportation

For a logical Clifford `U`, prepare and verify the encoded Choi state

\[
|U\rangle=(I\otimes U)|\Phi_L\rangle.
\]

Perform destructive pairwise physical Bell measurements between each input
rail and the first resource block.  This is not a logical transversal SUM:
each rail is measured once and then discarded.  The five-rail syndrome table
decodes one bad rail outcome.  The surviving half receives a logical product
Pauli determined by the Bell result, represented by the explicit logical
Pauli words frozen in the code packet.

The finite checker verifies every branch:

- logical `H`: 4 branches;
- logical `F3`: 9 branches;
- logical qubit SUM: 16 branches;
- logical qutrit SUM: 81 branches.

All 110 corrections are product Paulis.  A one-system Choi resource uses two
encoded blocks and five destructive Bell rail pairs.  A SUM resource uses
four blocks and ten rail pairs.

Verified Choi preparation is explicit.  The selected logical `X,Z` words both
have physical weight three.  The two Fourier-resource stabilizers therefore
have weights `(6,6)` and require 36 cat--data contacts plus 30 cat checks over
three verification rounds.  The four SUM-resource stabilizers have weights
`(9,6,6,9)` and require 90 contacts plus 78 checks.  A logical Pauli frame sets
the measured eigenvalues to `+1`, followed by final component recovery.

## Controlled inversion is the hybrid magic gate

Full `S3` multiplication contains

\[
C\!I:\ |e,k\rangle\longmapsto|e,(-1)^e k\rangle
\]

on a qubit tensor qutrit.  Exhaustive conjugation of the four product-Pauli
generators shows that only the qubit `Z` image remains a product Pauli.  Thus
`CI` is not Clifford for the frozen hybrid Pauli structure.

Naive Choi teleportation has 36 Bell branches.  Only four have Clifford
feed-forward; 32 require a non-Clifford correction.  Its apparent `1/9`
Clifford branch therefore gives a postselected experiment, not a deterministic
fault-tolerant gate.  Stabilizer ancillas, product-Pauli measurements,
Clifford Choi resources, and Pauli feed-forward cannot deterministically
implement full `S3` multiplication.

The required new source is a verified controlled-inversion magic state or an
explicit code switch to a gate set containing the same hybrid non-Clifford
operation.

## Record-phase inventory

Write the sector residue as `r=4 b2+2 b1+b0`.  The record-controlled phase
factors into three two-qubit controlled phases.  Exact four-qubit normalizer
tests give:

| controlled power | Clifford? | missing resource |
| --- | --- | --- |
| `U` | no | controlled-`T`-type phase |
| `U^2` | no | controlled-`S`-type phase |
| `U^4` | yes | none beyond Clifford teleportation |

Once an eight-sector residue already exists in three logical qubits, copying
it into another label block is three logical qubit SUMs and is covered by the
Clifford teleportation construction.  Coherently *extracting* those bits from
holonomy and charge modes remains a controlled lookup and inherits the same
nonstabilizer-source problem; it is not licensed by the easy label-to-label
copy.

## Verification

Run:

```text
uv run --with numpy python research/kitaev/checkers/check_s3_encoded_clifford_teleportation.py
uv run --with numpy python research/kitaev/checkers/check_s3_controlled_inversion_magic_obstruction.py
uv run --with numpy python research/kitaev/checkers/check_s3_record_phase_magic_obstruction.py
python research/kitaev/checkers/check_s3_clifford_choi_verification.py
```

Saved outputs use the same stems under `research/kitaev/results/`.

The result is a typed construction/no-go split.  It does not infer that magic
states are physically available merely because their addition would restore
universality.
