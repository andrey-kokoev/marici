# Local-to-global Ramsey obstructions from matching and residual support

## Scope

These are proved general obstruction criteria, together with an explicit counterexample to the sufficiency of the *rooted neighborhood* conditions used in the preceding investigation. They do not constitute a new enumeration-free proof of R(3,7) = 23. No claim of novelty relative to the graph-theory literature is made: the matching theorem below follows from classical matching/vertex-cover duality.

The counterexample satisfies the stated incidence equations, internal degrees, triangle-freeness, root-level pair-multiplicity condition, and every A-star and B-neighborhood Hall test relative to the fixed root. It does **not** satisfy the full global independence requirement, nor alpha(H) <= 5, nor Hall tests at every possible change of root. Thus it does not contradict the earlier exhaustive support proof or the exact Hall reformulation. It demonstrates why rooted neighborhood feasibility by itself is insufficient.

## 1. General two-matching obstruction

Let G be a finite simple graph and A an independent set of size s. Let W be disjoint from A, and suppose the induced graph G[W] is bipartite. Write

- nu_R(W) for the maximum size of a matching in G[W];
- r_A(W) for the maximum size of a matching in the bipartite graph between W and A, using the edges of G.

Then

    alpha(G) >= s + max(0, |W| - nu_R(W) - r_A(W)).

Consequently, alpha(G) <= s requires

    nu_R(W) + r_A(W) >= |W|

for every such W. No regularity or triangle-freeness is required for this theorem.

### Proof by two covers

By Konig's theorem, G[W] has a vertex cover C_R of size nu_R(W). The attachment graph between W and A has a vertex cover C_B union C_A, with C_B contained in W, C_A contained in A, and

    |C_B| + |C_A| = r_A(W).

The set

    I = (W \ (C_R union C_B)) union (A \ C_A)

is independent. Its W part is independent because C_R covers every internal edge. Its A part is independent by assumption. There are no attachment edges between the parts because C_B union C_A covers those edges.

Therefore

    |I| >= |W| - |C_R| - |C_B| + s - |C_A|
         = s + |W| - nu_R(W) - r_A(W).

Also alpha(G) >= s. This proves the theorem and gives a constructive certificate.

Both matching sizes and the displayed independent set can be computed without enumerating all independent sets. The verifier implements augmenting paths and alternating-path vertex covers using only exact integer/set operations.

## 2. Composition of two independent local pieces

For b outside A, define its support T_b = N_G(b) intersect A. Let Y and Z be two independent sets outside A, and put

    W = Y union Z,
    U_Y = union_{b in Y} T_b,
    U_Z = union_{b in Z} T_b.

The induced graph on W is bipartite: Y intersect Z is isolated within W, and the remaining edges run between Y \ Z and Z \ Y. Hence the theorem applies.

Since r_A(W) <= |U_Y union U_Z|, alpha(G) <= s implies

    nu_R(W) >= |Y union Z| - |U_Y union U_Z|.

Let sigma_Y = |U_Y| - |Y| and sigma_Z = |U_Z| - |Z|. Then

    nu_R(W) >= |U_Y intersect U_Z| - |Y intersect Z| - sigma_Y - sigma_Z.

In particular, if each local piece uses exactly as many support labels as it has vertices, the required number of disjoint red edges between their exclusive parts is at least

    |U_Y intersect U_Z| - |Y intersect Z|.

Thus individual Hall feasibility does not settle composition: overlap of attachment labels can require an internal matching between distinct local choices. We do not impose an extra rule that arbitrarily chosen Hall matchings must agree. The inequality follows only from the independent-set restriction.

### Regular rooted specialization

In the previous rooted setup, take A = N(v), |A| = d, H = G[B], and d_H(b) = d - |T_b|. For b,c in B, let

    Y = N_H(b), Z = N_H(c), h = |Y intersect Z|.

Triangle-freeness makes Y,Z independent and ensures their supports avoid T_b,T_c respectively. Consequently

    nu_R(Y union Z) >= d - |T_b union T_c| - h

is necessary if alpha(G) <= d. If the actual attachment rank on Y union Z is smaller than the number of available labels, the general rank version is stronger.

## 3. Residual-support theorem

Let G be triangle-free and A an independent s-set, and assume alpha(G) <= s. Let P be an independent set outside A, and let U be any subset of A containing every support of a vertex in P. Write

    r = |U|, p = |P|, q = r-p.

Let W be disjoint from A union P, with all supports contained in U, and assume there are no edges between P and W. Then

    alpha(G[W]) <= q.

Indeed, for every independent Z contained in W,

    P union Z union (A \ U)

is independent. Its cardinality is p + |Z| + s-r, proving the assertion.

If q < 0, P already gives a contradiction. If q >= 0, the Ramsey consequence is

    |W| < R(3,q+1).

This uses a smaller independence budget than the original problem whenever p > 0 and U is no larger than A. It does not assume a new Ramsey bound.

### Pure-incidence version

The conclusion can be forced before choosing any internal edges. Suppose:

1. The supports of the vertices in P pairwise intersect.
2. Every support in W lies inside U and intersects every support in P.

