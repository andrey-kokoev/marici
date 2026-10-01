# Eighteen promotions of the minimal growing seed

Starting seed and rule are unchanged: AB,AC,BC,AD, with each reciprocal pair
promoted to a record and shared endpoints determining the next adjacency.

The checker materializes graphs through promotion7 (4552 vertices,101024 edges).
It computes exact degree histograms through promotion10 using weighted incidence
profiles, and obtains exact vertex/edge totals through promotion11. Vertex count
at promotion12 is also exact, since it equals the preceding edge count.

The shortcut uses degree_L(G)(uv)=degree_G(u)+degree_G(v)-2. Incident-edge degree
profiles give the next histogram by counting all unordered pairs with their
multiplicities. A profile at line-graph vertex uv is constructed from the
profiles at u and v, subtracting the two occurrences of uv. It thereby supplies
two additional histogram steps without materializing the millions or billions
of intermediate edges. Assertions check every adjacent histogram's vertex and
edge count against the preceding degree sums.

Beyond the exact prefix, the report gives certified integer intervals. For mean
degree m and maximum degree D,

    V_next = E,
    m_next >= 2m-2,
    D_next <= 2D-2.

The mean inequality follows from Cauchy-Schwarz; the maximum bound follows from
the line-graph degree formula. Exact rational lower bounds on mean degree and
integer upper bounds on maximum degree propagate into vertex/edge intervals,
with outward integer rounding. These are enclosures, not estimates of typical
values.

| Promotion | Exact records | Exact undirected relationships |
|---:|---:|---:|
|0|4|4|
|1|4|5|
|2|5|8|
|3|8|18|
|4|18|64|
|5|64|396|
|6|396|4552|
|7|4552|101024|
|8|101024|4419384|
|9|4419384|385099432|
|10|385099432|67181536344|
|11|67181536344|23516590975224|

Promotion12 has exactly23516590975224 records. Further counts and all full-precision
interval endpoints are in `results/line-graph-eighteen-cycles.json`.
At promotion18 there are between
89437642907437243187615229455180308 and
158527435472832798844759782952026360 records, and between
3995968109155820931787079958444198358673 and
7792099035796150561616477611440951673080 undirected relationships.
Directed packet slots are twice the relationship count.

This is an18-index combinatorial count analysis with an exact prefix. It does
not construct18 complete graphs or claim exact late counts. It neither runs
18 physical tower cycles nor assigns particle identities or independent
information content to graph size.

## Reproduction

```
python research/nima/checkers/check_line_graph_eighteen_cycles.py
```

All assertions passed. No external dependencies or floating-point arithmetic
are used for the counts or bounds.
