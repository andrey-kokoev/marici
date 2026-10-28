# Ru-98: sixteen-strand native-edge candidate

Wiring is separate from the preserved native graph in Lattice.

The input and output carry the same sixteen `(a,b,p,e)` identities. `a` is retained in/out polarity, `b` information-flow polarity, and `p,e` transport-role polarities. No branch creates or destroys an identity.

## Explicit embedding convention

The tetrahedral carrier has opposite edges, not Sulfur's opposite octahedral tips. Choose the coordinate partition `{0,1} | {2,3}`. The two bits `(a,b)` select one of four interior lattice ports on each opposite edge, indexed `k=1..4`.

At the input port the coordinates are `(-1,-1,k-1,4-k)`. Over five native steps, transfer the `k` units of coordinate 2 and `5-k` units of coordinate 3 into coordinates 0 and 1. `p` chooses the order of deposition into 0/1, while `e` chooses the withdrawal order from 2/3. The output is `(k-1,4-k,-1,-1)`.

This is a declared candidate routing convention, not a derivation of the physical polarity meanings. Four-by-four external bundles retain all identities at both ends. Wire lane offsets are display geometry; the retained guides are exact honeycomb edges.

## Checks and limitations

- 16 distinct, nonbranching, five-edge paths; 78 distinct occupied native edges.
- Every guide point remains in the edge-five tetrahedron.
- Every guide segment is an actual cell edge.
- Swapping coordinate pairs and reversing paths maps the candidate to itself under `(a,b,p,e) -> (a,b,-e,-p)`.
- All 20 geometric N carrier cells have edge incidence with the paths.
- The displayed retained inventory of 54 N records belongs to the earlier witness/extension construction. It has not been identified with these paths or with a tube count. `NChannelCount` remains unset.

Verified by `tests/ruthenium-98-wiring.test.mjs` and `scripts/test-ruthenium-98.mjs`.
