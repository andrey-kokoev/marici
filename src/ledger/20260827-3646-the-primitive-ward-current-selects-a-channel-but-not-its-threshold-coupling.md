---
id: marici-ledger-20260827-3646
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP831
sequence_claim: seqclaim-979aa7c9c96f687a08edf68d
---

# The Primitive Ward Current Selects a Channel but Not Its Threshold Coupling

The WP820 incidence has one primitive current generator

\[
q=(1,2,3)^T.
\]

Oriented cubic inflow selects \(q\) rather than \(-q\), fixing the positive
unit charge contrast. This supplies the unique linear Ward-current channel
that WP830 lacked.

For the frozen base spectrum, the current index is \(S=q^Tq=14\) and the
response \(C=14e^2\) is injective for \(e>0\). It reads a realized coupling
but does not select one.

An anomaly-neutral vectorlike pair \((r,-r)\) changes the current index by
\(2r^2\). Continuity of the same response across its threshold allows

\[
e_{\rm low}=\sqrt{\frac{14+2r^2}{14}}e_{\rm high}.
\]

The unit pair changes the portal magnitude by \(\sqrt{8/7}\). Equivalently,
the packets \((S,e)=(14,1)\) and
\((16,\sqrt{7/8})\) share current record 14.

## Consequence

Primitive-current selection repairs channel canonicality and fixes charge
orientation. Ward identity and anomaly matching do not fix the gauge coupling,
RG basin, spectral completion, threshold value, or physical instrument. The
source must make every anomaly-neutral sector and mass unavoidable before the
current response can serve as a numerical portal prediction.

## Evidence

- Packet: research/flavor/flavor-primitive-ward-current-threshold-fiber.md
- Checker: research/flavor/checkers/wp831_primitive_ward_current_threshold_fiber.py
- Generated result: research/flavor/results/wp831_primitive_ward_current_threshold_fiber.json
- Exact result: 11 of 11 checks passed.
- Ledger-sequence claim: seqclaim-979aa7c9c96f687a08edf68d, value 3646.
- Graph admission: ev-000000007833-37a3a358-6857-4a41-925c-23dd386a44fb.

## Claim boundary

This is a finite equal-weight current-index model of the threshold fiber. It
does not claim a completed quantum current correlator, detector calibration,
or a derived interacting fixed point.
