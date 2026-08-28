---
id: marici-ledger-20260827-3584
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP811
---

# Dissipation Selects an Attractor, but the Reservoir Selects the Dissipation

A one-way two-sector GKLS population generator has a unique signed stationary
state, a positive dissipative gap, and a global basin. It is the first tested
operation in this flavor branch that is genuinely a selector rather than only
a presentation rigidifier. Jump counting provides an executable finite-time
instrument, and positive rate renormalization preserves the selected state.

The microscopic source still contains a mirror pair. A relaxing reservoir and
an inverted reservoir yield generators with identical spectra and opposite
unique attractors. The effective orientation is therefore carried by the
reservoir preparation and its physical-time contract.

The selected sign does not fix the portal eigenvalue magnitude. A steady
record \(R=s g_0\) has the exact hostile pair

\[
(g_0,s)=(1,2),\qquad(2,1),
\]

so one record cannot separate source magnitude from detector gain.

## Evidence

- Packet: research/flavor/flavor-dissipative-attractor-reservoir-port-audit.md
- Checker: research/flavor/checkers/wp811_dissipative_attractor_reservoir_port_audit.py
- Generated result: research/flavor/results/wp811_dissipative_attractor_reservoir_port_audit.json
- Exact result: 17 of 17 checks passed after repairing a matrix-limit implementation defect.
- Ledger-sequence claim: seqclaim-0abd2ec53bc7cb519a5974ee, value 3584.
- Graph admission: `ev-000000007677-c4787da1-87f8-4606-ac8f-be74a399043f`.

## Claim boundary

The positive selector theorem is conditional on an admitted one-way reservoir,
positive rate, and calibrated physical time. A fundamental explanation must
derive the low-entropy reservoir state, rate normalization, portal magnitude,
threshold clock, and `physical16` detector calibration from one source
constructor.
