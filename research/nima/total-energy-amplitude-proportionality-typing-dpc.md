# Total-energy residue proportionality typing

## Problem

The previous cycle withdrew the claim that the frozen source supplies a normalized reverse arrow. A weaker residual conjecture says the explicit total-energy residue is at least proportional to a scattering amplitude.

## Bold conjecture

The three-site `E`-residue candidate is proportional to a flat-space scattering amplitude, with only scalar and orientation left undetermined.

## Named rivals

1. proportionality is meaningful before normalization;
2. the source contains a flat-space wavefunction but no scattering-amplitude object or common coefficient space, so proportionality is undefined;
3. the residue candidate is merely a twisted-period boundary object until an amplitude comparison is sourced.

## Risky consequences

A proportionality claim requires two typed objects in one coefficient category and a comparison map between them. The frozen source must contain an amplitude object distinct from the flat-space wavefunction used in the forward site-energy integral.

## Strongest falsification attempt and residual

The frozen source chain contains the flat-space wavefunction, its site-energy integral, the graph coefficient, the twisted-period presentation, and the explicit `E`-residue candidate. It does not contain:

- an independently normalized scattering-amplitude object;
- a common coefficient object containing both sides;
- a comparison map.

Execution `structured_command_execution:e_32940_1788308888383114200_3` verifies these missing typed objects. A flat-space wavefunction in the source of the forward integral cannot be silently retyped as a scattering amplitude in the codomain of a reverse residue. Therefore even the proportionality statement is undefined and is falsified as a typed claim.

## Disposition and residual conjecture

Only the `E`-residue candidate is established. Its amplitude interpretation is withdrawn. The remaining statement is presentation-level: the source integrand has a labelled simple total-energy pole whose residue can be computed as a twisted-period boundary object.

Reopening requires an independently sourced scattering amplitude, a common coefficient category, and an explicit comparison map. No weaker amplitude claim survives without those objects.

## Evidence

- `research/nima/checkers/check_total_energy_amplitude_proportionality_typing.py`
- `research/benincasa/three-site-keldysh-source-provenance-audit.md`
- `research/benincasa/cyclic_q_assembly_certificate.md`
- `research/nima/three-site-total-energy-reverse-arrow-dpc.md`
