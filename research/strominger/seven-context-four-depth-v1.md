# Native test of 28 × 2 × 2 as seven contexts × four retained depths

## The seven has a source binding

The native active endpoint faces are

```
P: [C0, M0, C1]
E: [M1, C1, C2].
```

They meet at exactly C1. Their nonempty faces containing C1 are:

- the vertex C1;
- four edges: C0–C1, M0–C1, C1–M1, C1–C2;
- the two endpoint triangles.

That is **1 + 4 + 2 = 7** actual incident contexts. Each triangle is checked against its native tetrahedral body. This concerns the active triangles: the complete P and E tetrahedra share an edge, as in the previous pair test.

The two-triangle complex has 13 nonempty faces in total. Its seven-face incident star is not itself a face-closed simplicial complex.

## The four is a retained-depth construction

Starting from the prepared native P/E pair, execute four in-place flow reversals, each followed by positive confirmation. Keep depths 1,2,3,4 as distinct occurrences. Orientation alternates −,+,−,+; history lengths are 2,4,6,8.

At each depth, evaluate all seven endpoint contexts against the same retained comparison bank:

```
[ aa  ab ]   aa = P self-comparison
[ ba  bb ]   bb = E self-comparison
             ab, ba = opposite readings of the same native N interface.
```

This supplies **7 × 4 = 28 indexed positions**, each carrying a **2 × 2 bank**. The 112 indexed bank entries are not 112 independent values or particles. Seven positions at a given depth reference one retained bank. The fixture still has three physical bodies and five independent complex coefficients.

The ordering of the seven contexts is a declared presentation order. Four is the requested retained-depth cutoff; native incidence has not independently forced that cutoff.

## Two different 4-simplex interpretations

### Reference simplex

The two triangles use five reference names, C0, M0, C1, M1, C2, so they sit inside an **abstract** 4-simplex on those names. The actual coordinates all have coordinate sum one and lie in an affine three-dimensional hyperplane. They do not form a nondegenerate physical 4-simplex.

The native N active triangle is the mixed face [M0, C1, M1]. It is not one of the two endpoint triangles. Adding this face increases the number of C1-incident contexts from seven to **eight**. The seven-count therefore treats N as the comparison witness, not a third endpoint-face context.

### Depth simplex

Four composable confirmed reversals have five occurrence vertices, 0 through 4. They define a strict 4-simplex diagram in the nerve of the transport operations:

- ten typed edges;
- ten triangular composition comparisons;
- five tetrahedral faces;
- eight ordered factorizations from occurrence 0 to occurrence 4.

Every route is checked on the complete native state and the retained action history, not only the final parity. All factorizations agree. This is a strict diagram built from the declared reversal operation, not an independently derived nontrivial higher braid filler.

The five depth occurrences are **not identified** with the five reference vertices. Equal cardinalities do not supply that identification.

## Actual transport checks

Each endpoint context carries its native local face reading. Restriction along the eight covering incidences commutes, including both triangle-to-vertex diamonds. Restriction also commutes with confirmed flow reversal. The off-diagonal N readings exchange orientation, while their coefficients and the diagonal self-comparisons remain intact.

Full five-coefficient recovery is tested on every basis vector. An incompatible P/E endpoint fails positive confirmation; an inconsistent common C1 value fails local face agreement.

There is also a retained-information control: change the two hidden input coefficients. All 28 local face readings remain the same while the full neutron changes. Four reversals do not make those hidden coefficients observable. The retained bank remains essential.

## What is established

The factorization is now more than numerical:

```
7 native endpoint-face contexts
× 4 confirmed reversal occurrences
× 2×2 compatible comparison entries.
```

It is a coherent indexing and transport construction on the native P/E/N fixture. It is not yet a mechanism generating new particles or the surface layers. It has not been identified with the earlier LRRR/Sigma clock, the seven matching rounds, or the proposed fourteen-forward/fourteen-return word evolution.

## Reproduce

```
node research/strominger/checkers/check_seven_context_four_depth.mjs
```

**12 check groups pass.**

- Model: `seven-context-four-depth-model.mjs`
- Full trace: `results/seven-context-four-depth-v1.json`
- Pair interpretation: [single-pe-pair-v1.md](single-pe-pair-v1.md)

The existing viewer and native rules are unchanged.
