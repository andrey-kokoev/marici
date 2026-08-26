# Dual-clock coprime anti-alias instrument

Owner: `marici.Aspect`

Strength: finite sampling-quotient theorem.

## Bounded question

Can a second independently calibrated sampling clock resolve a known
single-clock alias, and what frequency ambiguity necessarily remains?

## Source, ports, and frame

The source is an integer frequency label restricted, for the positive theorem,
to the declared band \(0\leq f<20\). The two detector ports are sampling
clocks of rates 4 and 5. Their phase origins, timebase transfer, ordering, and
residue conventions are calibrated before comparison. The output record is

\[
f\longmapsto(f\bmod4, f\bmod5).
\]

Constructor order is source preparation, parallel sampling by both clocks,
ordered residue recording, then joint decoding. Combining already integrated
or unordered records would be a different detector.

## Exact anti-alias range

A rate-4 clock identifies frequencies 1 and 5. The rate-5 clock separates
them, so the joint record repairs Buzzard's explicit four-sample hostile.
Because 4 and 5 are coprime, the joint record is injective on the 20 declared
frequency classes. This is the exact finite anti-alias range.

The conserved datum is the frequency class modulo the joint period; individual
clock phase is not conserved under source frequency shifts. Both detector
ports are required for faithfulness on the declared band.

## Smallest surviving hostile

Frequencies 1 and 21 are distinct but have the same ordered residue pair.
Thus the joint detector remains periodic with period 20. Two coprime clocks
enlarge the faithful quotient; they do not make unrestricted integer frequency
readout injective.

## Completion gate

This finite theorem does not establish a continuum-frequency identity,
bandlimit, sampling jitter model, finite-time linewidth, phase-noise process,
Plancherel theorem, or reconstruction kernel. A physical anti-alias claim must
declare a source band and clock covariance. Without the band restriction,
the period-20 hostile remains.

Run:

```powershell
python research/aspect/checkers/dual_clock_coprime_antialias_instrument.py
```
