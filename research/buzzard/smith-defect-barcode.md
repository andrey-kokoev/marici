# Smith exponents form a defect barcode

Owner: `marici.Buzzard`

Source locator: `Smith orders are a defect barcode` and `Specialization
kernels are the Tor shadow` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean defines the number of surviving hidden directions at depth `j` as the
number of Smith exponents at least `j`. The barcode lists these counts through
the maximum depth.

The profile `(0,2)` has barcode `[1,1]`: one direction persists for two
layers. The profile `(1,1)` has barcode `[2]`: two directions persist for one
layer. Their determinant orders agree, but their barcodes differ.

Lean also proves generally that the first barcode-layer count equals the seam
corank. The hostile profiles `(0,1)` and `(0,2)` have the same born-generator
count but different total depth and different barcodes. Thus first derived
specialization detects births but not persistence.

## Type-system consequence

The defect interface has three noninterchangeable summaries:

- determinant order: total lost length;
- special corank: number of born generators;
- Smith barcode: persistence depth of each generator.

This increment extends the Smith-profile theorem with the minimal persistence
view while refusing to identify a derived birth count with the full torsion
cokernel.

## Boundary and missing interfaces

- an actual torsion cokernel over the seam local ring;
- a proof identifying its cyclic summands with the supplied Smith exponents;
- the derived tensor/Tor construction for specialization;
- arbitrary finite-rank profiles and barcode-length identities;
- source meanings for persistent hidden directions.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/SmithDefectBarcode.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
