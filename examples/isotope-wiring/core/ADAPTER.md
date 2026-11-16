# Attributed incidence and the legacy adapter

## Implemented scope

This milestone adds `attributed-diagrams.mjs`, `legacy-adapter.mjs`, and
`isotopeSupportSchema` without changing the visual application or its data.
The APIs consume checked finite diagrams and absolute legacy definitions.
They do not resolve mutable delta registries, derive isotope targets, or certify
physical interpretations.

## 1. Attributes form a separate category

An attributed object is `(X, a)`, with a checked incidence diagram X and a finite
JSON model label for every record of every sort. An arrow `f:(X,a) -> (Y,b)` is
an incidence-preserving map satisfying `b_s(f_s(x)) = a_s(x)` at every sort s.
Label equality is normalized JSON equality, not pointer identity. All data is
copied and frozen; missing/extra label-domain entries are refused.

`attributedIdentity` and `composeAttributed` implement the category operations.
The preservation equation is stable under identities and composition. Forgetting
labels returns the underlying incidence diagram/map. Provenance is deliberately
not a model label: two occurrences can have identical model roles but different
record histories.

For a label-preserving span, the underlying pushout equivalence classes have
constant labels. Assign each quotient class that label. The universal factor
preserves it because every class has an input representative. Consequently the
underlying pushout lifts to an attributed pushout with its universal property;
`attributedPushout` constructs and checks those maps.

This is a pushout-closure argument, not a claim that all finite limits of the
unattributed kernel lift unchanged. Arbitrary JSON labels have an unbounded value
domain, so a finite terminal attributed object need not exist. No such object is
invented by discarding labels. Generic attributed diagrams remain permissive, while the separate
[model checker](MODEL.md) now checks explicit attribute types and the concrete
shell-lattice predicates. The adapter supplies the roles listed below.

## 2. Explicit support-interface policy

`glueSupport(f,g)` applies `isotope-wiring.support-interface.v1`:

1. Both legs are checked label-preserving monomorphisms.
2. The interface contains no `pair`, `lineWitness`, or `boundaryWitness` records.
3. If a support record is shared, the interface includes every directed edge
   incident to its image in either component. Ordinary schema closure also
   includes the source/target vertices of those edges.
4. Identifications come only from the supplied maps.

The returned pushout retains both image maps and quotient membership. Thus
sharing an edge or its support never merges independently owned EP/neutron
occurrences. Counts may increase beyond supplied targets; that is a later model
constraint, not permission to delete records during gluing.

Condition 3 refuses a support-only identification that omits its directed-edge
incidence. This first policy is deliberately strict: components with different
incident-edge sets may require a different explicitly justified policy rather
than an inferred match. There is no automatic interface search or alignment.
The subsequent [policy-composition milestone](MODEL.md) adds checked open
components, rechecks external legs after composition, and supplies a closure
argument plus bounded pentagon and unit-triangle tests.

## 3. Source adapter and exact support identity

`importLegacyAbsolute(definition)` produces:

- an attributed diagram over `isotope-wiring.support-incidence.v1`;
- a map from every source shell, cell, pair, and witness occurrence to its target;
- the complete frozen source, including unknown fields and collection order;
- supplied target values in a separately marked model context;
- a loss/interpretation report and the declared lattice-policy version.

The support schema extends the earlier incidence schema with a `support` sort
and `edgeSupport:edge -> support`. Direction belongs to the edge; undirected
support has its own occurrence. Oppositely oriented edges can share support
without identifying either their directions or their owned pair records.

For a cell at row r, column c, the four local lattice vertices are

\[
(c-r,\ r+c+1)+d,
\qquad
 d_T=(0,-1),\ d_R=(1,0),\ d_B=(0,1),\ d_L=(-1,0).
\]

A vertex is keyed by the shell ID and this exact integer pair. There is no float,
rounding, screen placement, zoom, shell-spacing constant, or SVG calculation.
Within a fixed shell this is the combinatorial lattice underlying the legacy
layout; it is a declared adapter policy, not a derivation of physical geometry.

Vertices from different shells are never implicitly identified, even if a display
happens to place them together. A cross-shell identification requires an explicit
interface and, where labels differ, a separately specified frame adapter. Current
attribute maps fix the frame labels; they do not perform that transport.

Ports use tagged tuples `(cell ID, role)` rather than concatenated coordinates.
Duplicate legacy IDs and overlapping cells are refused rather than guessed apart.
Valid cells `(1,10)` and `(11,0)` with distinct IDs remain distinct. This avoids
introducing the old concatenation defect but does not repair ambiguous saved
files or change the old editor's ID generator.

### Labels and retained-only data

| Sort/layer | Model data in the new representation |
|---|---|
| shell | Declared order and size |
| cell | Row and column; shell is an incidence map |
| port | Local T/R/B/L role; owner and vertex are incidence maps |
| vertex | Shell-local frame label and exact lattice pair |
| edge | Direction from structural source/target; support via `edgeSupport` |
| support | Undirected-support kind and endpoint frame/lattice labels |
| pair | Cell and red/blue routes via structural maps |
| line witness | H/V axis, owner, route and support references |
| boundary | Named shell-frame role and shell incidence |
| boundary witness | Named boundary support and shell incidence |
| model context | Supplied Z/N/shell targets, explicitly not derived |
| retained source | Histories, annotations, all additional fields, original IDs and order |

A named boundary is not a certified closed cycle. The adapter constructs matching support labels and edge endpoints by definition.
The [model checker](MODEL.md) separately tests this consistency for independently
constructed attributed diagrams.

## 4. Recovery and information loss

`recoverLegacySource(packet)` returns an independent copy of the exact retained
source. It accepts only a checked immutable packet from this process. For durable
storage, export the recovered source and re-import it; serializing an envelope
and pretending it is checked is refused.

The tested roundtrip is

\[
\operatorname{recover}(\operatorname{import}(D))=D.
\]

It depends on retained source data. It is **not** an inverse of the bare incidence
projection: model labels and incidence alone do not determine history, notes,
unknown fields, or input ordering. Reconstructing a legacy source from a modified
or glued incidence object is not implemented. A future rewrite/export layer must
name how new records acquire provenance and how metadata changes are represented.

The report's `omittedSourceFields: []` means all source fields are retained in the
packet, not that all have been interpreted as incidence. `modelValidity:
not-checked` remains explicit, including for the deliberate miscount fixture.

## 5. Verification

```
node --test tests/isotope-wiring-adapter.test.mjs tests/isotope-wiring-category.test.mjs
```

The adapter suite tests all nine legacy fixtures, exact recovery of extra data,
nonmutation/frozen packets, opposite directions with shared support, ambiguous
input rejection, multi-digit coordinates, cross-shell separation, label mismatch
refusal, attributed identity/composition, ownership-preserving gluing, universal
factors, and policy refusals. These tests do not verify isotope counts as derived
physical properties or establish global completeness of model constraints.

Attribute/model predicates and bounded policy-composition coherence checks are
now implemented in [MODEL.md](MODEL.md). Remaining structural work includes
explicit frame transport and selective evidence transport. [RULES.md](RULES.md)
adds reusable monic rules and preserved-context match transport. [Immutable revisions and ground rewrites](REVISIONS.md) now implement
exact operation boundaries, dangling-reference refusal, before-image recovery,
and dependency-complete replay. Visualization integration stays deferred.
