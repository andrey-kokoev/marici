# Prepare relative opposition using the existing flip witness

## What is reused and what is new

The existing tetrahedral source contains a Boolean flip and its inverse. `TetrahedralEdgeReadout.agda` proves those transport functions for the actual retained edge paths. Their counting-basis matrix is X=[[0,1],[1,0]]. The previous Clifford construction supplies J, with X J X=-J.

This test introduces an explicit preparation protocol using those operations. It does NOT claim that prior research or WG uniquely selected the protocol, that a flip should physically act on a reference, or that the source has prepared J from nothing.

## Conditional protocol

Start with the supplied retained pair (A,B)=(J,J). Act on A alone by the existing flip:

    A_next=X A X^-1,    B_next=B.

Retain the acted-on side, previous state and operation history. Conjugating A again recovers its original value. The returned reference values are equal to the initial pair, but the two-operation history is not identified with the empty history.

For flat H=I, the previous rooted return reads b0=(1/2) B A^-1. Its trace follows

    +1 -> -1 -> +1.

The minus sign is computed from the actual conjugation, not assigned as a desired response coefficient. The summed squared Frobenius norm of the two reference matrices is preserved at four; this is a coefficient budget, not calibrated energy.

## Distinguish intervention from passive transport

Conjugating BOTH references by a common frame change conjugates b0 and preserves its trace. Acting on one reference changes their relation. Flipping both separately also restores alignment, with both operation records retained.

All four single-flip parity cases and both Boolean root-frame choices are checked exactly. The relative signal depends on the parity of single-reference interventions, not on an absolute sign chosen for both references.

## What has and has not been supplied

We now have a concrete conditional preparation of opposed alignment using an existing source operation, rather than supplying unrelated +J and -J matrices by hand. The initial pointing J, the pair preparation, and the choice to intervene on one member remain explicit protocol inputs.

This does not close the physical source-selection problem: an actual coupling must determine which reference is acted on and when. Nor does it identify the seed's reciprocal seam with these matrix reference ports. It supplies no autonomous clock or gravitational normalization.

This checker concerns reference preparation and its relational readout only. It does not establish conservation for a new joint dynamics in which evolving references also change the old fixed bank mixer. The old fixed-mixer feedback theorem must not be transferred to such a combined system without checking that enlarged operation.

## Verification

`python research/nima/checkers/check_reference_alignment_preparation.py` passed using exact rational arithmetic. The checker verifies the existing Agda edge-readout receipt and current proof-source digest, then uses its explicit Boolean truth-table contract; this is not extracted Agda execution. Results: `results/reference-alignment-preparation.json`.

No prior dynamics implementation was modified. No ledger entry, commit or publication is claimed.
