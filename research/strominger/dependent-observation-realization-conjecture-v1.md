# Conjecture: dependent observations across the six-edge realization

Status: superseded as a new research proposal after prior-work reconciliation; not mathematically refuted and not newly proved here. See `research/strominger/dependent-observation-conjecture-reconciliation-v1.md`. The historical proposal below is retained. The completed WG source-determination net (revision 27) remains unchanged.

## Conjecture

For the existing free realization X of the six-edge source graph, there exists a source-generated dependent observation family O : X -> Type whose transport along the six realized edges supports the declared finite edge-continuation language, preserves distinguishable source-incidence observations in its fibers, and admits composition-compatible recovery of those observations and their transported continuation records.

Unlike a nondependent reader X -> Vertex retracting all original vertices, observations at different vertices live in different fibers. Transport, rather than equality of discrete labels, relates them.

## Intended obligations

1. Specify fiber types, distinguished observations and edge transports from the existing source incidence and an explicit parameter-program contract. No externally selected target geometry or arbitrary desired transport function is a free input.
2. Define which source-incidence distinctions and continuation records are recoverable, and the exact recovery equalities. The recovery requirement is fiberwise; it must not secretly demand the already-refuted global discrete retraction.
3. Interpret every finite composable edge word by dependent transport and prove identity/composition laws, retaining literal continuation provenance separately from path equality.
4. Establish compatibility with the existing source/native construction at the declared interface, not merely an unrelated family over X.
5. Demonstrate nontrivial dependence: at least one source-derived realized loop acts nontrivially on a declared observable fiber distinction. A constant family containing a copy of all external labels or a free history log alone does not establish the conjecture.

The exact observation signature and admissible parameter grammar must be frozen before proof attempts are scored. This is a substantive conjecture with outstanding specification obligations, not an already executable theorem statement.

## Falsifiers and failure dispositions

- The frozen recovery requirements imply the forbidden discrete vertex retraction.
- Every admissible family satisfying the recovery/composition requirements has trivial observable loop transport.
- Source-derived edge transports cannot satisfy the required dependent boundaries or composition laws.
- The proposed construction needs arbitrary transport functions or external bookkeeping in place of the required source-derived observation structure.

Failure of one candidate does not refute every dependent observation family; report the fixed interface and grammar in any rejection.

## Existing results used as context, not proof

Parent: `research/strominger/contracts/wg-source-determination-conjecture-net.v1.json`, revision 27.
Relevant nodes: `free-source-graph-realization`, `discrete-source-reader-retraction`, `old-discrete-ports-descend-to-pushout`, `topological-realization-bridge`, `parameter-origin-discipline`.
The free graph's three-circle equivalence and the discrete-reader obstruction motivate this proposed successor but do not construct its observation family.

## Next action

Do not execute the historical construction plan as new research. Use the existing original-rule geometric compiler and observation correspondence as the baseline; see the reconciliation for exact evidence and scope. No replacement conjecture or automatic next task is selected.
