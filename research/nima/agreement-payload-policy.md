# What agreement actually preserves: payload, not every retained history

## Fresh source audit and formal counterexample

Read the exchange uniqueness packet and the actual `TriangleComparisonFeedbackRegression.agda` implementation. The latter exchanges the two retained routes and their certificates while reversing the equality witness. Its first exchange is nontrivial even when the two routes have the same effect.

`agda/AgreementPolicyBoundary.agda` specializes the already existing `TetrahedralComparisonFeedback.Fixture`, using its actual filled typed-value tetrahedron. Fresh safe Cubical checking proves:

- Its two route effects agree.
- Its retained comparison changes under the existing exchange.
- Its decoded tetrahedral payload is unchanged.
- Therefore a blanket rule saying equal effects force the whole comparison record to remain fixed is false for this existing implementation.

The same module checks a different operation: `RetainedTetrahedralPackage`'s generator retains an already completed package unchanged. That is an explicit constructor clause, not a universal consequence of agreement. The two operations should not be conflated.

This rules out using generic WG effect agreement as an unqualified justification for freezing all records. It does not invalidate the earlier numerical exchange theorem under its explicitly stronger full-state agreement hypothesis.

## A more faithful numerical selection question

The source feedback preserves a decoded payload while allowing its histories to change. Can the numerical memory model preserve a similarly reconstructing payload, instead of requiring native history stasis?

Keep the current twelve-mode projector, mean-zero bank Pw=0, and phase family

    U_eta(x,w)=(Px+eta*w,(I-P)x).

Require a fixed LINEAR decoder D on this current numerical state, with two reconstruction contracts:

    D(x,0)=x,
    D(Px,(I-P)x)=x.

The first decodes the initial preparation. The second decodes the same payload after the already specified lossless first write. They are not merely agreement of normalized intensities.

Write D(x,w)=A x+B w. The first contract gives A=I. The second gives BQ=Q, so on the physical bank sector w=Qw the decoder is forced:

    D(x,w)=x+w.

The checker independently verifies that the two families of constrained inputs span all 23 dimensions of this sector. Thus the decoder is uniquely fixed there, rather than selected after examining the desired center trajectory. This is not a reconstruction of all 23 state coordinates into twelve; it decodes the initial coefficient payload while retaining the state/history separately.

## Payload conservation selects the original return phase conditionally

Requiring that decoder to remain invariant under feedback gives

    D(U_eta(x,w))=x+eta*w = D(x,w)=x+w.

For all stored contrasts this forces eta=1. By contrast, the weaker decoder Px stays fixed for every return phase and cannot select one.

The original memory swap therefore has a better conditional justification than blanket history stasis: it conserves the fixed linear reconstructed payload before and after record exchange. At the same time it permits nontrivial motion between active carrier and memory, as the source feedback permits nontrivial retained-history changes.

This also clarifies the earlier coherent-sum first moment: x+w is the candidate decoded payload, so its conserved first moment is not an accidentally chosen invariant of the trajectories. Its physical interpretation as spatial density is still separate.

## Unclosed identification

The Agda source decoder recovers a retained tetrahedral object. The numerical decoder recovers a twelve-coefficient field. We have not supplied an intertwining map identifying those two payloads, nor proved that the source demands a fixed linear current-state decoder. A history-dependent decoder could recover phase-twisted executions without obeying D(x,w)=x+w at every stage.

Therefore this is a source-informed conditional selection, not an end-to-end derivation of physical dynamics. Port, metric, numerical realization, fixed-decoder policy and physical readout still need their source justification. No electron charge, mass or recoil law follows from the argument alone.

## Verification

- `pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module AgreementPolicyBoundary -Fresh` passed with stable inputs. The compiler reports an inherited `TypedGeneratorLayers.agda` import warning about `isPropIsContr`; no theorem in this new module depends on that missing export.
- Receipt: `results/agda-AgreementPolicyBoundary.json`.
- `python research/nima/checkers/check_agreement_payload_policy.py` passed exact spanning, decoder and phase controls and verified the current formal source digest.
- Results: `results/agreement-payload-policy.json`.

No prior source law was changed. No source-to-physics identification, ledger entry, commit or publication is claimed.
