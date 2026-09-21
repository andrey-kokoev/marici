# Checked canonical cofiber cut pentagon

## Result

The five-assembly pentagon is now proved for the canonical homotopy-cofiber collapse model, for arbitrary small types and composable maps

`A --f--> B --g--> C --h--> D --k--> E`.

All five routes are equivalences from a common fourfold quotient to E/D. The proof compares the three-edge path with the two-edge path around the pentagon. It is an equality of path witnesses, not just equality of endpoint values or of quotient types.

Code: `agda/ClosureCutPentagon.agda`.
Regression: `agda/ClosureCutPentagonRegression.agda`.

## Common source and intermediate quotients

Let

- Z_D = ((D/A)/(B/A)) / ((C/A)/(B/A));
- Z_E = ((E/A)/(B/A)) / ((C/A)/(B/A)).

`upper` constructs the induced map Z_D -> Z_E with its attachment boundaries. The common source `FourfoldQuotient` is cofib(upper), namely Z_E/Z_D.

Three independently defined first-collapse maps land in different intermediate types:

1. `collapseFirst`: ((E/B)/(C/B)) / ((D/B)/(C/B));
2. `collapseSecond`: ((E/A)/(C/A)) / ((D/A)/(C/A));
3. `collapseThird`: ((E/A)/(B/A)) / ((D/A)/(B/A)).

Every slash denotes a homotopy cofiber of the specified induced map, not a set quotient.

## Five routes and pentagon edges

The routes assemble these first-collapse maps with the previously checked intermediate-cut routes. Their deepest attachment coordinates have the five bracketings:

- v0: (((uv)w)t);
- v1: ((u(vw))t);
- v2: (u((vw)t));
- v3: (u(v(wt)));
- v4: ((uv)(wt)).

Juxtaposition here denotes interval meet in the attachment formulas. The routes themselves are compositions of maps between the actual quotient types, not just expressions in four interval variables.

The pentagon is

`v0 --e01--> v1 --e12--> v2 --e23--> v3`

versus

`v0 --e04--> v4 --e43--> v3`.

Edges e12 and e04 are instances of the existing `CutComparison.cutComparison` theorem applied after the corresponding first collapse. The other three edges are proved by elimination on the fourfold quotient. Their clauses check all 31 nested constructor forms, including the full four-dimensional attachment and all its faces.

`longRoute` and `shortRoute` are the displayed concatenations. `pentagon` proves them equal over every point and higher constructor of the source. `functionPentagon` exports the corresponding equality of paths in the function space.

Interval meet supplies the coinciding constructor formulas, while the path unit law explicitly compares the different reflexivity concatenations. No strict concatenation law, assumed pentagon filler, hom-set truncation, or analytical positivity is installed.

## Equivalence certification

`firstNaturality` checks the naturality of the first-collapse map on all triple-quotient constructors. The library pushout-equivalence theorem then proves that its induced map is an equivalence. `firstSpanComparison` identifies the library forward map with the explicit one, retaining the unit-path correction.

Composing with the existing rejoin equivalences certifies v0. The already proved edge homotopies transfer equivalence to v1 through v4. Cancellation with the final certified routes proves `collapseSecond` and `collapseThird` are equivalences as well. Exports include `firstEquiv`, `secondEquiv`, `thirdEquiv`, and `E0` through `E4`.

Only the checked isEquiv witnesses are abstract, to avoid unnecessary expansion of large inverse proofs. The maps, attachment equations, edge homotopies, and pentagon remain transparent.

## Regression and negative control

The fixture sets A=B=C=D=Bool, E=Unit, f=g=h=Boolean negation, and k the terminal map. Thus all four attachment domains are nonempty and all three initial maps are nonidentity. The fourfold quotient is equivalent to the circle.

Checks include:

- the pentagon on the complete four-dimensional attachment;
- concrete left- and right-associated target attachment normal forms;
- the pentagon-comparison family along an entire lifted circle loop.

A temporary negative-control copy changed the deepest `collapseThird` formula from w meet t to w join t. Agda rejected it with exit 42 and an `UnequalTerms` error specifically on the clause boundary. This was not a parsing/import failure. The temporary file was removed automatically and the admitted source was not changed.

## Verification

The repetitive constructor clauses were generated as ordinary explicit Agda source, then inspected and kernel-checked; the generator is not a proof assumption.

Fresh closure check:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureCutPentagonRegression.agda`

Result: exit 0. Both new modules use `--safe --cubical --guardedness`. No holes or postulates were added. Existing source modules were not modified.

## Scope and next gates

This closes the five-route pentagon gate for these canonical space-valued cofiber collapses. It is not a theorem about the moduli space of all stable filtrations, all choices of octahedral comparison, or an analytical realization functor.

Still separate are:

- identification with the earlier opaque 3-by-3/univalence-transported implementation;
- coherence for arbitrary finite towers, beyond this pentagon;
- naturality under maps of entire filtrations, not only the target-postcomposition already checked;
- stable/rational-complex and conductor–Morse realization layers.
