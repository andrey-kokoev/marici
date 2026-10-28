# Binding the 28-channel scheduler to actual native attachments

## Executed result

The channel scheduler now drives a real, native-certified three-cell assembly:

| Stage | Active native action | Result |
|---:|---|---|
| 1–2 | none | retain P seed |
| 3 | PN, coefficient pair 03 | attach N across its native face |
| 4 | none | retain P and N |
| 5 | NE, coefficient pair 14 | attach E across its native face |
| 6–7 | none | retain certified P/N/E assembly |
| 8–14 | dual returns | NE pullback at 10, PN pullback at 12 |

The native inspection reports one P, one N, one E, every contact witnessed, every packet able to reach the E exit, and `certifiedExit: true`. These are actual native bodies, not species labels assigned to channel slots.

## Explicit selection policy

The experimental binding maintains one current frontier and a retained occupied-cell set. At each forward matching:

1. ask the native engine for outgoing operations;
2. require a new, face-attached body;
3. require unchanged named coefficient references, present in the retained bank;
4. embed the source-defined coefficient permutation in that bank;
5. admit the operation only if every moved coefficient pair lies in the current matching;
6. fail on multiple eligible moves rather than introducing a fitted tie-breaker;
7. retain source state, coefficients, geometry and occurrence provenance.

This selects PN and NE at stages 3 and 5 without loading P/N/E layer words. The policy is a declared experiment, not a proof that the native rules uniquely require that schedule or the unchanged-reference restriction.

## Time alignment matters

Unlike the preceding passive communication atlas, the field now changes. A reference value sampled at stage 1 need not equal its value after the stage-3 PN swap. Naively gluing all 28 channel samples as if they were simultaneous fails the shared-reference check.

Each packet therefore carries a stage occurrence and the accumulated coefficient transport. Pulling all observations back to their common initial coefficient slots restores exact agreement. All eight values are recovered, including the three extra context values, which can remain unspecified symbols.

The native occurrence origin stays zero during this same-occurrence PN/NE chain. Fourteen scheduling occurrences do not become fourteen native phase advances or a Sigma return.

## Contravariant return is not reverse growth

Reverse stages use the actual adjoints of the embedded coefficient permutations. They obey the complex evaluation identity at every stage and for the total composition. A second algebraic inverse replay recovers the retained input.

This does not add an E-to-N operation to the native generator. It transports a dual observation back through the recorded forward computation. The three-cell assembly and its forward provenance remain retained.

## Verification and remaining boundary

All eight context frames yield the same attachment stages when the matching order is transported with the frame. Their actual bodies and full coefficient states agree by the source coordinate action.

**11 new exact check groups pass**, plus the existing 14 context checks and 11 channel checks.

The important limitation is explicit: the current policy rejects **NN phase continuation because it changes references**. It also uses only one live frontier, and E is terminal. Thus it generates one certified P-to-N-to-E chain, not the prescribed surface layers. A path word is not compared with a surface-layer word as if they were the same observable.

The next necessary construction is the time-indexed reference-changing NN port map and a multiple-frontier attachment rule. The present result supplies an actual native attachment and adjoint-return implementation to build on, not a finished growth law.

## Files

- Model: `aligned-native-growth-model.mjs`
- Checker: `checkers/check_aligned_native_growth.mjs`
- Trace and receipt: `results/aligned-native-growth-v1.json`
- Scheduler: [aligned-pair-channels-v1.md](aligned-pair-channels-v1.md)

Run:

```
node research/strominger/checkers/check_aligned_native_growth.mjs
```

The viewer and its layer definitions are unchanged.
