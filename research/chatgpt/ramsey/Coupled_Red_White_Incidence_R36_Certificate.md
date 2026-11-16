# Coupled red–white incidence and an R(3,6) certificate

## Result and scope

A single overlap inequality couples red paths with white-clique extension. Combining it with the classical degree-deficiency identity proves that an 18-vertex triangle-free graph has an independent six-set. An exact verifier checks the resulting finite certificate, its degree-bound prerequisites, and seven 17-vertex lower-bound witnesses.

This is a reconstruction of a known Ramsey result, not a new Ramsey value or a claim of novelty for the underlying combinatorics. The overlap inequality is an elementary decomposition identity. The degree-deficiency method is classical. The singleton/doubleton incidence structure also appears in Cariolaro's proof. The work here organizes those ingredients into a reusable rule and checks an explicit short completion certificate. It does not determine R(3,18).

## 1. Exact coupling law

Let G be the red graph; white edges are the pairs not in G. Assume G has no triangle. Fix v and write

- B = N_G(v), with d = |B|;
- H = G[V(G) minus (B union {v})];
- sigma(x) = N_G(x) intersect B, for x in V(H).

Because G has no triangle, B is independent: all its internal relationships are white.

For any independent set T in H, let

    sigma(T) = union of sigma(x) over x in T.

Then the following set is independent in G:

    T union (B minus sigma(T)).

Its size is exactly |T| + d - |sigma(T)|. Therefore avoidance of an independent t-set requires

    |sigma(T)| >= |T| + d - (t-1).                       (1)

When d=t-1, this reduces to |sigma(T)| >= |T|. Thus a set of white-linked vertices cannot use fewer distinct red-neighbor labels than its own size.

The full statement is exact, not merely a necessary relaxation:

    alpha(G) = max(1 + alpha(H),
                   d + max over independent T in H of (|T|-|sigma(T)|)).   (2)

Proof: an independent set containing v consists of v and an independent subset of H. One not containing v chooses an independent T in H and can add precisely the available vertices of B minus sigma(T). The two cases cover every independent set, and each displayed maximum is attainable.

Consequently, at this fixed v, alpha(G) <= t-1 is equivalent to alpha(H) <= t-2 together with (1) for every independent T in H. The identity itself has no t parameter; t specifies the question to which it is applied.

This requires the actual sets sigma(x), not only their cardinalities or an averaged transport spectrum. It does not require a circular ordering, equal color counts, or invertible vertex updates.

## 2. Uniform degree reduction

Write m=e(G), d_v=deg(v), and H_v=G-N[v]. In a triangle-free graph,

    e(H_v) = m - sum over u in N(v) of d_u.

The reason is that N(v) is independent: the degree sum over N(v) counts each edge removed by deleting N[v] exactly once. Summing over v gives

    sum_v e(H_v) = n*m - sum_v d_v^2.                  (3)

For an arbitrary graph, the corresponding right side has the additional term 3 times the number of triangles. The verifier checks that more general identity too.

Let f_t(q) be a proved lower bound on the number of edges of any triangle-free q-vertex graph with alpha < t, and use infinity when nonexistence has been proved. Since H_v has alpha < t-1,

    n*m >= sum_v [d_v^2 + f_(t-1)(n-d_v-1)].           (4)

Every degree lies between 0 and t-1, and sum_v d_v=2m. The verifier derives lower bounds using integer dynamic programming over degree totals, starting only from the trivial t=2 case. Feasibility of these inequalities does not prove a graph exists.

For the present proof it obtains:

| Class | Proved minimum-edge lower bound |
|---|---:|
| (3,3) on 3 vertices | 1 |
| (3,3) on 4 vertices | 2 |
| (3,3) on 5 vertices | 5 |
| (3,4) on 7 vertices | 6 |
| (3,4) on 8 vertices | 10 |
| (3,5) on 12 vertices | 20 |
| (3,5) on 13 vertices | 26 |

It also proves nonexistence at (3,3;6), (3,4;9), and (3,5;14). The numerical bounds are outputs of the recurrence, not a table supplied to it.

### Short arithmetic reconstruction

For (3,3) on five vertices, all degrees must be two; on six vertices the degree bounds already conflict. This also supplies the elementary three- and four-vertex bounds.

For (3,4) on seven vertices, allowed degrees are 1,2,3. Each summand in (4) is at least six. Therefore 7m >= 42 and m >= 6. On eight vertices, degrees are two or three. If x vertices have degree two, then m=12-x/2 and (3) gives sum e(H_v)=24+x. The lower bounds on the five- and four-vertex residuals require at least 5x+2(8-x)=16+3x. Hence x<=4 and m>=10. On nine vertices every degree would be three, contradicting the even degree sum.

For (3,5) on twelve vertices, degrees are three or four. If x vertices have degree three, then m=24-x/2 and sum e(H_v)=96+x. The eight- and seven-vertex residual bounds require at least 10x+6(12-x)=72+4x. Thus x<=8 and m>=20. On thirteen vertices all degrees are four, giving m=26. Fourteen vertices are impossible by the same neighborhood bounds.

Now suppose G is a (3,6) graph on eighteen vertices. Its degrees are four or five. If x vertices have degree four,

    m = 45-x/2,
    sum d_v^2 = 450-9x,
    sum e(H_v) = 360.

But the twelve- and thirteen-vertex residual bounds require

    sum e(H_v) >= 26x + 20(18-x) = 360+6x.

