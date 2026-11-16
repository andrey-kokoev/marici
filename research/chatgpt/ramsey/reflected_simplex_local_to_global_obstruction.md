# Reflected simplex trees: the first intrinsic local-to-global obstructions

**Date:** 2026-11-09  
**Status:** Exact finite simplicial enumeration plus elementary proofs. No source-generated green completion, no new Ramsey theorem, no new Cubical Agda compilation. The Marici repository was not modified.

## Question

For a simplicial tree of faces `R` and its point reflection `B = -R`, do pairwise admissibility and local shared-face coherence force a globally admissible simplicial completion `G`? What is the smallest obstruction that is not visible to pairwise incidence checks?

We must distinguish three targets: (i) a simplicial complex; (ii) a triangulated 2-manifold, possibly with boundary; (iii) a coherent higher-decorated simplicial object. These have different completion theorems. The bare union of abstract simplicial complexes is already a simplicial complex, and does not require any green faces; hence no nonempty G follows from incidence alone.

All operations in the tests below are **positive**, meaning existing vertices/edges/faces are retained, and only new simplices may be added. Replacing or deleting existing faces, changing identifications, or allowing controlled singularities defines different completion tasks.

## Test A: genuine branching 2-simplex trees

Let `R` have faces

```
(0,1,2), (0,1,3), (0,2,4), (1,2,5).
```

The first face is central and each remaining face attaches along a distinct boundary edge. Its dual graph is `K_(1,3)`. Every vertex link in R is a path; the boundary is a six-edge cycle. R is a triangulated disk.

Use the vertex involution

```
ρ(0)=1, ρ(1)=0,
ρ(2)=6, ρ(3)=7, ρ(4)=8, ρ(5)=9,
ρ²=id.
```

Define `B=ρ(R)`. This is a second triangulated disk with the same branching dual graph. An explicit point-reflection realization in R³ uses

```
0=(1,0,0), 1=(-1,0,0),
2=(0,1,0), 3=(0,0,1),
4=(2,2,0), 5=(-2,2,0),
ρ(k)=-k geometrically, with ρ(0)=1 and ρ(1)=0.
```

The two disks meet along the geometric edge `[0,1]`. Each has **two** triangular faces incident to that edge, but their union has **four**:

```
R: (0,1,2), (0,1,3)
B: (0,1,6), (0,1,7).
```

Any two of these four triangles form an admissible two-triangle disk, but the complete set violates the manifold condition that an interior edge have exactly two incident triangles (a boundary edge has one).

**Proposition A.** No positive 2-manifold completion of `R ∪ B` exists: attaching additional triangles cannot lower the incidence multiplicity of `[0,1]` from four to two. This remains true with arbitrarily many new vertices. No green-only additive rule can repair it.

This is a genuine counterexample for the original **two reflected branching trees of 2-simplices**, under the additional request that their union become a 2-manifold retaining every red and blue face. It is not a failure to form an abstract simplicial complex: the singular union already is one.

## Test B: first obstruction beyond all edge-incidence checks

Take a tetrahedron with vertices `{o,a,b,c}` and its reflection with vertices `{o,-a,-b,-c}`, where `o` is the reflection center. Let R and B be their **boundary 2-spheres**:

```
R: (o,a,b), (o,a,c), (o,b,c), (a,b,c)
B: (o,-a,-b), (o,-a,-c), (o,-b,-c), (-a,-b,-c).
```

These are reflected boundaries of two **single 3-simplices**. They are not trees in the *2-face-dual* sense: the four faces of each tetrahedral boundary have a cyclic dual graph. This distinction is essential.

Their union `K` has

```
V=7, E=12, F=8, χ=3.
```

Every edge is contained in exactly two triangles. The complex is connected, and all vertex links other than `o` are circles. But

```
Lk_K(o) = C₃ ⊔ C₃ ≅ S¹ ⊔ S¹.
```

Thus K is the wedge `S² ∨ S²`, not a surface. Its integral homology is `H₀=Z`, `H₁=0`, `H₂=Z²`. The obstruction at `o` is

