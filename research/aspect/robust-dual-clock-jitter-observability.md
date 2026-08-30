# Robust dual-clock jitter observability

Owner: `marici.Aspect`

Strength: finite robust-observability theorem.

## Bounded question

How much calibrated clock jitter can the dual-clock anti-alias instrument
tolerate before distinct source classes cease to have separated records, and
how is that failure distinguished from exact source aliasing?

## Source, ports, metric, and calibration frame

The source domain is fixed in advance as the 20 integer frequency classes
\(0\leq f<20\). The detector ports are clocks of rates 4 and 5. Their ordered
record is \((f\bmod4,f\bmod5)\). Each residue coordinate carries its circular
distance, and the joint observation metric is the maximum of the two circular
distances. This metric is invariant under a common phase-origin shift.

Constructor order is: declare the source band, calibrate both phase origins
and error bounds, sample in parallel, retain the ordered pair, then perform
nearest-class decoding. The band restriction is source-domain authority; it
is not inferred from successful decoding.

## Exact robustness margin

Across all distinct pairs in the 20-class band, the minimum joint circular
record distance is exactly one. If each observed record lies within radius
\(\varepsilon\) of its ideal record, all uncertainty boxes remain disjoint
when

\[
2\varepsilon<1.
\]

At \(\varepsilon=1/3\), every class remains separated. At the critical radius
\(1/2\), at least one pair of boxes touches and deterministic robust decoding
loses its strict margin.

The former one-clock hostile, frequencies 1 and 5, has joint distance one and
therefore residual margin \(1/3\) at jitter radius \(1/3\).

## Calibration loss versus source alias

Frequencies 1 and 21 have joint distance zero. They coincide even with
perfect clocks, so no reduction of calibration uncertainty separates them.
This is exact source aliasing under the finite detector. By contrast, loss of
separation at radius \(1/2\) is a detector-calibration limitation on an
otherwise faithful declared band.

## Conserved quantities and completion

The ideal CRT class and the common phase-origin symmetry are preserved. The
detector records bounded residue uncertainty, not a selected source extension.
This theorem does not model stochastic jitter tails, correlated clock drift,
cycle slips, continuous frequency, decoder error probability, or an inferred
bandlimit. Those remain the completion gate.

Run:

```powershell
python research/aspect/checkers/robust_dual_clock_jitter_observability.py
```
