# Triangle-wall filtered-basis cache conventions

## Scope

`triangle_wall_dual_rank --write-basis-cache` serializes the completed
length-three filtered basis and the tracked quadratic quotient basis.  The
cache accelerates repeated reductions against one frozen packet.  It does not
certify that a separately generated probe row retained every connection-image
label.

## Binary contract

The cache magic is `MRCBAS01`, schema version 1.  Its header freezes:

- field prime;
- ambient degree;
- column count;
- raw relation-row count;
- FNV-1a digest of the complete source packet;
- FNV-1a digest of the reducer source used to compile the binary;
- filtered-basis rank;
- quadratic-basis rank.

The body stores every filtered pivot row and every quadratic pivot row with
its tracked provenance.  Loading refuses an invalid magic, any header or
digest mismatch, duplicate/out-of-range pivots, or trailing bytes.

The current packet format does not independently encode `K_DEPTH` or
`Q_DEPTH`; those parameters are therefore protected indirectly by the full
packet digest rather than duplicated in the cache header.

## Commands

```text
triangle_wall_dual_rank PACKET --write-basis-cache CACHE PROBES
triangle_wall_dual_rank PACKET --load-basis-cache CACHE PROBES
```

The load command reads the packet header, validates the cache, skips basis
reconstruction, and reduces the supplied probes.

## Verification

On the frozen small packet, write and load modes produced identical probe
remainder and coordinate data.  Loading the cache against a distinct packet
failed with `basis-cache header mismatch`.

On the ambient-15, K-depth-4 packet:

```text
columns = 33600
raw rows = 59072
filtered rank = 65549
quadratic rank = 18
probe count = 26
nonzero remainders = 24
zero probe indices = 6, 19
cached replay = 0.498 seconds
```

The cached replay agrees semantically with the construction pass on every
probe.  This certifies the cache and reduction.  It does **not** certify the
upstream probe export: strict no-omission metadata for connection-image labels
is still required before the 24 remainders can support a finite-step descent
claim.

The labelled ambient-15 remainder profile is exported in
`triangle-wall-cofinal-target-ambient15-labelled-residuals.json`.

## Strict ambient-13 replay

The source-derived strict target census later identified ambient degree 13 as
the first complete K-depth-4 target.  Its cache has:

```text
columns = 27360
raw rows = 44280
filtered rank = 50607
quadratic rank = 18
strict transported probes = 26
nonzero remainders = 26
cached replay = 0.398 seconds
```

Construction and replay agree on all sparse remainder and coordinate rows.
The complete labelled packet is
`triangle-wall-cofinal-target-ambient13-labelled-residuals.json`.
