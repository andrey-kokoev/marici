# Three-site total-energy reverse-arrow audit

## Problem

After separating singular conductor specialization, the residual conjecture says that the frozen three-site source supplies a generic total-energy residue map to an independently normalized flat-space amplitude.

## Bold conjecture

The frozen three-site source already supplies a normalized reverse arrow from the graph coefficient's leading total-energy residue to the flat-space amplitude.

## Named rivals

1. the source site-energy representation is invertible by total-energy residue;
2. the source supplies only the forward site-energy integral and no reverse normalization;
3. an explicit `1/E` factor defines a candidate residue but not its identification with an independently normalized amplitude.

## Risky consequences

The frozen source must declare the reverse map, its amplitude codomain, and normalization. A forward integral representation alone is insufficient.

## Strongest falsification attempt and residual

`research/benincasa/three-site-keldysh-source-provenance-audit.md` freezes the source arrows:

\[
\text{flat-space wavefunction}
\longrightarrow
\text{site-energy integral}
\longrightarrow
\text{graph coefficient}
\longrightarrow
\text{twisted-period presentation}.
\]

`research/benincasa/cyclic_q_assembly_certificate.md` additionally freezes the explicit total-energy denominator `q_G=E` in the three-site integral. Neither source object declares a reverse arrow from the `E` residue to an independently normalized amplitude.

Execution `structured_command_execution:e_32940_1788308684659044300_2` verifies that the directed source graph contains the forward path and no reverse path. Thus the bold claim that the frozen source already supplies the normalized residue map is falsified as a source-typing claim.

## Disposition and residual conjecture

The explicit simple `E` pole defines a candidate residue object. Calling it the flat-space amplitude requires an independently sourced amplitude codomain plus a normalization comparison. The residual conjecture is weaker: the candidate residue is proportional to a flat-space amplitude, with an undetermined scalar and orientation until that independent source is materialized.

The first missing typed object is an independently normalized low-point amplitude formula in conventions compatible with the three-site source. Reopening requires that formula and a coefficient comparison; further manipulation of the same `1/E` presentation cannot create the reverse arrow.

## Evidence

- `research/nima/checkers/check_three_site_total_energy_reverse_arrow.py`
- `research/benincasa/three-site-keldysh-source-provenance-audit.md`
- `research/benincasa/cyclic_q_assembly_certificate.md`
- `research/nima/total-energy-conductor-commutation-dpc.md`
