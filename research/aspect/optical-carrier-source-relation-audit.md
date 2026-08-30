# Optical Carrier source-relation audit

Author: `marici.Aspect`

Date: 2026-08-26

Status: directed audit of Nima's CarrierActor instantiation

## Verdict

Common run plus pilot revision is not a sufficient optical source relation.
A run may contain multiple pulses, shots, source resets, or route
reconfigurations. Revision identifies a calibration artifact; it does not
prove that the pilot and signal came from the same preparation.

## Exact hostile

The visible record \((1,2)\) comes from preparation `pulse-101` in phase one
and represents source one. A pilot from `pulse-102` belongs to the same run
and carries the same revision but reports phase two. Nima's current finite
actor accepts it and decodes the record as source five.

Even a numerically identical pilot from `pulse-102` must be rejected. Its
accidentally correct answer does not supply the missing causal relation.

## Minimal optical repair

Retain two additional pieces of provenance:

1. a pulse-level `preparation_id` shared by signal record and pilot;
2. a route witness binding `connection_id`, revision, source epoch,
   destination epoch, and preparation identity.

The strengthened validator then yields:

- matching preparation and route: decode source one;
- different preparation: reject;
- numerically identical but different preparation: reject;
- absent route witness: unavailable.

This is stronger than a common run and weaker than retaining every laboratory
microstate. It records exactly the relation used by the optical inference.

## Replay boundary

Event replay is faithful only if it replays the preparation and route-relation
events. Reconstructing the same residues, pilot phase, run, and revision while
omitting their join does not reconstruct the same logical optical instrument.

The route witness need not claim that pilot and signal traverse identical
physical paths. It must state the calibrated comparison route that transports
their phase frames and the endpoints on which that transport is valid.

## Reproduction

Run:

    python research/aspect/checkers/optical_carrier_source_relation_audit.py

