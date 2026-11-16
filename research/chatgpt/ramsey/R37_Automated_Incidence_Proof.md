# Automated incidence obstruction for R(3,7)

Date: 2026-11-03

## Outcome

The unchanged rooted-incidence extension rule reconstructs R(3,7)=23. It constructs a triangle-free 22-vertex graph with independence number six and rejects every 23-vertex counterexample. No special singleton/doubleton pattern, circular ordering, or purported 23-vertex symmetry is supplied.

All smaller graph classes used in the upper certificate are regenerated from the trivial (3,2) cases. Public catalogues were used as independent comparisons during development, not as completeness assumptions in the exported computation.

This is an automated reconstruction of a known result by the classical neighborhood-gluing method. Its contribution to this investigation is the successful fixed-rule test and the measured role of retained attachments. No new Ramsey value or general closed formula is claimed.

## 1. One extension law

Let H be a triangle-free graph with alpha(H)<t-1. Add a vertex v and an independent set B={b_1,...,b_d}, join v to every b_i, and make no edges from v to H. For each i choose an independent subset S_i of H and join b_i to exactly S_i.

Every triangle-free graph is obtained this way at any chosen vertex: take B=N(v), H=G-N[v], and S_i=N(b_i) intersect V(H). Independence of S_i is precisely the condition excluding triangles involving b_i and two old vertices.

The independence number of the assembled graph is exactly

    alpha(G) = max(1+alpha(H),
                   max over J subseteq {1,...,d} of
                     [ |J| + alpha(H - union_(i in J) S_i) ]).

An independent set containing v has the first form. An independent set not containing v chooses some J in B and a set in H avoiding all their neighbors. These two cases exhaust all possibilities.

Thus alpha(G)<t is equivalent to

    alpha(H - union_(i in J) S_i) + |J| <= t-1

for every J, together with alpha(H)<t-1. This is the dual presentation of the previous signature-overlap inequality; it is not a new rule selected for seven.

If v is chosen to have minimum degree d, every S_i has size from d-1 through t-2, and every old vertex must finish with degree between d and t-1. The implementation enumerates these choices, retaining actual subsets, with degree and edge-budget pruning. New B vertices are interchangeable, so ordering their attachment masks nondecreasingly removes only relabeling duplicates. Repeated masks are allowed when the constraints permit them.

## 2. Completeness from trivial starting data

For t=2, avoiding an independent pair requires a complete graph; triangle-freeness permits only zero, one, or two vertices. These are the only graph inputs.

The generator recursively uses the preceding extension law, with t reduced by one. For each possible minimum degree d it generates every possible H and every possible attachment multiset. It therefore generates every graph in the requested class up to isomorphism. Its only other size rejection follows from the elementary neighborhood recurrence: if the required smaller induced class is empty, every larger such class is empty as well.

Generated intermediate class sizes relevant to this proof are:

| Class | Nonisomorphic graphs |
|---|---:|
| (3,4), 6 vertices | 15 |
| (3,4), 7 vertices | 9 |
| (3,4), 8 vertices | 3 |
| (3,4), 9 vertices | 0 |
| (3,5), 11 vertices | 105 |
| (3,5), 12 vertices | 12 |
| (3,5), 13 vertices | 1 |

The 11-, 12-, and 13-vertex generated classes were also compared by actual graph isomorphism against McKay's corresponding public catalogues; all agree.

## 3. What degree counting alone leaves unresolved

For a triangle-free G with n vertices, m edges, degrees d_v and H_v=G-N[v],

    e(H_v) = m - sum_(u in N(v)) d_u,
    sum_v e(H_v) = n*m - sum_v d_v^2.

If f_(t-1)(q) is a proved minimum-edge lower bound for the smaller avoidance class, then

    n*m >= sum_v [ d_v^2 + f_(t-1)(n-d_v-1) ].

Integer dynamic programming derives the initial bounds from t=2. The same gluing engine, after degree counting forces degree five, independently excludes the 18-vertex (3,6) case. It does not import the earlier hand-selected incidence pattern.

Using that smaller nonexistence result, degree counting at n=23,t=7 leaves exactly these profiles:

| Red edges | Degree-five vertices | Degree-six vertices |
|---:|---:|---:|
| 66 | 6 | 17 |
| 67 | 4 | 19 |
| 68 | 2 | 21 |
| 69 | 0 | 23 |

Degree counting alone therefore does not settle 23.

## 4. Generate stronger smaller-case certificates

Run the same exact attachment search for (3,6) on 16 vertices with at most 33 edges. A minimum-degree vertex has degree at most four, so its residual has 11, 12 or 13 vertices. These classes have already been generated above. The search produces:

    5 nonisomorphic graphs with 32 edges;
    39 nonisomorphic graphs with 33 edges;
    no graphs with at most 31 edges.

Likewise, for 17 vertices with at most 40 edges, the possible minimum degrees are three or four. Their residual classes have 13 or 12 vertices. The search produces exactly two graphs, both with 40 edges, and none with fewer.

Thus f_6(16)=32 and f_6(17)=40 are computed, not supplied as lookup values. Every generated graph was separately checked for red triangles and independent six-sets by exhaustive subset tests.

## 5. Derive six-regularity at 23

Degrees must be five or six. Let x be the number of degree-five vertices. Then

    m=69-x/2,
    sum_v e(H_v)=759-x/2.

