# Su-32 continuation: carrier constraints before filler synthesis

## Outcome

The proposed binding has a substantive whole-carrier obligation: retaining two independently variable packets does not enforce that they came from the same preparation.

For the fixed chart `reading:0:-1`, source `neutron:0,0,2,1`, binding `[0,0]`, the checked Boolean record domains are:

| Construction | Values in the finite record model |
|---|---:|
| Shared-E+ producer C | 8 |
| Shared-P+ producer D | 8 |
| Independent C/D pair | 64 |
| C/D pair consistent with one preparation | 16 |
| Independent complete preparation / C pair | 128 |
| Preparation / C pair satisfying their record equations | 16 |

The difference is not a counting convention. An explicit native counterexample has matching records within each producer but conflicting P+ values between the producers. It belongs to their raw native `Pi` carrier. It cannot belong to the constrained consumer carrier.

This is not a bug in `Pi` or `attachReference`: those operations permit independent operands. It is an obstruction to interpreting their unrestricted carriers as the smaller common-preparation family.

## Actual geometry, without inferred transfer

`build_su32_native_join_geometry.mjs` verifies the entire 51-cell, 104-shared-face incidence carrier against the geometry source and generates `agda/Su32JoinGeometry.agda`. Agda checks its finite owner table and the selected contacts using actual endpoint equalities.

The selected producers are:

- C = `proton:0,1,1,0`, comparing the two P directions at E+;
- D = `electron:0,0,0,0`, comparing the two E directions at P+.

Their consumer is the actual channel at `neutron:1,1,1,0` in the next chart, whose two reference cells are precisely C and D. The certificate retains the source-to-reference contacts, all four pair-channel incidences, both producer input pairs, and both producer-to-consumer faces. It also records both original five-cell incidence paths with their exact physical ports.

A `Contact` proves geometric shared-face incidence. It does **not** fill the fixture's `shared-interface-compatibility` witness, which remains null.

The declared periodic wire model has no internal edge connecting either C input port to the chosen C output port. The axes and wire identities differ. Both missing transfers are recorded. This is a bounded statement about that model, not an exclusion of every contextual or multiwire operation.

## Native simultaneous compatibility

`agda/Su32CoherentReferenceCarrier.agda` imports the checked geometry dictionary and instantiates the existing native shared-reader join.

Both producers are derived from the same four-record preparation, using its actual premise proofs. Their overlapping complete record types are P+ and E+. The corrected consumer is formed with the carrier constraint

\[
\operatorname{common}_C(c)=\operatorname{common}_D(d).
\]

This equality is part of every carrier value, not a fact checked only at the selected point. Its two native operand derivations remain recoverable by the existing join theorem.

The full preparation is retained with a second constraint:

\[
R=\operatorname{records}(\text{consumer}).
\]

Thus adding preparation context does not introduce another independently variable copy and silently assume agreement. The four physically named records are read through the checked reference dictionary. No payload transformation is introduced.

The formal results are whole-carrier compatibility, actual native derivations, and the counterexample to unconstrained `Pi` compatibility. The finite checker verifies the Boolean cardinalities separately. It is not a formal cardinality or normalization theorem for all native carriers, nor a proof of injectivity for arbitrary history-bearing readers.

These are simultaneous constraints on the chart's record domain. They do not construct the global physical assembly by chaining locally accepted steps.

## Three continuation notions must remain separate

### Literal reference attachment

The existing JavaScript `attachReference` stores C literally as one consumer payload and accepts an independent other payload. It accepts all 64 C/D combinations in this Boolean test, and `splitAttachment` recovers both. Of these, 48 fail common-preparation compatibility.

The earlier contextual-exchange wrapper restricts this API by reconstructing both inputs from one retained registry. Its 16-point family is therefore a restriction, not the full independent-payload domain.

### Native `Pi` packet construction

Native `Pi` similarly retains its input packages and derivations, but its current values vary independently. Matching selected values does not prove an equation throughout that carrier. The corrected native joins above supply the missing equations.

### Native all-outgoing attachment

The operation in `InternalSourceComparisons` has carrier `Out(v)` together with a loop at the **fixed preceding selected value**. When that preceding carrier is a set, its current values normalize to `Out(v)`, as established in `GeneratedReaderClassification` for its specified fragment.

For the actual charged output port probed here, the declared wire graph has exactly one outgoing edge: the shared-face edge to the N port. The corresponding fixed-input, set-valued all-outgoing carrier therefore has one current value. That is not the 16-value common-preparation family above.

Crucially, varying the retained input preparation varies the native package. A disjoint union over those packages must not be counted as the current carrier of one fixed package. Earlier histories remain retained even when the new current carrier has fewer alternatives.

This is exactly the caution in `native_filler_result.md`: recovery of old records does not make native attachment cancellable on filler admission.

## Reader and filler boundary

A physical-port-only reader has eight producer values, or sixteen common-preparation consumer values, over the same fixed port profile in this finite record model. It is not injective there.

The existing image-matching compiler remains valid for its proven generated-reader fragment. These findings neither invalidate that theorem nor instantiate it for Su-32. The remaining tasks are:

1. prove the relevant embedding or full fiber comparison theorem for the corrected packet reader, with its precise value/history boundary;
2. establish which continuation is source-admitted—not substitute literal attachment, native `Pi`, and native all-outgoing extension for one another;
3. supply the physical operation if different charged ports are to be related.

No native Su-32 filler, wire execution, period-return relation, or cancellation law is claimed. The existing native and JavaScript constructors are unchanged.

## Fresh verification

```sh
python research/strominger/checkers/check_su32_coherent_reference_carrier.py
```

This checks the generated geometry without rewriting it, runs a fresh safe Cubical Agda closure, checks two expected failures (inconsistent consumer and wrong geometric face port), and executes the finite carrier/port audit. It locks a conservative source inventory and records dependency warnings and receipt hashes.

Artifacts under `results/su32-native-join-binding-v1/`:

- `geometry.json`: full contact certificate, source hashes and missing wire transfers;
- `carrier-audit.json`: retained incompatible example, counts and actual outgoing edge;
- `verification.json`: fresh proof/check results and scope flags;
- `dependency-manifest.json`: conservative include-root source inventory.

Only the existing Cubical unsupported-indexed-match dependency warnings are allowed; repository source warnings are rejected.
