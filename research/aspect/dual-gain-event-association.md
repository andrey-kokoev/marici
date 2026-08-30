# Event association and dead time in a dual-gain optical instrument

## Marginal recovery is not conditional attribution

Freeze two pulses: amplitude `2` under a reset condition and amplitude `4`
under a control condition. The high-gain channel clips both to one and raises
the same overflow flag. The low-gain channel records the multiset `{1/2,1}`.

Without same-pulse identifiers, two condition assignments remain compatible:

```text
reset -> 1/2, control -> 1
reset -> 1,   control -> 1/2.
```

The marginal amplitude distribution is recovered perfectly, yet the causal
comparison between reset and control is unidentified.

Attach an immutable event key at the source trigger and carry it through both
gain chains. Joining on that key restores the first assignment exactly. A
timestamp alone is sufficient only when clock offset, jitter, and event density
make the temporal match unique; otherwise the key needs a sequence identifier
or optical pilot code.

## Duplicated digitizers do not repair shared dead time

Freeze pulse times `(0,1,3)` and a nonparalyzable recovery time `2`. One front
end accepts times `(0,3)` and misses the pulse at one. Two digitizers attached
after that front end both receive `(0,3)`. Their agreement verifies downstream
electronics but cannot reveal the censored event.

An independently live low-gain front end records `(0,1,3)` in the frozen model.
The independence must occur before the dead-time locus. Splitting one already
avalanching detector output into two cables does not create it.

## Instrument contract

A physically faithful dual-gain record therefore needs:

- a common source event key;
- independently calibrated gain and latency for each channel;
- independence before saturation and recovery when dead-time repair is claimed;
- explicit missing-event and overflow states rather than silently absent rows.

This architecture separates marginal amplitude recovery, conditional
attribution, and event-completeness claims.

## Claim boundary

The checker assumes perfect event keys and deterministic nonparalyzable dead
time. Clock collisions, waveform pileup, paralyzable recovery, source-tap
back-action, and key loss remain outside the claim.

## Verification

```text
python research/aspect/checkers/check_dual_gain_event_association.py
```
