# Finite dead-time photodetection memory instrument

Owner: `marici.Aspect`

## Bounded question

How does the finite lossy destructive counter change when the detector has an
explicit ready/dead memory state, and what is the smallest exact falsifier to
independent-bin photon counting?

## Source authority and typed ports

The joint state space is

`span{|0,R>,|1,R>,|0,D>,|1,D>}`,

where `R` and `D` are calibrated detector ready and dead states.  Each time
bin supplies at most one photon.  The optical number basis and detector-memory
basis are fixed before reading any click record.

In the ready sector, the detector retains the parent efficiency amplitudes:

- vacuum gives no click and stays ready;
- a photon clicks with amplitude `3/5`, is destroyed, and leaves the detector
  dead;
- a missed photon has loss amplitude `4/5`, is destroyed, and leaves the
  detector ready.

In the dead sector every input gives no click and is destroyed.  During that
bin the detector recovers with amplitude `3/5` or remains dead with amplitude
`4/5`.  Separate Kraus operators are used for the zero- and one-photon dead
inputs so their coherences are not manufactured by sharing an environment
label.

## Sequential quantum instrument

The `click` outcome contains the single ready-photon click Kraus operator.
The `no-click` outcome contains ready vacuum, ready photon loss, and the four
dead-sector recovery/stay operators.  Their exact completeness sum is the
identity on the four-dimensional joint space, so the outcome maps are
completely positive and their sum is trace preserving.

Source preparation between bins is a separate constructor.  It maps retained
vacuum to the declared next-bin optical input without resetting detector
memory.  Silently resetting `D` to `R` between bins replaces the instrument by
an independent trial model.

## Dead-time hostile

Prepare one photon in a ready detector.  A click has probability `9/25` and
leaves the detector dead.  Conditional on that click, prepare a second photon
immediately.  Its click probability is exactly zero.

An independent-bin model would instead assign two consecutive clicks
probability `(9/25)^2=81/625`.  The exact instrument assigns zero.  This is the
smallest history-dependent hostile.

The complementary record is also exact.  If the first photon is missed, with
probability `16/25`, the detector remains ready and the second photon clicks
with joint probability `144/625` for the sequence `no-click, click`.

## Recovery gap

After a registered click, insert one empty recovery bin.  The detector returns
to ready with probability `9/25`.  A photon in the following bin then clicks
with conditional probability `81/625` relative to the state immediately
after the original click.  Thus the observed click process is not iid; its
conditional intensity depends on the hidden memory state and the elapsed gap.

## Constructor order and phase frame

The order is input preparation, joint instrument, classical outcome record,
then next-bin preparation.  Detector memory is transported between bins even
when its state is not included in the public record.  The number detector has
no optical phase reference and continues to erase relative phase.

## Detector kernel and environment

A click/no-click sequence without the detector-memory port is a hidden-state
record.  Different ready/dead mixtures can predict different future clicks
while sharing the same present no-click outcome.  Access to the memory state
or a sufficiently long calibrated history is required for faithful prediction
on the declared finite model.

Total probability is conserved across Kraus outcomes.  Photon number is not:
every incident photon is destroyed into the detector or loss environment.

## Smallest additional hostiles

- reset the detector after every bin and obtain the false double-click weight
  `81/625`;
- identify no-click with ready, ignoring the dead no-click branch;
- use one recovery operator for both dead optical inputs and thereby create
  unsupported coherence;
- infer exact detector state from a single no-click record.

## Completion gate

The packet has two memory states, rational recovery amplitudes, one-bin dead
time, and no afterpulse.  It omits multiphoton pileup, dark counts, graded
recovery ages, timing jitter, afterpulsing, continuous time, stationarity, and
point-process convergence.  Those require a larger detector state and new
outcome maps.

Run
`python research/aspect/checkers/finite_dead_time_photodetection_memory_instrument.py`.
The result is
`research/aspect/results/finite_dead_time_photodetection_memory_instrument.json`.
