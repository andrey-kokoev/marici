---
author: marici.Aspect
---

# 4169 — Complementary Probes and Instrument Faithfulness

## Question

What common conclusion is supported by the twenty-four executable simulations in the canonical Aspect instrument registry?

## Result

Instrument completeness depends more on complementary probe families and explicit hidden-port retention than on model complexity or repeated sampling of one readout. A nonfaithful detector map remains nonfaithful when sampled again under the same regime. A separately typed complementary row can instead remove its kernel on a declared source class.

The simulations exhibit this distinction in several forms:

- a selected dark channel does not distinguish coherent cancellation, imbalance, and loss, while a predeclared complementary tomography row makes the finite detector map invertible;
- one homodyne phase has a one-dimensional kernel, while two calibrated independent phases recover the declared coherent displacement;
- click/no-click records erase phase, integrated counts erase arrival order, and public dead-time records hide the detector's latent ready/dead state;
- system–environment dilation restores exact loss bookkeeping without making the retained-system observation faithful on the environment;
- coprime clocks separate the declared twenty alias classes, but the period-twenty hostile marks the exact regime boundary;
- Bell-context instruments are compatible within each context while rejecting one globally glued counterfactual carrier.

The resulting design rule is: identify the readout kernel first, then add a probe that separates that kernel on the declared quotient. More samples of the same row improve estimation but do not improve algebraic faithfulness.

## Scope

This entry states a finite-model synthesis. It does not claim unrestricted tomography, continuum completion, source-type identity, hardware execution, or a universal minimal probe family. Faithfulness is relative to each recorded assessment regime and quotient.

## Durable verification

- Registry contract: `research/aspect/contracts/instrument-registry.v1.json`
- Registry checker: `research/aspect/checkers/check_instrument_registry.py`
- Registry result: `research/aspect/results/instrument_registry.json`
- SCC profile checker: `research/aspect/checkers/check_instrument_profiles.py`
- SCC profile result: `research/aspect/results/instrument_profiles.json`
- Checked simulations: 24 of 24
- Checked SCC profiles: 24 of 24
- Ledger sequence claim: `seqclaim-ca10bc5dd44861d007ea1751`
- Epistemic graph event: `ev-000000010460-0b9d0e0f-7dc8-4f02-b08d-3fef4bbe044f`
