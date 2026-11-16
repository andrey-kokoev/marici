# Two-neighborhood completeness test: exact family audit and a structural reduction

## Status

The universal completeness claim is **not proved or disproved** here. No escaping graph was found. What is established is:

- A mathematical proof that every triangle-free 6-regular graph on 23 vertices with independence number at least eight has a root-plus-six certificate using the union of two internal neighborhoods.
- An exact audit of all vertex-transitive graphs in the stated class, via all 165 three-generator circulant descriptions, of which 55 are triangle-free. These fall into five distinct multiplier orbits and all are detected.
- An exact audit of a nonsymmetric, independence-seven search example: 166 of its 3,128 root-and-pair tests are positive. This is a sample, not a global minimum claim.

The unresolved case is independence number exactly seven, without vertex transitivity. The word “exactly” here also uses the previously known R(3,7)=23 to exclude independence number at most six. Our new structural reduction itself proves only that an escaping graph has independence number at most seven; it does not reprove R(3,7)=23.

No claim of novelty relative to the graph-theory literature is made.

## 1. The criterion

Let G be a triangle-free 6-regular graph with 23 vertices. For a root v, put

    A = N_G(v),
    B = V(G) \ (A union {v}),
    H = G[B].

For b,c in B, permitting b=c, set

    W = N_H(b) union N_H(c).

This induced patch is bipartite. Let nu(W) be its maximum matching size, and let r_A(W) be the maximum matching size in the attachment graph between W and A. Define

    Delta_v(b,c) = |W| - nu(W) - min(5, r_A(W)).

A positive value constructs an independent seven-set. If |W|-nu(W) >= 6, a minimum vertex cover of the bipartite patch leaves an independent six-set; add v. Otherwise the two-cover argument from the preceding investigation applies because |W|-nu(W)-r_A(W) > 0.

There are 23 * binomial(17,2) = 3,128 root-and-unordered-pair tests. The binomial coefficient includes the 16 repeated pairs b=c at each root.

The bipartite matching/vertex-cover equality is Konig's theorem. The implementation verifies a matching and a vertex cover of equal size for every maximum-matching calculation, so its maximality certificates do not rely on trusting the search algorithm alone.

## 2. A support-union condition forced by escaping the root-plus-six test

Let I be any independent set of size k >= 7, and for x outside I write

    S_x = N_G(x) intersection I.

If two vertices x,y outside I, allowing x=y, satisfy

    6 <= |S_x union S_y| <= k-1,

choose v in I \ (S_x union S_y). Then x and y are outside the closed neighborhood of v. Their internal-neighborhood union W contains at least six vertices of I, so W has independence number at least six. Consequently |W|-nu(W) >= 6 and the root-plus-six test is positive.

Thus any graph avoiding all root-plus-six certificates must satisfy, for every independent I of size at least seven,

    |S_x union S_y| <= 5, or S_x union S_y = I.                  (U)

This is a necessary condition, not asserted to be sufficient.

Now choose I to be a maximum independent set, with k=alpha(G). Since G is 6-regular, (U) with x=y gives

    1 <= |S_x| <= 5.

Nonemptiness follows from maximality of I. Counting edges from I gives

    sum_{x outside I} |S_x| = 6k.

There are 23-k outside vertices, hence

    6k <= 5(23-k),

so k <= 10.

Two further elementary facts will be used repeatedly:

1. Adjacent outside vertices have disjoint supports, by triangle-freeness. A support of size r belongs to a vertex of internal degree 6-r.
2. For any independent family Y outside I,

       |Y| <= |union_{x in Y} S_x|.                            (M)

   Otherwise replace the support union in I by Y to obtain a larger independent set. In particular, at most r vertices can have an identical r-element support. Any family with a common support label is independent.

We now eliminate k=10,9,8 using only (U), (M), triangle-freeness, and regularity.

## 3. Eliminate k=10

