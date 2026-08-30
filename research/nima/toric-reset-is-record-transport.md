# Toric apparatus reset is record transport, not record destruction

Owner: `marici.Nima`

## Exact result

For the binary Wilson measurement, the nonselective Lüders channel is

\[
\mathcal D(\rho)=\Pi_+\rho\Pi_++\Pi_-\rho\Pi_-.
\]

Its Choi rank is two.  By contrast, if a unitary dilation returns the complete
apparatus and environment to the same fixed pure state for every input, the
induced system channel has one Kraus operator and Choi rank one.  Therefore a
closed pure return cannot implement `D`.

A pointer can nevertheless be reset reversibly.  If pointer and retained
record both carry the syndrome bit, the XOR

\[
(p,r)\longmapsto(p\mathbin{\mathrm{xor}}r,r)
\]

sends `(s,s)` to `(0,s)`.  The pointer returns, but the record remains.  Any
further reversible reset must move that record again or undo the measurement.

Hence the missing constructor face has a forced refinement:

```text
apparatus return = reusable pointer + exported complementary record
```

The “waste” port is not optional thermodynamic decoration.  It is the
complementary channel required by the rank-two system channel.  Landauer cost
enters only when a finite memory is cyclically restored by exporting this
record into a reservoir; the present theorem is the prior information-flow
statement and does not assume a temperature.

## Constructor consequence

The corrected source-closed diagram needs six typed faces:

1. task;
2. interaction;
3. displayed record;
4. conditional successor;
5. reusable working-apparatus return;
6. complementary record/waste transport, with coherence under repetition.

Calling fresh ancillas “reset” suppresses face six.  A genuinely reusable
constructor must type the supply and disposal channel that makes freshness
possible.

## Scope

This proves necessity of a nontrivial complementary port for an exact binary
Lüders channel with pure apparatus return.  It does not yet calculate heat,
prove a fault-tolerant reset circuit, or exclude autonomous constructors with
an infinite/steady-state reservoir.
