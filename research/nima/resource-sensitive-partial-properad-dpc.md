# Resource-Sensitive Partial Properad DPC

## Objective

Test whether the cross-sector constructor language must be enlarged from a
typed partial multicategory to a resource-sensitive partial properad.

A multicategory operation has many inputs and one output. The live joint
instrument problem requires primitive many-output operations:

\[
(A_1,\ldots,A_m)\rightharpoonup(B_1,\ldots,B_n).
\]

Treating the output tuple as an ordinary product is unsound when formation of
that product would require copying, repeated use of a consumable source, or an
undeclared joint acquisition.

## Properadic constructor

Each admitted operation carries:

- ordered input and output signatures;
- source authority;
- a same-preparation or same-packet contract;
- a resource equation;
- a completion scope;
- declared boundary faces;
- optional symmetry and orientation data.

Composition is defined only when wired port signatures agree and the combined
resource equations remain admitted.

## Observation nerve

The nerve records separately executable faces and candidate joint fillers. A
horn is not fillable merely because every listed face exists. A filler must:

1. have the required many-input/many-output signature;
2. be source-authorized;
3. realize every declared face by projection or admitted postprocessing;
4. obey the same-preparation contract;
5. introduce no undeclared copying;
6. conserve the declared resources;
7. select orientation when the boundary admits mirror fillers;
8. remain stable under the declared completion.

Verdicts are:

- `fillable`;
- `unfillable`;
- `ambiguous_fillers`;
- `unstable_filler`.

## Exact fixtures

The compiler includes six minimal fixtures.

1. Optical pairwise overlaps exist, but no cyclic triple instrument exists.
   The triangle horn is unfillable.
2. A synthetic optical triple instrument with explicit three-copy resource
   authority fills the same horn.
3. Electric and magnetic sheet ports exist separately, but no same-packet
   joint instrument exists. The character horn is unfillable.
4. A synthetic sheet operation emitting both sheet amplitudes allows admitted
   postprocessing to electric and magnetic outputs and fills the horn.
5. Product packaging that silently duplicates a consumable preparation is
   rejected.
6. A finite filler whose lower observability bound collapses at completion is
   classified as unstable.

## DPC

The properadic enlargement is justified if the compiler simultaneously:

- accepts primitive authorized multi-output fillers;
- rejects facewise existence as proof of a filler;
- rejects product packaging that hides copying;
- distinguishes orientation ambiguity from absence;
- distinguishes finite fillability from completion stability.

The strong necessity claim is falsified if an admitted many-output constructor
can be represented in the existing multicategory as one primitive opaque
bundle output with separately authorized projections, without adding copying
or a universal product law.

## Outcome

The finite compiler passes all declared horn fixtures, but the strong claim
that Marici must replace its multicategory is false. A joint operation

\[
X\rightharpoonup(Y_1,Y_2)
\]

can be encoded as

\[
X\rightharpoonup J_{12},
\qquad
J_{12}\rightharpoonup Y_1,
\qquad
J_{12}\rightharpoonup Y_2,
\]

where (J_{12}) is an opaque source-authorized joint packet rather than an
inferred Cartesian product. This preserves the no-copy and same-preparation
distinctions.

The properad is therefore a useful explicit intermediate representation and
audit projection, not a foundational necessity. Its advantage is that the
many-output boundary, wiring, and horn obligations are visible without
inventing one bundle type per joint instrument. The existing typed partial
multicategory remains adequate if joint packet types and their projections are
primitive and authority-bearing.
