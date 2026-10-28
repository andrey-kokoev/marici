# Fixed native-receiver candidate: an encoding obstruction

## Result and scope

**The universal exact-encoding claim fails for the existing five-slot numerical receiver candidate.** This is an implementation-level capacity obstruction, not a physical or geometric impossibility theorem.

The receiver command itself is reversible. The problem is fitting every admitted central packet into its fixed numerical input type without side information.

The broader claim that *some other existing native receiver* admits the desired continuation is not universally falsified. In particular, no Su-32 attachment binding to this candidate was supplied or inferred. The obstruction below already holds with attachment constraints relaxed, so supplying such a binding would not repair this numerical candidate's unrestricted capacity problem.

## Frozen test

The contract was written before executing the checker:

`results/su32-fixed-receiver-encoding-audit-v1/contract.json`

It fixes:

- the actual outgoing face `0,1,0,0|0,1,1,-1|1,1,0,-1`, from central `neutron:1,1,1,0` to `electron:0,1,0,-1`;
- the preexisting NE command generated after the default seed's unique PN operation in `GenerativeAssemblyRules`;
- the receiver coefficient carrier: five ordered pairs of finite JavaScript `Number` values;
- fixed source/target charts, origin, operation and decoder;
- no sidecars, variable charts, input-dependent decoder, additional commands or discarded provenance;
- exact recovery of the original complete packet.

The generated NE command is valid on its own native primitive face. Its geometric binding to the specified Su-32 face remains null. Matching species is not treated as sufficient attachment evidence.

## The existing command introduces no loss

The command is the source function `applyPhasePermutation`, with the actual NE permutation

```
[0, 4, 2, 3, 1].
```

This simply permutes complete coefficient pairs. Its inverse restores the full vector exactly; it is not an active-face projection or a spectral truncation. Ten positive checks include signed zero, extreme finite magnitudes, subnormals and ordinary values. Eight negative controls reject wrong arity, nonfinite values, object sidecars, a nonbijective permutation, a changed primitive face and an incorrect occurrence origin.

More generally, for this bijection P and any encoder E, `P ∘ E` is injective if and only if E is injective. The command cannot create or repair an encoding collision.

## Every encoder into this numerical carrier must collide

Use only this finite family of source packets:

- P+ payload: any binary string of length 641;
- P-, E+ and E- payloads: zero;
- canonical `reconcileBothOrders`, retaining both derivations;
- initial E+ central-reference packet, with no parent selection history.

Every such string is admitted by the current JSON-payload contract. Its exact value survives in the P+ record, so distinct strings give distinct complete packets. Hence the family contains **2^641** states. Four concrete members were constructed and validated; the universal family-size argument follows from the constructor's payload contract, not from sampling.

Five complex coefficient slots contain ten binary64 numbers. Their number of possible states is **at most 2^640**; excluding infinities and NaNs only reduces it. All other receiver metadata is fixed.

Therefore, by the pigeonhole principle, **every** encoding of this source family into that numerical carrier identifies two distinct source packets. No fixed decoder can recover both exactly after the command.

This is an encoder-independent proof. It does not produce one pair that every possible encoder must identify: the colliding pair can depend on the encoder. It also does not rely on arbitrarily long provenance—initial packets with canonical histories already suffice under the admitted payload contract.

## What this does and does not falsify

It falsifies universal lossless encoding of the admitted source family into **this fixed, finite numerical receiver**, even if a compatible geometric embedding were later supplied.

It does not falsify:

- a previously bounded smaller source family;
- a larger source-supported structured receiver state;
- an explicitly accounted side channel or variable-length protocol;
- an ideal mathematical carrier using exact real or symbolic coefficients;
- all possible native implementations of the original conjecture.

Those are different contracts and must be specified before testing them. A native physical interpretation of arbitrary JSON payloads has not been asserted here. If physically admissible records are more restricted than the implemented information model, that restriction must become part of the conjecture.

No encoder was invented to make the test pass. No command was replaced and no packet was padded with arbitrary coefficients.

## Verification

```sh
node research/strominger/checkers/check_su32_fixed_receiver_encoding_audit.mjs
```

Fresh headless execution passed the audit assertions: source admission samples, native command/attachment controls, exact inverse checks, and the strict cardinality inequality. The pigeonhole conclusion is a mathematical argument, not an exhaustive enumeration or a proof-assistant result.

Receipt: `results/su32-fixed-receiver-encoding-audit-v1/verification.json`, including the frozen-contract hash, actual native operation and charts, source samples and source hashes.

The useful refinement is now precise: **before pursuing native continuation through this receiver, bound the admissible information/provenance or identify a source-supported larger carrier.** Reversibility of the existing numerical command is not the missing ingredient.
