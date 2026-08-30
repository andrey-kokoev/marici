# Five-rail generalized Shor recovery

Owner: `marici.Kitaev`

Status: explicit bounded syndrome/recovery schedule; nonstabilizer gate sources
remain absent.

## Schedule

Measure each frozen stabilizer generator with a fresh generalized Shor cat.
A weight-`w` generator uses `w` cat rails; cat rail `i` contacts only data rail
`i`.  Verify adjacent cat differences before use and discard a rejected cat.
Repeat the complete four-generator syndrome three times and decode each
syndrome component by majority.  Apply the correction from the complete
component recovery table in the code-freeze result.

The checker exhausts every cat shift pattern.  For every cat length used and
for fields `F2` and `F3`, the only patterns passing all adjacent checks are
constant global shifts.  Those shifts preserve the uniform cat state.  A
nonglobal shift that could propagate distinct data errors is rejected.  Cat
phase or readout errors do not propagate through the chosen controlled-Pauli
orientation and one wrong syndrome sample is removed by the three-round
majority.

## Exact resources

The qubit generator weights are `(4,4,4,4)`:

- 48 cat--data contacts per recovery;
- 36 cat-verification checks;
- 48 fresh cat rails prepared.

The qutrit weights are `(5,5,5,4)`:

- 57 cat--data contacts;
- 45 verification checks;
- 57 fresh cat rails.

A six-level bus recovery therefore uses 105 cat--data contacts, 81 checks,
and 105 freshly prepared cat rails, with qubit/qutrit components schedulable
in parallel.  An eight-level label bus with three binary components uses 144
contacts, 108 checks, and 144 fresh cat rails.

These are consumed preparation counts; peak ancillary width can be reduced by
sequential generator measurement and is not equated with 105 or 144.

## Fault boundary

This is a one-error-correcting `1-EC` statement at the standard separated
boundaries:

- a fault-free recovery corrects one input error;
- with clean input, one recovery fault leaves at most one correctable rail
  error.

An existing input error together with a recovery fault is a two-location case
and is deferred to the malignant-pair audit.  The schedule makes recovery
explicit but does not prepare controlled-inversion or controlled-phase magic
states.

## Verification

Run:

```text
python research/kitaev/checkers/check_s3_five_rail_shor_recovery.py
```

Saved output:
`research/kitaev/results/s3-five-rail-shor-recovery.json`.