Triangle-freeness forces P to be independent and forces the absence of all P--W edges. Thus if |W| >= R(3,r-p+1), no triangle-free realization with alpha(G) <= s exists.

### One unit of residual independence

For p = r-1, W must have independence number at most one, so it must be a clique. Triangle-freeness then forces |W| <= 2.

Therefore, an independent (r-1)-set supported on r labels cannot coexist with three vertices confined to those labels and anticomplete to it.

A useful incidence-only forbidden pattern is: r-1 vertices all having the same r-element support U, together with singleton-supported vertices for three distinct labels in U (r >= 3). The identical supports force the first group to be independent and anticomplete to the three singletons. Avoiding an independent (s+1)-set would force all three singleton pairs red, creating a red triangle.

For r = 3, this forbids two copies of a triple support together with all three corresponding singleton supports, regardless of all other vertices and edges.

## 4. Exact rooted counterexample

The graph has root v, labels a_0,...,a_5, and attachment vertices b_0,...,b_15. Join v to every a_i, join b_j to a_i exactly when i is in T_j, and add the 33 internal edges listed in rooted_hall_counterexample.json.

The supports, in index order, are:

    b0: 0       b1: 1       b2: 2       b3: 3
    b4: 04      b5: 05      b6: 13      b7: 15
    b8: 23      b9: 24      b10: 34     b11: 35
    b12: 45     b13: 45     b14: 012    b15: 012

Exact checks establish:

- 23 vertices; every degree is 6; no red triangles.
- Support counts (a1,a2,a3) = (4,10,2), and each label occurs five times.
- Sum of pair multiplicities is 16 = 14+a3.
- Zero-multiplicity pairs are 03,14,25, a matching.
- The five supports incident to each label admit distinct representatives.
- For every b, the supports of its internal neighbors match perfectly onto A \ T_b and cover exactly that complement.

The graph is not Ramsey-admissible: alpha(G) = 8 and alpha(H) = 6. These last two numbers are computed exactly by a branching verifier; the argument only needs the explicitly displayed independent seven-set below.

### Two local neighborhoods that cannot compose

Take

    Y = N_H(b14) = {b3,b10,b11},
    Z = N_H(b15) = {b11,b12,b13}.

Each is independent and matches perfectly into labels {3,4,5}. For instance:

    Y: b3 -> 3, b10 -> 4, b11 -> 5;
    Z: b11 -> 3, b12 -> 4, b13 -> 5.

Their union W has five vertices. The only internal red edge is b3 b13, hence nu_R(W) = 1. Its attachment rank is 3. Thus

    |W| - nu_R(W) - r_A(W) = 5 - 1 - 3 = 1,

and the theorem gives alpha(G) >= 7. Explicitly,

    {a0,a1,a2,b3,b10,b11,b12}

is independent.

There is also a support-only obstruction independent of the chosen internal edges: P={b14,b15} has the common three-label support 012, while b0,b1,b2 are all confined to it and anticomplete to P. The one-unit residual theorem forces b0,b1,b2 to be a red triangle if an independent seven-set is forbidden. Therefore this entire support system is impossible under the full Ramsey requirements, even though its rooted neighborhood tests are feasible.

## 5. Relation to exterior algebra

A generic support matrix, with a separate indeterminate in each allowed incidence, has rank r_A(W): a nonzero minor is equivalent to a support matching. A generic bipartite red-edge matrix likewise has rank nu_R(W). Thus the compatibility inequality is a sum-of-two-generic-ranks obstruction.

Neither rank is a simplicial boundary operator, and no exterior derivative or Stokes identity is used in the proof. Exterior products encode the attachment rank, but the internal red matching supplies additional information about coexistence of local pieces.

## 6. Verification and limitations

Run:

    python verify_local_global.py

The script checks the explicit graph and all 22 rooted Hall tests, constructs the two-matching witness, computes the claimed independence numbers, and checks the general matching bound on all 4096 graphs with a two-vertex independent base and a fixed 2+2 bipartite patch, allowing every attachment pattern. The small tests are a check on the implementation, not the proof of the theorem.

What is proved: the two-matching inequality, its overlap form, the residual-support theorem, and the incidence-only forbidden-pattern corollary. The counterexample establishes separation from the previous rooted neighborhood conditions.

What is not proved: that every hypothetical 23-vertex Ramsey graph necessarily contains a patch violating one of these criteria. The preceding finite support enumeration is not eliminated by this result. Nor is any claimed minimum locality universal: the criteria concern independent-set replacement, not an imposed commutativity rule for choices of matchings.

## References

P. Hall, On Representatives of Subsets, Journal of the London Mathematical Society, s1-10 (1935), 26-30. DOI: 10.1112/jlms/s1-10.37.26.

D. Konig, Graphs and matrices (1931); English translation by Gabor Szarnyas, arXiv:2009.03780 (2020). This is the matching/vertex-cover theorem used twice in Section 1.

S. Brandt, Triangle-free graphs whose independence number equals the degree, Discrete Mathematics 310 (2010), 662-669. DOI: 10.1016/j.disc.2009.05.021. This provides context for the regular alpha=d class, not a proof of the criteria derived here.
