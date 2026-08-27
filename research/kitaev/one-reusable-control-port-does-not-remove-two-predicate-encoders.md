# One reusable control port does not remove two predicate encoders

Owner: `marici.Kitaev`

## Bounded question

Can the two conditional bus interactions required by the catalytic qutrit
compiler be reduced to one reusable hardware coupling?

## Verdict

Yes at the actuator-template level, but not at the information-incidence
level.

One fixed control-port-to-bus interaction can serve both predicates if each
predicate can be coherently encoded into that port, used, and uncomputed. The
two physical interaction laws then collapse to one. But the system still needs
two source-authorized predicate encoders, one for `P` and one for `Q`.

This is not bookkeeping. Coherent predicate encoding is precisely the missing
constructor that tells the common actuator which subspace of each source
system should control it. A classical scalar description of the predicate
does not supply that encoder.

## Reusable port theorem

Let `R=|1><1|` be the active projector of a two-level control port `C`, and let
the bus interaction be

\[
H_{CB}=R\otimes h_B,
\]

where the traceless part of `h_B` is nonzero.

For a source projector `P` on `S`, suppose there is a coherent encoder
`E_P` satisfying, for a ready port state,

\[
E_P(|\psi\rangle\otimes|0\rangle_C)
=
(I-P)|\psi\rangle\otimes|0\rangle_C
+
P|\psi\rangle\otimes|1\rangle_C.
\]

Then the sequence

```text
encode P into C
apply the C-to-bus interaction
uncompute the encoding
```

implements the corresponding `P`-conditioned bus evolution while returning
the control port to its ready state. The statement holds coherently on
superpositions across the two `P` sectors and after tensoring the source with
an arbitrary untouched reference.

The same hardware interaction serves `Q` by replacing `E_P` with `E_Q`.

Thus one actuator template plus two encoders realizes both marginal
incidences.

## Same-space conjugacy criterion

If the source predicate and hardware control projector act on one common
finite-dimensional space, a unitary routing operation `U` with

\[
UPU^*=R
\]

exists exactly when `P` and `R` have the same rank.

Equal rank is therefore the complete algebraic condition for reusing one
projector-conditioned interaction by local conjugation on a common space.

It is not the physical condition when the predicates live on different
subsystems. There one additionally needs a coherent route to the common port,
with bounded support, preserved superselection charge, and an exact return
map.

## Why this does not erase the two incidences

The encoder `E_P` contains the operator-valued distinction between `P` and
`I-P`. If only separate source and port operations are available, no such map
can be synthesized: separate operations cannot correlate the port with the
source predicate.

Likewise, knowing the scalar value of `P` on a prepared eigenstate does not
define `E_P` on an unknown superposition. The encoder must preserve the
off-diagonal blocks

\[
P\rho(I-P)
\]

as coherence between the two port branches. Measuring the predicate and then
classically driving the bus deletes those blocks.

For a task that uses only a classical mixture of predicate eigenstates, that
deletion may be harmless. It is not harmless in the present catalytic
commutator, where the flag begins in a coherent superposition and must be
recombined afterward.

The hardware reduction is consequently

```text
two conditional bus actuators
    -> one common port-to-bus actuator
       plus two coherent predicate encoders
```

It is not a reduction to one untyped operation.

## Classical and quantum predicates

If `Q` is certified to belong to an already decohered pointer algebra, its
encoder may be implemented by ordinary classical routing. That replacement is
valid only when no later step requires coherence between the `Q=0` and `Q=1`
branches.

In the sixth-root injection construction, the flag is prepared in a real
superposition and later measured in a complementary basis. It is therefore a
quantum control during the interaction. Calling it a classical bit before the
final record forms changes the instrument.

The distinction is temporal:

- before complementary recombination, `Q` is a coherent projector;
- after the record is irreversibly formed, its value may be treated as a
  classical pointer variable.

## Minimal source interface

The catalytic compiler can now be factored into four constructors:

1. a continuously controllable internal qutrit bus;
2. one non-scalar reusable port-to-bus coupling;
3. a coherent encoder for the anyonic predicate `P`;
4. a coherent encoder for the flag predicate `Q`.

If the two source systems share an authorized coherent routing network, the
same physical port and coupling can be reused sequentially. If they do not,
two spatial couplings remain necessary even though their local interaction
type is identical.

## Fault locality

Reusing one port introduces a common-mode fault locus. A persistent port-frame
error can corrupt both marginal interactions coherently and survive the ideal
group-commutator cancellation.

The fault audit must distinguish:

- encoder faults specific to `P`;
- encoder faults specific to `Q`;
- bus-control faults;
- common port-to-bus calibration faults;
- failure to reset or uncompute the shared port.

Redundant encoders do not diagnose a common actuator fault. Conversely,
duplicating the actuator does not certify that the two encoders represent the
intended predicates rather than a common displaced frame.

## Highest-information experiment

The best source-level test is to derive one coherent charge-to-port encoder
and inspect its action on an off-diagonal input, not merely on charge
eigenstates. The decisive witness is preservation of phase between the active
and inactive sectors through encode, interact, and uncompute.

Once that exists for `P`, the same port coupling can be retained while the
programme separately asks whether the flag encoder is native, synthesized, or
already classical only after an irreversible record.

## Falsifiers

- A unitary maps finite-dimensional projectors of unequal rank by conjugacy.
- Separate source-only and port-only gates create a source-port correlation.
- Measure-and-feed-forward preserves arbitrary coherence between predicate
  sectors.
- The sixth-root flag is already an irreversible classical record before its
  complementary-basis recombination.
- One common port coupling eliminates the need to specify how `P` and `Q` are
  encoded into that port.
- Reusing one actuator creates no possible common-mode fault channel.

## Claim boundary

This packet gives an algebraic and control-interface factorization. It does
not derive either predicate encoder from a `D(S3)` lattice operation, prove a
bounded-support route, or supply a fault-tolerant port reset.

The exact contribution is that two conditional interaction types can be
replaced by one reusable interaction template, but the two semantic incidence
maps remain indispensable. Hardware reuse is not constructor equivalence.

No build, checker, or Git operation was used.
