# Typed three-bit protocol for optimal eight-branch sector dephasing

Owner: `marici.Kitaev`

Status: exact finite randomized target protocol; timed microscopic synthesis
of the central generator remains unresolved.

## Bounded question

Can the sharp eight-branch dephasing theorem be written as an executable
classical-control protocol with an explicit random source and branch map?

Choose the reachable central target `Z` with sector eigenvalues, in
`(A,B,C,D,E,F,G,H)` order,

\[
(-8,1,2,3,6,7,20,5).
\]

Their residues modulo eight are

\[
(0,1,2,3,6,7,4,5),
\]

which are all distinct.  Prepare three fresh independent unbiased classical
bits and set

\[
k=b_0+2b_1+4b_2.
\]

Apply

\[
U_k=\exp\!\left(-\frac{2\pi i k}{8}Z\right)
\]

and discard the classical branch record.  Equivalently, conditionally apply
the three powers `U1,U2,U4` selected by the three bits.

Character orthogonality kills all 56 ordered cross-sector matrix units and
fixes every within-sector unit.  The uniform law is the unique exact branch
distribution.  Eight branches and three ideal random bits are therefore both
sharp.

## Source boundary

The dimension-34 source group contains `Z`, so every `U_k` is an exact
group-level reachable target.  The recorded rational coefficients express
`Z` in an exact computed center basis.  That basis is not yet resolved into
named finite words of gauge, flux, and orbit-current pulses.  The randomized
target protocol is explicit; calibrated microscopic pulse durations remain a
live obligation.

The random source must provide a fresh independent uniform three-bit record
per channel use.  Retaining or correlating the record changes the instrument,
and biased weights leave the Fourier residual quantified in the earlier
weight-error packet.

## Verification and falsifiers

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_s3_eight_branch_dephasing_protocol.py
```

The checker emits the complete eight-row branch table, tests all 64 sector
pairs, proves the unique uniform solution, and records the input result
digest.  Eight aggregate gates are declared.  Saved result:
`research/kitaev/results/s3-eight-branch-dephasing-protocol.json`.

Falsifiers are a residue collision, any nonzero cross-sector multiplier,
nonunique exact branch weights, a protocol with fewer than eight branches,
or failure to supply fresh independent unbiased bits.  Primitive timed-pulse
completion is falsified until named finite source words are derived.