```
\tilde H₀(Lk_K(o);Z) ≅ Z.
```

Under the point reflection, the two components of this link are exchanged, so the obstruction transforms with sign `-1`.

**Proposition B (no additive repair).** A new triangle containing `o` and any existing neighbor of `o` would add a third triangle to an edge already of multiplicity two. New triangles containing `o` but none of its original neighbors can only create additional link components. Triangles not containing `o` leave its link unchanged. Hence no positive, closed 2-manifold completion of K is possible, even when adding arbitrarily many vertices. With the original seven vertices, direct enumeration of all 27 missing triangle candidates finds zero candidates consistent with edge multiplicity at most two.

**Sharpness.** In a pure 2-dimensional simplicial complex where each edge is in exactly two triangles, every vertex link is a finite 2-regular *simple* graph, i.e. a disjoint union of cycles, each with at least three vertices. A disconnected link requires at least six distinct neighbors and therefore at least **seven vertices overall**. K attains that bound. Thus seven is the minimum number of vertices for this kind of vertex-link failure under exact two-face-per-edge incidence.

The construction is a **weak 2-pseudomanifold** (edge-regular, but not necessarily facet-connected). Some definitions of pseudomanifold also require facet-adjacency connectivity; the wedge does not satisfy that stronger condition. We avoid relying on the ambiguous terminology.

## Test C: genuinely higher coherence requires additional decoration

There is a separate smallest higher-boundary incompatibility for `Z/2`-valued 2-cochains on a tetrahedron. Prescribe a bit `w_ijk` on each of its four triangular faces. A flat 2-cochain is required to satisfy the cocycle relation

```
w_123 + w_023 + w_013 + w_012 = 0 (mod 2).
```

Every choice of **three** face labels admits exactly one choice of the fourth that satisfies this condition. Yet a fully prescribed odd assignment, e.g. `(1,0,0,0)`, admits none. Enumerating all 16 assignments gives eight flat and eight obstructed boundaries.

This is a genuine four-face local-to-global obstruction, but **flatness is additional semantic structure**. The geometric tetrahedron still exists; only the required flat decoration fails. We must not misstate this as failure of ordinary simplicial triangulation. It is related to the established higher-filler controls already recorded in `research/chatgpt/marici_codim_one_pair_research_note.md`.

## General conclusion

The question “does a perfectly triangulated space exist?” is too weak if all abstract simplicial complexes count: the R/B union is itself such a space, and green incidences need not appear. If we require a *2-manifold*, the obstruction is entirely local once links are examined: codimension-one ridge multiplicities and vertex links decide the answer. There is no further global manifoldness obstruction in dimension 2 after all these local conditions pass. Global topology (sphere versus torus, fundamental group, prescribed monodromy, etc.) is a different and stronger target.

The hierarchy of intrinsic obstructions is:

1. Overfilled ridge: `deg_K(e)>2`; no additive repair. Present in an explicit reflected `K_(1,3)` pair.
2. Broken vertex link: edge multiplicities all equal two, but `\tilde H_0(Lk(v))≠0`; no additive repair in the seven-vertex reflected shell example.
3. Decorated higher coherence: complete boundary labels violate a cocycle or horn-filler condition even though proper subsets extend. This requires specified coefficients and a declared filler semantics.

For Ramsey research, a valuable next theorem must first provide a **faithful, non-fitted map** from color-avoiding configurations into a particular simplicial or decorated incidence class, proving that a Ramsey violation corresponds to one of these computable obstruction types. No such map is established here. Without it, these are general triangulation results, not an explanation of `R(3,7)=23`.

## Reproducibility

Run:

```
python check_reflected_link_obstructions.py
```

The stdlib-only checker verifies both reflected constructions, dual-tree shapes, all local edge counts, all vertex links, the mod-2 boundary ranks, Euler characteristics, sharpness input, the impossibility of adding any triangle on the existing seven vertices, and all tetrahedral 2-cochain assignments. The integral wedge-of-spheres homology and the minimality proof are mathematical arguments independent of the finite field computation.
