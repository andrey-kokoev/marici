# Source-detector gain-law gate: WP1239

## Question

Can a coherent Physical16 instrument acquire the source-detector gain?

## DPC resolution

- **Problem:** derive the source-to-Yukawa or source-to-detector gain in
  the threshold frame with absolute or interference-calibrated Physical16
  readout.
- **Bold conjecture:** background, absolute rate, and phase-flipped
  coherent difference acquire the gain.
- **Named rivals:** pure-rate confounder; gain-visibility kernel;
  reference/common-frame mismatch; stale epoch drift; partial coherent
  overlap; lossy overlap monitor.
- **Risky consequences:** pure rate has rank two while the coherent row
  raises rank to three; a reference row raises gain-visibility rank from
  three to four; common-frame transport raises rank to five; a live epoch
  anchor separates stale packets with wrong gain decode; overlap \(c\)
  multiplies \(D\); monitor loss \(\eta\) multiplies overlap \(H\).
- **Strongest falsification attempt:** each calibration row removes one
  exact collision, but no source-derived Physical16 process or gain value
  is supplied.
- **Exact residual:** one Physical16 coherent final-state process with
  independent reference visibility, common-frame live transport, cofinality
  or overlap monitor, null-complete accounting, and source provenance for
  \(g\).
- **Disposition:** accept a minimal conditional acquisition schema; reject
  any current source-detector gain law.

Checker: `research/flavor/checkers/wp1239_source_detector_gain_law_gate.py`

Result: `results/wp1239_source_detector_gain_law_gate.json`
