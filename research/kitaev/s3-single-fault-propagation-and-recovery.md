# Single-fault propagation and recovery typing

Owner: `marici.Kitaev`

Status: exact finite propagation census for explicit gates; primitive Weyl
pulse faults and a preferred decoder remain unresolved.

## Bounded question

How far can one fault spread through the explicit compilers, and which
recovery layer can see it?

## Holonomy compiler

The edge labels are controls and the six-level ancilla is the target of each
group-multiplication gate.  Exhaustive insertion of a nontrivial group error
at every circuit boundary shows:

- one edge fault changes at most that one data edge at the end;
- one ancilla fault changes no data edge;
- every tested ancilla fault leaves a non-`e` final ancilla and is therefore
  flagged by a clean-return check.

An edge fault can also leave a residual ancilla, depending on whether it
occurs between the matching compute/uncompute gates.  Recovery must not reuse
an unverified ancilla.

## Separator coordinate gate

The reversible gate

\[
R(g_0,g_3)=(g_0,g_0^{-1}g_3)
\]

is not fault-nonspreading.  A fault on its first input changes both output
registers; a fault on its second input changes one.  Therefore one physical
fault can become a weight-two data error.  Arbitrary correction of that event
requires code distance at least five, not merely a single-error-correcting
distance-three code.

## Classical and readout faults

All 24 combinations of one bit flip on one of the eight three-bit sector
records change the decoded label.  They require classical redundancy or
repeated measurement and are invisible to a local quantum syndrome decoder.

A random-branch bit flip changes the applied central unitary but does not
change the sector label.  It appears as a branch-law/control error, again not
as a local syndrome event.

## Recovery boundary

Single data-edge faults must be routed to a declared `D(S3)` syndrome decoder.
Neither the syndrome nor this propagation audit selects a preferred decoder.
Faults inside the unresolved primitive pulse words for block Weyl targets
cannot yet be propagated honestly.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_single_fault_propagation.py
```

The dependency-free checker exhausts 46,656 edge-fault paths, 11,664 ancilla-fault
paths, 36 relative-coordinate basis pairs, and 24 record-bit faults.  Eight
aggregate gates are declared.  Saved result:
`research/kitaev/results/s3-single-fault-propagation.json`.

Falsifiers include data spread from an ancilla-target fault, a clean final
ancilla after a tested nontrivial ancilla fault, coordinate-gate support other
than `(2,1)`, or a decoder theorem correcting arbitrary weight two below
distance five.
