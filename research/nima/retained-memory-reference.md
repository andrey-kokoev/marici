# The prior exchange generates a reference from retained past carrier data

## Recover the existing mechanism before adding preparation rules

`comparison-update-dynamics-and-energy-normalization.md` already stores the previous longitudinal carrier value in the record. `four-packet-record-feedback.md` already gives its multi-component conservative implementation. This step traces that source of reference data explicitly; it does not introduce a new response law.

There are two distinct uses of “reference” in the preceding work:

- the comparison VALUE read from the retained bank;
- the orientation/mixing operator J and its physical framing.

The present result supplies the former from memory. It does not derive the latter or eliminate its frame-selection requirements.

## Comparison and record lineage

After the already declared rotations, put

    x_bar=R x, t_bar=L t,
    delta=C t_bar-x_bar.

The actual prior exchange is exactly

    x_next=x_bar+delta,
    t_next=t_bar-C^T delta.

Thus the active response is driven by the discrepancy between a current carrier value and a separately retained bank value. Neither is defined retrospectively as the certified output of the other. If delta=0, the exchange leaves its entire input state unchanged, as required by the source condition.

The readable record after exchange is

    C t_(n+1)=R x_n.

After one further advance, that retained value appears at the hidden return port:

    C L t_(n+2)=R x_n.

Both identities are checked over a full basis. The record used in a later comparison therefore has concrete ancestry in an earlier carrier value.

## Empty-bank control

Start with the declared empty bank and scalar-unit carrier. The first three comparisons have discrepancies

    -1, 0, +1,

and carrier outputs

    0, 0, 1.

The initial budget is one and remains one. The nonzero reference was not added as a second externally prepared value: the original carrier budget moved into retained records and returned. Every parent state is retained and all three advances reverse exactly.

Zero-bank initialization and the initial carrier are still supplied inputs. This does not derive their physical preparation, and it does not prepare the richer ordinary/twisted tetrahedral banks from the carrier alone.

Those existing banks were checked separately. Their mismatch histories differ, and their first carrier outputs remain +1/2 versus -1/2 under the unchanged fixed-reference law. The previously recorded physical/frame interpretation limits still apply.

## Consequence for the earlier detour

The failure of comparing a witness against its own certified target does not imply a need to invent another independent reference protocol. The existing memory lift already provides a distinct earlier record. This lets us return to the original conservative comparison model instead of making the added Boolean flip controller a prerequisite for every response.

What remains unselected is the port, its relation to complete tetrahedral witnesses, the mixing/frame structure, preparation and any physical readout. No new autonomous physical law or gravitational coefficient follows from this memory-lineage check.

## Verification

`python research/nima/checkers/check_retained_memory_reference.py` passed with exact rational mismatch identities, full-basis lineage checks, empty-bank and existing fixture controls, budget preservation and reverse history recovery. Results: `results/retained-memory-reference.json` with source digests.

No prior update implementation was modified. No ledger entry, commit or publication is claimed.
