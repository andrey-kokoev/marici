# Smallest growing seed under retained line-graph promotion

## Result

For the explicitly chosen rule (promote undirected relationships to records;
connect promoted records sharing an old endpoint), four vertices and four edges
suffice for unbounded graph growth. No seed with fewer vertices or fewer edges
can grow. With each undirected edge stored as reciprocal packets, the minimum
is eight directed packets.

The seed is a triangle with a single pendant edge, called the paw graph:

```
    B
   / \
  A---C
  |
  D
```

Its edges are AB, AC, BC, AD. The packet set is their eight orientations.
Among four-vertex four-edge seeds this is the unique growing isomorphism class.
This uniqueness is specifically at both minimum counts: a four-edge star on
five vertices also grows, but uses more vertices.

## Consecutive promotions

| Promotions | Records | Undirected relationships | Directed packet slots |
|---:|---:|---:|---:|
| 0 | 4 | 4 | 8 |
| 1 | 4 | 5 | 10 |
| 2 | 5 | 8 | 16 |
| 3 | 8 | 18 | 36 |
| 4 | 18 | 64 | 128 |

The first promoted graph consists of two triangles sharing an edge (the diamond,
K4 with one edge missing). The triangles are:

- AB, AC, AD: the three old edges meeting at A;
- AB, AC, BC: the old triangle's three edges, pairwise incident.

Their shared promoted edge joins records AB and AC. This explicitly explains
where the first overlapping cycles appear.

## Continued-growth certificate

After one promotion, every vertex has degree at least two and some have degree
three. In a connected graph with minimum degree at least two and mean degree
m>2, line promotion preserves connectedness and minimum degree at least two.
Its mean degree satisfies

    m_next = sum_v d(v)(d(v)-1) / E >= 2m-2.

The inequality follows from sum d(v)^2 >= (sum d(v))^2/V. Thus m_next-2 is at
least twice m-2, and the mean degree grows without bound. A simple graph has
mean degree at most V-1, so its vertex count also grows without bound.

The diamond has mean degree5/2, meeting this certificate immediately. This is
an analytical continuation argument, rather than an inference from the four
finite promotions alone. The degree inequalities are checked in exact rational
arithmetic at each certified seed; the general argument is given above, not
formalized in Agda.

## Exhaustive minimality checks

The checker exhausts all75 labelled simple graphs on one through four vertices.
None on at most three vertices grows. On four vertices, nineteen labelled graphs
grow: twelve paws, six diamonds, and one complete tetrahedral graph.

Separately it exhausts all3683 edge subsets of sizes zero through three on eight
labels. Every graph with at most three edges has at most six nonisolated vertices,
so this covers every smaller-edge seed up to relabelling and arbitrary added
isolated records. Every such seed terminates or repeats; none grows.

The classifier elides isolated records, which cannot contribute later edges. It
checks repetition by exact isomorphism and growth by the certificate. A search
cutoff is an error, never a non-growth verdict. The displayed growing trajectory
has no isolated records, so its vertex counts are unaffected by that convention.

## Scope

Minimality is for simple undirected graphs with this shared-endpoint promotion
rule, and eight packets assumes reciprocal directed storage. Loops, parallel
edges, directed-only promotion or other compatibility rules define different
problems. The result concerns incidence growth; it does not identify particles,
derive the chosen rule from physical dynamics, or establish growth of independent
information.

## Verification

```
python research/nima/checkers/check_minimal_line_graph_growth.py
```

Exact enumeration and all assertions passed.

- Checker: `checkers/check_minimal_line_graph_growth.py`
- Results: `results/minimal-line-graph-growth.json`
