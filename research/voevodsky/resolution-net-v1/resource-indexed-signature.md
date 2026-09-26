# Resource-indexed rules preserve one history, not one chosen world

The new finite resource signature leaves the net engine unchanged. A package contains an owned resource footprint O and a spent subset D. Consumption of t is admitted only when t is in O minus D, producing(O,D union{t}). Binary combination requires DISJOINT OWNED footprints, not merely disjoint spent sets; its output unions both footprints and both spent sets.

Why owned rather than spent matters: joining a used copy with an unused copy of the same original ticket would otherwise resurrect availability through the unused branch. Tests reject both duplicate-consumed branches and this mixed used/unused alias. Disjoint independent branches combine normally.

Six permutations of three consumption steps have the same final package but six distinct witnessed histories; all flatten correctly with the unchanged local rewrite engine. Six negative cases cover repeated use, absent tokens, overlapping joins, and an invented revival rule. Generic package/arity matching alone accepts a typed revival rule; domain-signature admission rejects it. This is necessary rule evidence, not something the resolution operator can infer.

## Checked minimal formal model

agda/ResolutionNetOneResource.agda specializes the original closure to fresh/used worlds, arbitrary idle steps, two alternative fresh-to-used witnesses, and no binary rules. Agda proves uses(d)=spent-count(endpoint(d)) for EVERY admitted history. Thus fresh histories have zero spends and used histories exactly one, regardless of how many idle steps occur. Both alternative spending histories are inhabitants; the theorem does not choose an external commit.

Fresh --ignore-interfaces check passes under --safe --cubical --guardedness, without postulates or holes. Log: results/agda-one-resource.log. This is a one-resource unary model, NOT a formal proof of the multi-resource binary Python signature.

## Conclusion

Within one derivation, suitable package indices and rule witnesses enforce consumption/separation without adding internal net primitives. Across alternative derivations sharing an initial world, both can remain well-typed. Only an explicit execution/commit interpretation chooses the authoritative branch. Therefore the single resolution operator survives this test, but its domain rule signature must carry resource structure; generic syntactic Rule construction is not authorization.

Files: resource_signature.py, check_resource_signature.py, results/resource-signature.json. Next formalize finite footprint separation and binary accounting, then examine whether the resulting rules suffice for representative legacy ownership patterns. The formal-total-refinement branch remains open independently.
