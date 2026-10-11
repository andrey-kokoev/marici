# First typed compilation of the prepopulated three-arrow receiver

## Explicit bridge, not a numerical append

Consume the endpoint-complete fifteen-packet source and the freshly verified original proton protocol. Keep the marked face ABC.

For each primitive face vertex, choose the source triangle on ABC whose oriented outer arrow starts at that vertex:

```text
A → local/AB/x,y,z
B → local/BC/x,y,z
C → local/CA/x,y,z.
```

These are existing typed ports, not invented copies of the primitive vertices. If v_t is the triangle's generated mode, its scalar amplitude is

```text
s_t = v_t* x_t / (v_t* v_t).
```

The bridge uses those normalized amplitudes directly, with no extra phase factors. This is an explicit compilation choice for the previously missing channel bridge. It is not implied by the primitive endpoint graph alone.

Each extraction has three nonzero coefficients, giving nine transfers into three `receiver-source` ports. The three primitive receiver maps then supply three transfers into distinct labelled arrival ports at e. Keeping them distinct is necessary: summing three arrows into an ordinary scalar port would not test equal-image compatibility.

Finally, construct the two differences arrival A−arrival B and arrival A−arrival C, using four more transfers. The receiver output is arrival A together with those two defect values. Acceptance means both defects are zero.

## Exact comparable support count

| Retained support | Arrows |
|---|---:|
| Original proton protocol | 1836 |
| Actual local-mode amplitude extraction | 9 |
| Three primitive receiver legs | 3 |
| Two compatibility differences | 4 |
| **Total** | **1852** |

There are 116 typed coefficient ports. Every counted arrow has nonzero weight, and all source-target pairs are distinct. The count is for this complete fixed implementation and its explicit observable, not a universal cost for any three-arrow receiver.

The old arrows remain protected by the original return/pruning certificate. Removing each new transfer changes the retained receiver-output operator, even after accounting for the preceding local selection. The receiver observable therefore makes the new arrows deletion-essential without manufacturing feedback paths from the sink.

## What the compiled interaction actually does

On the proton's nonzero collective mode, all normalized local amplitudes agree. On ABC they are

```text
(s_A,s_B,s_C)=(z,z,z).
```

The receiver's fixed weights (1,ω²,ω) therefore produce

```text
(z,ω²z,ωz).
```

They are equal only when z=0. Thus this bridge does not provide a nonzero receiver compatible with the unchanged proton coherent state.

Conversely, the receiver accepts the relative face-amplitude pattern

```text
(z,ωz,ω²z),
```

whose three weighted arrivals equal z. The checker constructs this as an actual input at the selected source triangle ports. The old collective feedback annihilates it because 1+ω+ω²=0 and the three local modes have equal norm.

This is a concrete mismatch between the receiver character and the unchanged collective closure, not a failure to find typed ports or a counting ambiguity.

## Why this matters for the earlier character argument

The earlier three-channel pullback was the nontrivial cyclic character of a three-component channel vector. The present bridge supplies amplitudes of **three different already-selected local modes**. In the old coherent state those amplitudes carry the trivial relative character: they agree.

Each local mode already contains its internal cyclic phases. Transferring that character once more to the relationship between the three amplitudes is not automatically the same construction. The explicit bridge makes this distinction testable; it must not be hidden by inserting compensating phases to force acceptance.

## Status

We now have a compiled, source-bound network and an exact retained-support count: **1852**. It has a valid receiver readout and deletion witnesses. It is **not yet a nonzero jointly coherent H-1 realization**.

This compiler retains the old closed proton subsystem and adds the source's open receiver. It does not regenerate the collective closure on all fifteen primitive packets. The result shows exactly where that retained-subsystem choice conflicts with the receiver's selected character. A different bridge or a joint-generation rule would be a new, explicit construction to test—not a reason to label 1852 as an H-1 prediction.

## Verification

```text
python research/voevodsky/checkers/check_compiled_three_arrow_receiver.py
```

Fifteen exact checks pass. The self-contained `results/compiled_three_arrow_receiver_store.json` binds the original proton packet, the prepopulated source, bridge ports, all sixteen added coefficient arrows, and the observable. Replay reconstructs the recipe, and an honestly rehashed missing-transfer mutation is rejected.

`results/compiled_three_arrow_receiver.json` records the support count, coherent-state mismatch, accepted relative-mode witness, all new-arrow deletion tests, and source/checker hashes. Historical inputs remain unchanged.
