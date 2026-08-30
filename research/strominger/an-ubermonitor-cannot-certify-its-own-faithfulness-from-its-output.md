# An Ubermonitor Cannot Certify Its Own Faithfulness from Its Output

## Indistinguishable worlds

Let \(U:X\to S\) be the sixteen-outcome ubermonitor on the frozen health
object. When healthy, it reports \(U(x)\). Allow a monitor fault that can emit an
arbitrary valid packet.

Choose two different health states \(x\ne y\). Compare:

```text
world A
  actual health: x
  ubermonitor: healthy
  packet: U(x), self_test_ok

world B
  actual health: y
  ubermonitor: faulty
  packet: U(x), self_test_ok
```

Every verifier whose input factors through the ubermonitor-controlled packet
receives identical data in the two worlds. It cannot certify that world A,
rather than world B, is actual.

Adding another self-test bit produced by the same monitor does not help. A fault
capable of emulating the syndrome can emulate that bit as well. Recursive
self-monitoring remains inside the same information boundary.

## No contradiction with relative termination

Entry 3738 proved that \(U\) is monic on the declared object \(X\). That theorem
assumed the map \(U\) itself. Enlarging the ontology to include arbitrary faults
of \(U\) changes the observation relation; it does not refute monicity on the
original domain.

The tower therefore terminates only after one of the following is declared:

- monitor failure is outside the current ontology;
- an independently rooted witness checks the underlying health state;
- a restricted fault model plus redundancy makes spoofing impossible;
- a source theorem establishes the monitor implementation without relying on
  its own output.

Each is an authority or model boundary, not another endogenous monitor rung.

## Authority-plane interpretation

The ubermonitor supplies observational closure over lower instruments. It
cannot supply its own authority root. That root must arrive transversely—from a
source construction, independent calibration locus, or explicit fault-trust
assumption.

This prevents an infinite regress without pretending the top monitor is
infallible:

```text
diagnostic descent terminates at a faithful ubermonitor
authority ascent terminates only at a declared independent source root
```

Conflating those two terminations is authority laundering.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/ubermonitor_self_certification_no_go_checks.py
```

The exact checker enumerates all 240 healthy-versus-spoofed distinct-state
pairs.
