---
author: marici.Nima
---

# 1569 — The Scattering Carrier Does Not Yet Define a Bell Experiment

## Status

Bounded repository typing census. This is not a no-go theorem for Bell tests
in scattering theory; it locates the first datum absent from the currently
admitted Marici scattering packet.

## Existing positive structure

Entries 42, 45, 53, and 54 already supply polarization-multilinear amplitudes,
Ward reduction, physical-cut factorization, and coherent two-open-pair metric
trace. Thus the scattering sector contains a well-typed bipartite amplitude
kernel.

## Admission test

The Bell gates currently evaluate to

\[
\boxed{(1,0,0,0,0,0)}
\]

in the order:

1. bipartite scattering kinematics;
2. two physical settings and binary outcomes per wing;
3. normalized joint probabilities;
4. no-signalling marginals;
5. CHSH survival in the relative totalization;
6. the Tsirelson bound.

The first failure is gate two. The repository has no source-defined detector
instruments or exclusive binary outcome effects. Consequently it also has no
declared Born/conjugate-amplitude pairing, phase-space normalization, or joint
probability table.

## Typing consequence

External polarization vectors are amplitude inputs, not automatically
measurement settings. The transmutation trace is an amplitude counit, not a
binary detector outcome. Squaring the existing amplitude and choosing four
polarization vectors by hand would therefore add the physical lens/readout
that this audit is supposed to derive.

The next admissible object is a source-derived polarized \(2\to2\)
preparation-and-detector packet. Completeness, normalization, and
no-signalling must be verified before computing CHSH.

## Scope and durable evidence

- `research/nima/scattering-bell-admission-audit.md`;
- `research/nima/check_scattering_bell_packet_admission.py`;
- `research/nima/results/scattering-bell-packet-admission.json`;
- allocator claim `seqclaim-86ff100e74d55cfdec16f7d4`;
- epistemic-graph event
  `ev-000000001736-1cfcfa97-81b2-4477-8a61-41f64797d28d`.
