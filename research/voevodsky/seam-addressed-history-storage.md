# Addressed storage works on the coherent sector; history needs protection

## Result

The all-filled storage exchange has an explicit seam-addressed reversible
implementation. It uses the actual 21 seam projectors, the existing occupation
parameters, a 22-label history register and a finite 21-level battery ladder.
All 21 input branches preserve the coherent carrier and total bare energy at
every reachable stage. Reversing the schedule recovers the input exactly.

Two limitations are now tested rather than left implicit:

1. The seam-conditioned gates do not conserve the full bare Hamiltonian outside
   the prepared coherent sector. The prior globally N-controlled gate did.
2. An energy-neutral history phase error changes the recovered state while every
   bond remains occupied. Occupation protection is not coherent-memory protection.

## Addressed reversible sequence

Use physically orthonormal pointer bases. The earlier non-normalized record
coordinates are re-expressed with their inherited weights; no physical metric
or energy coefficient is changed.

First coherently record the one-hot address j by controlled modular addition
into the ready history register. On a superposition this entangles the record
and history; it is not measurement or cloning of an arbitrary quantum state.
The modular addition is defined for populated histories and has an exact inverse.

Then visit seams e=0,...,20. Skip the initially occupied seam recorded in history.
For every other seam, exchange

    |n_e=0, battery=k> <-> |n_e=1, battery=k+1>,
    k=0,...,19.

The remaining battery boundary states are fixed. History zero disables these
steps, so the empty ready input stays empty. Twenty active exchanges fill all
bonds. Battery levels are k/4, ending at five units with no overflow.

With the actual projector P_e, the corresponding carrier-controlled gate is

    G_e = (I-P_e) tensor F_e + P_e tensor I,

where F_e includes the history condition and the bit/battery exchange. Since
P_e is a metric-self-adjoint projector and F_e is an involution, G_e is a
metric-unitary involution. The existing generator pi*(I-G_e)/2 supplies its
positive spectral pulse; the schedule/timing is still declared.

Every P_e annihilates N, so every step fixes the coherent carrier. On that
sector a newly filled bond changes energy by epsilon-J=-1/4 while the battery
gains 1/4. Total bare energy stays 41/4 through the schedule, including during
an ideal interpolation within the equal-energy paired states.

Reading reverses seam order and then inverts the history addition. It restores
all amplitudes, the original one-hot occupations, ready history and empty
battery. The finite battery is an explicit storage degree of freedom, not a
reservoir with hidden negative or unbounded levels.

## What "addressed" does not establish

Each step refers to a specific geometric seam instead of the complete coherent
projector N. But the carrier is a 36-coordinate direct-sum field, not an already
derived lattice of microscopic tensor factors. Spatial locality, controller
hardware and signal propagation are not obtained merely by writing a seam index.
The shared history and battery also remain controller resources.

Moreover, on a general carrier state the other seam and native energies do not
commute with P_e. The checker forms the actual off-diagonal energy residual

    H_after*(I-P_e) - (I-P_e)*H_before.

All twenty active steps of the first input branch have a nonzero residual.
Every residual annihilates N on both sides. Thus energy matching is exact on
the prepared coherent sector, not globally. Off-sector noise requires an
additional energy-resolving implementation or explicit control accounting.
This does not invalidate the previous globally N-controlled construction;
it limits this more addressed replacement.

## History-noise control

The existing hold law gives all history labels equal energy. Apply a phase
flip to history label 1 in a retained superposition with all 21 amplitudes
nonzero. This preserves:

- every filled occupation;
- register energy 21/4;
- battery energy 5;
- the total norm and coherent carrier.

Nevertheless, inverse read returns one amplitude with the wrong sign. The
exact recovered-state fidelity in the retained weighted fixture is

    38646202671977891760133045941169 /
    38919360224794286695723746027121 < 1.

A known phase error can be undone. No automatic correction of an unknown error
has been constructed. Discarding a correlated environment would also not be
reversible on the retained system alone.

An isolated occupation flip from filled to empty costs J-epsilon=1/4 on the
coherent carrier when no battery compensates it. In contrast, the logical phase
error costs zero under the declared degenerate-history law. A bond gap therefore
does not furnish a protection gap for the stored information.

## Verification and next gate

    python research/voevodsky/checkers/check_seam_addressed_history_storage.py

Fresh exact execution passed: 38,808 pointer-step cases, all 21 complete branch
histories, finite battery boundaries, inverses, actual source energy residuals,
and the logical phase-error control. Receipt:
`results/seam_addressed_history_storage.json`.

The source snapshot and preceding storage receipt are hash-bound. No enormous
tensor matrix was numerically diagonalized. The general lift follows the
projector/involution identities and the explicit reversible maps above.

The next useful task is **history protection under a declared noise model**,
reusing prior quantum-memory work where available. A controller/latch and
microscopic locality remain separate tasks. Repeating the occupied-bond energy
calculation cannot resolve either issue. No particle lifetime, mass or isotope
binding/stability is inferred.