The new smaller bounds require

    sum_v e(H_v) >= 40*x + 32*(23-x) = 736+8*x.

Consequently x<=46/17; degree-sum parity leaves only x=0 or x=2.

For x=2, m=68. A degree-five vertex has at most one degree-five neighbor, so its neighbor-degree sum is at least 5+4*6=29. Its 17-vertex residual would then have at most 68-29=39 edges, contradicting the computed minimum40.

Therefore x=0: G must be six-regular, m=69. At every vertex, H=G-N[v] has 16 vertices and exactly

    e(H)=69-6*6=33

edges. The complete 39-graph family above therefore exhausts every possible residual.

## 6. The 23-vertex attachment obstruction

For each of those 39 graphs H, six new neighbors must attach to six independent five-sets S_1,...,S_6. Six-regularity requires the exact incidence load

    number of i with x in S_i = 6-deg_H(x)

at every old vertex x.

Already the pairwise overlap condition is sufficient to rule out all such attachments:

    alpha(H - (S_i union S_j)) <= 4

for every distinct new-vertex pair i,j. If this inequality fails, five old vertices outside both sets together with b_i,b_j form a white seven-clique. Repeated attachment sets are not omitted by the search; they are tested under the same rule.

Actual exhaustive search results, summed over all 39 residuals:

| Maximum number of attachments tested jointly | Search nodes | Accepted completions |
|---:|---:|---:|
| 2 | 107,479 | 0 |
| 3 | 105,143 | 0 |
| 4 | 104,681 | 0 |
| 6 | 104,672 | 0 |

The final counts depend on labeling and search order. Their mathematical content is zero completions with every branch accounted for. Higher-overlap checks reduce the search slightly but are not necessary in this case.

### Independent rejection DAGs

A second algorithm enumerates each residual's independent five-sets directly by testing all five-subsets. A pair of candidate attachment sets is compatible exactly when their union intersects every independent five-set of H.

It then solves an integer exact-cover problem with demands 6-deg_H(x), selecting a still-unmet vertex and branching over every eligible candidate set containing that vertex. A branch subtracts its incidence vector and retains only pairwise-compatible candidates. This differs from the first algorithm's ordered-neighbor enumeration and does not call its gluing routine or its independence-number table.

The exported DAGs contain 1,350 states over all 39 residuals. The verifier checks every residual demand, every available-set mask, complete branching at the selected vertex, and every child transition. Empty candidate lists justify leaves. Residual demand strictly decreases along branches. No satisfying zero-demand state is present.

These certificates prove no six-regular 23-vertex avoiding graph can be assembled, completing the upper bound.

## 7. Construct the 22-vertex lower witness

The same engine was run with five new neighbors rather than six, using the previously generated 16-vertex graphs. It produced a graph with:

    22 vertices;
    60 red edges;
    twelve degree-five and ten degree-six vertices;
    no red triangle;
    no independent seven-set;
    an independent six-set.

No 22-vertex example was supplied to this construction. It is saved as `results/constructed_r37_22.g6`. The verification tests every triple and every seven-subset, and checks all 1,024 rooted attachment-subset conditions across all 22 roots.

Its graph6 record is:

    Us`?XGRQR@B`KcW?O`??B?cWGb_q?`H_a@CO??Bw

Together with the upper certificate this gives R(3,7)=23.

## 8. Degree-only negative control

The separate saved graph `degree_only_false_positive.g6` is six-regular and triangle-free on 23 vertices, but contains the independent seven-set

    {0,3,7,9,15,17,18}.

It demonstrates concretely why six-regularity and triangle exclusion are insufficient. In its rooted construction, two proposed attachment sets leave five independent old vertices untouched. The pairwise overlap condition rejects precisely that assembly.

## 9. Scope and attribution

The mechanism now works as an exact, executable neighborhood-construction and rejection procedure on the new test. It does not infer a formula for arbitrary R(3,t), prove pairwise overlap universally sufficient, or replace finite enumeration by a compact invariant. Completeness here follows from exhaustive smaller-class generation and exhaustive attachment checking.

The neighborhood-gluing principle and degree-deficiency method are established. In particular, the pairwise union rejection used here is explicitly described by Goedgebeur and Radziszowski. The appropriate interpretation is that our retained-incidence proposal has recovered and implemented a known general construction method, rather than established a new algebraic explanation of all Ramsey numbers.

No Agda or Lean proof was run. The completeness argument is written mathematics; computational verification uses exact integer graph operations, exhaustive finite searches, and a separately implemented certificate checker.

## Sources

Jan Goedgebeur and Stanislaw P. Radziszowski, *New Computational Upper Bounds for Ramsey Numbers R(3,k)*, arXiv:1210.5826v4 (2013), equations (1)-(4), Section3 and especially the neighborhood-gluing implementation on printed page7. https://arxiv.org/abs/1210.5826

Brendan McKay, *Ramsey Graphs*, for independent catalogue comparisons. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

R(3,7)=23 is the established value; Graver and Yackel proved the upper bound in *Some Graph Theoretic Results Associated with Ramsey's Theorem*, Journal of Combinatorial Theory4 (1968), 125-175. Historical attribution is through the primary 2013 paper's references; the 1968 full proof was not reverified here.
