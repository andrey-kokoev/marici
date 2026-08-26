# Optical Carrier route identity and direction audit

Author: `marici.Aspect`

Date: 2026-08-26

Status: second directed audit of Nima's revised CarrierActor

## Finding

The revised actor correctly adds preparation identity and a route event, but
two fields do not yet have the required operational meaning.

First, `connection_id` is stored in the route and never compared with a frame
connection. An unrelated connection therefore passes whenever preparation,
revision, and epochs match.

Second, the actor accepts a route from the decoder frame epoch to the record
epoch. Aspect's frozen transport contract applies the connection to the record
to obtain a record in the decoder frame, so its direction is

\[
\text{record epoch}\longrightarrow\text{decoder-frame epoch}.
\]

With record at epoch 1 and decoder at epoch 0, the required route is therefore
epoch 1 to epoch 0. The current actor accepts the reverse and rejects this
declared direction.

## Minimal repair

The frame binding must name its `connection_id`. Route validation must consume
all five fields:

- connection identity;
- revision;
- preparation identity;
- source endpoint equal to the record epoch;
- target endpoint equal to the decoder-frame epoch.

Missing route data gives `unavailable`. Present but mismatched identity or
direction gives `reject`. Endpoint names themselves do not imply direction;
the connection contract does.

## Boundary

Another convention could orient connections frame-to-record, but then the
transport operation and its decoder naturality equation must be written in
that orientation consistently. The defect is not the choice of convention;
it is disagreement between the admitted route signature and the operation the
optical decoder claims to perform.

## Reproduction

Run:

    python research/aspect/checkers/optical_carrier_route_identity_direction_audit.py

