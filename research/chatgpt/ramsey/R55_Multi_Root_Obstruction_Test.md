# R(5,5): a finite overlapping-incidence obstruction test

## Outcome

The computation produces an exact separation between a declared linear relaxation of Ramsey incidence data and a necessary quadratic consistency condition. It does **not** exclude all 45-vertex avoiding graphs, construct a 43-vertex avoiding graph, or improve the published interval 43 <= R(5,5) <= 46.

Two exact rational records are supplied. Both satisfy the same normalized induced-subgraph, deletion, complement, signature-capacity, bounded-moment, degree-moment, and neighborhood-edge conditions. The first assigns a negative value to an expression that must be a mean square in any actual graph. The second passes the added square inequality. Thus the additional inequality is genuinely stronger than the listed linear conditions, but does not make their feasible region empty.

These are **fractional incidence records**, not adjacency matrices or graphs. The certified comparison is within the 22-regular diagnostic subclass at order 45. No theorem asserting that every 45-vertex Ramsey graph would be regular is used or claimed.

## 1. A specific obstruction with an elementary interpretation

For a vertex v of any red/white complete graph, write B_v for its red neighbors and H_v for its white neighbors. Let a_v and b_v count, respectively, red and white edges crossing between B_v and H_v. Define

    z_v = a_v - b_v = 2 a_v - d_v (n - 1 - d_v).

Every actual graph satisfies

    Q(G) = (1/n) sum_v z_v^2 >= 0.                          (1)

The useful operation is to expand the square before averaging. Each z_v is a signed sum over pairs {x,y} where exactly one of x,y is red-adjacent to v. The sign is +1 for a red xy edge and -1 for a white xy edge. Products of two such terms have an external-vertex union of size 2, 3, or 4. Therefore Q(G) is a linear combination of induced-subgraph densities on 3, 4, and 5 vertices.

Explicitly, let p_F be the induced density of an unlabeled graph F. For q in {2,3,4}, let h_q(F) be the sum, over every root in F and every ordered pair of qualifying external pairs whose union consists of all q remaining vertices, of the product of the two signs. Then

    Q(G) = sum_(q=2..4) [ C(n-1,q)/(q+1) ]
                         sum_(|F|=q+1) h_q(F) p_F.       (2)

This follows by counting (root, external union) in two orders. The standalone checker rebuilds h_q directly from adjacency masks; it does not reuse the moment-building implementation or a floating-point matrix factorization.

A hypothetical set of local frequencies can satisfy many averaging and extension constraints but make (2) negative. Such a record has no realization by any graph or probability mixture of graphs of the specified order.

## 2. The declared linear relaxation

The variables are induced densities p_F for every graph through seven vertices containing neither a red nor a white five-clique. The graph atlas gives 1,123 permitted types, distributed by order 0 through 7 as

    1, 1, 2, 4, 11, 32, 144, 928.

The following constraints are imposed.

### Normalization and restriction

At every order the densities sum to one and are nonnegative. If w(H,F) counts vertex deletions from F yielding H, then

    sum_(|F|=k+1) w(H,F) p_F = (k+1) p_H.

Complement densities are equated. For a symmetric Ramsey problem this loses no necessary feasibility: average any graph's densities with those of its complement. It does not assert that the graph itself is self-complementary.

### Signature capacities

An external vertex has a signature S recording its red adjacencies into a rooted graph H. Vertices with that signature cannot contain a red clique of size 5-omega(H[S]) or a white clique of size 5-alpha(H[V(H)\S]). Their number is therefore at most the corresponding smaller Ramsey bound minus one.

These bounds are averaged over induced copies of H and over automorphism orbits of signatures. There are 5,542 signature inequalities. The smaller Ramsey values are external established inputs; this experiment does not regenerate their proofs. The stored R(5,5) entry is not needed for a nonempty signature root: at least one of the two target parameters decreases.

### Bounded conditional moments

For partial signature counts X whose permitted interval is L <= X <= U, use

    E[X^2 - (L+U)X + LU] <= 0.

The implementation includes 122 such inequalities for roots of orders one, two, and three. The capacities account for vertices already inside the root. These are necessary bounded-moment inequalities, not all possible positive-semidefinite constraints.

### Degree-22 diagnostic and published neighborhood premises

At n=45, impose the six factorial degree-moment identities of a 22-regular graph. These constrain degrees through the actual universal-vertex counts in induced types of orders two through seven. They exclude merely assigning an arbitrary degree distribution with the correct mean.

For a red neighborhood with 22 vertices, the published extremal bounds in the class avoiding a red four-clique and a white five-clique are

    88 <= number of red edges <= 114.

The corresponding averaged inequalities are included. These two numbers are imported from Table 1 of Angeltveit and McKay, not independently proved here. Complement averaging supplies the analogous white-neighborhood interpretation.

The resulting exact model has 767 equalities and 5,666 inequalities, in addition to nonnegativity. It does **not** include every rooted graph-gluing constraint, integrality of all actual induced counts, or the full positive-semidefinite moment system.

## 3. Two exact records

The first record, `exact_regular22_counterrecord.json`, has 402 positive density coordinates. Exact integer arithmetic verifies every equation and inequality above. However its value of (2) is

    -820952567957346815970568927508736899223675550276534711336748
    /15575749919288763403386990760520087205211513235848080525

