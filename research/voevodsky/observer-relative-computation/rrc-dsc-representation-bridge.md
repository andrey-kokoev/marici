# First RRC–DSC bridge: one native application, with full boundary retention

`agda/ObserverRRCDSCBridge.agda` freezes a shared semantic fragment: one native dependent E or Pi application, supplied with its entire Complete input family and actual child Resolve derivations. It imports Nima's existing constructors and the actual ResolutionNetDependentSubstitution interface; no Nima-owned source was edited.

## Exact translations

For E, the RRC boundary is a nested dependent package (family, child derivations, selected index). The DSC boundary groups (family, child derivations) as the first input and the selected index as its dependent-interface second input. Explicit reassociation maps have both roundtrips.

The DSC continuation is fixed to the specific native E constructor, producing the actual output Closure, including its native apply history. Its execution agrees with that constructor and commutes with environment substitution. This is not a proof synthesizing arbitrary continuations or witnesses.

The application graphs additionally retain the output closure and its actual evaluation equality. The translations retain those fields verbatim and have both roundtrips; a path-level roundtrip is also checked. Reifying the entire DSC application at the next universe and decoding recovers the original RRC application.

Pi already takes the whole supplied input-family context. Its native apply history is produced by DSC composition, with checked substitution compatibility. This is an interface/effect bridge, not a distinct recursively translated Pi syntax.

## Negative boundary

A concrete Bool-indexed E example changes only an UNSELECTED child's raw seed label. Its output Complete packet is unchanged, but the full boundaries and their translated DSC boundaries are provably distinct. No endpoint-only inverse can recover every boundary. Thus the positive bridge deliberately retains the premise histories rather than claiming terminal values are a faithful encoding.

## What this does NOT establish

This is one-layer context/application preservation. Child histories remain actual supplied RRC derivations; they have NOT been recursively translated into an independent DSC object syntax. The continuation explicitly invokes a fixed native RRC constructor. The existing DSC semantic model still uses host dependent functions. Calling this a reduction of all RRC primitives to one autonomous rewrite would therefore be false.

The result connects the actual modules through familiar dependent context reassociation; it is not a new universal foundation theorem. Arbitrary source comparison synthesis, operational adequacy, resource ownership and full calculus equivalence remain separate branches.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-rrc-dsc-bridge.log. The aggregate includes the new module. Fresh check_transport_gate.py passes all checks with inventoried source bytes unchanged: results/transport-gate.json. The earlier46-entry canonical audit is now historical for its recorded source snapshot; it was not relabelled as covering this additional module.

## Next

Develop a recursively explicit DSC representation for the frozen native fragment, rather than storing child RRC histories as opaque translated terms. Relate recursive translation to actual seed substitution/flattening and state which raw history structure is preserved. This is a refinement of the existing representation obligation, not a duplicate of the separate broad operational-realization branch.
