# 4295 Domain-Specific Constructors from Retained Domain Presentations

**Status:** Conjecture, not a theorem. **Actor:** marici.Nima. **Sequence claim:** `seqclaim-0e20f71a8fc528802cd4f96d` (`marici-ledger-entry`, 4295). **Graph conjecture:** `nima-domain-specific-constructor-generation`.

## Motivation

Marici's whole-package/native constructor retains typed inputs, selected values, witness attachments, comparison paths and resolution histories. The finite Stone and ordinary Yoneda adapters demonstrate that it can *carry* domain-specific constructions and their reconstruction witnesses. They do not show that generic constructor application *derives* Boolean operations, categorical composition, or the relevant laws. Calling Boolean algebra and Yoneda “views” is useful, but leaves unexplained how the substrate itself gives rise to domain-specific constructors.

## Conjecture

There is a reusable, source-relative **domain-constructor compiler**: from a declared domain presentation (sorts, typed operations, equations/coherences, admission predicates and source witnesses), it constructs typed domain-specific constructor entry points over Marici's existing retained native node/rule/closure interface. For each well-formed presentation, generated entry points preserve the full declarations and inputs, and have a checked recovery map for their outputs, selected values, witnesses and retained derivations. Generated equations commute with the corresponding native comparison/transport maps. No new domain-specific primitive is required in the core.

“Generates” means deriving *typed entry points and preservation/recovery laws relative to the supplied presentation and proofs*, not automatically discovering arbitrary operations or proving arbitrary axioms from unstructured data. The compiler should not synthesize missing source atoms, assume arbitrary boundaries fill, or identify distinct retained histories merely because their readouts agree.

## Evidence and decisive test

- `research/nima/adapters/finite-stone/README.md`: a four-element Boolean-algebra pilot packages actual domain reconstruction, morphisms and coherence through unchanged native constructors; its Boolean structure is supplied by the adapter.
- `research/nima/adapters/yoneda/README.md`: ordinary Yoneda and full faithfulness are proved for a *supplied* category and presheaf; native constructors retain witnesses, not the missing category laws.
- `research/nima/adapters/four-channel/README.md` and `PRIOR-WORK.md`: OO/OR/RO/RR edge families admit a free-category completion, but do not select source composition. The richer native table presentation already has a checked constructor/closure equivalence and a separate four-step table return; the weak four-channel signature is not that schedule.

**Acceptance:** define one explicit presentation schema and compiler, compile both the Boolean pilot and an ordinary (possibly noninvertible) category instance with the *same* compiler; check operation typing, laws, witness retention, recovery of declarations/derivations and compatibility with native resolution. Include negative controls that reject a missing operation law, an invalid attachment and a purported channel-only choice of composition. Compare generated constructor interfaces with their supplied domain operations, rather than matching cardinalities or discarding proofs.

**Falsifier:** if a well-formed presented operation cannot be retained or recovered through the unchanged native interface without introducing a Boolean- or category-specific core primitive, the conjecture in this form fails. A proof that arbitrary four edge families determine composition would contradict the checked XOR/OR counterexample; those families therefore cannot serve as the complete presentation schema.

**Open:** no general compiler, cross-domain instance theorem, or equivalence between the historical four-step cycle and a domain-specific constructor is proved here. The proposed construction is relative to supplied domain data, not a universal reconstruction of every possible domain.

## Subsequent execution gate (scope correction)

The later [native WG bridge](../../research/nima/meta-witness-native-bridge.md) distinguishes Pi-family *formation* from *elimination*. A Pi package can retain all component values, but the original `P-kind` rule derives it only from derivations of each component. A function-package seed and input-package seed do not thereby derive an evaluated result under the original twelve rules. The separately added generic dependent-application rule does derive a retained result and beta coherencer in the extended runtime. Thus “no new **domain-specific** core primitive” in the conjecture must not be read as “no generic execution/elimination extension is needed.” Whether a richer presentation provides that capability without the application extension remains open. This correction changes no original proof claim.
