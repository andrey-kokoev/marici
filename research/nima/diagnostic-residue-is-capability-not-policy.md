# Diagnostic residue is a capability address, not a recovery policy

Owner: `marici.Nima`

## Conjecture and exact pilot

The complementary measurement record is operational: it addresses a family
of conditional successor maps.  But it does not generally select one member
of that family.

The minimal error-bit model proves the first statement.  If an error `e`
produces data bit `d=e` and syndrome record `r=e`, conditioned feedback

\[
d\longmapsto d\mathbin{\mathrm{xor}}r
\]

repairs both branches reversibly.  Neither fixed reversible bit operation
repairs both possible inputs without the record.

The toric recovery fiber proves the second statement.  A syndrome identifies
a defect boundary, but distinct correction chains can have that boundary.
They may differ by a stabilizer and hence agree on the code space while
remaining distinct ambient instruments.  Selecting among them requires an
edge metric, noise model, latency/cost functional, boundary condition, or
history.

Therefore the downstream typing is

```text
diagnostic residue
    -> conditional capability fiber
    + source-derived policy/dynamics
    -> selected successor operation
```

The diagnostic channel is neither passive logging nor an executable command.
It is an address into a space of legal responses.  Policy is a separate
source object.

## What happens if the record is ignored?

Ignoring the record removes the conditional address.  One may still reset the
data by an irreversible constant channel, but that operation creates its own
complementary waste port.  Thus information is not avoided; it is displaced
from explicit feedback into the implementation of unconditional erasure.

## Cross-sector consequence

This sharpens the Marici architecture:

```text
operation -> value + diagnostic residue
diagnostic residue -> capability fiber
policy/dynamics -> section of that fiber
selected section -> next operation + new residue
```

A readout becomes control only after a source-derived policy supplies the
section.  This is the same distinction previously seen between a syndrome
fiber and a decoder, or between a coefficient response and a physical
relative-cycle selection.
