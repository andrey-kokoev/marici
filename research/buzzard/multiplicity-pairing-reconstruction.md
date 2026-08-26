# Multiplicity-two pairing reconstruction

Owner: `marici.Buzzard`

Source locator: `Four channels expose a multiplicity obstruction` and `Six
polarized probes are necessary and sufficient` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

A reflection-invariant four-channel pairing is represented in parity
coordinates by two symmetric rational `2 x 2` blocks. Each block has three
coefficients `(j11,j22,j12)`. Its energies on `(1,0)`, `(0,1)`, and `(1,1)`
are `j11`, `j22`, and `j11+j22+2*j12`.

Lean defines the polarization inverse and proves that the three-probe block
observation is injective. Applying it independently to the even and odd
multiplicity blocks proves that the six-probe observation is injective.

The hostile five-probe fixture omits the mixed even probe. The positive blocks
`diag(2,3)` and `[[2,1],[1,3]]` agree on both retained even basis energies and
share the complete odd block, but differ on the omitted mixed energy. Lean
proves strict positive-definiteness of both alternatives.

The exact fixtures `(2,3,7)` and `(4,2,4)` reconstruct off-diagonal
coefficients `1` and `-1` respectively.

## Type-system consequence

One scalar per parity sector is faithful only when each parity representation
has multiplicity one. At multiplicity two, the correct observation target is
the symmetric square of each multiplicity space. Probe count alone is not the
interface: the polarized feature tensors must span that parameter space.

This increment specializes the two-parity theorem and rejects its premature
promotion to the unreduced four-channel packet.

## Boundary and missing interfaces

- source authority for all six polarized flux ports;
- the physical four-channel-to-parity-coordinate isomorphism;
- real or complex Hermitian coefficient conventions;
- proof that no additional bulk-boundary symmetry reduces multiplicity;
- the general symmetric-square rank theorem for arbitrary probe families.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/MultiplicityPairingReconstruction.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
