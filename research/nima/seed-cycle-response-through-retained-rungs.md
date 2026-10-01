# A seed-generated route response through the existing rung candidates

## Bounded bridge, not a particle model

Reuse the four-state permutation action of the existing seed cycles g=(ABC) and h=(ADB). Compare their two actual execution orders. With column-vector permutation matrices, the responses are L=P(hg) and R=P(gh). Their entries are derived from endpoint actions, not fitted leg coefficients.

In A,B,C,D order the defect L-R is

    [ 1  0 -1  0 ]
    [ 0 -1  0  1 ]
    [ 0  1  0 -1 ]
    [-1  0  1  0 ].

Every row and column sums to zero; the common mode is unchanged. The squared Frobenius norm is eight, a counting-metric diagnostic, not physical energy. A probe at A is returned to A by g then h, but sent to D by h then g. Thus the response detects order already present in seed operations.

This is a state-changing order comparison, not a supplied equality filler between those different actions. No higher witness equating the operators is asserted.

## Reuse of actual rung implementation

The existing `check_rung_transport_diagram.py` was minimally generalized: mean zero initialization now takes the input matrix shape; `read_at_four` accepts an optional explicit rung4 reference while preserving the original default fixture. Its existing137-slot checks still run and pass unchanged.

The new adapter encodes L in four labelled column records, each four times its column contribution. Their uniform mean reconstructs L exactly. This factor four is an explicit encoding normalization, not a seed energy coefficient. Labels retain both ordered cycle words. The initial direct comparison uses R at the readout interface as a diagnostic, not a physical calibration. The fixed-reference follow-through below instead transports both preparations against one common2I4 reference.

| Diagram role | Executed data |
|---|---|
|12|Four witnessed column records encoding L|
|11|Source-indexed records|
|10|Target-indexed records|
|9|Existing two-stage incoming-family promotion candidate|
|8,7|Its source/target presentations|
|6|Promoted records retaining all original columns|
|5|Source-indexed promoted records|
|4|Target-indexed promoted records; response mean minus R equals L-R|

Both existing endpoint policies commute through the diagram and preserve the entire defect. Here the columns share one operator target, so the experiment does not discriminate those policies. All four original records reconstruct. Comparing L against L gives exactly zero as a control.

## Fixed-reference and observation follow-through

The checker now encodes BOTH route responses in the same column scheme and carries each through both existing transport candidates. It compares them against one fixed d4=2I4. This is the four-dimensional analogue of the original fixture's2I2 convention, not a derived physical normalization or an identification of its response space with the old two-dimensional space.

Writing rho_L=L-d4 and rho_R=R-d4 gives

    rho_L-rho_R=L-R.

The route-order distinction therefore does not require changing the reference for each state. More generally any common reference cancels in this difference.

The responses have equal trace and equal squared Frobenius norm. The common-state readout also cannot detect their difference, since every row and column of L-R sums to zero. However the named preparation/readout pair 'input A, read output A' gives

    e_A^T (rho_L-rho_R) e_A=1.

All24 vertex relabellings preserve this statement when the marked preparation and reader move with the source. This is a concrete state-resolved observation profile, not a claimed physical detector. It is not permissible to turn trace/norm equality into identification of the complete responses.

For pair synthesis this is a control rather than a species result: the two operations have the same unmarked permutation cycle type. The test establishes a context-sensitive order response, not two invariantly different particle species or different masses. The next physical question concerns which retained preparation/readout profile is supplied at rung4; the calculation does not select it.

## Does the seed select the distinguishing probe?

A further exact control enumerates automorphisms of the actual six directed edges, not of the completed K4. They are identity and s=(AB)(CD). This symmetry exchanges the two triangle generators:

    s g s^-1=h, s h s^-1=g,
    P(s) L P(s)^-1=R.

Consequently any scalar observation invariant under this seed symmetry has the same value on L and R. This is stronger than the trace/norm controls and includes nonlinear invariant scalar readings. The full symmetry-averaged matrices coincide; the averaged defect vanishes exactly.

This does not erase the order effect or forbid covariant marked probes. It establishes that the unmarked directed graph cannot select a probe that distinguishes these symmetry-related orders without further retained structure. If the ordered pair of triangle generators (g,h) is itself part of the source record, only the identity automorphism preserves it. The order distinction then survives as provenance. Whether the physical observation is allowed to use that marking is not decided by graph symmetry alone.

This control connects to the existing `arrow-history-window.md` and `retained-square-reversal.md` distinction between retained schedules and equal/coarse readouts. No new history-retention mechanism is needed. What is missing is a physical use of that already retained order, not storage of the order itself.

For the proposed particle pair, this branch establishes no invariant species asymmetry. It should not be extended by assigning masses to L and R. The symmetry result is scoped to the unmarked seed and these two permutation responses, not a no-go theorem for every seed-derived packet or source-marked realization.

## What this closes

There is now one explicit amplitude-free-in-the-sense-of-no-fitting seed-action response carried through the existing retained rung machinery. It connects concrete endpoint permutations to the numerical record interface, rather than assuming the old matrices I+(i/3)H and I+(j/5)K.

It does not construct the original137-slot shared-leg response from the seed, identify the chosen horizontal candidate as physical dynamics, or connect this reference R to the physically calibrated fixed d4. It uses a declared permutation representation and column/mean encoding; these assumptions remain visible. No source-policy Agda derivation or native-to-DG filler adapter is claimed. Nor are the two execution orders two particle species.

## Verification

    python research/nima/checkers/check_seed_cycle_response_transport.py

Passes exact rational checks for derived permutations, nonzero contrast defect, both commuting routes, leaf/word retention, the matched-order zero control, common fixed-reference subtraction, trace/norm blindness, a separating state probe and all24 relabellings. It reruns the original rung diagram and its shared-leg DG checks. No physical scale is fitted.
