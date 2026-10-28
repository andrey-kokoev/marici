# Two-ended sector transport: passing works, stage-28 exchange does not

## Candidate tested

The operator's conjecture is two full 28-stage fibrations of the same whole, from opposite P/E presentations. They pass through one another without merging histories and arrive at the opposite endpoint presentations. This is not a 14+14 construction that terminates at a midpoint.

Test the previously displayed sector-label model first. Let A=00, B=10, C=01, D=11, with L and R flipping the respective bits. Retain twelve labelled rows (label,i,j), i != j, and transport both endpoints by g: (i,j) -> (i xor g,j xor g). Source-column fibration groups them into four triples and retains their labels and reconstruction data.

Choose opposite corners A,D as candidate endpoint presentations; their identification as P/E is not derived. Initialize the two traces independently in those endpoint charts. The forward trace applies L,R,L,R,...; the other applies R,L,R,L,.... A phase here is label translation followed by re-fibration, NOT one operation of the separate four-stage group/reversed-unpack cycle. Alternation is a declared candidate rule, not a recovered whole-state evolution law. No phase is specially inserted to force the number 28.

## Actual trace

| Stage | Forward source corner | Opposite traversal source corner | Comparison |
|---:|---|---|---|
| 0 | A | D | Distinct endpoints |
| 1 | B | B | Same complete labelled table; different histories |
| 2 | D | A | Opposite endpoints reached |
| 3 | C | C | Same complete labelled table; different histories |
| 4 | A | D | Original endpoint tables restored |
| 14 | D | A | Exchanged |
| 27 | C | C | Passing again |
| 28 | A | D | Returned, not exchanged |

At each phase the marked fibers reconstruct all twelve rows. Canonical chart comparisons compose exactly, and the three nonzero endpoint differences are conserved channel labels. Same-stage coincidences occur at every odd stage through 27. The retained operation words differ there; no history is identified merely because its current table agrees.

Endpoint exchange occurs at 2 modulo 4. The script also checks stage 30 as a control of that formula, NOT as a proposed replacement for the operator's conjectured 28. At an exchange horizon, complementary-stage tables agree; at horizon 28 they do not literally agree, though the declared chart comparison still exists.

## What this means

The minimal periodic sector model constructs the proposed passing behavior and exact label-level coherence. It does not construct the requested 28-stage endpoint exchange. This rejects that periodic candidate, not the global conjecture or an explicitly different initial-stage convention.

If P/E are fixed readouts of this four-periodic endpoint table, 28 cannot exchange them. A successful binding would have to use additional retained structure, such as nested fibration state or a changing contextual window, to distinguish the endpoint presentations despite a repeated table. An arbitrary stage-count-triggered relabeling would not derive the claim.

The missing test is the binding of the three-active-plus-context windows to this sector trace and its retained ancestry. Mere sector-label motion is not yet the full operator on coefficients and higher coherence witnesses.

## Verification

`python research/strominger/checkers/check_two_ended_sector_trace.py`

18 exact checks pass, with 48 discrete frame/sense cases (all 24 endpoint relabelings and both traversal senses). [Receipt](results/two-ended-sector-trace.json) retains both complete 31-state traces, histories, all twelve rows at every stage, source fibers and source hashes.

Scope: labelled incidence, fibration recovery and the candidate square's comparison laws. This does not certify arbitrary continuous-frame covariance, C3 coefficient action, a physical P/E assignment, full esd7 coherence or Pb-208 assembly. The existing source constructors were not modified.
