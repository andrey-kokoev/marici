# Sixteen retained strands: full-carrier native-edge candidate

Wiring carries sixteen identities `wire:abpe`:

- `a`: retained in/out polarity, not endpoint location;
- `b`: information-flow polarity;
- `p`, `e`: transport-role polarities.

Both external bundles expose the same sixteen records, with an explicitly retained endpoint permutation. The four colours encode `(p,e)`; each colour has four `(a,b)` lanes. Grouping never creates or deletes records.

## Construction conventions

For each `(p,e)` entry edge, its adjoining charged faces are sorted by cell ID. `a` selects a face. Its two descending native surface edges are sorted by vertex coordinates; `b` selects one. These are candidate embedding conventions, **not derivations of the physical polarity meanings**.

The resulting eight middle-plane ports each have two incoming identities. Order the ports cyclically around the slicing axis and the identities by ID. Route the first occurrence at each port along native rim edges to the next port, and the second through the native middle-plane edge graph to the opposite port. Shortest-path search prefers vertices closer to the centre when distances tie. The two port permutations are bijective. Attach each arrival to the reflected upper half of its destination slot, preserving the arriving wire's identity, colours and all four signs.

This yields eight rim routes and eight interior routes. No strand branches, retraces a vertex, or disappears. The geometry uses 63 distinct native edges, including 11 interior edges. Shared-edge lanes are spaced in a fixed adjacent face plane; the bundle mouths remain cut back onto their edges rather than pinched into one vertex.

## Coverage and its limits

The preceding surface-only construction covered 14 N cells and missed the central cell and four transverse tips. The middle matching now covers **all 19 geometric N carriers**, by native-edge incidence.

Coverage is also checked against the actual groups returned by `buildSulfur32Wiring()`, rather than a fresh count-based grouping. **All 16 retained N groups** have nonempty strand incidence, including all three opposite-tip pairs and the central group. The model retains each group's source members and incident wire IDs.

This establishes coverage, not a one-wire-per-N-group bijection or equivalence to the older periodic routing. A path can meet several N groups; no extra wire is created by such membership. The previous periodic model has 64 wire records and additional seam identifications. `NChannelCount` remains `null` for this candidate; `NGroupCoverage.count` is 16. The chosen middle matching is one explicit reversible candidate, not a uniqueness or physical-routing result.

## Verification

`tests/sulfur-32-incoming-bundle.test.mjs` checks all sixteen sign tuples, endpoint inventory conservation and permutation, native-edge validity, non-increasing slicing height, simple paths, reflected lower halves, absence of copied branches, full carrier/group coverage, renderer identity, and equal stripe pitch. Browser checks verify audit counts, persistence and unchanged other views.
