# Semantic crosswalk and checked substitution bridge

New module agda/ResolutionNetSubstitution.agda imports the original Nima CoherenceResolutionClosure without changing it. It is checked under --safe --cubical --guardedness, with no new postulates or holes. A fresh --ignore-interfaces run with Agda2.8.0.1 and Cubical0.9 passes. Reproduce via check_agda_substitution.py; results/agda-substitution.json records source hashes, command and checker version.

## Correspondence

| Prototype | Generic semantic object | Qualification |
|---|---|---|
| finite Package record | p:P | Python representation only; arbitrary higher/type-valued packages not implemented |
| Admission witness string | s:S(p) | symbolic finite witness data, not automatic Agda evidence of an external scientific claim |
| Rule with one/two inputs | u:U(p,q), v:V(p,q,r) | runtime package matching substitutes for dependent typing only in the finite model |
| Seed/Step history | Resolve(S,p) | constructors preserve the occurrence tree, witnesses and ordered premises |
| nested seed evidence | Resolve(Resolve S,p) | homogeneous layer checks correspond to iterated closure |
| external Hole(slot,p) | an element h:H(p) | evidence of a named slot obligation, NOT an inhabitant of the final admitted family S |
| supplied pure history | f(p,h):Resolve(S,p) | a total valuation is needed to obtain a closed result; partial arrivals remain open |
| receipt sequence | extra operational provenance | not quotiented or represented by the closure theorem automatically |

## Checked laws

Define plug(f,d)=flatten(mapSeeds(f,d)), where f maps typed slots to witnessed resolutions. Agda checks:

* plug-unit: substitution by seed is identity;
* plug-compose: successive substitutions equal their composed valuation;
* plug-flatten: supplying histories before or after eliminating the outer closure layer agrees;
* plug-cong: pointwise paths between supplied histories induce a path between filled resolutions.

The last two provide the semantic target for arrival/rewrite comparison without declaring receipt histories equal. No truncation or idempotence of retained histories is used.

## What this does not certify

The Python compiler, wire rewriting, allocator, transactional publication, admission validator and alpha-renaming arguments have NOT been connected to this Agda module by a formal refinement theorem. Their evidence is still executable bounded checking plus the written structural arguments. The module proves generic reference-semantics laws; it does not upgrade Python strings into inhabitants of arbitrary U/V types, certify global ticket ownership, or justify release timing equivalence.

Next formal branch: introduce a small indexed pending-term reduction calculus in Agda and prove each of the three rewrite schemas preserves interpretation. That can capture the abstract local rules before attempting a concrete port-graph encoding. The independent ticket-fork/linear-authority branch remains open.
