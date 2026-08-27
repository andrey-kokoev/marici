# Exact attaching data do not select an instrument

## Conjecture under attack

Exact coefficient- and orientation-typed attaching morphisms determine the
finite invariant object.  A stronger explanatory reading would say that this
object also determines its admissible observable readout.

That stronger claim is false.

## Minimal hostile carrier

Use the degree-seven attachment

\[
\mathbb Z\xrightarrow{\times7}\mathbb Z.
\]

Its invariant residue is

\[
C=\mathbb Z/7.
\]

There are seven linear readouts from this residue to a seven-valued record
module.  They are

\[
r_k(x)=kx,
\qquad k\in\mathbb F_7.
\]

All seven readouts have the same source object, attaching matrix, coefficient
system, and finite completion.  Their capabilities differ:

- \(r_0\) is completely blind;
- each \(r_k\) with \(k\neq0\) is faithful;
- the six faithful ports differ by a record-frame automorphism.

Therefore existence of the residue does not construct an observation port,
and existence of a seven-valued codomain does not prove faithfulness.

## Falsification verdict

The invariant object and the executable observation fiber are separate typed
data.  Exact source attachment determines the former, not the latter.

The smallest additional constructor is:

```text
ObservationPort
  source_object
  record_object
  pairing_or_map
  kernel
  executable_domain
  calibration_equivalence
  source_authority
```

The port must be proved faithful on the intended quotient.  It cannot be
selected merely because a faithful map exists algebraically.

## What the seven now counts

The number seven appears at three distinct types:

1. seven residue values in \(C\);
2. seven lifts in each fiber of \(\mathbb Z/49\to\mathbb Z/7\);
3. seven linear labelled readout maps \(C\to C\).

These cardinalities coincide because the same field \(\mathbb F_7\) controls
them.  They are not interchangeable objects.  In particular, six algebraic
faithful ports do not imply six executable instruments.

## Revised Deutschian conjecture

> Atomic constructors and exact attaching morphisms determine the invariant
> finite object.  A separately source-authorized instrument functor determines
> which distinctions become records.  Explanatory closure requires both, plus
> an explicit faithfulness or kernel theorem for the selected ports.

This version predicts a concrete failure mode: two sectors may share the same
invariant residue and disagree operationally because their authorized port
families have different joint kernels.
