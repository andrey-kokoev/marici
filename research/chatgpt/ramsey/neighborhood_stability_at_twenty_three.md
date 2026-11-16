# Neighborhood stability at twenty-three vertices

## Result and scope

Let G be a finite simple triangle-free, six-regular graph. Fix one vertex r and write A=N(r), B=V(G)\(A union {r}). For b in B, its exact support is T_b=N(b) intersect A.

A neighborhood improvement replaces U contained in A by an independent set Y contained in B, where N_A(Y)=U and |Y|>|U|. Its rank is |U|. Say the selected root is three-stable if no improvement has rank at most three, including rank zero.

**Theorem. If even one root of G is three-stable, then |V(G)|<=23.**

The bound is sharp for a single selected root. An explicit triangle-free six-regular graph on 23 vertices is constructed below. The smallest improvement at its distinguished root has rank four, whereas another root has a rank-one improvement. The graph's independence number is seven.

The theorem and the construction do not prove that a graph with every root three-stable has at most 22 vertices. That simultaneous-stability assertion remains the missing step in the present enumeration-free argument. No claim of novelty relative to the literature is made. The proof below uses no Ramsey value, catalog of Ramsey graphs, linear-programming infeasibility result, or enumeration of six-label support systems.

## 1. The incidence budget

Number the six vertices of A by six labels. Triangle-freeness makes A independent. Each label belongs to exactly five supports, since it has one neighbor r and degree six. Hence

    sum_{b in B} |T_b| = 30.

Let a_j count supports of size j. Zero-stability means that all supports are nonempty. One-stability means that singleton supports are distinct: two vertices with support {i} are nonadjacent through their common neighbor a_i and would replace that one label. Therefore

    sum_{j=1}^6 a_j = n-7,
    sum_{j=1}^6 j*a_j = 30,
    a_1 <= 6.

Subtracting the second equation from twice the first gives

    a_1 = 2n-44 + sum_{j>=3}(j-2)*a_j.                 (1)

Thus n<=25. If n=25, the only possibility is

    (a_1,a_2,a_3,a_4,a_5,a_6)=(6,12,0,0,0,0).

If n=24, equation (1) gives exactly four possibilities:

    (4,13,0,0,0,0),
    (5,11,1,0,0,0),
    (6, 9,2,0,0,0),
    (6,10,0,1,0,0).

These are arithmetic cases, not an enumeration of attachment-support configurations.

## 2. Pair supports consume edges among singleton vertices

Let X be the set of labels with singleton supports, and let s_i be the unique outside vertex supported on {i}, for i in X. Let Z=A\X.

Three consequences of two-stability will be used.

* A pair support meeting X occurs at most once. Two copies of {i,j}, together with s_i when i belongs to X, would be three mutually nonadjacent vertices supported on two labels.
* If i,j both belong to X and {i,j} occurs as a support, then s_i s_j must be an edge. Otherwise s_i,s_j and the pair-supported vertex would be an independent three-set supported on two labels.
* A pair support disjoint from X can occur at most twice: three copies alone would form such an independent three-set.

Consequently, pair supports entirely in X form a simple triangle-free graph on X, realized by forced edges among the s_i. In particular there are at most floor(|X|^2/4) such supports.

For completeness, the edge bound follows directly. In any triangle-free graph on m vertices, the degree sum of the endpoints of an edge is at most m. Summing over edges gives sum_v d(v)^2 <= m*e. Cauchy-Schwarz gives sum_v d(v)^2 >=4e^2/m. Thus e<=m^2/4.

The equality graphs used here are K_{2,2} on four vertices, K_{2,3} on five vertices, and K_{3,3} on six vertices. For the even orders these follow from equality in the displayed inequalities. For five vertices with six edges, a nonbipartite triangle-free graph would have a five-cycle; every additional edge would make a triangle. Thus the graph is bipartite and six edges force K_{2,3}.

## 3. Excluding order 25

All six labels have singleton supports, and there are twelve pair supports. They are all distinct and force twelve edges among the six singleton vertices. The triangle-free maximum is nine. This contradiction uses only two-stability.

## 4. Excluding order 24

### Four singleton supports

All other supports are pairs. Write p_XX,p_XZ,p_ZZ for their numbers, with |X|=4 and |Z|=2. Counting incidences on the two label parts gives

    2*p_XX + p_XZ = 16,
    p_XZ + 2*p_ZZ = 10.

