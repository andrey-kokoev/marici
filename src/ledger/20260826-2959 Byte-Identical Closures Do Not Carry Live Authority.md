---
title: "Byte-Identical Closures Do Not Carry Live Authority"
date: 2026-08-26
sequence: 2959
author: marici.Sontag
status: hard-to-vary-controlled-variation
epistemic_event: ev-000000005160-6503ced6-7de7-4203-bbb0-4cf85d41ae49
---

Two counterfactual worlds receive byte-identical closure packages with the
same code, captured data, schemas, request identity, fresh nonce state, and
physical target capability. In the live world the target epoch matches the
captured lease epoch and one protected effect executes. In the revoked world
the target epoch differs, so a conforming evaluator rejects the effect.

Pure computation remains identical. Copying the package repeatedly never
refreshes its standing. If live target observation is deleted and the captured
epoch is trusted, the stale package executes. The authority observer therefore
does unique counterfactual work.

This impossibility is architectural relative to a conforming evaluator; it is
not a claim that a rogue actuator outside the model is physically incapable of
the effect. The exact checker passes 11 of 11 tests.

Research packet:
[deutschian-live-authority-binding-variation.md](../../research/sontag/deutschian-live-authority-binding-variation.md)
