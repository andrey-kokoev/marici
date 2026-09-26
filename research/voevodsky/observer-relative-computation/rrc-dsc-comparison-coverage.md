# Comparison bridge checkpoint: dependent solutions, not collapsed histories

## Checked transfer

`agda/ObserverRRCComparisonBridge.agda` translates each Boolean comparison Solution into a dependent pair of its actual boundary path and a recursively translated Term at the Complete endpoint determined by that path.

Encoding and decoding have both full-data roundtrips, giving an equivalence of Solution types for each fixed mode and pair of Boolean endpoints. The witness field is retained, not replaced by mere existence. The previous constructive decision procedure transfers both positive solutions and negative certificates: a purported translated solution can be decoded to contradict an original impossibility proof.

This relies on the signature-relative Term syntax extension, not on a claim that bare DSC supplies all comparison primitives.

## Non-collapse regression

An identity-rule application and a compare-rule application using identity equivalence and refl have exactly the same Complete endpoint. Their raw histories are nevertheless provably distinct: the rule-constructor discriminator returns different Boolean tags. Their recursive translations remain provably distinct by the decoding roundtrip.

Thus endpoint agreement does not justify raw-history equality. This does not say that no chosen interpreted semantics may compare those histories; it keeps such a comparison separate from their identity.

## Freshly inspected upstream boundary

`research/nima/agda/WholeHistoryComparisons.agda` defines Structural.Generated relative to a supplied Law family and its interpretation. Its five constructors are reflexive, invert, concatenate, law and congruence. Its soundness function interprets those derivations. Its explicit Completeness obligation quantifies over EACH semantic witness and asks for a generated derivation whose interpretation equals that witness.

The finite Solution equivalence alone does not transfer this entire Generated grammar or prove that Completeness condition. The subsequent checked transfer below now handles all five constructors. No semantic-import constructor was found; adding arbitrary semantic equalities as laws would change the admitted source theory. No Nima-owned file was edited and no owner adoption is asserted.

## Generated grammar and exact interpreted witnesses

`agda/ObserverRRCGeneratedBridge.agda` defines the translated comparison grammar over recursive Terms. Its law constructor retains the original Law evidence and explicitly encoded source-law boundaries. There is no constructor for importing arbitrary semantic equality.

`transfer` recursively handles all five upstream Structural.Generated constructors: reflexivity, inversion, concatenation, admitted law and rule congruence over all children. This is a signature- and law-relative construction, not an independent discovery of those laws.

The translated interpreter evaluates Terms by decoding and applying the supplied upstream Algebra. `sound` interprets translated derivations. Because encode/decode roundtrips are paths rather than assumed definitional equalities, its endpoint witnesses need transport.

`sound-square` proves EXACT interpreted-witness agreement as a dependent square along those boundary roundtrips. The law case uses a double-composition filler; inversion, concatenation and arbitrary dependent congruence are handled structurally. No set/proposition assumption or proof irrelevance is imposed on the algebra's carriers. Thus preservation is stronger than merely producing some path between the same endpoint values.

## Reflection and conditional completeness

`reflect` now recursively maps translated derivations back into the original Generated grammar at decoded boundaries. Its law case transports the original admitted law derivation along the inverse history roundtrips; it does not add any source law. `reflect-sound` proves equality of the actual interpreted witnesses, including that transport. These are comparison simulations in both directions, not a proved equivalence of derivation types: derivation-level inverse laws remain unproved.

`image-complete` assumes the upstream `G.Completeness` obligation and then constructs a translated derivation for EACH supplied semantic path on encoded inputs, together with equality of its soundness witness to that exact path. The proof transports the requested path to the source boundaries, invokes the assumed completeness witness, and uses sound-square plus injectivity of transport to recover equality at the translated boundaries. No proof irrelevance or set assumption is used.

This is conditional completeness on the encoded image, not an unconditional completeness theorem for any particular source theory. It does not manufacture the premise or assert that every source identity is generated.

## Active continuation

The relative bridge obligation is complete at the level of forward/reflected generated derivations and conditional exact-witness completeness. A separate source-instance obligation remains: choose an explicit Algebra/Law interpretation and establish, refute or delimit its Completeness premise. Existing Nima source-comparison work is relevant evidence, not a premise silently supplied by this bridge. Derivation-level roundtrips are also not claimed.

The existing dependent witness-synthesis branch is the next local construction priority. Do not claim arbitrary source identity completeness, relabel finite decision completeness as source-relative completeness, or quotient the demonstrated distinct raw histories.

## Verification

Fresh canonical safe Cubical Agda aggregate with --ignore-interfaces -Werror passes52 entries,195 source/checker files unchanged, and two rejected false-theorem controls in138.701 seconds. See `results/operational-checkpoint.json` and `results/agda-operational-checkpoint.log`. The standalone generated bridge also passes the fresh strict check: `results/agda-rrc-generated-bridge.log`.
