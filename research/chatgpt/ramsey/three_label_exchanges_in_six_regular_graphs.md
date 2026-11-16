# Root changes and three-label exchanges in six-regular graphs

## What is established

For a triangle-free, six-regular graph on 23 vertices, the existence of an independent seven-set is equivalent to the existence of a neighborhood replacement belonging to a list of sixteen incidence shapes. The list has one zero-label shape, one one-label shape, three two-label shapes, and eleven three-label shapes.

The localization argument and the shape classification below are mathematical proofs. They do not use R(3,7), a graph catalog, a linear-programming solver, or support-pattern enumeration.

They localize an improvement if an independent seven-set exists. They do not, by themselves, prove that a seven-set must exist. The earlier exact 1,961-support exclusion supplies that existence statement for the regular case. Combining it with localization makes the sixteen shapes an unavoidable family, but retains the earlier enumeration in the existence step. No assertion of a new enumeration-free Ramsey proof is made.

The augmenting-graph formulation and strict Hall characterization of minimal augmenting graphs are established mathematics. The contribution here is their degree-counting specialization, the freedom to change the root, and the explicit small shape classification. No claim of novelty relative to the literature is made.

## 1. Neighborhood replacements

Let G be triangle-free and d-regular. For a root v, write A=N(v), an independent d-set, and B=V(G)\(A union {v}). For independent Y contained in B, let U=N(Y) intersect A.

If |Y|>|U|, then

    (A\U) union Y

is independent and larger than A. Call |U| the number of replaced labels. The supports T_y=N(y) intersect A are the entire attachment neighborhoods, not selected subsets of them.

The root v is not among the new vertices in any replacement using fewer than d labels: its support relative to A is all of A.

## 2. Localization by degree counting

Theorem. Suppose a triangle-free d-regular graph G on n vertices contains an independent set I of size d+1. Some root admits an independent-set replacement using at most

    d - ceil(d(d+1)/(n-d-1))

labels.

Proof. The d+1 independent vertices send exactly d(d+1) edges to the n-d-1 outside vertices. Hence some outside vertex w has

    t = |N(w) intersect I| >= ceil(d(d+1)/(n-d-1)).

Use the independent neighborhood A=N(w) as the new base and put Y=I\A. The t retained vertices of I belong to A. Since I is independent, every attachment of Y into A lies outside those t vertices. Thus

    |Y|=d+1-t,
    |N_A(Y)| <= d-t.

So Y is an improving replacement using at most d-t labels. If it is not inclusion-minimal, take an inclusion-minimal deficient subset. This cannot increase its support size. QED.

For d=6 and n=23, the average is 42/16>2. Thus t>=3 and at most three labels are replaced. The same conclusion holds for every n<=27 for which the hypotheses are possible.

This theorem concerns an actual independent seven-set and actual graph edges. It makes no claim about a fractional fixed-root LP solution.

A useful quantitative form at n=23 is that every independent seven-set has at least three outside vertices with at least three neighbors in it: if q vertices have at least three incidences, then

    42 <= 2(16-q)+6q = 32+4q,

so q>=3. Those are candidate roots, not necessarily distinct exchange shapes.

## 3. Minimality and strict Hall expansion

Choose an inclusion-minimal independent Y with |Y|>|N_A(Y)| and put U=N_A(Y), r=|U|.

For each y in Y, minimality gives

    |Y|-1 <= |N_A(Y\{y})| <= r < |Y|.

Therefore |Y|=r+1 and removing any one new vertex still covers every label of U.

There is a stronger equivalent condition:

    |N_Y(X)| >= |X|+1 for every nonempty X contained in U.

To prove necessity, suppose |N_Y(X)|<=|X|. Then Y\N_Y(X) has at least r+1-|X| vertices and all its supports lie in U\X, which has r-|X| labels. It is a smaller deficient subset, a contradiction.

For sufficiency, suppose a proper Z contained in Y is deficient. Put X=U\N_A(Z). This X is nonempty and N_Y(X) is contained in Y\Z. The deficit gives |N_Y(X)|<=|X|, contradicting strict expansion.

Every label therefore has degree at least two into Y. The incidence graph between U and Y is connected: a disconnected graph with total excess one would have a deficient proper component.

These are the usual irreducible augmenting-graph conditions. See Dabrowski, de Werra, Lozin and Zamaraev, arXiv:1410.8774, Section 3.

## 4. Changing the root removes nine apparent three-label types

Choose a replacement using the smallest possible number of labels across all roots; then choose its added set inclusion-minimal. Localization shows r<=3 if any independent seven-set exists.

If r=3, Y has four vertices. A removed label a cannot be adjacent to all four members of Y. Otherwise the resulting independent seven-set

    I=(A\U) union Y

has four neighbors of a. Re-rooting at a retains those four vertices of I inside N(a) and replaces at most the other two labels. That contradicts global minimality of r=3.

Consequently, in a globally smallest three-label replacement, each of its three labels has degree either two or three into its four new vertices.

A different root does not have to preserve the previous support coordinates. Requiring it to do so would reintroduce the fixed-root restriction we are removing.

## 5. Classification of the sixteen shapes

A shape is specified by the supports of its distinct, mutually nonadjacent new vertices. Repeated supports denote different vertices. Letters a,b,c name removed labels. The remaining neighborhood vertices must be anticomplete to all new vertices because these are exact supports.

Zero labels: one new vertex with empty support.

One label:

    a, a

Two labels:

    a, b, ab
    a, ab, ab
    ab, ab, ab

Three labels:

    a, b, c, abc
    a, b, ac, bc
    a, b, ac, abc
    a, b, abc, abc
    a, ab, ac, bc
    a, ab, bc, bc
    a, ab, bc, abc
    a, bc, bc, abc
    a, bc, abc, abc
    ab, ab, ac, bc
    ab, ac, bc, abc