Hence p_XX-p_ZZ=3. The triangle-free bound gives p_XX<=4, and uniqueness of pairs meeting X gives p_XZ<=8. Together they force

    p_XX=4, p_XZ=8, p_ZZ=1.

Thus all eight X-Z pair supports occur. Let Z={z,w}, and let p_zw denote the vertex with support {z,w}.

For every i in X, consider the four outside vertices

    s_i, p_iz, p_iw, p_zw.

Their supports lie on {i,z,w}. Every pair among them has overlapping supports except s_i,p_zw. Overlapping supports prohibit adjacency by triangle-freeness. Three-stability therefore forces s_i p_zw to be an edge.

So p_zw is adjacent to all four singleton vertices. But the four pair supports within X already force edges among those singleton vertices. Any such edge, together with p_zw, makes a triangle. Contradiction.

### Five singleton supports

There are eleven pair supports and one triple T. Let z be the single label outside X, and let epsilon be one if z belongs to T and zero otherwise.

The number of pair supports joining z to X is 5-epsilon. Thus the number entirely in X is

    11-(5-epsilon)=6+epsilon.

The triangle-free maximum on five singleton vertices is six. Therefore epsilon=0, and those six forced edges form K_{2,3}. All five pairs between z and X occur.

For i in X, the number of forced neighbors within X equals

    4 - 1_{i in T} - 1 = 3 - 1_{i in T}.

The triple T is therefore exactly the three-vertex part of K_{2,3}. Its singleton vertices are mutually nonadjacent, and the T-supported vertex is nonadjacent to each of them. This is an independent four-set supported on T, a rank-three improvement. Contradiction.

### Six singleton supports

If there is one four-element support, there are ten pair supports. These force ten edges among six singleton vertices, contradicting the maximum nine.

The remaining case has nine pair supports and two triples. The nine pairs force K_{3,3} on the singleton vertices, and every cross-part pair occurs.

Take either triple T. If its labels lie in one part, its three singleton vertices together with the T-supported vertex form an independent four-set on three labels.

Otherwise T has one label k in one part and two labels i,j in the other. The supports

    {k}, {k,i}, {k,j}, {k,i,j}

all occur. They all contain k, so their four vertices are mutually nonadjacent. Again they form an independent four-set on three labels.

This eliminates the last order-24 case and proves the theorem.

## 5. Equality at one root: an explicit 23-vertex graph

Use vertices r,a_0,...,a_5,b_0,...,b_15. Join r to every a_i. Give the b-vertices the following exact supports in A:

    b0: 0       b1: 1       b2: 2       b3: 3
    b4: 02      b5: 03      b6: 04      b7: 12
    b8: 13      b9: 14      b10: 25     b11: 35
    b12: 45     b13: 45     b14: 014    b15: 235

Here, for example, 014 means {a_0,a_1,a_4}. Add the following edges within B; each line lists the higher-index neighbors of b_i:

    0:  2,3,7,9,12
    1:  2,3,5,6,12
    2:  8,11,13
    3:  4,10,13
    4:  9,11,12
    5:  9,10,13
    6:  7,8,15
    7:  11,13
    8:  10,12
    9:  15
    10: 14
    11: 14
    14: 15

There are no other edges. These data define the entire graph; no catalog lookup is needed. Every label occurs in five supports, and b_j has internal degree 6-|T_j|. The graph is six-regular, has 69 edges, and is triangle-free. The attached verifier checks each assertion exactly.

### Why the distinguished root has no exchange on at most three labels

For J contained in A, write B_J={b:T_b is contained in J}. Three-stability is equivalent to

    alpha(G[B_J]) <= |J| for every |J|<=3.

The singleton supports are distinct. For two labels, the only blocks with three vertices are 02,03,12,13; each contains the corresponding edge between singleton vertices. All other two-label blocks have at most two vertices.

For three labels, six blocks have five vertices. Each has two vertex-disjoint edges, shown below. An independent set must omit at least one endpoint of each edge, so has at most three vertices.

