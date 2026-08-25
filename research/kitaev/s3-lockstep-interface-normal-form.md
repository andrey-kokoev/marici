# CDFG has an exact lockstep interface normal form

Owner: `marici.Kitaev`

## Bounded question

Does the ideal four-port Wilson interaction ever require a mixed
native/binary interface configuration, or can all pointer interactions occur
inside one synchronized digit-exposed window?

## Exact normal form

The CDFG compiler contains 21 elementary Boolean-predicate-controlled
(Z_4^c) terms across ports (C,D,F,G). They are all diagonal in the same
three-bit data and four-pointer residue basis. The checker evaluates all

\[
2^3 4^4=2048
\]

basis states and compares compiler order, reverse order, predicate-grouped
order, and odd/even-grouped order. Every phase exponent agrees modulo four.

Thus all controlled-phase interactions can be grouped inside a synchronized
digit-exposed window. The actual circuit algebra supplies the lockstep
coherence law; ideal interaction ordering does not demand any of the fourteen
mixed configurations missing from a one-bit joint selector.

## Correction to the joint-selector gate

The 16-state/four-bit bound remains the correct gate for *independent* port
switching, but independence is not required by the ideal CDFG interaction
layer. The relevant ideal selector orbit is the two-state lockstep orbit.

## Remaining physical boundary

This reordering does not commute native (F_4) layers through controlled
(Z_4), construct a physical four-block switch, establish independent fault
domains, or derive joint switch cost. One common switch can still correlate
faults across all four pointers. The (83T)-equivalent interface allowance
therefore remains conditional.

## Falsifiers

- A declared CDFG interaction term is not diagonal in the common basis.
- Any tested ordering changes a phase exponent modulo four.
- A required intermediate operation forces a native (F_4) layer inside the
  interaction block.
- A physical interface contract invalidates synchronized switching.

## Artifacts

- Checker: `checkers/check_s3_lockstep_interface_normal_form.py`
- Result: `results/s3-lockstep-interface-normal-form.json`
- Result SHA256:
  `6822F9D9283E24292E442C8F2836829971EDDAED85A2FFD365C0A368DF19D265`
- Graph admission: `ev-000000003489-14d9df04-462e-431b-8cd1-65479299c759`
- Ledger: entry 2519, `seqclaim-f8df6cb678a0b7a9ccff44de`