There are 13 outside vertices and 60 incidences into I. Some support T has size five. Its vertex has one internal neighbor. The neighbor's support is disjoint from T; (U) therefore forces it to be the complementary five-set I\T.

Any other support of size at most four would have to be contained in both complementary five-sets: its union with either is too small to be all ten labels, and any union larger than five is forbidden by (U). This is impossible for a nonempty support.

Thus all 13 supports have size five. Their total incidence is 65, contrary to the required 60.

## 4. Eliminate k=9

There are 14 outside vertices and 54 incidences.

### A five-element support occurs

Let T be such a support, and let U=I\T, of size four. The internal neighbor of a T-vertex must have support U.

There can be no distinct five-element support T'. Indeed, (U) would force T union T'=I, so the complementary four-sets U and U'=I\T' would be disjoint. Both U and U' occur as supports, by the same internal-neighbor argument. Their union has size eight, violating (U).

Every support S is now either contained in T or contains U, by applying (U) to T and S. The latter possibility is only S=U: a larger such support would be another five-set. Applying (U) to U and a subset of T excludes subset sizes two, three, and four. Hence all supports are U, T, or singletons inside T.

Each label of U has degree six and occurs only in U-supports. There are therefore exactly six copies of U. The remaining eight supports are T or singletons. If t of them are T, their incidences on the five labels of T total

    5t+(8-t)=8+4t.

But those five labels have degree six, requiring 30 incidences. The equation 8+4t=30 has no integer solution.

### No five-element support occurs

All 14 supports have size at most four and sum to 54. The deficit from 14*4=56 is two. Thus there is a four-element support and no singleton support.

Its vertex needs two internal neighbors. A disjoint support could have size at least two and at most four, making the union size six, seven, or eight, forbidden by (U). No internal neighbor is possible, a contradiction.

## 5. Eliminate k=8

There are 15 outside vertices and 48 incidences.

### 5.1 A five-element support occurs

Let T have size five and U=I\T have size three. The sole internal neighbor of a T-vertex must have support U.

There is only one five-element support type. Otherwise two distinct five-sets would have union I, and their complementary triples would be disjoint occurring supports. Their union of size six would violate (U).

Applying (U) with T and U shows that the only support types are:

- singletons and pairs inside T;
- the full five-set T;
- the triple U;
- four-sets U union {a}, for a in T.

Let X be the outside vertices whose supports contain U. Every label in U has degree six and occurs in exactly X, so |X|=6. Let L be the set of T-labels occurring in the four-element supports in X. All of X is independent, because its supports share U. By (M),

    6 <= |U union L| = 3+|L|,

so |L| >= 3.

If a pair P inside T occurred, then for every a in L its union with U union {a} could not have size six. Thus a would have to lie in P. This would give L subseteq P, impossible because |L|>=3>|P|. Therefore no pair supports occur.

There are nine remaining outside vertices, supported by singletons or the full T. Let t be the number with support T, and h the number of four-element supports in X. Counting incidences on T gives

    5t+(9-t)+h = 30,
    4t+h = 21.

By (M), t<=5. Also h>=|L|>=3 and h<=6. The only integer solution is t=4, h=5.

Thus X has five four-set vertices and only one triple-U vertex. Each of the four T-vertices must use that triple-U vertex as its internal neighbor. But a triple-supported vertex has internal degree only three. Contradiction.

### 5.2 No five-element support occurs

Let n_i be the number of supports of size i, for 1<=i<=4. Then

    n_1+n_2+n_3+n_4=15,
    n_1+2n_2+3n_3+4n_4=48,

hence

    3n_1+2n_2+n_3=12,
    n_4=3+2n_1+n_2.                                          (C)

First suppose complementary four-set supports U and V both occur. Any other four-set support must equal U or V: otherwise it would have to meet each in at least three labels, impossible. No triple support can occur, since it would have to meet each of U,V in at least two labels.

Therefore n_3=0. From (C),

    n_4=9+n_1/2 >= 9.

