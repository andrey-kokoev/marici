# Structural contract

Active coherence obligation: route/coherencer compatibility. This iteration checks the finite combinatorial domain of that obligation, not a higher-coherence proof or an SCC certification. No physical-time interpretation is attached to sequence indices.

## Ordered occurrences

RDF triple order carries no sequence meaning. A Path owns PathStep occurrences with unique consecutive integer indices starting at zero. Every occurrence has exactly one owning path and one directed Arrow. Repeating the same Arrow in different occurrences is permitted. Empty paths are identities and require equal declared endpoints. Nonempty paths must start/end at their declared vertices and compose at every consecutive step.

A Boundary owns BoundaryStep occurrences, also indexed from zero, and declares a base vertex. Every boundary step references an undirected Edge and an explicit boolean `reversed`. Its source/target are determined from end0/end1 and that bit; reversal remains distinguishable even on loop supports. Consecutive uses compose; the first starts and the last ends at the base. An empty boundary is a constant loop at its base. This is a closed walk, not a claim of an embedded/simple polygon.

## Cells and declarations

A Cell names exactly one Boundary and one filling Witness. A filling declaration names that same cell and boundary, reciprocally. Cell shape and geometric realization are not inferred from boundary length.

Witness records have one explicit kind:

- BoundaryDeclaration: names a Boundary.
- FillingDeclaration: names a Cell and its Boundary.
- ComparisonDeclaration: names left and right Paths with the same source and target.

All witnesses explicitly have status Declared. A free-text description is optional and cannot replace a payload. These checks establish well-formed declarations only. In particular, parallel paths are not thereby equivalent; filling declarations are not proofs of a geometric realization. Verified evidence status is not accepted by this schema without a separately implemented evidence verifier.

## Membership and identities

Referenced vertices, supports, arrows, boundaries, paths, cells and witnesses must belong to the containing structure. A step occurrence belongs to exactly one path or boundary; sharing an arrow or edge does not identify step occurrences. New objects receive typed provenance references. Constituent coverage and inventory exclusions include the new structural roles. No coordinates, SVG paths or color-to-particle correspondence are inferred.

## Shells and oriented incidence

A Shell declares a positive level and its cell/electron members. Levels are unique within a structure; a cell or electron cannot belong to two of its shells. This is declared grouping, not an inferred orbital occupancy or capacity law. Gaps between occupied shell levels are not forbidden.

A Junction belongs to a declared vertex and owns its Port occurrences. Each port identifies an Edge and endpoint slot 0 or 1. Both ends of a loop are distinct occurrences even though they meet at one vertex. Port indices uniquely enumerate a consecutive positive cyclic order; the successor of the last is the first. This order is supplied data, not extracted from SVG coordinates. A junction cannot duplicate an edge-end occurrence. One structure has at most one frame at each vertex.

A port may declare at most one opposite port. These pairs must be reciprocal, distinct, and local to the same junction: a partial fixed-point-free involution. Absence means no declared straight continuation, not a request to infer collinearity. This validates combinatorial straight/turn inputs, not their Euclidean realizability or a runtime tracing algorithm.

## Complete combinatorial profile

The profile describes a nonempty arrow/cell record, not every possible abstract complex or a source-certified physical isotope. It requires nonempty vertex, edge, arrow, cell, shell and junction inventories. Existing cell constraints then require their boundaries and typed filling declarations. Paths and comparisons are checked when declared; inventing an arbitrary comparison is not required for completeness.

Every declared constituent must have an in-structure role binding. Every cell and every declared electron must be assigned to exactly one shell. Every vertex must have exactly one frame, and every edge-end occurrence must have its unique port. Existing membership, sequence, ownership and witness-payload constraints all remain active. The electronic state may explicitly remain unspecified; completeness does not manufacture an electron inventory. Isolated vertices, free edges, repeated supports and loop endpoints are not ruled out by an invented physical law.

The complete fixture is an explicit test construction: load `two-cells.ttl`, remove its PartialStructureProfile assertion, and merge `complete-organization.ttl`. No implicit imports or inference are used. Neither this construction nor a passing complete profile proves source derivation, physical correctness, path equivalence or filling existence. Those evidence obligations remain separate.
