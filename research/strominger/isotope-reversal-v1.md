# Reversal around N-14: local closure, whole-assembly asymmetry

## Samples and explicit transformation

Tested the saved N-15 and O-16 native witnesses and both successful experimental
N-14 terminal-PE deletion candidates (N-15 cells 16 and 17 deleted). N-14 still
uses the experimental shortcut; it is not relabelled a native witness.

Keep geometric coordinates fixed; swap P/E reader species, preserve N, swap
M/C occurrence roles and reflect occurrence indices by i -> K-i, where K is
the largest index in that sample. Reverse graph arrows and invert their full
five-slot permutations. These choices define a concrete finite test, not all
possible spatial or mode-space dualities.

Prior context: `polarization-reversal-transport.md` establishes an involutive
norm-preserving reversal on a constructed two-mode plane using a dual/Riesz
identification and normalization. It explicitly does NOT identify reversal
with a raw occurrence permutation. This new test does not implement that
mode-space identification on isotope assemblies.

## Results

| Check | N-15 | N-14 delete 16 | N-14 delete 17 | O-16 |
|---|---:|---:|---:|---:|
| Selected records | 44 | 43 | 42 | 49 |
| Full edge maps invert exactly | yes | yes | yes | yes |
| Context-aware reversal squares to identity | yes | yes | yes | yes |
| Reversed PN/NE local face checks pass | 25/25 | 23/23 | 21/21 | 27/27 |
| Reversed graph covered from all original exits | yes | yes | yes | yes |
| Reversed graph covered from any one original exit | no | no | no | no |
| NN faces failing current reversed role-count rule | 4 | 4 | 4 | 4 |
| Old E bodies failing current P-shape rule | 7 | 7 | 7 | 8 |

Particle totals remain unchanged under P/E swapping because each sample is
neutral. This is count invariance, not yet full native assembly equivalence.

## The context slot is essential

Simply reversing the three active window positions while holding the context
slot fixed gives zero locally native frames in all samples. We then exhaustively
tested all 24 permutations of the four occurrences after role/index reversal.
Every frame has exactly one compatible permutation, uniform within each species:

With original positions `[w0,w1,w2,context]`:

```
P -> E: [w2, context, w1 ; w0]
N -> N: [context, w2, w1 ; w0]
E -> P: [context, w2, w0 ; w1]
```

Semicolon separates the new active window from its new context. P/E orders are
mutual inverses; the N order is self-inverse. Including M/C and index reflection,
two transformations restore the exact original frame. No per-frame choice of
indices or independent per-vertex phase reset was introduced.

With this context-aware transformation, every tested original PN and NE face
passes `auditPhaseCombination` as reversed NE and PN respectively, retaining
actual face coordinates and same-occurrence identification. This is a stronger
finding than mere invertibility of the coefficient permutations.

## Why whole-assembly closure still fails

1. **NN face rule:** existing NN contacts require one M vertex on the shared
   face. M/C reversal gives two M vertices. N remains N, so the unchanged
   directional NN guard rejects all four such faces in each sample. This flags
   a particular asymmetry to investigate rather than a failure of every local
   reversal.
2. **Shape convention:** all occupied E bodies in these samples are split
   tetrahedra. The native proton chart accepts regular tetrahedra only. Literal
   same-coordinate P/E body exchange therefore fails that convention. A
   geometry-transforming duality was not searched.
3. **Boundary condition:** reversing a rooted network with many E exits gives
   a multi-entry network. All former E exits together reach every reversed
   record; none individually does. Best single-exit coverage is 18 records in
   the nitrogen samples and 14 in O-16. A single-root reverse is not equivalent
   to reversing the full entry/exit boundary.

For every operation, inverse permutation applied to the target packet exactly
recovers the source packet permutation. However, inverse coefficient maps are
not automatically registered native operations: inverse reader advances,
inverse NE and the experimental PE inverse still require appropriate reversed
admission rules. Global simultaneous path/field sewing was not tested.

## Conclusion

The supplied local PN/NE templates have a precise context-aware reversal that
survives on every tested face. Current whole-isotope admission is not closed
under literal P/E and M/C exchange. The concrete remaining work is a compatible
NN reverse rule, a treatment of regular/split geometry under the duality, and
an entry/exit boundary convention—not just reversing active arrows.

Production/viewer and existing witness receipts were left unchanged.

## Reproduction

```sh
node research/strominger/checkers/probe_isotope_reversal.mjs
```

`results/isotope-reversal/verification.json` retains per-frame permutations,
per-face checks, single-exit reachability trials, shape/NN failures and hashes.