But (M) permits at most four copies of U and four copies of V, giving n_4<=8. Contradiction.

So no complementary pair of four-set supports occurs. A vertex with a four-element support can now have internal neighbors only among singleton-supported vertices: supports of size two or three would have disjoint union of size six or seven, and a disjoint four-set would be a prohibited complementary support.

The four-set vertices each need two internal neighbors. The singleton vertices each have internal degree five. Hence

    2n_4 <= 5n_1.

Using (C),

    6+4n_1+2n_2 <= 5n_1,
    n_1 >= 6+2n_2.

But 3n_1+2n_2+n_3=12 gives n_1<=4. Contradiction.

## 6. Structural conclusion

Every triangle-free 6-regular 23-vertex graph with alpha(G)>=8 has a positive root-plus-six test for some root and some pair of centers. In particular, it has Delta_v(b,c)>0.

Equivalently, an escaping graph must have alpha(G)<=7. The argument neither enumerates support patterns nor uses smaller Ramsey bounds.

Using the already known R(3,7)=23 identifies the unresolved completeness case as alpha(G)=7. That use is for classifying potential counterexamples to this certificate family, not a new proof of the Ramsey number.

## 7. Complete vertex-transitive audit

A transitive automorphism group on 23 vertices has order divisible by 23. By Cauchy's theorem it contains an element of order 23, necessarily a 23-cycle on these vertices. Thus every vertex-transitive graph of this order is a circulant after relabeling.

An undirected 6-regular circulant on Z/23Z is determined by three opposite difference pairs, hence by a triple chosen from {1,...,11}. There are 165 triples. Direct exact generation finds 55 triangle-free triples. Multiplication of labels by nonzero residues partitions these into five orbits of eleven triples each.

Representatives and counts of positive tests at root zero (out of 136):

| Positive steps | Positive pairs | Maximum Delta |
| --- | ---: | ---: |
| 1,3,5 | 136 | 3 |
| 1,3,7 | 119 | 2 |
| 1,3,8 | 78 | 1 |
| 1,4,6 | 83 | 2 |
| 1,4,10 | 81 | 2 |

The five root-test histograms are distinct, so the five representatives are nonisomorphic. Translation is an automorphism, so root-zero checks also describe every other root after relabeling.

The audit does not infer general completeness from these symmetric examples.

## 8. Nonsymmetric search and limitations

Heuristic degree-preserving, triangle-free edge switches did not find an escaping graph. The included sample graph is the least-positive example found in those runs, not a certified optimum.

Its exact properties are:

- 23 vertices, degree six, triangle-free, independence number seven.
- Exactly eleven independent seven-sets.
- All 3,128 root-pair tests checked.
- Delta histogram: {-2:20, -1:404, 0:2538, 1:166}.
- Every root has at least one positive test.

Some solver experiments also imposed necessary support-union constraints. They did not produce a completeness certificate or a counterexample and are not used as evidence of unsatisfiability.

A counterexample, if one exists, must therefore be non-vertex-transitive and have independence number exactly seven. Neither condition asserts that its automorphism group is trivial.

## 9. Reproduction

Run `python verify.py` using Python 3.10 or newer. Only the standard library is used.

The verifier regenerates all circulants, checks matching/cover certificates, validates explicit independent-seven witnesses, checks all sample-graph root pairs, and computes the sample independence number exactly. `PROOF.md` supplies the general structural argument; finite checks are not a formal proof of that argument or of the unresolved alpha-seven case.

## References

Gabor Szarnyas, translation of Denes Konig's 1931 “Graphs and matrices”, arXiv:2009.03780. This is the matching/vertex-cover equality used in the certificate.

Jack E. Graver and James Yackel, “Some graph theoretic results associated with Ramsey's theorem”, Journal of Combinatorial Theory 4 (1968), 125–175, DOI 10.1016/S0021-9800(68)80038-9. This is background for the previously known Ramsey value, not an input to Sections 2–6.