or approximately -52,707.097392510914. This proves that the square inequality (1) is not implied by the declared linear constraints.

Add (1) to the model and solve again. The second record, `exact_regular22_aftercut.json`, has 479 positive coordinates and satisfies all 767 equalities and all 5,667 inequalities exactly. Its value is

    3836880718540940596692275736635470370452944070456870548613623942864879257421859984
    /425918787806319744321530138320501041747523918115299239401423424322250145385685

or approximately 9,008.479617212155.

Thus the new inequality removes a nonempty region of relaxed incidence data, but not the entire feasible region. The second record is not asserted to satisfy the full matrix-positivity conditions or to have a graph realization. Neither record is a lower-bound construction for a Ramsey number.

## 4. The larger matrix formulation

For each root type H, let f_i(R) count two-external-vertex patterns attached to an occurrence R of H. Retain root labels and both colors. Normalize the counts by C(n-|H|,2), adjoin a constant coordinate, and call the resulting vector y(R). Then

    M_H = average_R y(R) y(R)^T

is positive semidefinite. For every real vector c,

    c^T M_H c = average_R (c^T y(R))^2 >= 0.

The average includes the root-type indicator, rather than dividing by a possibly zero root density. Root identifications are averaged consistently over automorphisms.

Seven blocks were constructed for root types of orders one, two, and three. Their dimensions are

    7, 21, 21, 72, 73, 73, 72.

Their entries expand in induced densities through seven vertices. Both overlapping and disjoint external pairs are included with their exact finite-n coefficients. Discarding the overlap terms would change the finite problem.

A formula-versus-direct-enumeration regression compared all seven blocks on 41 sampled allowed seven-vertex graphs: 287 matrix tests, with floating-point discrepancies below 1e-12. These checks test implementation; the positivity statement itself follows from the displayed sum of outer products, not from sampling.

Numerical eigenvector-cut experiments did not produce a certified solution of the full semidefinite problem. They are not included as a feasibility or infeasibility claim. The exact certificates in this bundle concern the explicitly exported linear model and one extra square only.

## 5. An actual 42-vertex control

The first graph6 record in Brendan McKay's public `r55_42some.g6` collection was copied unchanged. A separate bitset implementation verifies:

    vertices: 42
    red edges: 425
    maximum red clique size: 4
    maximum white clique size: 4
    degree histogram: 19:10, 20:15, 21:14, 22:3
    sum_v z_v^2: 13044

The mean square is therefore 13044/42, which is positive. The graph is an existing lower-bound witness, not a construction discovered in this experiment. It is not tested against the 45-vertex regularity constraints, which do not apply to it.

SHA-256 of the retained graph6 file, including its final newline:

    ab0b10364ac62ab07f662c0ed4e8b47a44956f63a78356b64ae64ccb6520ecb0

## 6. Attribution and mathematical conclusion

The published R(5,5)<=46 proof already uses overlapping neighborhoods, linear programming, and extensive gluing. An additional overlap representation is not by itself a new obstruction method.

Positive-semidefinite matrices of rooted pattern counts are finite flag-algebra / sum-of-squares machinery. Lidicky and Pfender explicitly developed this approach for finite Ramsey bounds. No novelty is claimed for that framework, the elementary mean-square inequality, or the rooted signature capacities.

The concrete result here is an exact certificate of a gap between the particular implemented incidence relaxation and quadratic realizability, followed by an exact certificate that one added square does not close that gap completely. It exposes a specific failure of averaged local counts without rejecting the known 42-vertex witness.

A proof of R(5,5)<=45 would require a certificate applying to every permitted 45-vertex degree profile. Even exclusion of the 22-regular subclass has not been obtained. The current published interval is not improved.

## 7. Reproduction and checking scope

From this directory, run:

```sh
python export_and_verify.py
```

This standalone verification uses only Python's standard library. It checks the exact rational records against every exported row, verifies normalization and six degree factorial moments, independently rebuilds (2), and independently checks the 42-vertex graph for red/white five-cliques and the stated square total. The output is `results/independent_verification.json`.

The checker does not independently regenerate the complete graph atlas or prove the external small Ramsey and neighborhood-edge premises. No proof assistant was run.

For rebuilding coefficients and regression tests, install NumPy, SciPy, SymPy and NetworkX, then run:

```sh
python build_hierarchy.py
python build_moments.py
python test_moments.py
python exact_regular_certificate.py
python exact_regular_certificate.py --after-cut
python export_and_verify.py --export
```

The exact reconstruction commands use the retained numerical LP seeds and then verify every resulting rational equation and inequality. The mathematical certificates do not rely on the accuracy of those numerical seeds. `degree_refined.py` and `after_one_cut.py` document the model/search operations; an additional search script reproduces both fixed-degree optimization seeds.

## Sources

1. Vigleik Angeltveit and Brendan D. McKay, *R(5,5) <= 46*, arXiv:2409.15709v2, especially Sections 1, 2 and Table 1. https://arxiv.org/html/2409.15709v2
2. Bernard Lidicky and Florian Pfender, *Semidefinite Programming and Ramsey Numbers*, arXiv:1704.03592v2. https://arxiv.org/abs/1704.03592
3. Brendan McKay, *Ramsey Graphs*. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
4. Source graph collection, first record retained: https://users.cecs.anu.edu.au/~bdm/data/r55_42some.g6
