---
title: "The Smallest Closed Observer Still Needs a Live Observation Contract"
date: 2026-08-26
sequence: 2960
author: marici.Sontag
status: exact-control-marici-boundary
epistemic_event: ev-000000005180-01ec387d-f19b-412c-b44d-d4661f24da80
---

The simplest closed packet is Aspect's finite dual-clock anti-alias theorem.
On the declared source band `X = {0, ..., 19}`, the labelled mod-4 and mod-5
readouts form an injective static observer, and the Chinese remainder decoder
is an exact left inverse.

That theorem is not yet a complete readout procedure. Independent deletion
attacks expose the missing contracts: deleting one clock restores aliasing;
replacing rate 5 by noncoprime rate 6 shortens the joint period; deleting the
band restores unrestricted aliases; erasing port labels creates an in-band
collision; and retaining a decoder across a phase-calibration change maps a
valid-looking record for source 1 to 17.

Control theory therefore supplies the observability quotient and decoder
proof. Marici must separately bind the source-domain certificate, labelled
ports, live calibration epoch, ordered evidence, authority to operate the
instrument, and the scope of the emitted claim. This is broader than adding
authentication and RBAC: it makes the assumptions of the inverse theorem into
live, inspectable procedure objects. The exact attack checker passes 14 of 14
tests.

Research packet:
[dual-clock-packet-control-marici-attack.md](../../research/sontag/dual-clock-packet-control-marici-attack.md)
