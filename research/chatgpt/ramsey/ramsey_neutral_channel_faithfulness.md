# Faithful Ramsey extension algebra and the `esd7` bridge

9 November 2026. Status: theorem for an algebraic encoding; `esd7` realization unproved.

## Exact extension theorem

Let H=(V,E) be triangle-free, with alpha(H)<k. Edges in E are red; other pairs are blue. Let I be the collection of all independent sets of cardinality k-1 in H. A new vertex x, connected by red edges exactly to S subset V, produces a (3,k)-admissible graph if and only if

1. S is independent in H, and
2. S intersects each I in I.

Proof: any new red triangle must contain x and an old red edge entirely in S. Any new blue k-clique must contain x and an old blue (k-1)-clique disjoint from S. There are no other new forbidden patterns. QED.

## Algebra (explicit and exact, not asserted to be new)

Let A_H be the N-semiring with basis symbols e_S for every independent set S of H (including the empty set). Multiplication on basis elements is

    e_S * e_T = e_(S union T)  if S union T is independent;
              = 0            otherwise.

The unit is e_empty. This is an associative, commutative semiring: equivalently, the polynomial semiring in idempotent variables z_v with z_u z_v=0 on red edges uv.

For each independent (k-1)-set I define p_I = sum_(v in I) e_{ {v} }. Put P(H,k) = product_(I in I) p_I (empty product = unit).

**Theorem:** P(H,k) != 0 if and only if H has an admissible one-vertex (3,k)-extension.

Proof: By distributivity, each product term chooses a vertex v_I in I. The term survives exactly when the union of its choices is independent. That union hits every I, so is a valid red neighborhood. Conversely an admissible S supplies a surviving term by choosing v_I in I intersect S. Coefficients are nonnegative; no cancellation occurs. QED.

For any subfamily F of I, P_F=product_(I in F)p_I=0 is a finite obstruction certificate for H: it already prevents all independent red neighborhoods. If P_F != 0, the selected factors alone are insufficient and the entire I family may still obstruct.

## Proposed four-role interpretation (candidate, not identified with source `esd7`)

- R: an old red edge; the relation z_u*z_v=0.
- B: an old independent (k-1)-set; the factor p_I.
- N1: expansion of a retained candidate S by a representative v in I.
- N2: annihilation of an expanded candidate when a red edge occurs in its support.

The two neutral channels are **operations on candidate histories**, not additional Ramsey edge colors. This preserves faithfulness. Identifying them with the two neutral vertices of the conjectured tetrahedral representation requires a further, source-defined map.

For a family I_1,...,I_t, use support-only iteration:

    C_0 = {empty}
    C_(j+1) = {S union {v} : S in C_j, v in I_(j+1),
                S union {v} is independent in H}.

Then C_t is empty exactly if the product of those t factors is zero. No graph-completion search is hidden in a single step, but a step can still read an entire (k-1)-set. Consequently **factor count is not an adversarial tetrahedral move count**.

## Exactly reproduced finite checks

Input: the first five 22-vertex (3,7) graphs in McKay's `r37_22.g6` and all seven 17-vertex (3,6) graphs in `r36_17.g6`. The supplied Python script recomputes the independent sets, constructs coverage constraints, solves a 0-1 set-cover MILP, and independently verifies each returned annihilating family by the algebraic support iteration.

For the five tested R(3,7) graphs: all optimal family sizes reported by the MILP are exactly 6; all six-factor products evaluate to zero. For the seven R(3,6) graphs: sizes in catalogue order are 5,6,6,5,6,5,5. The solver reports optimality; minimum-size claims depend on the optimizer, whereas zero-product claims are independently and exactly checked by integer bitset iteration.

For first (3,7) graph, an actual six-factor family is:

    (0,1,4,8,16,18)
    (0,2,4,8,10,20)
    (0,5,7,9,13,16)
    (2,3,5,7,11,13)
    (6,12,17,18,19,21)
    (12,14,15,17,18,21)

The number of distinct surviving independent supports after each factor is 6, 28, 89, 169, 93, 0. This demonstrates a genuine finite cancellation-by-incompatibility. It does not explain why the graph has the obstruction independently of the input adjacency matrix.

## Two no-go statements for overly strict four-role encoding

**Four-local no-go:** Suppose an admissibility test imposes only conditions on induced colored subgraphs of at most four vertices, with face-gluing requiring matching shared edge labels and no additional state or accumulated history. It cannot exactly recognize (3,7)-admissibility. Proof: all-blue K_7 is forbidden, but every induced subgraph on at most four vertices is an admissible all-blue coloring. Local checks and overlaps cannot distinguish it from globally consistent allowed local patterns. In fact, the corresponding obstruction has vertex arity seven. This does not rule out tetrahedral systems that retain enough context or compose cells into higher-arity witnesses.

**Color-swap no-go:** A symmetry that interchanges red and blue on each edge cannot preserve (3,7)-admissibility: all-blue K_3 is admissible, while its swap all-red K_3 is not. Therefore the source order-four chart rotation can only act on Ramsey roles via a typed, possibly nontrivial functor, not as a literal swap of the asymmetric edge colors.

## Actual source and missing map

Marici's `esd_7(Delta^3)` has 120 geometric vertices, 560 edges, 784 faces and 343 tetrahedra. Source tetrahedra have six edge maps, four face homotopies, and one higher coherence equation; that geometry is **not** yet assigned the above R/B/N1/N2 semantics. The attachment-channel note explicitly leaves all 784 face homotopies and 343 tetrahedral analytical coherence obligations undischarged. Chart rotation `rho` is a cyclic barycentric coordinate action, not a Ramsey edge-color symmetry.

Required bridge: an assignment Phi mapping source occurrences, faces, tetrahedra and their transport witnesses to the independent-set algebra, preserving original admissible operations and reflection/chart transport, while exactly recognizing the old red-edge annihilator and old blue (k-1)-set factor. It must neither introduce extra constraints nor erase distinct source histories. Without Phi, the algebra establishes a target semantics, not a proof that the proposed tetrahedral construction is faithful.

## Best next test

Try constructing Phi on one tetrahedral chart and its first nontrivial overlap. Determine whether one complete independent six-set factor p_I is generated by a bounded sequence of source-admitted tetrahedral operations, and whether two ways of generating it give a coherent comparison witness. If no such source-local factor generation exists, the tetrahedral Ramsey generator conjecture fails in its current form.

References:
- https://github.com/andrey-kokoev/marici/blob/main/research/strominger/esd7-coherence-layout-recovery.md
- https://github.com/andrey-kokoev/marici/blob/main/research/strominger/esd7-attachment-channel-v1.md
- https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md
- https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