The list is up to relabeling the removed labels and reordering the new vertices. It is a sufficient complete family for a globally minimal rooted replacement, not a claim that all sixteen types are realized as globally minimal replacements in six-regular 23-vertex graphs. Irredundancy in that graph class is not established.

### A classification proof without graph enumeration

For three labels, transpose the incidence description: each of the three labels is adjacent to a two- or three-element subset of the four new vertices. Strict Hall expansion says that each pair of these subsets has union of size at least three and that their total union has size four.

Classify by q, the number of labels adjacent to three new vertices.

For q=0, the three distinct two-subsets are the edges of a tree on four vertices. There are two possibilities, a path and a star.

For q=1, fix the three-subset. The two two-subsets must cover the fourth vertex. Either both contain it, or exactly one does. In the latter case its other endpoint lies in, or outside, the remaining two-subset. These give three possibilities.

For q=2, equal three-subsets force the two-subset to include the uncovered vertex, giving one possibility. Distinct three-subsets have a two-vertex intersection; the two-subset can be that intersection, the two exclusive vertices, or one intersection vertex and one exclusive vertex. These give three more possibilities.

For q=3, the three-subsets cannot all be equal. Their multiplicity pattern is either two equal and one different, or three distinct. There are two possibilities.

Thus there are 2+3+4+2=11 three-label types. With one and two labels, the strict Hall condition immediately gives the lists above.

An independent brute-force check in verify_neighborhood_exchanges.py starts with all support multisets, rather than assuming this classification. It finds 20 fixed-root minimal three-label types. Nine have a label of degree four and re-root to a smaller replacement. The remaining eleven agree with the classification.

## 6. Exact equivalence and the remaining existence step

For any triangle-free six-regular graph on 23 vertices:

    alpha(G)>=7

is equivalent to containing one of the sixteen rooted replacement configurations.

The forward direction is localization, global minimality, and classification. The reverse direction is the displayed replacement operation. Neither direction assumes the value of R(3,7).

This is not yet the enumeration-free statement that such a configuration must occur. A graph with alpha(G)<=6 has none of them by definition, and the new argument alone does not rule that graph out.

The previously stored symbolic checker was rerun. It reconstructed all 1,961 support patterns and excluded 1,322 directly, 638 by sound cardinality propagation, and the final pattern by the red-square/two-triple motif. It is included, under the descriptive name verify_six_label_support_exclusions.py, so the finite existence step is explicit rather than hidden.

For the already six-regular case, the preliminary support-size reduction uses the smaller values R(3,4)=9 and R(3,5)=14 and the elementary 26-edge consequence on 13 vertices. The more difficult e(3,6,17)>=40 input is needed in the earlier argument forcing an arbitrary hypothetical 23-vertex Ramsey graph to be six-regular, not in the localization theorem above.

A brief account of the support reduction: at root v, the 16 nonneighbors have supports of size one through three and total incidence 30, so their multiplicities are (t+2,14-2t,t), t=0,...,4. Singleton supports are distinct, repeated pairs have the usual independent-set exclusions, and triples occur at most twice. These are the cases regenerated by the stored symbolic checker. That checker still enumerates them.

## 7. What the saved examples actually test

The new verifier finds independent seven-sets by searching only local replacements with at most three labels; it does not first enumerate independent seven-sets.

All 55 triangle-free six-regular circulant descriptions on 23 vertices have a zero-label replacement. In other words, a neighborhood can already be enlarged by a vertex having no neighbors in it. Their success under the earlier two-neighborhood matching test was not evidence that a difficult composed matching obstruction was necessary.

The saved nonsymmetric graph previously having 166 positive two-neighborhood tests has a one-label replacement. Its root 1 has neighborhood

    {4,6,7,11,15,21}.

Both vertices 13 and 17 have support {6} relative to that neighborhood, and they are nonadjacent. Replace 6 by 13 and 17 to obtain

    {4,7,11,13,15,17,21}.

Every asserted edge and nonedge is checked from the saved graph. The archive also contains a 22-vertex six-regular triangle-free graph with independence number six. Exact branching checks that it has no independent seven-set, and the local detector correctly returns no replacement.

The tests do not establish that three labels are needed, that all sixteen shapes occur, or that a graph-independent one-label rule is impossible. A supplementary heuristic search for a 23-vertex graph with no zero- or one-label replacements did not produce such a graph; no impossibility inference is drawn from that search, and it is not part of the proof.

## 8. Reproduction

Run these two commands from the extracted directory:

    python verify_neighborhood_exchanges.py
    python verify_six_label_support_exclusions.py

The first regenerates the minimal shape classification, tests all 55 triangle-free circulant descriptions, checks the saved positive graph and the 22-vertex negative control, and writes exchange_verification_results.json. The second reruns the prior complete finite support exclusion. Both use Python's standard library only.

The file exchange_test_graphs.json contains explicit edge lists. No graph catalog, solver, network access, or external data file is needed.

## References

Konrad K. Dabrowski, Dominique de Werra, Vadim V. Lozin, and Viktor Zamaraev, Combinatorics and algorithms for augmenting graphs, arXiv:1410.8774, Sections 2-3. This is the source for the augmenting-graph terminology and standard minimality characterization.

Jack E. Graver and James Yackel, Some graph theoretic results associated with Ramsey's theorem, Journal of Combinatorial Theory 4 (1968), 125-175, DOI 10.1016/S0021-9800(68)80038-9. This is background for the established Ramsey values and earlier reductions, not an input to the root-localization or shape-classification proof.
