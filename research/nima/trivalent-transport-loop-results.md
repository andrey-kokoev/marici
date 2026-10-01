# The twenty retained transport loops

## Status and reproduction

Analysis of the 20 ordered-terminal discrepancies from the
[retained gluing experiment](trivalent-retained-gluing-results.md), separate
from the successful [disjoint four-vertex interchange test](trivalent-four-vertex-interchange-results.md).

```text
python research/nima/checkers/check_trivalent_transport_loops.py
```

Evidence: `results/trivalent-transport-loops.json`, containing all route words,
primitive replays, closing boundary permutations, based programs, inverse
programs, symmetry classes and pair-composition tests. The source-report hash
chain is checked before reusing graph or placement IDs. All assertions pass.

## 1. Constructing a retained loop

For each discrepancy, let D be the direct ordered terminal and S the staged
ordered terminal. The stored data give a comparison path

    D → original glued diagram → staged glued diagram → S,

where the first segment reverses the direct normalization. Append the explicit
boundary swap carrying S to D. This closes a loop on the diagram record.

The decorated state includes port labels carried through that path. It does
**not** return to its original labelled state after one circuit: the return
permutation is nonidentity. Calling this a loop must not erase that decoration.

For composition tests, transport each diagram loop to the chosen representative
of its terminal pair, retaining the conjugating symmetry. Only loops at the
same boundary/base are composed.

## 2. Classification and replay results

| Quantity | Result |
|---|---:|
| Original gluing discrepancies | 20 |
| Input-side cases, boundary (2,1) | 8 |
| Output-side cases, boundary (1,2) | 12 |
| Open comparison-path orbits under boundary action and path inversion | 2 |
| Primitive steps in each open comparison path | 3 |
| Compatible ordered loop-pair replays | 208 |
| Triple permutation-associativity checks | 2,240 |

All three-step paths replay exactly. None shortens by adjacent primitive
inverse cancellation. The two path orbits are **exactly the two earlier residual
fork path orbits**, checked against their saved derivations. The 20 gluings
therefore do not introduce a new comparison-path family in this classification.

This orbit calculation uses simultaneous boundary permutations and inversion
of the comparison path, not global reversal, cyclic path rotation, interchange
relations or arbitrary higher coherence. It is not a classification of all
possible loops in the calculus.

## 3. What returns after a circuit?

Every input-side loop returns the external input transposition:

    inputs: (1,0),    outputs: (0).

Every output-side loop returns the output transposition:

    inputs: (0),      outputs: (1,0).

All 208 compatible pairs replay as closed diagram paths with identity boundary
return. The count is 8²+12²; loops of different boundary types are not composed.
Each loop followed by its explicitly inverted program also returns both the
diagram and its boundary labels exactly. The 2,240 triple checks establish
associativity of the recorded permutation composition, not a new higher-cell
identity between arbitrary paths.

Thus each family's boundary-transport image is the two-element group generated
by a transposition. This does **not** identify the full group of comparison
loops with that group. In particular:

- squaring a loop restores its boundary labels;
- it does not supply a contraction of the retained comparison path;
- no relation equating that squared path with an identity path has been added.

The three primitive steps plus the closing symmetry remain explicit evidence.
An order-two permutation is only the finite boundary readout of that evidence.

## 4. A concrete interpretation: a symmetric composite in a noncommutative model

Use 2×2 integer matrices, with multiplication as merge and its matrix transpose
as split in the matrix-unit basis. The checker verifies the experimental
associativity/coassociativity/Frobenius equations before interpreting the loops.

For the saved input-side terminal, its represented operation is exactly

    H(x,y) = trace(x*y) I.

This formula is checked on the full basis matrix of the bilinear map. Swapping
x and y leaves H unchanged. The output-side terminal is also invariant under
its corresponding output swap; that equality is checked directly.

This is a symmetry of the **derived composite**, not primitive multiplication:
E00*E01=E01 whereas E01*E00=0. The boundary swap can therefore be invisible in
this composite's linear readout while remaining present in the retained path
and port transport.

The formula describes this particular Frobenius model. It does not identify
the abstract calculus with matrix algebras, define a trace in every model, or
show that every loop with trivial linear readout is contractible.

## 5. Interpretation

The direct/staged discrepancies have a small, reproducible transport signature:
one input-swap family and one output-swap family, each represented by an already
derived three-step path. This supports retaining boundary transport rather than
forcing distinct routes into a strict ordered normal form.

It also sharpens the coherence question. Endpoint agreement, invariant linear
readouts, and order-two boundary return are three weaker facts than an explicit
higher identification of comparison paths. None should be substituted for that
higher datum.

These results do not derive seven grades or select a new independent primitive.
They describe two families in the conditional reversible Frobenius extension,
not consequences of the original trivalent vertex alone.

## 6. Next executable work

The [four-vertex overlap test](trivalent-four-vertex-overlap-results.md) now
saturates 91 one-vertex extensions to 414 diagrams. Of 257 forks, 40 remain
unjoined after old macros; all have nonconvex support unions. Boundary transport
accounts for 32, but eight remain unjoined even modulo boundary symmetry and
the old macros. Their terminal attachment signatures differ. Next test
four-vertex derived shortcuts with explicit route provenance.

If testing contraction of a doubled loop, first declare which path relations
are permitted—for example which interchange or pentagon faces are actually
included. Without that higher presentation, a request to decide contractibility
is underspecified; matching endpoints or permutations is not a substitute.