| Labels J | Two disjoint edges, using b-indices |
|---|---|
| 012 | (0,7), (1,2) |
| 013 | (0,3), (1,5) |
| 014 | (0,9), (1,6) |
| 023 | (0,2), (3,4) |
| 123 | (1,3), (2,8) |
| 235 | (2,11), (3,10) |

The blocks 015 and 234 have only two vertices. Each of the other twelve blocks has four vertices and at least one edge. In eight of them the edge is one of b0b2,b0b3,b1b2,b1b3. In the four blocks 045,145,245,345 the edges b0b12,b1b12,b2b13,b3b13 respectively suffice. Thus every three-label block has independence number at most three.

This is a direct small certificate of three-stability; it does not depend on trusting the search procedure that found the graph.

### The same improvement has ranks four and one at different roots

Let

    P={b6,b9,b12,b13,b14}.

These vertices share attachment label 4, so they are independent. Their support union is {0,1,4,5}. At root r, replace those four labels by P. The resulting independent seven-set is

    {a2,a3,b6,b9,b12,b13,b14}.                         (2)

The preceding certificate excludes all smaller exchanges at r, so its minimum exchange rank is exactly four.

But

    N(a4)={r,b6,b9,b12,b13,b14}.

Both a2 and a3 have exactly the one neighbor r in this neighborhood. They are nonadjacent. Replacing r by a2,a3 yields the same set (2), now as a rank-one improvement.

An exhaustive exact check gives independence number seven and the following distribution of minimum exchange ranks across the 23 roots:

    rank 1:  8 roots
    rank 2: 10 roots
    rank 3:  4 roots
    rank 4:  1 root

These are properties of this one explicitly given graph, not universal lower bounds or classifications.

## 6. The cross-root condition the example violates

At any root r, define a graph M_r on A=N(r) by joining a,b exactly when

    N(a) intersect N(b) = {r}.

Equivalently, the pair of labels a,b never co-occurs in an outside support.

If M_r has edges ab and ac, then b,c are nonadjacent because they both lie in N(r). At root a, each has the exact singleton support {r}. Hence replacing r by b,c improves N(a).

Conversely, assume every root is zero-stable. Then every vertex added in a rank-one improvement has the same nonempty singleton support. Any rank-one neighborhood improvement at a root a therefore produces such a two-edge star in M_r, where r is the removed neighbor. Within the class of graphs whose roots are all zero-stable, we obtain

    every root is one-stable
    iff M_r is a matching for every root r.

Without zero-stability, only the forward necessity of the matching condition is asserted.

In the explicit graph, the absent co-occurrences at r are

    05,15,24,34.

They form two two-edge stars. The star centered at 4 gives the rank-one improvement at a4 described above; the star centered at 5 gives the corresponding improvement at a5.

The distinguished root therefore realizes the order-23 incidence budget and all its own three-label stability constraints, but its coordinates expose one-label instability at other roots. This is why a sharp single-root bound stops at 23.

The current proof does not establish that every possible order-23 configuration must violate this cross-root matching condition, or must otherwise have an exchange of at most three labels at some root. That unavoidability step is still open in this investigation. The prior finite support proof is not being claimed to have disappeared.

## 7. Reproduction and provenance

Run

    python verify_neighborhood_stability.py

using Python 3.10 or newer. Only the standard library is required. The script checks the degree-profile arithmetic, verifies the small triangle-free edge extrema as an independent implementation check, constructs the explicit graph, checks triangle-freeness and regularity, exhausts the independent subsets at every root, and verifies the independence number. It writes neighborhood_stability_checks.json.

The mathematical proof of the order bound is Sections 1-4. The finite checks are not a substitute for that proof. The equality graph was found by an integer feasibility search on one previously stored support pattern; all claims about the resulting graph are independently checkable from the explicit edges. The graph is not a counterexample to R(3,7)=23, since it contains independent seven-sets.

The augmenting-graph framework is established mathematics; see K. K. Dabrowski, D. de Werra, V. V. Lozin and V. Zamaraev, *Combinatorics and algorithms for augmenting graphs*, arXiv:1410.8774. The related class of triangle-free regular graphs with independence number equal to their degree is studied in S. Brandt, *Triangle-free graphs whose independence number equals the degree*, Discrete Mathematics 310 (2010), 662-669, DOI 10.1016/j.disc.2009.05.021. These references provide context; neither paper is invoked as an unproved input to the order-bound derivation here.
