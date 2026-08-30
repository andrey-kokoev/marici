# Faithful probes and relational references remain nonselective (WP80, move 9/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

The maximal declared probe algebra—masses, CKM moduli, and signed CP-odd
data—descends and is generically faithful on `physical16`. Its task is
`x -> (x,I(x))`: it preserves the substrate and appends a record. Algebraic
closure cannot turn this signature into preparation or stabilization.

A fixed generation-space reference gives values `1` and `73/25` on two
representatives of the same original orbit, so it fails original descent.
Transforming reference and state together restores descent on a new relational
substrate over the reference stabilizer groupoid. The source declares no
preparation, measurement, calibration, or degradation model for that ray. It
is a new readout experiment, not absolute-phase recovery or a selector of
original `physical16`.

Instrument completeness and constructor completeness are therefore
independent. The typed probe family separates physical points but does not
reduce them; the reference changes the experiment without a proper-image task.

Verification: `python
research/flavor/checkers/wp80_probe_reference_constructor_instruments.py`.
