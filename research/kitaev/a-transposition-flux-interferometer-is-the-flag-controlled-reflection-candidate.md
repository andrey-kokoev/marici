# A transposition-flux interferometer is the flag controlled-reflection candidate

Owner: `marici.Kitaev`

## Bounded question

What is the smallest source-native extended-ribbon candidate for the coherent
controlled reflection of the four-anyon `A_F/B_F` fusion flag?

## Verdict

Use a transposition-flux probe in two coherent path classes. One path does not
enclose the middle electric pair; the other loops once around it. On total
electric charge `A` the loop contributes `+1`, while on total charge `B` it
contributes `-1`. If the probe, path geometry, dynamical phase, and environment
all return cleanly, the relative operation is exactly a path-controlled flag
reflection.

This is the required extended-ribbon constructor at the categorical level. It
does not yet prove a lattice interferometer, protected path splitting, or
whole-instrument closure.

## Sign character supplies the reflection

Let `tau` be any transposition. The electric charges `A` and `B` carry the
trivial and sign representations of `S3`, so

\[
\rho_A(\tau)=1,
\qquad
\rho_B(\tau)=-1.
\]

The normalized Wilson response already pinned in the programme is

\[
W_A(\tau)=1,
\qquad
W_B(\tau)=-1.
\]

A transposition-flux worldline encircling an electric object therefore applies
the sign-character phase to its total electric charge. When the loop encloses
the two middle `C` anyons, topological fusion locality makes it depend on their
combined charge, not on a chosen tensor-factor basis.

Restricted to the protected vacuum-compatible channels,

\[
M_\tau
=
P_{A_F}-P_{B_F}
=
I-2P_{B_F}.
\]

This is the same flag reflection previously identified with middle electric
exchange, now realized by a charge-sensitive extended loop rather than by
exchanging the stored constituents.

## Coherent two-path construction

Let the path qubit have basis `0_path,1_path`. Prepare a probe-antiprobe pair
from vacuum. Route the probe along two coherent histories:

- path zero returns without enclosing the middle pair;
- path one encloses the middle pair once with transposition flux.

After returning both histories to the same typed endpoint, the ideal induced
operation on path and fusion flag is

\[
U_{path,F}
=
|0\rangle\langle0|\otimes I_F
+
|1\rangle\langle1|\otimes M_\tau.
\]

Thus

\[
U_{path,F}=C(I-2P_{B_F}).
\]

Hadamards before and after this operation on a ready path qubit coherently
encode the `A_F/B_F` predicate into the path output. A path phase followed by
uncomputation gives the flag reflection by kickback.

The laboratory command need not be coherently switched between two braid
words if the path degree of freedom is itself the coherent carrier and the
ribbon network implements both arms in one fixed device.

## Clean-return conditions

The categorical phase becomes a controlled unitary only when the full two-arm
instrument closes. The two histories must agree in every persistent port
except the declared monodromy:

1. the same probe species and centralizer state return;
2. probe and antiprobe annihilate to the same vacuum channel;
3. path wave packets end in the same recombination modes;
4. dynamical and geometric phases are equal or source-calibrated;
5. no local excitation, deformation, clock, or bath distinguishes the arms;
6. the middle-pair total charge and outer compensating channel are unchanged;
7. the path ancilla can be uncomputed after its bus interaction.

If the persistent environment states are `e_0,e_1`, the off-diagonal
controlled term is multiplied by

\[
\langle e_0|e_1\rangle.
\]

Magnitude below one turns the ideal controlled reflection into dephasing of
the path and fusion flag. A correct monodromy scalar alone does not prevent
that failure.

## Why a transposition probe is minimal for A/B

The distinction between `A` and `B` is the sign character. It is trivial on
the identity and on three-cycles and equals `-1` exactly on transpositions.
Therefore:

- an identity-flux loop cannot distinguish the channels;
- a three-cycle-flux loop cannot distinguish the channels;
- a transposition-flux loop gives the exact binary sign in one winding.

Within conjugacy-class-resolved flux probes, the transposition class is thus
necessary and sufficient for the `A/B` flag reflection.

No choice of one named transposition is required for the scalar sign response:
all three transpositions have the same sign. This makes the phase gauge
invariant even though a flux-resolved lattice implementation still carries a
relational frame and transport path.

## Relation to the qutrit bus

The path qubit now provides a coherent flag pointer. To make the flag control
the qutrit Weyl bus, insert the reusable path-to-bus interaction before
uncomputing the interferometer:

```text
split transposition probe paths
accumulate A/B monodromy
couple coherent path pointer to qutrit bus
reverse the probe loop and recombine
annihilate probe pair
```

This implements the required flag incidence if the path pointer represents
the predicate without residual entanglement after reversal.

The data-qutrit predicate still requires its own coherent encoder. The
transposition loop closes only the flag side.

## Support and time price

The enclosing path has diameter comparable to the separation and geometry of
the middle pair. Under bounded-range microscopic dynamics, the operation time
cannot remain independent of that diameter while producing an order-one
topological signal.

This respects the locality trilemma: the flag remains stored nonlocally, while
the actuator becomes an extended spacetime ribbon. The construction does not
turn the fusion flag into a single-site port.

## Fault classes

### Wrong flux class

A probe that loses transposition flux erases or changes the sign response.

### Arm leakage

An environment record of the enclosing arm dephases the flag-path coherence
even if both classical paths return.

### Incomplete enclosure

A path enclosing only one middle anyon probes a local charge relation rather
than the intended combined `A/B` channel and can leave the protected subspace.

### Extra winding

Because the desired phase is order two, even winding removes the reflection
and odd winding preserves it. The winding parity is a logical command
coordinate.

### Common frame fault

The sign character is constant across the transposition class, so conjugating
the chosen transposition does not change this particular phase. Frame faults
can still alter endpoint transport, centralizer state, or subsequent
noncentral bus couplings.

### Reset failure

A probe that fails to annihilate cleanly retains fusion-channel information
and converts a coherent actuator into a recorded instrument.

## Highest-information lattice audit

Construct two explicit ribbon histories on the frozen lattice and calculate
their complete compressed maps on the four-anyon vacuum space. The required
finite outputs are:

- identity for the nonenclosing arm;
- `P_A_F-P_B_F` for the enclosing arm;
- identical returned probe and environment states;
- explicit support diameter and operation depth;
- leakage blocks out of the protected space;
- the first fault whose accepted branch is not a unitary reflection.

This is a direct operator test, not a scalar Wilson expectation test.

## Falsifiers

- The sign representation assigns `+1` to a transposition.
- A three-cycle flux distinguishes `A` from `B` through the sign character.
- A transposition loop around the combined middle pair fails to act as
  `P_A_F-P_B_F` in the ideal ribbon category.
- Two arms with distinguishable returned environments are called a controlled
  unitary.
- Correct destructive `A/B` probabilities are promoted to coherent path
  encoding.
- The enclosing support is claimed to remain bounded while anyon separation
  grows.
- The data-qutrit vacuum predicate is declared encoded by this flag-only loop.
- A frozen lattice ribbon pair with all clean-return conditions has already
  been supplied.

## Claim boundary

This packet derives the minimal categorical interferometer and its exact
operator target from the pinned sign-character monodromy. It does not provide
the microscopic lattice paths, a beam splitter for topological probes, or a
fault-tolerant return protocol.

Its new contribution is constructive but conditional: one transposition-flux
probe in a coherent enclosing/nonenclosing path pair is the source-native
extended-ribbon candidate for the flag controlled reflection.

No build, checker, or Git operation was used.
