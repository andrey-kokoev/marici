# Fine refinement can force history separation, but tighter lifting does not

## Important correction to the target

The moment-curve histories A=[f,1] and B=[0,g] have a common exact section because f<=g everywhere. Tightening an approximate-lift tolerance, even to zero, therefore cannot by itself prove that the histories must be split. It may invalidate the current section or require more section pieces. A genuine incompatibility certificate must concern a stronger contract with different required answers.

The control freshly verifies Nima's n=18, eta=0 whole-polygon certificate: it has sixteen cells. This rules out presenting a failed approximate selector as impossibility of common exact lifting.

## One fine continuation with incompatible answers

Use the same n=18 owning m=4 family and apply the SAME fine refinement to both possible original histories:

    h<=1/2, equivalently t0<=50+128^-4/2.

Request exact admission of the public point (p,q)=(1,1) after that refinement. These coordinates correspond to exact original moments U=206+128^-4 and V=V(center)+128^-4.

At this public vertex both scalar envelopes equal one. Consequently:

- A requires h>=1, contradicting the refinement. The refined A fiber is empty.
- B permits h=0. Its actual source lift obeys the atom caps, exact public moments, t1=51, all B envelope bounds and the new fine upper bound.

The negative certificate selects an independently reconstructed lower supporting plane whose value here is one. Combining -h<=-1 with h<=1/2 using weights (1,1) proves 0<=-1/2. The positive certificate is a rational original-atom witness, not a claim about a normalized candidate alone.

## What this proves

If both histories map to exactly the same retained semantic state, then the identical continuation and identical point request must produce the same answer. Correctness requires false for A and true for B. Thus no deterministic exact interface can support that continuation for both from the same state without history-dependent side information. Exact randomized correctness does not help: the required answer distributions are disjoint.

This is not an impossibility of returning some common pre-refinement lift. Nor is it a claim that the entire refined A domain is empty: only the displayed public fiber is certified empty. One differing admissibility answer already proves the required distinction.

## Archives cannot recreate erased identity

An archive containing both candidate histories and the refinement lets us compute both possible answers. It does NOT identify which original history actually occurred. Splitting into two possible branches can represent uncertainty, but does not restore actual-history authority.

For this two-branch family, at least one history-selection bit (or equivalent independently supplied provenance) is required to choose the actual branch. If that bit is retained privately in an archive, then the LIVE state may be merged, but the TOTAL retained state has not forgotten the distinction. Archive tokens, handles or external logs carrying it must be counted as side information.

The implementation records this logical accounting boundary. It does not implement an authenticated archive, reversible merge operation or authorized branch-selection protocol. Those require an owning provenance contract beyond arithmetic feasibility.

## Verification

`verify_fine_refinement_obstruction.py` imports neither the candidate constructor nor a retirement session. It checks the independently expected family/operation, public-domain membership, actual lower-plane membership, strict contradiction, original atom witness, exact moments and all B inequalities.

Five mutations are rejected: changed operation, false contradiction, invalid positive witness, invented supporting plane and changed family. The zero-tolerance common-section control is checked separately by Nima's independent whole-polygon verifier.

## Reproduction

    python research/voevodsky/checkers/check_fine_refinement_obstruction.py

Artifact: `results/fine-refinement-obstruction.json`.

The next operational step is a fail-closed capability-request interface that returns this verified ambiguity and accepts history provenance only through an explicit owning authority. It must not infer actual history from whichever old-compatible witness happened to be selected.
