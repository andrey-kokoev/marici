# Boundary Hiding Is Not Boundary Erasure

## Question

When an interface is narrowed and later enlarged, has a latent port remained
inside the Marici object, or was it quotiented away and subsequently replaced
by newly chosen data?

## Open and restricted interfaces

Let an open Carrier state be a pair \((s,m)\), where \(s\) is the currently
accessible system coordinate and \(m\) is a memory or reference port. The
restricted presentation exposes only

\[
q(s,m)=s.
\]

There are two different operations that can produce this presentation.

**Boundary hiding** restricts the available Task alphabet while retaining the
full Carrier state \((s,m)\). A later enlargement can restore access because
the memory never left the object.

**Boundary erasure** replaces the Carrier by the quotient state \(s\). The
memory is no longer present. A later map back to pairs must choose a new value.

## No reopening after erasure

A candidate reopening section has the form

\[
j(s)=(s,d(s)).
\]

It satisfies \(qj=\operatorname{id}\), so closing again reproduces the visible
system state. But no section satisfies \(jq=\operatorname{id}\) on every open
state: the two states \((s,0)\) and \((s,1)\) have the same image under \(q\).

There are several valid sections, corresponding to different default memories.
Nothing in the restricted state selects one. “Reopening” the erased boundary
is therefore a preparation operation with a choice, not recovery.

## Congruence gate for forgetting

The quotient \(q\) is a valid predictive boundary map only if every retained
Task and record descends through it. For system-only operations this can hold.

Now admit the recall operation

\[
C(s,m)=(m,m).
\]

The open states \((0,0)\) and \((0,1)\) have equal restricted state, but their
visible states after recall are zero and one. Therefore no operation
\(\bar C\) on the quotient can satisfy

\[
qC=\bar Cq.
\]

The quotient kernel is not a constructor congruence for the enlarged Task
alphabet. Either the memory must have remained behind a hidden boundary or the
recall operation is not available.

## Boundary-change morphisms

A lawful interface contraction must carry a loss certificate:

- the exact ports hidden or erased;
- the Task operations and effects retained;
- proof that the quotient kernel is a congruence for that retained family;
- the shortest known operation that would invalidate the quotient if later
  admitted;
- whether a state-preserving lift remains physically available.

A lawful interface enlargement must carry an origin certificate for each new
port:

- retained latent state revealed without alteration;
- newly prepared state with an explicit constructor;
- state supplied by an external system with a lineage binding;
- or reconstructed state under a proved faithful recovery theorem.

These cases must not be conflated. A right inverse of forgetting is not proof
that forgotten physical state was recovered.

## Relation to Marici completion

Completion is relative to one declared interface, but Marici also needs lawful
maps between interfaces. These maps are generally not equivalences:

- hiding changes access while retaining realization state;
- erasure is a noninvertible predictive quotient;
- revelation restores access to retained state;
- preparation supplies a new port;
- faithful recovery requires an independent reconstruction theorem.

This is more precise than speaking about different object versions. The
objects are related by typed boundary morphisms with explicit loss and origin
data.

## Optical realization

Aspect's phase-reference example has exactly this form. Polarization-only
readout hides or erases a phase-reference mode. A later coherent recombiner is
the recall operation. If the reference mode was retained, opposite output-port
differences can be recovered. If it was physically discarded, supplying a new
local oscillator is a new preparation whose phase requires a lineage relation;
it is not recovery of the old phase.

## Deutschian pressure

The explanation must answer: what physical process kept the latent port, or
what physical process created its replacement? “The interface was reopened”
conceals that distinction. The no-section obstruction makes the question hard
to evade: lost fiber coordinates do not return from the quotient itself.

## Verification boundary

The dependency-free checker enumerates all sections of the two-bit projection.
It verifies that every section is a right inverse, none is a left inverse on
the open Carrier, system-only dynamics descends, and memory recall does not.
This is a finite deterministic boundary theorem, not a general recovery
theorem for stochastic or quantum processes.

