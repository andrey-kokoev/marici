# Final source-to-instrument verdict for finite `D(S3)`

Owner: `marici.Kitaev`

Status: consolidated twelve-move finite audit; no commit or push authorized.

## Verdict first

The eight-dimensional center algebra and its 36-Kraus conditional expectation
are exact mathematical targets.  The explicitly enlarged control surface is
channel-sufficient at the group level: its Lie algebra has dimension 34,
containing all 28 projective block directions and a six-dimensional center
that separates all eight sectors.

The center-expectation **instrument is not physically established from the
frozen source**.  The native commuting `D(S3)` Hamiltonian does not supply the
noncentral element ports.  The enlarged ancilla gate contracts compile those
ports, but two further source gaps remain decisive: named timed primitive
pulse words for the block and central targets, and controlled central powers
for the record-producing phase-estimation dilation.  Fault tolerance is also
unproved.

This is not a global impossibility theorem.  With the explicitly listed
couplings, controlled-power interface, measurement/reset apparatus, calibrated
pulses, and recovery layer, the exact target instrument is conditionally
specified.

## Twelve-move disposition

| Move | Exact disposition |
|---|---|
| 1 | Native square, Hamiltonian, orientation, and source gates frozen. |
| 2 | Transposition port: exact conditional nine-gate ancilla compiler. |
| 3 | Three-cycle port: exact conditional nine-gate ancilla compiler. |
| 4 | `G/H` current: exact conditional thirteen-gate orbit compiler. |
| 5 | Compiled source Lie algebra: dimension 34, not 36. |
| 6 | Six-stage within-block target twirl exact; timed primitive words open. |
| 7 | Unique uniform eight-branch, fresh-three-bit dephasing target exact. |
| 8 | Vacuum, excitation leakage, transient, and fixed-point energy formulas exact. |
| 9 | Timing/amplitude/phase/weight formulas exact for declared error models. |
| 10 | Three-qubit/36-Kraus instrument target exact; controlled powers open. |
| 11 | Explicit-gate single-fault census exact; weight-two spread found. |
| 12 | Full-center physical record unproved on native source; conditional extended target frozen. |

## Accessible algebra hierarchy

\[
\underbrace{8}_{\text{center readout}}
\subset
\underbrace{34}_{\text{compiled source Lie algebra}}
\subset
\underbrace{36}_{\text{endpoint block algebra}}
\subset
\underbrace{256}_{\text{ambient Hermitian operators}}.
\]

The center expectation has image dimension eight and kernel dimension 248.
Its readout algebra is formally complete for sector weights.  A full physical
record of that algebra requires the unresolved controlled measurement
interface; the nonselective random-unitary channel alone emits no sector
record.

## Remaining source obligations

- finite named pulse words, amplitudes, and durations for every block Weyl
  target and for the central generator `Z`;
- controlled `U1,U2,U4`, not inferred from uncontrolled reachability;
- hardware preparation, verification/reset, Fourier gates, measurement, and
  classical redundancy;
- a fault-tolerant replacement or protection for the weight-two spreading
  coordinate gate;
- a declared `D(S3)` decoder and recovery theorem.

These are apparatus/typing failures, not missing finite-dimensional algebra.

## Completion evidence

Run:

```text
python research/kitaev/checkers/check_s3_source_to_instrument_audit.py
```

The checker reads twelve authoritative result packets, records their schemas
and SHA-256 digests, verifies every move disposition, and checks all 82 new
aggregate gates plus the `8/34/36/256` hierarchy.  Saved result:
`research/kitaev/results/s3-source-to-instrument-audit.json`.

Full checker regression and `pnpm run build` are required at closeout.

## Optionality-space delta and process calibration

The audit eliminated native-port availability, full 36-dimensional coherent
control, zero excitation leakage, automatic controlization, and blanket
single-fault nonspreading.  It opened exact ancilla compilation of both flux
ports, an orbit-Fourier compilation of the `G/H` current, a dimension-34
channel-sufficient source group, a unique three-bit dephasing law, and an
exact three-qubit record target.  Ten microscopic/channel maps were
constructed or composed; 82 aggregate tests are declared and passed before
the final regression.  Five source obligations remain above; there is no
unresolved algebra-dimension contradiction.

Post phase: excitement `9/10`, because the audit found a constructive route
and a precise physical boundary rather than a vague controllability claim;
confidence `9/10` in the finite conditional verdict; realized information
gain `10/10`.  Confounds are the fixed-point finite lattice, idealized exact
gates, and absence of a device noise model.  These are process observations,
not evidence.
