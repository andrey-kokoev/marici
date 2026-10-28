# Su-32 clue: Towards Simplicial Chern-Simons Theory I

Source: Pavel Mnëv, `references/Towards_simplicial_CS.pdf`, 20 PDF pages. This is a different author/work from Nikolai Mnëv's circle-bundle triangulation paper. Read PDF pp. 1–2, 10–13, 17–20. Canonical extraction: `references/extractions/pdf-search-all/towards-simplicial-cs/`. Full reindex after adding this source: 5,692 pages, 70 PDFs.

## What this adds

The circle-bundle paper gives a discrete topological classifier. This paper gives a method for deriving **operations and their higher coherence** on a discretization. It is directly relevant to the gap between our lossless layer-4 record join and a native interaction/comparison law.

### Transfer is more than restriction

PDF pp. 1–2 begin with a differential graded algebra of fields and the BF-type expression `v(q)=dq+q²`, with fields paired against antifields. The BV master equation constrains the algebraic operations.

A subcomplex V' is embedded in V, with an acyclic complement V''. Gauge fixing uses a chain homotopy K satisfying

```
dK + Kd = P_UV = id - i I.
```

Here i is the embedding and I the projection/integration map. Integrating out the complement yields an effective action satisfying the master equation. Its tree part generates an L-infinity structure; its one-loop part supplies quantum operations. These are derived from the ambient algebra and contraction, not chosen independently at each local reader.

PDF pp. 10–12 give the triangle realization: cochains on vertices, edges and face are embedded as Whitney forms, I integrates over the corresponding simplices, and K is the Dupont homotopy. Whitney interpolation respects the differential but does not generally close under multiplication; higher transferred operations retain the missing algebraic information.

### A genuine two-route comparison

PDF pp. 17–19 compare:

1. transfer from continuous forms directly to one triangle;
2. transfer to three triangles meeting at an interior vertex, then integrate out the internal degrees of freedom.

The paper supplies explicit subdivision embeddings and K on p. 18, with `dK+Kd=P_UV` and `K²=0`. This is not merely equality of final record unions: both routes produce effective operations to compare.

At the calculated order (through cubic classical and quadratic one-loop terms), the tree parts agree. The loop parts differ by a BV-exact renormalization, with a fixed point for the coefficient studied. The extension to the full triangle action is a conjecture checked at this order, not an all-orders result. For segments, exact gluing is established (p. 10).

The subdivision's fourth vertex is **inside the triangle**. Its three faces plus outer boundary must not be mistaken for the four-face tetrahedron boundary used in the separate binary-Chern test.

## Proposed Su-32 test

Start with one globally specified carrier complex and its restrictions, rather than constructing wiring by extending local readers.

1. Identify the graded field/cochain assignment, differential and algebraic product or bracket that the native source actually supports.
2. Supply one embedding/projection/homotopy package. Check its contraction identities and compatibility with the relevant face restrictions.
3. Derive the transferred comparison operations. Compare direct and staged transfer at the actual layer-4/central-N operands.
4. Retain a higher homotopy or BV equivalence where appropriate, rather than treating equality of decoded records as equality of operations or erasing the two histories.

The present set-valued join has no graded differential, bracket or contraction package. Consequently this paper supplies a construction strategy and a more informative coherence test, not an already instantiated Su-32 interaction. In particular, its K is a homotopy for a chain contraction, not automatically a U(1) phase connection.

## Combined priority

Keep the two source contributions separate and complementary:

- **Nikolai Mnëv:** source cyclic orders -> circle bundle -> Chern class on the comparison base.
- **Pavel Mnëv:** source differential/algebra + contraction -> higher comparison operations -> direct/staged transfer coherence.

This means a phase-sensitive scalar law is not the only next object worth looking for: native higher operations could provide the missing comparison data. A link from those operations to the circle-bundle classifier would still need construction.

No Su-32 adapter, transferred operation or new numerical test was implemented in this reading pass.
