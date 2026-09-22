# Wheel relational cuts still admit a task-defeating tail

## Frozen DPC and outcome

The general suggestion of a finite separating constraint family was not yet
a decisive DPC. Before running this experiment, freeze the following family:

- N=1e6, existing finite evidence, combined kernel and midpoint task;
- nonnegative integer-supported mass with each atom at most log n;
- the unchanged cumulative Chebyshev envelope M;
- support restricted to integers coprime to 210 or pure powers of 2,3,5,7;
- interval capacities induced by these support and atom restrictions at
  cuts 1e6, 6e6, 7.8e6, 8.2e6, 11e6.

The support rule follows directly from the definition of the Mangoldt
function: if a prime power is divisible by one of 2,3,5,7, its base prime
must be that divisor. This adds no unproved distribution assumption.

**Outcome: REFUTED_FOR_FROZEN_FAMILY.** A jointly admissible infinite measure
has certified upper gain

    6.280451573475991e-193,

below the frozen threshold

    6.280452051525288e-193.

This is not a refutation of all finite relational-cut families. It closes
this specified small-sieve extension as a sufficient certification route.

## One common witness, rather than matching local summaries

Let n_j enumerate the integers coprime to 210 above L=6,000,000. Define

    B(log n_j) = min(M(log n_j), 15j),

with no earlier tail mass and constant cumulative mass between nodes.
Assign zero to every other atom, including the exceptional pure powers.

Only the 210-residue wheel is enumerated. It has 48 allowed residues and
maximum cyclic gap 10. No new primes beyond N are enumerated.

For n>L, log n>15. Between successive allowed nodes, the increase of M is
at most

    10 (2log(2)+1/L) < 15.

Both branches in the minimum are increasing with increments at most 15.
Therefore B is cumulative, respects the envelope, and each atom is at most
15<log n. The schedule is a single globally admitted measure. Its restrictions
satisfy every declared interval cut, including nonadjacent pairs; there is
no attempt to assemble unrelated local extremizers by overlap equality.

By the last allowed node before 11,000,000, the 15j branch exceeds M.
It stays above forever because capacity increments are strictly smaller
than 15. Thus the measure follows the discretized envelope on the entire
remaining infinite tail. These finite guards establish infinite admission.

## Quantitative witness bound

The owning single-valley proof supplies the exact relaxed minimum E_* and
its root u_*. For this schedule, the excess is bounded by

    M(u_*) [K(log L)-K(u_*)]
    + M(log H) [K(log H)-K(u_*)]
    + 10(2log(2)+1/L) [-K(log H)],

where H=11,000,000. The first term bounds premature mass before the valley,
the second missing mass up to H, and the last all infinite wheel-rounding
loss after catchup. Every term uses whole interval/rational upper bounds.

The excess is at most 2.1381866678077958e-8. After adding unchanged finite
pairing and other C contributions,

    C_at_this_measure <= 1.9721821535721633.

Exact rational upper-endpoint theta/H/L evaluation gives the below-threshold
gain reported above. No sharp optimization of this new family is needed:
a single admitted primal witness refutes universal threshold separation.

## Structural consequence

Dependency-complete representation and joint admission are necessary for
sound assembly, but do not make an evidence family decisive. Here we have
an explicit common witness satisfying even stronger, globally stated support
and atom rules than the displayed finite cuts. Rearranging those cuts or
changing their ownership cannot eliminate that witness.

The remaining issue is strength of the admitted semantics: this wheel still
allows artificial mass at many composite integers. More importantly, its
short gaps let the witness track the coarse envelope indefinitely. The
obstruction is not a failure to remember the local constraints or to compose
them correctly. It is that their globally admitted carrier remains too large.

This separates three routes that should not be conflated:

1. repairing an unsound or incomplete local assembly;
2. adding a constraint that changes the extremum;
3. excluding every task-defeating admitted witness.

The previous local-capacity result achieved (2); this experiment shows that
correct joint composition plus a small-sieve support restriction still does
not achieve (3). A stronger future family must exclude this explicit schedule,
not merely offer another summary of the same restrictions.

## Reproduction and limits

    uv run --with python-flint python research/grothendieck/checkers/check_prime_tail_relational_cut_dpc.py
    uv run --with python-flint python research/grothendieck/checkers/verify_prime_tail_relational_cut_dpc.py

Contract: `results/prime-tail-relational-cut-dpc-contract.json`.
Result: `results/prime-tail-relational-cut-dpc.json`.

The producer freshly replays the single-valley construction. The separate
verifier reconstructs the wheel and infinite-primal guards, checks cut
admission and exact gain arithmetic, checks bindings, and rejects corrupted
rate/gain fields. It does not independently reimplement the owning interval
kernel analysis. No actual prime realization, physical execution guarantee,
or source-infeasibility verdict follows. Existing calibration branches and
the actual-source task status are unchanged.
