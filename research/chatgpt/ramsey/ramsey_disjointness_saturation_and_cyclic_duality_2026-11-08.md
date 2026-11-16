# Ramsey Disjointness Saturation and Cyclic Incidence Duality

**Date:** 2026-11-08  
**Scope:** Exact graph-theoretic derivations and checked finite instances for R(3,k), k=3,...,6. No assumption about a symmetry-derived Ramsey formula.

## 1. The complete one-vertex extension operator

Encode red edges by a triangle-free graph G. The Ramsey-admissible class at parameter k is

    F_k(n) = {triangle-free G on n vertices with alpha(G) <= k-1}/isomorphism.

For an independent red neighborhood S in V(G), attach a new vertex v adjacent precisely to S. Its independent-set complex is

    Ind(G+v) = Ind(G) union (v * Ind(G-S)).

In particular,

    alpha(G+v) = max(alpha(G), 1+alpha(G-S)).

The extension is admissible exactly when S is independent and alpha(G-S) <= k-2.

## 2. Disjointness-saturation criterion

At a saturated state alpha(G)=k-1, let

    Max(G) = inclusion-maximal independent sets of G,
    M(G) = maximum independent sets of G (each has k-1 vertices),
    D_G[T,I] = 1 if T cap I is empty, else 0, T in Max(G), I in M(G).

**Theorem.** G is unextendable by one vertex at parameter k if and only if *every row* of D_G has at least one nonzero entry.

Proof. An admissible S must hit all maximum independent sets. If S exists, it is contained in an inclusion-maximal independent set T, which also hits all maximum sets, so the corresponding D row is zero. Conversely, a zero D row is an independent red neighborhood meeting every maximum set. The alpha(G)<k-1 case is always extendible via S=empty.

**Corollary (cloning).** At alpha(G)=k-1, duplicating an existing vertex v as a nonadjacent red-neighborhood twin is admissible if and only if v belongs to *no* maximum independent set of G.

Proof. N(v) is independent because G is triangle-free. The independent sets containing v have maximum size 1+alpha(G-N[v])=alpha(G-N(v)). The neighborhood N(v) hits all maximum independent sets precisely when none contains v.

Thus every terminal graph is *vertex-covered by maximum independent sets*. The converse fails: all nine admissible seven-vertex R(3,4) graphs have that coverage, but four can still be extended.

## 3. Exact update of the disjointness matrix

Suppose alpha(G)=k-1 and S is an admissible neighborhood. Write

    A = G-S, H = G+v_S.

All old maximum independent sets persist: admissibility means every I in M(G) meets S, so each remains maximum in H.

The inclusion-maximal independent sets of H split into two types:

    old rows: T in Max(G) with T cap S nonempty;
    born rows: {v} union J, J in Max(A).

The maximum independent sets of H split into:

    old columns: I in M(G);
    born columns: {v} union J, where J in M(A) and |J|=k-2.

Born columns exist exactly when alpha(A)=k-2. Thus, in these row and column orders,

    D_H = [ D_old,old     D_old,born ]
          [ D_born,old          0   ].

The lower-right block is identically zero because both born sets contain v.

Explicitly:

    D_old,old[T,I] = 1[T cap I = empty]
    D_old,born[T,J] = 1[T cap J = empty]
    D_born,old[J,I] = 1[J cap I = empty]

**Saturation criterion after attachment.** H is terminal exactly when:

1. Every old row T meeting S is disjoint from an old maximum set I or a maximum set J in G-S of size k-2.
2. Every inclusion-maximal J of G-S is disjoint from at least one old maximum set I in G.

This is necessary and sufficient. The second test cannot be repaired by born columns; born rows and born columns always share v.

**Tight-capacity theorem.** If alpha(G-S)<=k-3, then H remains extendible: attach a second vertex with the same red neighborhood S and blue edge to v. Its independence number is max(k-1,2+alpha(G-S))<=k-1. Therefore terminalization via one new vertex requires alpha(G-S)=k-2.

These statements explain two simultaneous mechanisms: new maximum-set columns can resolve formerly zero old rows, while new maximal-set rows can create fresh requirements against the inherited old maximum sets.

## 4. Exhaustive finite extinction for R(3,3) and R(3,4)

The checker generates nonisomorphic admissible graphs *from the empty graph*, using only the exact neighborhood extension. It checks its levels against NetworkX's complete graph atlas through seven vertices, then continues by the same exhaustive extension rule. Isomorphisms are explicitly tested rather than presumed from hashes.

| n | # R(3,3)-admissible graphs | # R(3,4)-admissible graphs |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 6 |
| 5 | 1 | 9 |
| 6 | 0 | 15 |
| 7 | 0 | 9 |
| 8 | 0 | 3 |
| 9 | 0 | 0 |

Consequently the exact enumeration proves R(3,3)=6 and R(3,4)=9 within the stated complete graph generator.

At k=4, the nine seven-vertex admissible graphs comprise five terminal branches and four extendible branches. The four extendible graphs offer eight labelled red-neighborhood choices in total; every resulting eight-vertex graph is terminal, and the eight outputs reduce to three graph-isomorphism classes. Each of these eight extensions creates maximum independent sets containing the newly added vertex and has alpha(G-S)=k-2. None is a simple clone of an old vertex: every vertex in each seven-vertex graph belongs to some maximum independent set.

The three eight-vertex critical graphs have maximal/maximum independent-set row/column counts of 10/10, 12/12, and 8/8. Their minimum disjointness-row degrees are 1, 3, and 3 respectively. Their corresponding graph6 forms were independently checked against the three supplied critical graph codes.

