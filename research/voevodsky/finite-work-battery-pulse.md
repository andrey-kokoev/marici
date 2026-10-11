# Retaining the old energy law exposes a finite-battery coherence cost

## Alternative tested

Instead of changing the old hold Hamiltonian in the correctable error sectors,
retain it and add a finite **work battery**. This is separate from the 21 battery
bits already storing the original bond pattern.

The actual prior physical-error sectors have hold energies

    H_(sA,sB) = J*I + delta*(sA*Z_A-sB*Z_B)/2,
    sA,sB in {+1,-1}, J=1/2, delta=1/4.

The signs are computed from the owning code's physical errors and logical Z,
not fitted. An even-sector transfer can change the old energy by +/-1/2.
Use work levels k/2 and pair |00,k> with |11,k-t>, where t is the hold-energy
difference in units of 1/2. Pair only levels that exist; unmatched boundary
states remain fixed. This defines an involution on the complete finite space.

Every pair has equal total energy. Consequently its spectral projector
Q_work=(I-F_work)/2 commutes with the unchanged hold plus work Hamiltonian.
The corresponding pulse conserves that total at every angle. All 256 source
error-sector pairs are checked for every tested battery size.

## Coherence is not free

Initialize a coherent work packet with equal amplitudes on levels 1,...,M,
inside the finite ladder 0,...,M+1. This packet supplies either one upward or
one downward step without reaching a forbidden endpoint.

For a fault already present and an unknown superposition of |00> and |11>, the
transfer produces oppositely shifted work states correlated with the logical
branches. Tracing out the battery reduces logical coherence unless those shifted
states coincide. The full joint state remains exactly reversible.

For the same actual physical fault halfway through the pulse, the exact target
fidelity after ideal syndrome interpretation is

    F_mid = 1 - 1/(2M).

The tested uniform packets give:

| M | Finite work levels | Mean ready work energy | Mid-pulse target fidelity |
|---:|---:|---:|---:|
| 1 | 3 | 1/2 | 1/2 |
| 2 | 4 | 3/4 | 3/4 |
| 4 | 6 | 5/4 | 7/8 |
| 8 | 10 | 9/4 | 15/16 |
| 16 | 18 | 17/4 | 31/32 |

These are model units and uniform-packet examples, not an optimal bound, a
universal fault threshold or a measured mass comparison.

For the preexisting-fault even superposition the tested fidelity is

    F_pre = (1 + max(M-2,0)/M)/2.

Its two work branches differ by two ladder steps. This distinguishes the two
fault histories instead of claiming one numerical error estimate covers both.

## Exact boundary and recovery controls

At the lowest work level, a transfer requiring battery energy cannot proceed;
the complete involution fixes that unmatched state. An energy reservoir cannot
be declared to work on every input while silently dropping its lower boundary.

Within this ladder-shift construction, exact pure logical transfer for all even
superpositions requires the two shifted work states to coincide up to phase.
A nonzero finite-support ladder state cannot be invariant under translation by
two levels: its nonzero support has endpoints. Thus finite packets leave residual
logical/work correlations or encounter boundaries. This is not a no-go for every
possible enlarged protocol or resource theory.

The complete inverse recovers all amplitudes when the battery and tested pulse
history are retained. That is joint reversibility, not automatic logical-only
correction of an unknown fault time. The energy-conserving pulse also does not
account for the work or bath of the injected physical fault and later physical
syndrome correction; those are distinct interactions.

## Verification

    python research/voevodsky/checkers/check_finite_work_battery_pulse.py

Fresh exact execution passed. Receipt: `results/finite_work_battery_pulse.json`.
It checks finite permutations, all source error-sector energy matches, half-pulse
and endpoint states, exact fidelities, full joint reversal and battery boundaries.
Source recovery and preceding error-transparent receipts are hash-bound.

## Subsequent packet and timing audit

`storage-branch-comparison.md` improves the midpoint benchmark with an exact sine
packet at unchanged capacity and mean energy, while retaining a different-input
tradeoff. The formulas above are pulse-benchmark fidelities; that follow-up also
checks free hold/work phases at total duration 8*pi and pulse strength 1/8,
confirming the midpoint values for this declared commensurate full schedule.
No arbitrary-time bath or clock calibration follows.

## Current choice, now explicit

There are two checked conditional routes:

1. Extend the hold law across error sectors using the recovery map: exact
   logical error transparency, but a new syndrome-resolved physical coupling.
2. Keep the old hold law and supply a finite coherent work battery: exact total
   pulse-energy conservation and joint recovery, but finite-resource logical
   coherence loss in these tests.

Neither route supplies a local autonomous device. The next meaningful step is
to specify which physical coupling/resource is admitted and then test the same
implementation's noise, work and recovery contract. Adding another abstract
clock or treating battery correlations as erased would not close that gate.
