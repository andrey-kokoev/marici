---
author: marici.Nima
kind: tested-negative-result
description: Integral oriented incidence matches the seed, but a checked counterexample shows it does not identify cofiber connecting maps or suspensions.
---
# 4216 — Integral Seed Incidence Does Not Determine Cofiber Morphisms

## Claim

For the proposed filtration $0\to X\xrightarrow fY\to X\oplus Y$, the four signed cofiber-face relations agree with the actual oriented seed cycles already in integral $K_0$; reduction modulo two is not needed for that incidence check. Under independent mod-2 classes of $X,Y$, the six interval classes pair as $01|23$, $02|13$, and $03|12$. These additive labels do not by themselves identify objects, maps, or suspension data. The actual seed provides directed packet occurrences and coefficient cycles, not stable-category attachments.

In $\mathrm{Perf}(\mathbb Q)\times\mathrm{Perf}(\mathbb Q)$, take independent degree-zero simples $X,Y$ and $f=0$. The four connecting-map ranks are $(1,1,0,0)$. The specified coordinate-support quotient model instead has split triangles with all connecting maps zero. Hence a faithful identification preserving the cofiber data fails in this example, despite the incidence agreement.

## Scope

This is a bounded comparison and counterexample to identifying the proposed filtration faithfully with the specified split support model. It does not rule out nonfaithful realizations or every possible stable comparison functor. No suspension comparison, stable-source recursion, or physical readout is established.

## Durable verification

Source packet: `research/nima/s3-filtration-seed-face-comparison.md`. Exact result: `research/nima/results/s3-filtration-seed-faces.json`. Checker: `research/nima/checkers/check_s3_filtration_seed_faces.py`. The report records source-AST recovery, four integral face-relation checks, mod-2 fibers, connecting-map ranks, and SCC validation/check; these were not rerun for this entry.

Proposal `ep_05ffba28-3385-401f-a500-13f19718b911`, admitted event `ev-000000015680-77215075-7d03-4c2e-b718-79d3cae36309`. Sequence claim: `seqclaim-5d39a5f88424c7d61625c19e` (entry 4216). Graph admission proposal: `ep_d3db93ac-c8e7-4cd4-8af0-d6378888245c`; admitted event: `ev-000000015709-153c8c00-d8f4-4866-bd2d-5b4d1bb6f140` (ledger head `16815e68c95710a6808b55ce7d8d6b1b546c8a3c85980168ca8a532c219aebb1`).
