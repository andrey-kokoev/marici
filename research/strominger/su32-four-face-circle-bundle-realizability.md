# Four-face circle bundles: a realizability test

## Source and question

N. E. Mnëv, *Which circle bundles can be triangulated over the boundary of a 3-simplex?*, 2018, `references/znsl6589.pdf`. Read all seven PDF pages (printed pp. 75–81). Main index now contains 5,876 pages / 74 PDFs.

Question: what extra restriction does an ordinary simplicial realization impose on the four-face circle-bundle candidates from our earlier reading?

## The theorem

**Theorem 4.3, PDF p. 6:** with the unrefined tetrahedron boundary as base, an oriented circle bundle can have an ordinary simplicial triangulation only in the trivial or Hopf cases. In signed Chern-number notation:

```
c1 in {-1,0,1}.
```

Existence is also established: the trivial case has a product triangulation, and the Hopf case has the cited Madahar–Sarkaria construction.

**Section 5, same page:** the extremal degree-two case requires semi-simplicial triangulations over that fixed base. This is the unit-circle/tangent-frame bundle associated with TS2, not the rank-two real tangent bundle itself viewed as a circle bundle.

This sharpens, rather than contradicts, the 2019 binary-cocycle paper: that paper admits semi-simplicial realizations and its sixteen assignments include Chern numbers ±2. Ordinary simplicial realization is an additional condition. Nor is a minimal binary assignment with c=0 or ±1 already an ordinary simplicial total-space triangulation; the theorem asserts existence of an appropriate realization of that bundle class.

## An explicit local computation

PDF pp. 2–4 associate a cyclic word (a colored necklace) to the elementary bundle over each triangle. Its letters are the three base vertices; the beads record fiber intervals inside maximal simplices. Restricting to an edge deletes the omitted vertex's color.

Count all three-position subwords with one occurrence of each color. Let N_even and N_odd count their permutation parities. Then

```
P(w) = (N_even-N_odd)/(N_even+N_odd),
pC1(w) = -P(w)/2.
```

The signed sum of these local rational values over the four oriented faces is the integer Chern number. This rational cocycle is not numerically identical to the binary face cocycle used in the minimal semi-simplicial presentation; their normalizations/representatives must not be conflated.

## Why the strict inequality matters

**Lemma 4.1, PDF p. 5:** for an ordinary simplicial elementary bundle,

```
|pC1(w)| < 1/2.
```

Equality would require every proper subword to have the same parity. The necklace then consists of three solid color blocks, up to reversal/permutation. Delete one color to restrict to an edge. The remaining two blocks have two distinct boundary edges with exactly the same endpoint vertices. That is not an ordinary simplicial complex.

Four strict bounds give `|c1|<2`; integrality leaves only 0 and ±1. The argument requires a genuine bundle and its compatible local triangulations. Four arbitrarily chosen necklaces do not acquire an integer characteristic class merely by summing their parities.

## Consequence for Su-32

The four layer-4 record triples already give the required abstract base shape. What is not yet supplied is a circle-fiber realization above it.

The next realizability test is therefore concrete:

1. Recover cyclic fiber words, if the native retained paths supply them.
2. Check that restrictions agree by color deletion, retaining edge and simplex occurrence identities.
3. Determine whether the resulting total object is an ordinary simplicial complex or only semi-simplicial.
4. Compute the rational parity cocycle and its oriented integral sum.

Do not turn distinct edges with identical endpoints into one edge merely to obtain a simplicial model. That would erase exactly the obstruction used by the proof. Our reference-support complex is ordinary simplicial by construction, but that says nothing by itself about the as-yet-unconstructed **total space** above it.

If an ordinary simplicial bundle over this fixed four-face base is constructed and its Chern number is nonzero, the theorem identifies its bundle class as Hopf up to orientation. If repeated-edge incidences require a semi-simplicial total space, degree two remains available. Neither conclusion selects the class without the fiber data.

## Disposition

This source adds a concrete total-space realizability filter to the earlier sixteen-case classifier. The cellular BF construction and the FKMM classification remain separate: this theorem concerns oriented circle bundles over a fixed four-face base, not Quaternionic vector bundles with an anti-linear lift.

No native necklaces or bundle realization were constructed in this reading pass. Reindex execution: `structured_command_execution:e_29164_1793126832492497900_70`. No scientific checker or prior result was changed.
