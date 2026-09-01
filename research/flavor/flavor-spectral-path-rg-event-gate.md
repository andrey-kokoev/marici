# Spectral-path RG-event gate: WP1191

## Question

Can the spectral path be made into an RG trajectory with a selected event?

## DPC resolution

- **Conjecture:** coupling the spectral zero to a global RG heteroclinic
  selects the physical event.
- **Rivals:** juxtaposed index and scale; autonomous heteroclinic event;
  boundary-anchored heteroclinic; detector-calibrated event.
- **Risky consequences:** the logistic trajectory gives a positive transverse
  crossing at \(u=1/2\), a global open basin, and an autonomous translation
  modulus \(A\).
- **Falsification attempt:** \(A=1\) and \(A=2\) share endpoint regularity
  but produce different physical event scales; shifting the threshold
  criterion to \(3/4\) moves the event by \(\log3\).
- **Residual:** an independently fixed RG boundary or second physical event
  must anchor the heteroclinic phase.
- **Disposition:** construct the conditional RG spectral event; reject
  absolute event selection.

Checker: `research/flavor/checkers/wp1191_spectral_path_rg_event_gate.py`

Result: `results/wp1191_spectral_path_rg_event_gate.json`

The WP826 checker was also repaired to run without a symbolic-algebra
dependency while preserving its exact heteroclinic tests.
