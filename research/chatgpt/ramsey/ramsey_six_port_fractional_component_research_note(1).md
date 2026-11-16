# Six-port Ramsey obstruction: fractional certificates and a rewiring-closed component

Date: 2026-11-09. Status: exact theorem and verified finite subfamily; **no universal catalogue result claimed**.

## 1. Source reduction

Suppose there is a triangle-free graph `G` on 23 vertices with independence number at most 6. The earlier reduction based on `R(3,6)=18` and the seven 17-vertex extremal graphs shows that such a `G` would be 6-regular (assumed here as a previously established lemma, not reproved by these programs). Fix `v`, its six independent neighbors `S`, and the other 16 vertices `H`. Then `H` is triangle-free, `alpha(H)<=5`, `e(H)=33`, and `2<=d_H(w)<=5`. Every port `s in S` has an independent five-set `T_s=N_H(s)`, with `sum_{s in S} 1_{T_s}(w)=6-d_H(w)`.

For every independent five-set `I` of `H`, at most one port can have `T_s cap I=empty`. Otherwise `I` together with two such ports is an independent seven-set in `G`.

## 2. Exact fractional obstruction theorem

Let `F=I_5(H)` and define the disjointness matrix `D_{I,T}=1` if `I cap T=empty`, for `I,T in F`.

If nonnegative rational numbers `y_I` satisfy

    for every T in F: sum_{I disjoint T} y_I >= 1
    sum_{I in F} y_I < 6,

then no 6 ports with independent five-neighborhoods can satisfy even the rank-five Ramsey condition (regardless of degree-cover equations).

Proof: each of six chosen `T_s` requires at least one unit of total disjointness-weight; an independent `I` can be disjoint from at most one chosen `T_s`. Therefore the weighted total is simultaneously at least six and less than six, impossible.

The certificates are the dual feasible points of `maximize 1^T x` subject to `D x <= 1` and `x>=0`. Floating-point linear optimization is only used to *find* weights; all saved claims are checked using integers against every independently enumerated five-set.

## 3. A more general theorem for (3,k)

Let `G` be triangle-free with `alpha(G)<=k-1`. At a vertex `v`, let `S=N_G(v)` have size `d` and let `H=G-(S union {v})`; then `alpha(H)<=k-2`. For an independent `(k-2)`-set `I` of `H`, **at most one** `s in S` can have `I cap N_H(s)=empty`, since two such ports together with `I` give an independent k-set. Consequently any choice of a family of allowed independent port neighborhoods `T` and nonnegative weights on `I_{k-2}(H)` with coverage >=1 for every allowed `T` and total mass <d excludes that port assignment.

The general statement is a standard fractional covering/packing duality certificate adapted to the Ramsey port decomposition. It does **not** yield a general formula for R(3,k) without a graph-independent bound on the weights.

## 4. Verified component census

The program `ramsey_port_rewire_components.py` starts from 27 source-generated candidates (from the seven known extremal (3,6;17) graphs), the earlier explicit 16-vertex witness, and two independently generated Clebsch-derived 33-edge seeds. It exhausts *all admissible one-edge rewires from every encountered labelled representative*, retains every degree and forbidden-subgraph constraint, and deduplicates candidates by NetworkX's exact VF2 isomorphism check (a Weisfeiler–Lehman hash is only a prefilter).

The search closes with **39 nonisomorphic 16-vertex (3,6;33) graphs**, and **838** admissible labelled neighbor moves examined. An independent second pass recomputes all rewiring neighbors, checks exact graph isomorphism again, and verifies that the 39 isomorphism classes form one connected component with **212 undirected inter-class or self connections** (NetworkX loop accounting) under permitted rewiring. Every one of these 39 graphs has a dual certificate of denominator 1000, with all coverage inequalities verified exactly. The largest exact certificate mass is **5.775**. The maximum numerical primal LP objective in the component is **75/13 = 5.769230769...** (numerical objective only, not rational-optimum certification). The component is closed under its specified one-edge rewiring operation. This alone does NOT show that it includes all 33-edge (3,6;16) graphs.

An independent construction exhausts perfect matchings of the 16-vertex Clebsch graph whose removal preserves independence number at most five; it found 200 such matching deletions, with two nonisomorphic 32-edge, four-regular graphs. Adding any admissible triangle-free edge of maximum residual degree at most five yields only graphs already represented in the 39-class component. This is an independent seed check, not a classification of all 32-edge (3,6;16) graphs.

The complete 16-vertex (3,6) catalogue contains 2,576 nonisomorphic graphs, and the catalogue run is outstanding. Source: B. McKay, https://users.cecs.anu.edu.au/~bdm/data/ramsey.html. The known minimum `e(3,6;16)=32` also appears in Radziszowski & Kreher, *On (3,k) Ramsey Graphs: Theoretical and Computational Results* (1988), https://repository.rit.edu/article/640/.

## 5. Reproduction

    python ramsey_clebsch_matching32.py
    python ramsey_clebsch_component_seeds.py 4000
    python ramsey_port_rewire_components.py 3000
    python ramsey_fractional_component_verify.py

Outputs:

- `ramsey_port_rewire_components_results.json`: 39 adjacency lists, numeric objectives, completeness within the rewiring closure.
- `ramsey_fractional_component_certificates.json`: all integer-checkable dual witnesses.
- `ramsey_fractional_component_verify.py`: verifies every graph and certificate independently of LP numerical guarantees.
- `ramsey_clebsch_matching32.json`: matching-deletion control.

The next decisive experiment is to obtain McKay's complete `r36_16.g6.gz` source and test every `e=33, 2<=degree<=5` graph. **Even a full-catalogue positive result would be a computer-assisted finite proof, not yet a new general invariant theorem.** The subsequent structural problem is to derive the fractional bound from a compact graph property or source-generated family, without listing graph isomorphism types.
