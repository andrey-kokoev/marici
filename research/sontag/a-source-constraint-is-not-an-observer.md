# A Source Constraint Is Not an Observer

## Defect

The affine charge analysis correctly separates translation and reflection
characters, but the word *observer* can still hide two different control
roles. An equation such as

\[
L(q)=5
\]

may be either:

1. a source law restricting which states are admissible; or
2. an output map \(y=L(q)\), followed by a physical record \(y=5\).

These can have the same current fiber and different lawful continuations.
They are therefore not interchangeable parts of a Marici object.

## Exact affine hostile

Use Nima's affine family

\[
q(s,c)=s(3,2,0)+c(1,1,1),
\qquad
s\in\{-1,1\}.
\]

The sum output is

\[
L(q)=5s+3c.
\]

The fiber \(L(q)=5\) contains both

\[
(s,c)=(1,0)
\quad\hbox{and}\quad
(s,c)=(-1,10/3).
\]

Now compare two objects.

In the constrained object, that fiber is the admitted state space. A common
shift \(c\mapsto c+1\) exits the source law and is not an admitted
continuation.

In the observed object, the full affine family remains admitted. The record
\(L=5\) identifies a current fiber, but the same shift is a lawful
continuation and produces \(L=8\).

The objects agree on the current compatible states and disagree on the next
experiment. Equality of a solution set at one stage therefore does not imply
equality of capability witnesses.

## Orientation and lattice typing

The difference output

\[
D(q)=q_1-q_2=s
\]

is translation-invariant and reflection-odd. As an instrumented record it can
distinguish the two sheets. As a source law \(D=1\), it instead removes the
negative sheet from the domain. Again, the surviving set may coincide while
the counterfactual transition structure does not.

Charge-lattice typing is a third role. Restricting \(c\) to integers removes
the rational point \((-1,10/3)\), but it produces no record that distinguishes
that point. This is a reachability or admissibility restriction, not increased
observability. If the domain is enlarged back to rational charges, the second
sheet returns without any detector having failed.

## Control interpretation

Three structures must remain typed separately:

- **admissibility:** a subobject of states and transitions allowed by the
  source;
- **intervention:** a Task operation whose Carrier realization determines
  which continuations can actually be executed;
- **observation:** an output map plus an instrument and stable record.

An observed value forms a pullback of the output map along that record. A
source equation forms an admissible subobject. Those pullbacks can be
isomorphic as static sets while carrying different transition closure and
different counterfactual probes.

This sharpens the witness-span proposal. A capability witness must record not
only which Task and Carrier elements correspond, but whether a relation is a
law, an executable transformation, or a recorded effect. A bare compatibility
predicate erases that distinction.

## Consequence for minimality

Behavioral minimization may quotient states only by equality under every
admitted future record. It must not quotient a forbidden state as though an
observer had failed to distinguish it. Unreachable, inadmissible, and
unobservable are three different reasons a state may be absent from a current
record fiber.

## Verification boundary

The dependency-free checker enumerates the rational affine hostile. It verifies
the common current fiber, the different shift continuation, the independent
orientation character, and the fact that lattice restriction removes a state
without creating a distinguishing record.

This is a finite exact control criticism. It does not decide whether a concrete
Flavor anomaly relation is a source law, an instrumented output, or both. That
typing must come from its physical constructor.