Thus x=0: every vertex has degree five.

## 3. Derive the twelve outside signatures

Fix v. Its red neighborhood B has five vertices, and H has twelve.

For a nonadjacent pair u,v, the number c of common red neighbors is either one or two. It cannot be zero: u together with N(v) would be independent of size six. It cannot be at least three: the vertices outside N[u] union N[v] number 6+c>=9, and the already derived R(3,4)<=9 supplies an independent four-set there. Adjoining u,v gives six.

There are 5*4=20 red edges between B and H. Therefore H has four vertices with singleton signatures and eight with doubleton signatures.

The singleton signatures are distinct: two vertices using the same singleton are white-connected and can be joined to the other four vertices of B, giving six. Doubletons are distinct: two copies of {i,j} would give the nonadjacent B vertices i,j at least three common red neighbors, namely v and those two copies.

Each B vertex has four red edges into H. It follows that, up to renaming, B={s0,s1,s2,s3,s4}, and H has the following signatures:

    sigma(p0)={0}, sigma(p1)={1}, sigma(p2)={2}, sigma(p3)={3};
    sigma(qij)={i,j} for every pair except 01 and 23.

There are exactly 15 labeled singleton/doubleton patterns with these loads, and all have this form after relabeling. The verifier enumerates them. Algebraically, the omitted two pairs must form a matching on the four singleton labels.

## 4. Four forced edges

Intersecting signatures imply a white edge: a red edge would close a red triangle through the common B neighbor.

Apply (1), with d=5 and t=6. The following candidate T sets use too few B labels. Therefore T cannot be all white. In each row, all its internal edges except the indicated edge are already forced white by intersecting signatures.

| Candidate T | Union of signatures | Forced red edge |
|---|---|---|
| p0,p2,q02 | {0,2} | p0-p2 |
| p0,p3,q03 | {0,3} | p0-p3 |
| p0,q02,q04,q24 | {0,2,4} | p0-q24 |
| p0,q03,q04,q34 | {0,3,4} | p0-q34 |

Together with p0-s0 these saturate p0's red degree at five. Thus p0 is white-connected to p1,q12,q13,q14. Those four vertices are mutually white-connected because all their signatures contain 1. The vertex v is white-connected to every vertex of H. Hence

    {v,p0,p1,q12,q13,q14}

is a white six-clique, a contradiction. This proves R(3,6)<=18.

The verifier also runs generic unit propagation on the partial incidence graph, using the same three kinds of constraints everywhere: no red triangle, no white six-clique, degree five. It reaches a contradiction after 36 assignments, without prescribing the four-edge certificate above. The short certificate is verified separately. Unit propagation is not asserted to be a complete procedure for arbitrary Ramsey instances.

## 5. Lower-bound witnesses and actual verification

The seven graph6 records in mckay_r36_17.g6 reproduce the text returned by Brendan McKay's public catalog. Each was decoded independently with integer arithmetic. For every graph the verifier checks all 680 triples and all 12,376 six-subsets. All seven have zero red triangles and zero white six-cliques, and each contains a white five-clique. Their edge counts are 41,41,40,41,40,42,42.

Thus R(3,6)>=18, and together with the upper certificate R(3,6)=18.

Actual additional checks with --atlas:

- 1,253 unlabeled simple graphs through seven vertices: the general version of (3) passes.
- 173 triangle-free graphs in that atlas: equation (2) passes at all 1,089 rooted choices.
- All 15 possible labeled local signature patterns have the required form.
- Every premise and conclusion of the four forced-edge steps is checked, followed by all 15 edges of the final white six-clique.

These finite checks supplement the written proofs. They are not presented as proof by sampling of the universal identities, and no proof-assistant compilation is claimed.

## 6. Reproduction

Standard-library proof checks, including the 17-vertex witnesses:

```sh
python verify_coupled_incidence.py --output coupled_incidence_certificate.json
```

Optional atlas regression requires NetworkX:

```sh
python verify_coupled_incidence.py --atlas --output coupled_incidence_certificate.json
```

Keep mckay_r36_17.g6 beside the script. The JSON receipt includes the source-data SHA-256, derived degree lower bounds, signature census, forced-edge certificate, propagation trace, and lower-bound checks.

## 7. Boundary of the result

The general quantity is the overlap deficit

    delta_v(T) = |T|-|sigma(T)|.

At a vertex of degree t-1, a positive deficit for a white clique is forbidden. The full maximum identity is exact, but evaluating it may require searching many white cliques. This work establishes a uniform local composition constraint and a checked sharp test, not that bounded-size overlap information determines every Ramsey number.

## Sources

1. Jan Goedgebeur and Stanislaw P. Radziszowski, *New Computational Upper Bounds for Ramsey Numbers R(3,k)*, arXiv:1210.5826v4 (2013), equations (1)-(4), for the degree-deficiency method. https://arxiv.org/abs/1210.5826
2. David Cariolaro, *On the Ramsey number R(3,6)*, Australasian Journal of Combinatorics 37 (2007), 301-304, for the established result and the closely related singleton/doubleton incidence reduction. https://ajc.maths.uq.edu.au/pdf/37/ajc_v37_p301.pdf
3. Brendan McKay, *Ramsey Graphs*, seven (3,6)-graphs on seventeen vertices. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html ; source graph6 text: https://users.cecs.anu.edu.au/~bdm/data/r36_17.g6
