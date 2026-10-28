# Native P/N/E replay: the productive binding test

## Result

One actual retained native packet was replayed through PN,NE and embedded into the existing FCC/esd7 layout. A separate window-construction implementation reproduces the target geometry and carried identity. Full coefficient recovery passes.

**The native transport works without central dualization. The literal binding to the quarter-rotated seven-presentation flag fails.** This is a counterexample to that proposed binding, not a rejection of all possible global transport laws.

## Actual cells and interfaces

The native sum-one barycentric lattice embeds isometrically by

    x -> (2,2,2,2)-x,

followed by the existing FCC chart (a,b,c,d)->(a+b,a+c,b+c). No site fitting is needed:

    P: T184 -- F538 --> N: T242 -- F569 --> E: T256.

The native constructor and the independent `createWindowConstruction` agree on all three cells, all supplied context marks, and the final identity-bearing exit. Both implement the same declared window contract; this is an independent implementation check, not an independently derived physical law.

Five distinct complex reference coefficients are retained. PN exchanges slots0/3; NE exchanges slots1/4. The endpoint full vector and active E readout agree with those independently composed reference swaps. Inverse replay recovers all five coefficients.

A hostile test deletes the two initially hidden coefficients. The final active E readout still passes, but full recovery fails. Endpoint appearance alone therefore would have missed actual information loss.

## Where the seven-view binding breaks

Read the native protocol without introducing another evolution operator:

| View | Native marks | Source cell |
|---|---|---|
| P first mark | C0 | V051 |
| P prefix | C0 M0 | E270 |
| P active window | C0 M0 C1 | F403 |
| P carrier with context | C0 M0 C1 M1 | T184 |
| N active window | M0 C1 M1 | F538 |
| Fixed N/E overlap | C1 M1 | E389 |
| E first mark | M1 | V077 |

This is a valid source incidence path with profile1,2,3,4,3,2,1. However, the existing quarter-rotated bridge with the same ascent ends

    ... T184, F538, E368, V072,

where E368 is M0 C1 and V072 is M0. The native reading ends

    ... T184, F538, E389, V077.

Thus agreement of the rank profile and central cell does not establish the handoff. The unique vertex permutation mapping the native ascending flag to its outgoing flag is

    (C0,M0,C1,M1) -> (M1,C1,M0,C0),

an involution, not a four-cycle. Reindexing the frame cannot change its order. This statement concerns this literal flag correspondence, not every possible contextual whole-state action.

## The E exit is not the central dual vertex

The independent constructor places the E exit at the center of T256. In embedded barycentric coordinates it is

    (5/2,7/4,3/2,5/4),

whereas the proposed dual vertex of T184 is

    (7/4,7/4,7/4,7/4).

Their squared distance in the inherited metric is7/8. The final flag mark V077 is also not that exit center. An E-leading window mark, an E carrier, and an E exit must remain distinct.

Moreover, the initial P reference already retains C2 outside T184. The15-chain-coefficient cellular duality has not been supplied with a source-defined encoder for the native five coefficient slots and their external contexts. It is not automatically the same retained state.

## Consequence for the next step

Keep the dual-cell result as a separate available geometric construction; do not promote it to the native P/E evolution. Do not add Fourier machinery merely to hide the mismatch.

The next meaningful target is a source-backed comparison between **the native order-two flag reversal and the global quarter-chart action**, including their contextual state and clock. If they act on different retained data, specify that action and its readout explicitly, then rerun this fixture. Here PN,NE are two native operations with zero phase increment, not seven temporal steps or28 stages.

## Reproduction

```sh
node research/strominger/checkers/check_native_fcc_end_to_end.mjs
```

**18 assertions pass**, including the assertions detecting the failed quarter-flag and central-dual-vertex identifications. [Receipt](results/native-fcc-end-to-end.json) contains all five-slot values, actual operation records, source cell/face IDs, seven views, independent exit and input hashes.

Scope: one fixed native seed and selected PN,NE word. Native source files are unchanged. See [earlier native28-stage audit](global-28-stage-pe-candidate-audit.md), [central flag extraction](esd7-seven-stage-handoff-v1.md), and [geometric duality construction](central-dual-cell-handoff-v1.md).
