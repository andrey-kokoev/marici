# Actual triangle components produce successor detail under existing composition

## Inputs are occurrence indicators, not fitted amplitudes

Take the two ORIGINAL seed components:

    L=(AB,BC,CA), R=(BA,AD,DB).

Give each occurrence in its component count one. This counts the supplied
records once; it does not assert unit physical excitation or a preparation
of quantum amplitudes. The components have disjoint occurrence IDs but share
actual vertices. Keep their L/R roles attached.

The checker registers these two families through the existing
`RetainedSuccessorLedger`, then calls its unchanged endpoint-compatible
bilinear composition. The original operands and every parent-slot pair are
recoverable. No new response operator, signed input, metric or gain is added.

## Exact compositions

| Product | Available two-step words |
|---|---|
|LL|AB BC; BC CA; CA AB|
|LR|AB BA; CA AD|
|RL|BA AB; DB BC|
|RR|BA AD; AD DB; DB BA|

These partition the existing ten-word successor. Each coefficient is one.
The four cross words arise specifically because the components share their
vertices; they are not four new primitive arrows.

## Nonzero detail without a chosen contrast preparation

Represent each role-labelled product as its occurrence indicator in the
common ten-word successor. Splitting it with the EXISTING averaging decoder
produces decoded-parent means plus a zero-mean sibling remainder.

For LR the remainder is

    +1/2 [AB BA] -1/2 [AB BC]
    -1/2 [CA AB] +1/2 [CA AD].

For RL it is

    +1/2 [BA AB] -1/2 [BA AD]
    -1/2 [DB BA] +1/2 [DB BC].

The signs here are derived COMPARISON RESIDUALS, not signed primitive input
amplitudes. Negative entries do not mean negative occurrence counts.
Both products reconstruct exactly from their means and retained remainder.
The remainders survive aggregation by final occurrence.

## Actual endpoint readout

Using the real target of each composed path, in A,B,C,D order:

    targets(LR)=(1,0,0,1),
    targets(RL)=(0,1,1,0),
    difference=(1,-1,-1,1).

The corresponding detail-only target readings are respectively
`(1/2,-1/2,-1/2,1/2)` and its negative. Thus the structural difference reaches
an actual source-endpoint observer, rather than being a completely hidden
coordinate in the successor.

This four-entry observer is NOT automatically the intended rung-4 physical
reference or the 137-row matrix-response reader. No such identification is
made from dimension alone, and the endpoint contrast is not called momentum,
charge, a spatial displacement or physical energy.

## Two decisive controls

**Forgetting roles cancels the detail.** Sum LL,LR,RL,RR: every successor word
has coefficient one and its sibling detail is zero. The distinction depends
on retaining which component supplied each operand, not merely the final
unlabelled pool. This is consistent with unchanged-copy extension introducing
no detail. It does not generate excitation from a uniform or zero input.

**Ungluing removes the cross domain.** Give the two triangles disjoint copies
of their vertices while preserving their occurrence IDs and local cycles.
LL and RR keep their three words each; LR and RL become structurally empty
compositions. That is a change in available source composition, not a measured
zero physical interaction. No unavailable experiment is assigned a response.

## Progress and remaining gate

This branch gives a concrete source-sensitive alternative to another fixed-
bank preparation: the ACTUAL component roles and endpoint composition produce
nonzero retained successor detail, using no tuned input coefficient values.
It is construction/readout of existing source records, not an autonomous
physical energy source or executed interaction.

The next gate is to bind this role-labelled successor to the intended native
operation and rung-4 observer. In particular, it must preserve the component
roles that prevent cancellation and justify how structural counts acquire
physical readout meaning. The earlier fixed-bank resource results cannot be
transferred to this different carrier and operation without that bridge.

## Verification

    python research/nima/checkers/check_actual_triangle_branch_composition.py

36 exact checks pass, with the existing imported path-composition controls.
Covers component-cycle attachments, four registered products, operand recovery,
exact detail reconstruction, final-occurrence and endpoint readings, role
forgetting, ungluing, and the zero-input control.
Receipt: `results/actual-triangle-branch-composition.json`.
No new Agda native-execution or physical interpretation theorem is claimed.
