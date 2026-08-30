# Two parity fluxes reconstruct the reflection pairing

Owner: `marici.Buzzard`

Source locator: `The minimum normalization packet has two sector weights` and
`Two authorized fluxes are sufficient` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

The channel space, reflection, and invariant rational pairing are imported
from `ReflectionPairingAmbiguity.lean`. The even and odd parity channels are
the vectors `(1,1)` and `(1,-1)`. Lean computes their energies as

`E_even = 2 * (alpha + beta)` and `E_odd = 2 * (alpha - beta)`.

The hostile pair with coefficients `(2,0)` and `(3,-1)` assigns the same
even-sector energy four but distinct odd-sector energies four and eight. One
sector normalization is therefore not faithful.

Conversely, Lean reconstructs

`alpha = (E_even + E_odd) / 4` and
`beta = (E_even - E_odd) / 4`,

and proves the joint observation map is injective. The finite source fixture
with energies `(10,6)` reconstructs coefficients `(4,1)` and evaluates back to
the supplied energies.

## Type-system consequence

Reflection covariance restricts the pairing to two rational parameters. A
single authorized normalization does not determine both. Two independent
parity-sector flux records are sufficient, but the reconstruction theorem does
not manufacture or authorize those records.

The abstraction specialized the earlier nonselection result into an exact
minimal observation theorem: one parity probe has a nontrivial kernel, while
the paired observation is injective.

## Boundary and missing interfaces

This is a rational two-channel quadratic model. A faithful sector theorem
still needs:

- source-derived authority for both parity fluxes;
- the real or complex Hermitian pairing type used by the sector;
- normalization conventions connecting quadratic energy to boundary flux;
- multiplicity-space probes for higher-dimensional parity sectors;
- a proof that the physical reflection action diagonalizes into these sectors.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ParityFluxReconstruction.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/ParityFluxReconstruction.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/parity-flux-reconstruction.md`
