# Sector closure of the edge traces recovers the full proton field

Fresh mutable state remains local net revision21 with face-chart descent open. The moving-observation receipt showed that the fixed12 trace channels cannot recover their sector-rotated versions. This turn computes the exact minimal linear repair rather than adding an arbitrary larger readout.

## Result: dimension36, not a compressed channel

Let H be the12 original edge-occurrence tangent rows and R the actual order-three36-coordinate proton sector permutation. Stack

    S = [ H ; H R ; H R^2 ].

Exact rational elimination gives rank36. Its reduced row basis is I36. Every one of the12 patches contributes three independent covectors: closure requires its entire three-component field vector, not merely its original scalar tangent trace.

The smallest linear observation row space containing H and closed under R therefore has dimension36, requiring24 additional independent covectors. There is no discarded field direction. This conclusion concerns the full36-coordinate proton field, not merely a particular prepared subspace or additional spin coordinates.

## Certificates and minimality

The receipt retains the orbit matrix S, the elimination matrix L and both reconstruction directions:

    O = L S,
    S = D O,

where O = I36. It also contains the original-trace decoder and an output action K satisfying

    O R = K O,    K^3 = I.

Any invariant linear row space containing H contains H R and H R^2, hence contains row(S). These exact inclusions certify minimality, rather than just demonstrating one sufficient enlargement. Patchwise elimination independently gives rank3 on every patch and their ranks sum to36.

The zero-dimensional discarded subspace is trivially rotation invariant; no nonzero compression kernel is hidden by that wording. Full parent field information is retained.

## Consequence beyond linear channels

The certificate also explains an information-level limitation. Suppose a possibly nonlinear channel q has a deterministic update under R and decodes H for every field. If q(x)=q(y), then its first three decoded observations imply S x=S y. Since S is invertible, x=y. Thus such a channel cannot identify two distinct fields.

This is an injectivity consequence, not a dimensional lower bound on arbitrary nonlinear encodings, nor a physical implementation claim. The implemented numerical certificate is the exact linear rank/reconstruction calculation.

## Geometric boundary

Each added canonical covector remains supported on one patch. Nevertheless, retaining full patch vectors does not make the source sector permutation a geometric vertex/edge relabeling; the preceding support obstruction remains. The repair restores a closed field observation interface, not the original scalar edge convention or local face gluing.

The next net-facing question is now sharply about operation policy: is the actual sector permutation required to represent a geometric incidence transition, or is it a distinct internal field operation allowed to change observation supports? A retained full-field construction can handle the latter, but cannot silently assert the former. This distinction should be stated against the parent acceptance gate before adding another observation wrapper.

## Verification

- Contract: `contracts/ramsey-edge-observation-closure-attempt.v1.json`.
- Checker: `checkers/check_ramsey_edge_observation_closure.py`.
- Receipt: `results/ramsey-edge-observation-closure-v1.json`.
- Passing freeze: `scc-freezes/ramsey-edge-observation-closure-v1.cd3a726b7dd88957.json`.

The frozen challenge passes exact rational row-space, support, reconstruction and action checks with fresh direct source pins. No new kernel numerical interpretation, graph mutation or Git checkpoint occurred. The broader descent conjecture remains open.
