# Carrier-guide integration packet: exact QED Bell onset

## Why this belongs in the guide

The photon Bell calculation is a concrete successful test of the architecture

\[
\text{shared carrier/calculus}
+\text{sector coefficient object}
+\text{physical readout}
\longrightarrow\text{observable record}.
\]

The Carrier and Ward constraints construct a rank-two dimension-eight photon coefficient fiber, but do not select the QED ray in that fiber. The QED amplitude supplies the sector-specific coefficient object. The frozen Bell analyzer supplies the readout. Their typed pairing produces a new falsifiable record: a finite sub-threshold activation energy.

## Worked architecture block

```text
carrier/calculus:
    four-photon crossing + Ward fiber + helicity transport

coefficient object:
    exact massive-electron one-loop helicity amplitude
    (Phi1, Phi2, Phi5)

physical readout:
    frozen maximally-entangled input
    + fixed CHSH analyzers
    + normalized outgoing helicity pairing

record:
    |I(s, theta)|

derived threshold:
    s / m_e^2 = 0.4201576087546...
    sqrt(s) / m_e = 0.6481956562...
```

## Architectural lesson

The threshold is not stored in the Carrier and is not a universal coefficient. It appears only after a legitimate sector coefficient object is paired with an authorized physical readout. Conversely, it is not an arbitrary fit: the full exact amplitude confirms the onset predicted by two consecutive EFT jets.

This is the cleanest current example of the distinction between:

- structural possibility supplied by the Carrier;
- sector realization supplied by coefficients;
- experienced/observable multiplicity supplied by the readout;
- the final record produced by their pairing.

## Evidence

- Entries 1592, 1593, 1598, 1599, 1602, 1606, and 1609.
- `research/nima/check_exact_qed_bell_onset.py`
- `research/nima/check_exact_qed_bell_replication.py`
- `research/nima/results/exact-qed-bell-onset.json`
- `research/nima/results/exact-qed-bell-replication.json`

## Integration status

Prepared as a separate packet because `src/pages/guides/carrier-for-system-architects.astro` currently contains unrelated concurrent edits. Integrate after ownership is reconciled; do not overwrite the active guide work.
