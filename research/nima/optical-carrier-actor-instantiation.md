# Optical CarrierActor instantiation

## Bounded objective

Instantiate the provenance-bearing Carrier DPC on Aspect's two-clock optical instrument. The model must distinguish:

- a record decoded in its bound frame;
- a stale frame repaired by a source-related pilot;
- a cross-run pilot splice with identical numerical calibration;
- deletion of the pilot revision;
- replay of the logical instrument after transient process loss.

This is an exact finite actor model. It is not a physical continuous-frequency or stochastic-drift model and does not assert that Elixir or the BEAM runtime supplies these guarantees automatically.

## Logical actor identity

The logical actor is not its transient process identifier. Its durable packet contains:

\[
\mathcal A
=
(I,E,S,P,M,B,\Pi),
\]

where:

- \(I\) is the supervised logical identity;
- \(E\) is the admitted event log;
- \(S\) is the folded internal state;
- \(P\) is the accepted command and event protocol;
- \(M\) is the pending message boundary;
- \(B\) is the calibration, pilot, and revision binding;
- \(\Pi\) is the readout projection.

The ordered residue pair is only \(\Pi(\mathcal A)\).

## Source events

The finite protocol admits:

1. `frame_bound(run, epoch, phase5, revision)`;
2. `record_received(run, epoch, residues)`;
3. `pilot_received(run, preparation, epoch, revision, residues)`;
4. `route_bound(connection, preparation, revision, from_epoch, to_epoch)`;
5. `decode_requested`.

The fold is deterministic. Replay of the same admitted log reconstructs the same logical state and verdict.

## Optical transition law

For source frequency \(n\) and modulo-five phase displacement \(p\), sampling gives

\[
r(n,p)=(n\bmod4,(n+p)\bmod5).
\]

Decoding in phase \(p\) gives

\[
d_p(a,b)=5a+16(b-p)\pmod{20}.
\]

The visible record \((1,2)\) can therefore mean source \(17\) in phase zero or source \(1\) in phase one.

## Command authority

`decode_requested` is admitted only in one of two cases:

1. the record epoch equals the bound frame epoch;
2. a pilot from the same source preparation carries a matching revision and an explicit route witness constructs transport from the record epoch into the decoder-frame epoch.

Numerical agreement of phase values is insufficient. A pilot from another run does not authorize transport. Neither does a pilot from another preparation in the same run, even when revision and numerical phase agree.

Deleting the pilot revision yields `transport_unavailable`, not phase zero and not literal epoch inequality.

## Ordered boundary

Before a valid pilot arrives, the mismatched record remains pending. It is not decoded provisionally.

Thus event order has an operative but typed effect:

- decode before the required pilot: unavailable;
- admit the related pilot, then decode: source one;
- admit an unrelated pilot, then decode: rejected splice.
- admit a related pilot without its route witness: transport unavailable.

The actor mailbox represents unresolved interaction rather than missing scalar data.

## Recovery

A transient process may disappear after any event. The supervisor restores the logical instrument by replaying the admitted event log under the same protocol version.

Recovery preserves identity only because the log, revision, run binding, and fold law are retained. A new process with the same residue pair but no event provenance is not the same logical instrument.

## Finite hostiles

### Value-only alias

Both source-frame pairs produce \((1,2)\). A record-only actor confidently returns the wrong source under the stale decoder.

### Cross-run pilot splice

A pilot from another run reports the correct numerical phase. The actor rejects it because the common source relationship is absent.

### Same-run preparation splice

Two pulses may share a run and pilot revision. A pilot from the wrong pulse is rejected even if its numerical phase agrees. Run identity is not a source relationship.

### Revision deletion

Removing the pilot revision makes transport unavailable. The actor may not guess a default phase.

### Premature decode

A decode command received before calibration closure cannot consume the pending record.

### Snapshot recovery

A snapshot containing only \((1,2)\) cannot reconstruct the run, epoch, pilot, or authority context and therefore cannot authorize decoding.

## Result

The optics machinery supports the actor interpretation precisely when the actor is event-sourced and protocol-typed. A bare process state or mailbox is insufficient.

The source relationship between signal and pilot is the crucial capability. It requires a shared preparation identifier and a route witness binding the frame's connection, revision, record epoch, decoder-frame epoch, and preparation. It converts a numerically ambiguous record into a lawful transported observation while rejecting observationally identical cross-run and cross-preparation splices.
