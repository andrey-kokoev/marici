# Difference-constraint blocks have controlled certified interfaces

## Structural target and restriction

Take the owning atom-cap source box, but declare selected RAW ATOMS as the public observer, not the full (U,V) moment pair. Retain difference constraints x_v-x_u<=w, with an anchor x_0=0 (source atom j is node j+1). Caps are edges from and to the anchor.

This is a deliberately restricted evidence language. General moment rows or arbitrary two-variable linear coefficients are not difference constraints. Bounded interaction width alone is not the theorem proved here; closure within the difference-constraint class is the decisive additional structure.

## Exact interface theorem

Let D(a,b) be the shortest-path bound on x_b-x_a for a consistent finite difference system. Source caps make every distance finite. A retained interface A includes the zero anchor. Its exact projected presentation is

    y_b-y_a<=D(a,b), for all a,b in A.

Every original assignment satisfies these path inequalities. Conversely any admitted interface assignment with y_0=0 extends by

    x_v=min_(a in A) (y_a+D(a,v)).

The interface inequalities and D(a,a)=0 make this formula equal to y at interface nodes. For each edge u->v of weight w, D(a,v)<=D(a,u)+w, so x_v<=x_u+w. It therefore extends to every original constraint, including all owning source caps.

Thus a b-node interface needs at most b(b-1) rows, regardless of how many hidden nodes were removed. Negative cycles diagnose inconsistent systems; the executable controls here are consistent, and no negative-cycle packet branch is implemented.

## Block composition

Replace a block by its exact distance bounds on the nodes through which it connects to other blocks, retaining the zero anchor. Every exterior feasible assignment extends into that block by the formula above. Blocks whose interiors are disjoint can therefore be replaced independently and composed through their interfaces. Closing the composed summary and projecting again gives the same public relation as eliminating all hidden nodes at once.

This is ordinary shortest-path/difference-bound elimination with explicit certificate and filling semantics, not a new shortest-path theorem. It supplies the requested positive structural instance where block interfaces control summary row growth. For a chain with endpoint interface plus anchor, at most six rows remain.

## Owning chain controls

The evidence imposes 1/2<=t_(j+1)-t_j<=1 along the source chain, in addition to the original atom caps. Retain only the first and last raw atoms publicly. For m=4,8,16,32, exact closure leaves six interface rows. The producer also computes closure with hidden nodes eliminated in reversed order and checks equality with the first ordering. This tests elimination order; an independent modular runtime is not implemented.

Independent verification checks each proposed distance has an original-edge path of that length, all triangle inequalities hold, every original edge dominates its proposed distance, and diagonal distances are zero. Path certificates give one inequality and triangle closure the reverse, proving exact shortest distances without importing the producer's closure algorithm. Twelve source lifts and 1484 distance/path checks pass.

## Cost and meaning

Input source-plus-evidence rows grow from 14 to 126; summaries stay at six rows. Encoded row payloads shrink from 158/338/738/1554 bytes to 71/71/78/78 bytes. This comparison excludes metadata and does not compare against the shortest program encoding the regular chain. Source-generator rows are counted in the input table; the figures are not all attributable to run-specific information savings.

The full closure proof grows from 328 to 48499 bytes in these controls. It retains all-pairs distances and paths, and the witness extension needs distances to hidden nodes. Keeping that archive is much more expensive than keeping only the six public rows. A checked live summary can support public-only continuations; arbitrary fine-audit re-exposure requires the retained fine relation or equivalent information.

The practical gain is controlled live interface complexity, not total archive compression or disappearance of hidden information. The migration algorithm uses dense all-pairs closure; it does not exploit chain structure for runtime efficiency.

## Boundary

This answers one part of the block-retirement question: a relation language closed under min-plus path composition admits controlled projected interfaces and explicit source-compatible extensions. It does not show that small interfaces control arbitrary polyhedral projection complexity. Grothendieck's quadratic evidence example remains relevant outside this closed class.

## Reproduction

    python research/voevodsky/checkers/check_chain_audit_elimination.py
    python research/voevodsky/checkers/verify_chain_audit_elimination.py

Artifacts:

- `results/chain-audit-elimination.json`
- `results/chain-audit-elimination-verification.json`

The original cap formula is checked directly. No fresh upstream analytical-admission proof, noise model or authenticated observation is claimed.
