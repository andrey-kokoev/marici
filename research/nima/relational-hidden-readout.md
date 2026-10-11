# Hidden return as a relation between transported references

## Reuse the prior reference distinction

`recovered-reference-return-response-chain.md` already distinguishes a fixed retained comparison reference, its attachments to ports, and passive changes of port coordinates. `co-constructed-seam-reference-hypothesis.md` treats the reference as an accompanying relationship but does not supply its physical preparation or identify the seam with an invertible matrix connection. `equivariant-carrier-is-not-yet-a-reference-frame.md` distinguishes a reference-capable carrier from an actually prepared pointing or relational partner.

This step applies that distinction to the recently tested tetrahedral edge readout. It does not redo the generic flatness audit or claim to derive the six-arrow seed's physical connection.

## Root-relative decomposition

Write u=u01, v=u12 and d=d02 for the two edges and closing diagonal. Bring the comparison operators and path discrepancy to the same root:

    A = u^-1 J1 u,
    B = d^-1 J2 d,
    H = d^-1 v u.

Direct substitution into the previously checked closed readout yields

    b0 = (1/2) B H A^-1.

Thus the response depends on the relative references AND the route holonomy. It is not a function of unnamed absolute frame coordinates.

Under arbitrary invertible local changes Gi, with edges transforming at both endpoints and Ji by conjugation, A,B,H and b0 all transform by root conjugation G0. Therefore trace(b0) is invariant. The algebraic cancellation establishes this generally; the checker exhausts the Boolean frame changes on three concrete fixtures.

## What the existing +/- example actually distinguishes

All three cases below have flat edge-action holonomy H=I:

| Reference-bearing state | Root-relative references | trace(b0) |
|---|---|---:|
| Ordinary edges, fixed J1=J2=J | A=B | +1 |
| Twisted edges, fixed J1=J2=J | A=-B | -1 |
| Twisted edges, reference transported with the vertex-1 flip | A=B | +1 |

The first two therefore differ in a relational datum once the reference operators are included in the state. They are not passive coordinate changes of the SAME complete reference-bearing state. The first and third have the same readout under the corresponding transported presentation.

This recovers a precise, frame-covariant reading of the earlier response distinction, without declaring it physically meaningful or deriving preparation of the differing reference alignment.

## Test the same-root attachment option

If both references are transported from a single root operator along the SAME paths used in the readout,

    J1=u J0 u^-1,
    J2=d J0 d^-1,

then A=B=J0 and

    b0=(1/2) J0 H J0^-1.

For the actual flat tetrahedral edge-action fixtures, H=I, so the output is always I/2. That attachment does not produce the prior hidden sign response. Nontrivial behavior in this formula requires nontrivial relative reference alignment or nontrivial route holonomy. A diagnostic nonflat matrix example is checked but explicitly not admitted as a filled tetrahedral source.

These are one-step readout and attachment statements. Making reference transport depend on the evolving state would alter the fixed-mixer dynamics; conservation and six-step recurrence of that new protocol have NOT been established by the old checker.

## Disposition

The next source object is now more precise: a retained, prepared relative reference relationship and its attachment/transport witnesses. Merely declaring a common frame, or transporting one reference along a flat comparison, does not create the desired additional response. The comparison trace above is a mathematical invariant under the declared frame policy, not yet energy, a coupling or G.

## Verification

`python research/nima/checkers/check_relational_hidden_readout.py` passed with exact rational matrix identities, 24 fixture frame-covariance tests, four same-root flat attachment cases and the clearly labelled nonflat control. Results: `results/relational-hidden-readout.json` with source digests.

No prior dynamics implementation was changed. No ledger entry, commit or publication is claimed.
