# Different retained tetrahedral witnesses change the next active carrier

## Discriminating test

Use the existing ordinary and twisted filled tetrahedra in `RetainedTetrahedralPackage.LossyDiagonal`, not the obstructed free-seed realization. They have the same four marked vertex values and the same diagonal, but different retained edge witnesses.

The result is positive for an explicit two-edge adapter to the existing four-packet feedback law: equal initial carrier, equal current sewn record readout and equal total budget can lead to different next carrier values. The update law and its coefficients were not changed.

## Source-derived edge actions

`agda/TetrahedralEdgeReadout.agda` proves the transport functions on edges 01 and 12 of the actual filled packages, for every Boolean input:

| Package | Edge 01 | Edge 12 | Composite |
|---|---|---|---|
| ordinary | identity | identity | identity |
| twisted | flip | flip (inverse of flip) | identity |

It also checks equality of the marked vertex and reuses the same-diagonal theorem. These are computations from the existing paths via univalence, not guessed response matrices.

## Explicit new port adapter

Linearize those functions in the Boolean counting basis (false,true). Their permutation matrices are I and X=[[0,1],[1,0]]. In the existing Cl(2,0) coefficient basis, I is the scalar unit and X is e2. Matrix reconstruction is checked exactly.

Use the ordered pair of composable edges as the record bank:

    t = coefficients(edge12) tensor coefficients(edge01).

This ordering makes the existing sewing read edge12 after edge01. The two banks are

    t_ordinary = 1 tensor 1
    t_twisted  = e2 tensor e2.

Both sew to 1 since e2 squared is 1. The selected ordered edge port is a declared adapter; the seed has not uniquely selected it as a physical coupling. It reads two retained edges, not the whole tetrahedral package. The original package and other witnesses must remain available separately; they cannot be reconstructed from this bank alone.

## Unchanged prior feedback separates them

Reuse `check_four_packet_record_feedback.cycle` exactly:

    x_next = C L t
    t_next = C^T R x + (I-C^T C)Lt,

where C is half Clifford sewing, R is the existing half-turn and L=R tensor I. R fixes 1 and negates e2. Consequently:

| Quantity | Ordinary | Twisted |
|---|---|---|
| Initial carrier x | 1 | 1 |
| Initial record readout Ct | 1/2 | 1/2 |
| Initial total squared budget | 2 | 2 |
| Next carrier CLt | +1/2 | -1/2 |

All entries are exact rational coefficient statements. The response distinction holds for any shared initial x because this update's x_next depends only on the bank. The chosen x=1 gives a simple equal-budget fixture.

The checker verifies full budget preservation and inverse recovery for both cases. A reader retaining only (x,Ct) could not reproduce both next outputs: those inputs agree, while the outputs differ. Thus these records are causally relevant to the chosen update, not merely metadata attached to it.

## What this establishes

This is the requested bounded demonstration: existing distinct tetrahedral witnesses can feed different next active states through an existing conservative return map, with no fitted gain or alteration of its law. It goes beyond the earlier comparison-only adapter, whose tetrahedral payload was inert.

It does not derive the port selection, metric, Clifford interpretation or feedback schedule uniquely from WG. It is not a physical gravitational prediction or a universal tetrahedral back-reaction theorem. Whether these witness distinctions are physically observable, rather than identified by a physical gauge policy, also remains to be established. The test distinguishes fixed source records under the declared observation and update.

## Follow-up: fixed versus transported comparison references

`tetrahedral-hidden-readout-frames.md` checks the previously open frame issue. At the edge-action level, the ordinary/twisted pair is related by a local Boolean frame flip. Transporting the inserted J references with that change removes the sign distinction; holding them fixed preserves it. Thus the positive result here is a response relative to the declared fixed reference, not an established gauge-invariant physical signal.

## Verification boundary

1. Fresh safe Cubical Agda check: `TetrahedralEdgeReadout`, with ignored interfaces and stable inputs. Receipt: `results/agda-TetrahedralEdgeReadout.json`.
2. `python research/nima/checkers/check_tetrahedral_record_return.py`: exact Fraction arithmetic passed. Results: `results/tetrahedral-record-return.json`.

The Python checker verifies the proof receipt and its current source digest, then uses the four explicitly proved Boolean truth tables as its interface contract. This is a two-layer check, not extracted Agda execution or a single end-to-end formal proof of the numerical program. Source digests for the fixtures and unchanged feedback implementations are retained in the result.

No ledger entry, commit or publication is claimed.
