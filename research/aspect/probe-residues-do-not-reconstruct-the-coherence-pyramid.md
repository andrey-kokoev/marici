# Probe residues do not reconstruct the coherence pyramid

## Question

Do all unary and binary probe constraints determine the incidence structure of a finite coherence pyramid?

## Claim boundary

This packet gives a finite counterexample and sufficient reconstruction conditions for finite labelled simplicial incidence. It does not classify arbitrary globular, higher-categorical, or physical coherence structures.

## Counterexample

Let the labelled locations be \(V=\{0,1,2\}\). Consider two finite simplicial complexes:

- \(H\), the hollow triangle containing every vertex and edge but no two-simplex;
- \(F\), the filled triangle containing the same vertices and edges plus \(\{0,1,2\}\).

Their unary and binary admissible configurations are identical. Assign the same unary constraints and the same binary probe residues to corresponding vertices and edges. Every one- and two-probe observation is then identical, but the incidence structures differ:

\[
f(H)=(3,3,0),
\qquad
f(F)=(3,3,1).
\]

They are not isomorphic because simplex dimension and face counts are isomorphism invariants. The three-probe placement distinguishes them: it is absent in \(H\) and admitted in \(F\). If the observer records only unary and binary residues, this distinction is erased.

This generalizes. For every \(n\ge3\), the boundary of an \((n-1)\)-simplex and the filled simplex have identical proper faces and differ only at the top configuration. No probe semantics truncated below arity \(n\) reconstructs the top cell.

## A second failure mode

Even all-arity constraint values do not reconstruct incidence if the observer omits the configuration domain. A constant terminal value cannot distinguish an absent configuration from a present configuration carrying a terminal constraint object. Therefore domain-of-definition data and semantic values are independent reconstruction inputs.

## Sufficient finite reconstruction conditions

A finite labelled simplicial incidence structure is reconstructed when the probe record contains:

1. the labelled location set and interface types;
2. the admissibility predicate for every finite placement configuration, including explicit absence;
3. downward-closure verification;
4. faithful coordinates for labels and placements;
5. restriction maps with their source and target configurations.

The admissible configuration family itself then is the simplicial complex. Constraint objects enrich it but are not needed to recover bare incidence.

For reconstruction from constraint semantics without an explicit admissibility table, stronger conditions are required: the semantics must reflect existence, distinguish initial/terminal/empty objects from absence, and be conservative enough that distinct cells or incidence maps cannot have identical images. Equal dimensions, equal residue cardinalities, or equal truncated probe data do not establish this faithfulness.

## Hostile tests

1. Hollow versus filled triangle rejects unary/binary reconstruction.
2. Boundary versus filled simplex rejects every fixed arity truncation below the top.
3. Constant semantics rejects reconstruction when domain information is erased.
4. Permuting labels is harmless only when the requested reconstruction is up to labelled-compatible isomorphism.
5. A measured projection may identify configurations that faithful coordinates separate; reconstruction must use the faithful coordinate system.

## Disposition

The conjecture that unary and binary probe residues reconstruct the coherence pyramid is false. They reconstruct at most a decorated two-skeleton. Finite labelled simplicial incidence becomes reconstructible once the complete admissibility domain is retained; reconstruction from semantic values alone needs additional existence-reflection and faithfulness assumptions.
