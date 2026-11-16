# Saturated-neighborhood port theorem and simplex composition

Input: red triangle-free graph `G`, `alpha(G)=k`, a vertex `v` with red degree `k`.
Let `A=N(v)` (k vertices), `B=V\N[v]`, `P_b=N(b)∩A` for b in B.
All red edges between A and B are encoded by the `P_b`. There are no red edges
inside A, between v and B, or among A's vertices.

## Theorem 1: exact port/Hall characterization

G is triangle-free with independence number k if and only if:

1. The induced red graph G[B] is triangle-free and P_b ∩ P_c = ∅ on every
   red edge bc of G[B].
2. alpha(G[B]) <= k-1.
3. For every red-independent T⊆B, |∪_{b∈T}P_b| >= |T|.

The third condition is equivalent to alpha(G[B_U]) <= |U| for each of
only 2^k port subsets U⊆A, where B_U={b∈B:P_b⊆U}.

Proof: Any independent set that contains v lies in {v}∪B and is bounded
by (2). Any independent set avoiding v has a subset T independent in B;
its maximum possible completion using A is

    F(T)=T∪(A\∪_{b∈T}P_b),
    |F(T)|=k+|T|-|∪_{b∈T}P_b|.

Thus (3) is necessary and sufficient to preclude k+1 independent vertices.
For the 2^k formulation, take U=∪_{b∈T}P_b (forward direction), and
for the reverse direction choose a maximum independent set of B_U.
Triangle-freeness is precisely (1).

## Theorem 2: simplex codimension and tight-set composition

For independent T⊆B, put f(T)=|∪_{b∈T}P_b| and d(T)=f(T)-|T| >=0.
Then F(T) is a blue simplex of dimension k-d(T)-1. Thus the number of
blue-simplex dimensions lost is exactly its Hall slack d(T).

The coverage function f is submodular, so d=f-|T| is also submodular.
If two red-independent sets T1 and T2 are tight (d(T1)=d(T2)=0) and their
union is red-independent, submodularity and nonnegativity force

    d(T1∪T2)=d(T1∩T2)=0.

This is an exact composition rule for the maximum-dimensional blue
simplices corresponding to tight independent sets. Independence of the
union is essential.

Note: the `center capacity slack` sigma_v(U)=|U|-alpha(G[B_U]) is a
different quantity from the per-simplex slack d(T).

## Theorem 3: cardinality bounds in small port directions

Let s=|U|, X=B_U. Then |X|<=s(s+1)/2.
Proof: each color fiber X_a={b∈X:a∈P_b} is red-independent, so
|X_a|<=alpha(G[X])<=s. Every singleton-label class P_b={a}
contains at most one vertex (the Hall condition). If h<=s vertices
have singleton labels, the total number of port incidences I obeys

    2|X|-s <= 2|X|-h <= I <= s^2.

For s=3 the upper bound 6 cannot be attained: equality would give
three distinct singleton-label vertices and one doubleton-label vertex
for each of the three label pairs. The Hall condition would force all
three singleton-label vertices pairwise red-adjacent, a red triangle.
Thus |B_U|<=5 for s=3.

For s=4 the upper bound 10 cannot be attained: equality gives four
singleton-label vertices plus six doubleton-label vertices, with
exactly three doubleton incidences at each port. Each pair label occurs
at most twice, and every pair label forces a red edge between its two
singleton vertices. Triangle-freeness forces the support of pair labels
to be a 4-cycle with alternating multiplicities 1 and 2. Some three
consecutive ports then support at least six B-vertices, contradicting
the s=3 bound. Thus |B_U|<=9 for s=4.

These counting bounds are necessary but not sufficient for constructing
an admissible Ramsey coloring: red-edge compatibility inside B and the
exact independence-number conditions still matter.

## Theorem 4: deletion instability and saturated radius two

Every saturated red vertex z has distance at most two from every vertex:
otherwise N(z) together with a distance-at-least-three vertex would be
an independent set of size k+1.

Hence any vertex in the simplicial link lk_Ind(G)(N(v)) is deficient,
i.e. has original degree strictly less than k.
Choose any maximal red-independent set S in G-v containing N(v).
The added vertices lie in that link; the original neighbors of v lose
one red edge. Therefore every vertex of S has red degree at most k-1
in G-v. If alpha(G-v)=k, S avoids ALL saturated vertices of G-v.

This proves that saturation-based transversals are never hereditary
under vertex deletion that preserves the independence number.

## Audit of the 191 critical R(3,7;22) graphs

The supplied standard-library verifier (`ramsey_port_incidence_certificates.py`)
reads Brendan McKay's original 191 graph6 lines in `r37_22.g6`.
It verifies triangle-freeness, alpha(G)=6, the port theorem, all
64 inequalities per saturated center, and the local cardinality bounds.

- 3,249 saturated centers across 191 graphs.
- 2,921 centers have max_U sigma_v(U) = 1.
- 328 centers have max_U sigma_v(U) = 2.
- Every one of the 191 graphs has at least one center with max_U sigma_v(U)=1.
- The greedy maximal independent set in each of 4,202 vertex-deleted
  graphs avoids all degree-six vertices; 4,122 such sets have size 6,
  and 80 have size 5. Since 21>=R(3,6)=18, each deletion preserves alpha=6.

The `max sigma=1` property is **not sufficient** to imply a saturated
transversal. The verifier includes a triangle-free ten-vertex graph
with alpha=4, center max sigma=1, and an H-free maximal independent
set {0,1,3,7}. Its red adjacency masks are

    [52,352,321,592,393,515,142,592,534,424].

This rules out a shortcut that would infer bounded repair from Hall
near-equality alone.

## Directions for further research

For an extremal (3,k+1)-graph with saturated v, B has
R(3,k+1)-k-2 vertices. The candidate next step is to place a
structural upper bound on |B| using both the red graph G[B] and the
Hall port family, rather than relying only on numeric capacities or
post-hoc small facet covers. Only such a bound could contribute to
proving a new Ramsey threshold.

## Run

    python ramsey_port_incidence_certificates.py

The standard-library script writes `ramsey_port_incidence_results.json`.
Source of the input graphs: https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

## Why port cardinality bounds do not yet determine R(3,7)

A saturated vertex of a hypothetical admissible 23-vertex (3,7) graph
would have |A|=6 and |B|=16. The cardinality inequalities above do not
rule it out. The verifier additionally checks an explicit multiset of
17 **formal** port labels on six ports, with every port fiber of size 5;
it meets the bounds |B_U|<=1,3,5,9,12 for port subsets of sizes 1..5.
It is a witness to insufficiency of those **counting-only** inequalities,
NOT a Ramsey graph or a realization of the full Hall+triangle-free tests.
A proof of the Ramsey upper bound would have to use the missing red-edge
compatibility information or stronger constraints than these counts.