## 5. An actual self-duality of Ramsey constraints

For a well-covered graph G (every maximal independent set is maximum), define the disjointness graph T(G):

    vertices = maximum independent sets of G;
    edge I--J iff I cap J = empty.

Its adjacency matrix is exactly the disjointness matrix D_G. The terminal test is then equivalent to T(G) having no isolated vertices.

**C5.** Label the red graph on Z/5 by edges at offsets +-1. Its five maximum independent sets are cyclic translates of I0={0,2}. Translated sets I_a,I_b are disjoint exactly at offsets b-a in {1,4}. Consequently

    T(C5) ~= C5.

**Wagner graph W8.** Label its eight vertices on Z/8, with edges at offsets {1,4,7}. Its eight maximum independent sets are cyclic translates of I0={0,2,5}. Direct intersection gives

    I0 cap (I0+d)=empty iff d in {1,4,7}.

Hence

    T(W8) ~= W8.

These are exact symmetry-equivariant self-dualities: the original cyclic translation acts identically on the maximum-independent-set orbit. They do not imply that every critical Ramsey graph is fixed by T.

## 6. At R(3,5), one cyclic orbit splits into three

Take the triangle-free extremal circulant G=C13(+-1,+-5), isomorphic to the supplied unique 13-vertex critical R(3,5) graph. It has alpha(G)=4 and 39 maximum independent sets, forming exactly three translation orbits of size 13.

Representatives:

    A = {0,2,4,6}
    B = {0,2,6,9}
    C = {0,3,6,9}

Write A_i=A+i modulo 13, and similarly B_i,C_i. For a pair of representatives P,Q define

    E_PQ = {d modulo 13 : P cap (Q+d) = empty}.

The exact nine supports are:

| P\\Q | A | B | C |
|---|---|---|---|
| A | {1,3,5,8,10,12} | {1,3,5,12} | {5} |
| B | {1,8,10,12} | {1,5,8,12} | {1,5,8,11} |
| C | {8} | {2,5,8,12} | {1,2,5,8,11,12} |

The 39x39 matrix is reconstructed exactly by the 3x3 matrix over the cyclic group ring Z[C13] whose (P,Q) entry has support E_PQ: D[(P,a),(Q,b)] = 1[(b-a) mod 13 in E_PQ].

The count quotient is

        [6 4 1]
    B = [4 4 4]
        [1 4 6]

with row sums (11,12,11). Every row of the full D is nonzero; G is terminal. Multiplication by 5 on Z/13 preserves the red edge offsets and exchanges the outer two independent-set sectors A and C while fixing B.

This is an exact three-sector incidence structure, with no asserted M24 or S5 symmetry. A 3x3 *count* matrix suffices for terminality of this symmetric graph; the full cyclic-offset matrix is needed to retain all incidences.

## 7. Beyond the well-covered regime

The seven supplied critical R(3,6) graphs (17 vertices) have the following independent-set row/column counts and minimum D row degrees:

| Graph | Maximal rows | Maximum columns | Minimum row degree |
|---:|---:|---:|---:|
| 1 | 83 | 82 | 8 |
| 2 | 83 | 80 | 10 |
| 3 | 90 | 90 | 16 |
| 4 | 82 | 82 | 14 |
| 5 | 91 | 90 | 12 |
| 6 | 75 | 70 | 12 |
| 7 | 75 | 74 | 14 |

Five of seven have smaller inclusion-maximal independent sets as well as maximum independent sets. The rectangular D matrix is therefore the correct object in general; restricting attention to the graph on maximum independent sets would omit those additional rows.

## 8. Verification

Run from the directory containing the research helpers:

    python ramsey_disjointness_saturation_audit.py

Requires `networkx` and the already-produced `ramsey_two_channel_extension.py` and `ramsey_incidence_core_audit.py`.

Checks include:

- exhaustive generation and atlas cross-check through seven vertices;
- exact R(3,3) and R(3,4) extinction;
- 3,463 saturated one-vertex extensions using the four-block D update;
- terminalization requiring tight capacity, and the cloned-neighborhood theorem;
- the three eight-vertex critical structures;
- cyclic self-duality for C5 and W8;
- all 1,521 entries of the C13 three-sector block-circulant incidence matrix;
- terminality and row signatures of all seven supplied R(3,6) critical graphs.

## 9. Symmetry transport under an extension

The exact symmetry law is also available. Let Gamma=Aut(G), and let Gamma_S be its setwise stabilizer of the chosen red neighborhood S. Then

    Aut(G+v_S) fixing v  ~=  Gamma_S.

Every automorphism of G preserving S extends by fixing v; conversely, any automorphism of G+v_S fixing v preserves both the old graph and S. Therefore the block decomposition of D_H is equivariant under Gamma_S. Some old symmetry orbits may split when passing from Gamma to Gamma_S. This is the exact place to track newly distinguishable incidence sectors under growth. The full automorphism group of H may be larger when automorphisms exchange v with an old vertex.

## 10. Research consequence

The source symmetry of maximum-independent-set incidence **does** regenerate the full original red-graph adjacency for C5 and W8. At the next extremal Ramsey level it produces three cyclic sectors with an exact 3x3 group-ring incidence representation. At the following level, smaller maximal independent sets can create additional rows beyond the maximum-set symmetry representation.

This is a precise candidate for emergent higher-order incidence structure. It does not provide a formula for R(3,k), show that sector counts determine thresholds, or construct a complete symmetry-preserving quotient that remains closed under every possible extension. That last requirement is the next structural question.
