# Marici fifth-vertex cycle-closure admission theorem

## Status and source boundary

This is a combinatorial theorem and a source-specific admission audit. It does not assert a new Agda proof or that the unmodified Marici Witness Generator selects the task. Exact finite checks are in `ramsey_cycle_closure_native_admission.py` and `ramsey_cycle_closure_native_admission_results.json`.

Inspected native source declarations:
- `research/nima/agda/ActualSeedEndpointTable.agda` fixes `Vertex={A,B,C,D}` and primitive occurrences `AB BC CA AD DB BA`.
- `research/strominger/agda/SourceIndexedExtensionFamilies.agda` defines `Out(v)=Σ(w:Vertex) Edge(v,w)` for these four vertices.
- `research/strominger/agda/CanonicalComparisonSynthesis.agda` decides comparison admissibility through actual `Edge` constructors and generated reader images; it does not use a fifth vertex or two complementary path colors.
- `research/nima/agda/DomainWitnessCompiler.agda` takes a supplied `compute` map and, for a requested law, a supplied proof of it.
- `research/nima/seed-endpoint-sections-and-unique-return-cycle.md` constructs one four-vertex directed cycle under the declared one-in-one-out objective, explicitly not a uniquely forced WG task.

## Theorem A: unique double-cycle closure

Let `V` be a four-element set. Let `P,Q` be an unordered pair of edge-disjoint spanning paths of length three on `V` with `E(P) ∪ E(Q)=E(K4)`. Adjoin a new vertex `z`. A spoke assignment chooses, for every `v∈V`, whether `zv` belongs to `P` or `Q`, giving `2^4=16` assignments.

The endpoint sets `∂P,∂Q` are disjoint and partition `V`. Proof: `deg_P(v)+deg_Q(v)=3` for each `v` in `K4`, while each `deg` is one or two. Exactly one path has degree one at each vertex.

The only assignment extending both path bundles to 2-regular spanning graphs is

`zv∈P' ⇔ v∈∂P`; `zv∈Q' ⇔ v∈∂Q`.

The new vertex has degree two in each bundle automatically, and each bundle is a single five-cycle. Conversely any double cycle must attach the new vertex to exactly the old degree-one endpoints, so the assignment is unique. Therefore the dependent type of assignments with degree-two proofs is contractible, assuming the usual proof-irrelevance of finite decidable degree equalities.

## Theorem B: relationship to Ramsey admissibility

For any two-coloring of `K5`, no monochromatic triangle is equivalent to degree two in each color at every vertex, equivalent to two complementary five-cycles.

Proof: any vertex with three same-colored incident edges induces an opposite-colored triangle on those three neighboring vertices; so both degrees are at most two and sum to four, forcing two each. A simple 2-regular graph on five vertices has to be a `C5` (a two-vertex cycle is impossible). The converse follows because `C5` has no triangle.

Thus the double-cycle condition is an equivalent Ramsey restriction on `K5`, **not an independently derived native law**.

## Theorem C: source symmetry and apex balance are insufficient

Let `s=(AB)(CD)`. For either `s`-fixed complementary path pair, the two paths are each fixed as undirected sets. An `s`-invariant choice of four spokes is constant on the two vertex-orbits `{A,B}` and `{C,D}`: four choices. Requiring exactly two spokes in each bundle eliminates the two constant choices, leaving two. Exactly one gives two closed cycles.

Explicitly take `P=C-A-B-D`, `Q=B-C-D-A`. The correct extension assigns `zC,zD` to `P` and `zA,zB` to `Q`. The competing `s`-invariant balanced assignment puts `zA,zB` in `P` and `zC,zD` in `Q`. This second assignment creates triangles `zAB` in `P` and `zCD` in `Q`. It nevertheless has the same unlabeled `K5` incidence, apex degrees, and `s` invariance.

Therefore neither source incidence, equivariance, nor balance at the new vertex forces the unique closure rule. More generally, any admission predicate factoring through an unlabeled/incidence-only forgetful map must be constant on all sixteen extension labels.

## Theorem D: existing source cycle cover yields a 4+2 family, not a unique extension policy

The actual directed source's unique one-in-one-out cover is `A-D-B-C-A`; let `C` be its undirected edge set. The complementary matching on `K4` is `M={AB,CD}`, with `CD` available only as a composite macro incidence (`CA AD`) in the original seed.

Of the ten unordered partitions of `E(K4)` into two three-edge sets, six are complementary `P4/P4` decompositions and four are `K1,3/K3` decompositions. Four of the six arise as `{C−{e},M∪{e}}` for `e∈C`. The remaining two are `s`-fixed cross-sewn decompositions. The cycle-cover objective alone does not select these six partitions from the ten; requiring both parts to be paths is an extra predicate.

## Theorem E: K6 holonomy after the admission law is supplied

Each `K5` has six unordered complementary `C5/C5` structures; restriction to any one `K4` subset is a bijection onto its six complementary `P4/P4` structures (Theorem A). On six ambient vertices, each ordered pair of deleted-vertex facets therefore has a canonical six-state overlap transport.

For distinct deleted vertices `i,j,k`, the triangular holonomy on facet `V\{i}` equals the vertex transposition `(j k)`. It acts on the six complementary `C5/C5` structures as three disjoint transpositions, hence has no fixed point. Thus no coherent global selection of local pentagon-pair states exists.

Verification enumerated 6 K4 path pairs × 16 assignments = 96; 30 directed overlap transports across 6 K5 facets; 120 ordered triangular loops. All checks passed. This is conditional on the accepted five-cycle-completion task, not proof that Marici's original WG generates it.

## The missing native premise

There are two independent pieces not constructed by the unchanged fixed four-vertex source signature: (i) a fifth vertex and its four independently usable attachment incidences; (ii) a source-authorized requirement to close **both** boundary paths into degree-two cycles. The latter is equivalent to the Ramsey triangle-exclusion law on five vertices, although it can be expressed without referring to colors.

An ordinary WG can compile the *supplied* endpoint-deficit algorithm into a witnessed request/response step, preserving the original path and cut records. That compiler does not derive the task's authority from the seed. The next meaningful source gate is an explicit, source-generated double-cycle task rule or an independence theorem ruling it out under a frozen admissibility fragment.
