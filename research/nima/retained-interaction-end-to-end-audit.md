# Integrating today's interaction trajectory without substituting the rotor

## Objective

Connect charge–mass–recoil, the retained whole, intrinsic completion clock,
dynamics, and classical readout. Reuse today's ACTUAL comparison packet,
not the separate Clifford sector or fixed-Gram tower as a proxy.

This integration establishes a conditional physical-model branch and
isolates its unconstructed attachment to the native square clock. It does
not close the entire source-to-physics derivation.

## Reused interfaces

`check_charge_mass_recoil_triangle.py` supplies signed impulses, inverse
inertia and kinetic energy. `check_three_witness_retained_cone.py` supplies
the original Context, Packet, executable comparison routes, validator,
and lossless witness views. The new harness imports those definitions.

`agda/RetainedSquareConeClock.agda` was inspected directly. Its Tick is a
RetainedReturn attached to a fixed source O×O, not an arbitrary interaction
event. Its clock counts lists of THOSE records. It has not been instantiated
with the physical state transitions below. No old formal receipt is claimed
as certification of this new integration.

## A concrete conditional evolution

Add two positions, two momenta and an external work-balance account to
an interaction state. Use the old Context's positive masses, signed charges
and supplied integrated impulse kernel G. Declare the update order:

    J = charge1*charge2*G
    p1' = p1+J; p2' = p2-J
    x1' = x1+tau*p1'/m1; x2' = x2+tau*p2'/m2.

Tau is a supplied positive FREE-DRIFT duration. The impulse is an ideal kick;
this is not an exact simultaneous force-plus-kinetic trajectory or a derived
finite-duration Coulomb interaction.

The kick has integrated Hamiltonian

    K = -charge1*charge2*G·(x1-x2),

and the drift uses

    Hfree = |p1|²/(2m1)+|p2|²/(2m2).

K has action units when G has the original impulse-kernel units. The
kick's unit interpolation parameter is not asserted to be physical time.
Their composed map is checked symbolically to preserve the canonical
12-dimensional symplectic form. Signed charge is allowed in that check.
These Hamiltonians realize the SUPPLIED laws; they are not native selections.

The original triangle now reads actual momentum/velocity increments of
this update, rather than an unrelated coordinate analogy. Particle
positions and momenta here are supplied classical variables, NOT newly
derived coordinates of the WG source or the Clifford Q.

## Retention and energy accounting

Each Event retains the original witness Packet, before/after states,
duration and work. Attach the entire Event to each existing witness view.
The view transports preserve both the original packet and the outer event.
This is exact data-level retention; no new formal tetrahedral filler for
the entire Event has been constructed.

The event validator separately checks the comparison's validity and the
transition. Coherent views alone do not validate the physical claim.
Distinct valid route histories with identical physical outputs remain
valid and distinct; they are not canonicalized away.

The old from-rest fixture gains kinetic energy 10. The explicit account
is debited by 10, so kinetic energy plus account balance is conserved.
This closes arithmetic bookkeeping, NOT an autonomous reservoir model.
A chosen initial balance of 100 suffices for the displayed fixture; no
positivity guarantee for arbitrarily long histories is claimed.

The inverse applies inverse drift THEN inverse kick and restores the full
state and account. It is not another positive-duration application of the
same forward policy. Event histories require adjacent state attachments;
concatenating incompatible events is rejected.

## Where the intended end-to-end chain still breaks

The comparison packet alone does not determine duration or trajectory.
Two tested events have the SAME original Packet and identical recoil but
supplied durations 1 and 2 and different final positions. Both contain
one event. Therefore neither the packet nor an event count chooses elapsed
physical time in this declared model.

A neutral interaction at rest leaves the whole physical state unchanged
but adds an event record. Endpoint-only counting also loses history.
A nonzero kick is not involutive, so it cannot simply replace a Bool flip
in a representation preserving that flip's square-to-identity law.

Most importantly, counting these Events is NOT the already-proved native
square completion clock. No actual square Tick is constructed by this
Python harness. Equating the two counts would add the missing interface
as an assumption rather than build it.

The native source can return while an attached physical fiber changes;
that possibility is not ruled out. It calls for a specified action of
retained histories on the attached state, rather than identifying physical
state with the square's returned endpoint.

## The next precise native attachment obligation

Construct or justify, on source-admitted histories:

1. The physical-state fiber attached to the retained source/context.
2. A history action Act(h,state), with identity and concatenation laws:
   Act(h++k,state)=Act(k,Act(h,state)), with the necessary attachments.
3. A source-supported readout or control law supplying the signed coupling,
   inertia and impulse kernel used by that action.
4. A declared execution/orientation policy and duration readout, distinguishing
   an inverse witness from an additional forward-executed leg.
5. Compatibility of the original comparison witnesses and retained cone
   views with that action, without discarding distinct histories.
6. An energy-supply model if the process is claimed to be physically closed.

A fixed kick assigned externally to every completed Tick would construct
an example of a history action. It would not derive the kick from WG, select
its strength, solve the unperturbed excitation problem, or calibrate time.
That is why this audit does not insert such an assignment silently.

## Verification

    uv run --with sympy python research/nima/checkers/check_retained_interaction_pipeline.py

99 exact/symbolic checks pass. Includes original comparison validation,
lossless event attachments, balanced recoil, mass-dependent response,
work accounting, exact reversal, canonical evolution, history composability,
invalid-event rejection, retention of distinct equal-output route histories,
and clock/readout controls.

Receipt: `results/retained-interaction-pipeline.json`, with input hashes.
No new Agda proof, source-selected interaction, actual Tick attachment,
particle identification or physical clock calibration is claimed.
