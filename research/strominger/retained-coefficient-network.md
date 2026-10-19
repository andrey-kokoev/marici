# Retained coefficient networks across cell assemblies

## Implemented scope

`checkers/retained_coefficient_network.py` supplies one exact network assembler for arbitrary finite stage dimensions over Q(sqrt(3),i). Inputs are distinct labelled port lists and sparse operators between consecutive stages, including the final return stage. No dimension-three assumption or particle-specific branch appears in the core.

It validates endpoints, retains every matrix coefficient and stage label, composes the return operator, computes rank, Hermiticity and idempotence, enumerates closed stage traversals, checks their exact trace sum, and reports cycle coverage and positivity. `recover` reconstructs the supplied port/operator data exactly. It does not infer coefficient operators from geometric cells.

## Native protocol regression

Using the existing exact stored operator manifests (not regenerated geometric seeds):

| Protocol | Stage supports | Transfers | Return rank | Closed cycles | Trace |
|---|---|---:|---:|---:|---:|
| Proton | 108, 432, 1296 | 1836 | 1 | 1296 | 1 |
| Electron | 16, 64, 64 | 144 | 2 | 128 | 2 |

Both return operators are Hermitian idempotents; every transfer belongs to a positive weighted closed cycle. Exact recovery compares entire input operators, not merely counts. These are shared-core regression tests against retained native manifests, not an arrow-only reconstruction of their physical carriers.

## A declared five-cell transport implementation

To test the machinery beyond the old input limit, declare one identical eight-coordinate coefficient fiber over each of the five tetrahedral boundary cells. Copy the existing electron L,G,N into each fiber. The actual retained geometric generators permute the cells; identity maps between the chosen fiber coordinate systems implement an invertible transport.

Every transport commutes with all three block-diagonal operators. Thus the five admitted diagonal cases now pass typed transport and coefficient-network assembly under this **explicit trivialization**. Each generator transport has 40 nonzero entries and is retained separately from the three-stage protocol.

The resulting direct-sum network has:

- stage supports 80, 320, 320;
- 720 protocol transfers on 120 stage-typed ports;
- return rank 10, 640 positive closed cycles and trace 10;
- exact recovery of all port/operator data.

This is not the missing physically justified spinor transport. Copying five fibers and choosing identity identifications is new model input; it is not forced by the metric or arrows. In particular the rank is ten, not the native logical doublet's rank two. The 720 number is consequently a measured declared extension, **not a prediction for any of the modified electrons**. Generator transport edges are separate and not folded into 720 without an explicit execution schedule.

The extension demonstrates that the previous software dimension limit can be removed without hiding representation choices. All five cases share its coefficient counts, while retaining distinct cell permutations.

## Prior-research correction

A subsequent search recovered existing intrinsic spin transports and conditional
rank-two five-cell extensions. See [recovered machinery](prior-five-cell-coefficient-clues.md).
The direct-sum control above is not the strongest existing model. The remaining
work is adapting that existing transport to the added generators and declaring
a global staged coefficient protocol, not deriving all five-cell transport anew.

## Remaining scientific interface (original assessment, superseded above)

A source-derived lift of the geometric action to spinor frames, its central sign/coherence and an admissible cross-cell selection are still needed to identify a five-cell electron protocol rather than an auxiliary bundle. The present identity-fiber transport is one explicit candidate and exposes its extra rank instead of silently treating five copies as one electron.

## Verification

```sh
python research/strominger/checkers/check_retained_coefficient_network.py
```

Ten checks passed: native counts/ranks, both exact recoveries, positive coverage, five-cell count/rank, bundle recovery, transport intertwining and invalid-endpoint/duplicate-port rejection. Generated packets and receipt: `research/strominger/results/retained-coefficient-network/`.

No shared scientific source or prior store was modified. The generic core and experiment remain owner-local pending agreement to promote reusable machinery to a shared library.
