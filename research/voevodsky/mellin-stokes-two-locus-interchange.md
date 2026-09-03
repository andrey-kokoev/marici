# Mellin–Stokes two-locus interchange

## Question

Should Stokes basis mutation act directly on the spectral affine filler chain object?

## Claim boundary

The audit separates action loci. It does not deny the asserted covariance of periods or Mellin jets.

## Two chain loci

The spectral affine chain object contains the reciprocal parameter and its affine fillers. Reciprocal negation and conjugation act here.

Stokes mutation acts on a relative-cycle or thimble basis in the integration-variable plane. It changes cycle coefficients and presentations of the period class. This is a different chain object.

Period evaluation couples the loci schematically as

\[
P:C_{\mathrm{aff}}(D_w)\otimes C_{\mathrm{rel}}(U_z,E_z)
\longrightarrow V.
\]

## Typing correction

Covariance of Mellin jets under basis mutation does not make Stokes mutation an endomorphism of \(C_{\mathrm{aff}}(D_w)\). The required datum is an interchange cell comparing spectral reciprocal transport, cycle-basis transport, and the period pairing.

In a strict product fixture, actions on separate tensor factors commute exactly:

\[
(\rho\otimes1)(1\otimes T)=(1\otimes T)(\rho\otimes1).
\]

The checker verifies this shape. It does not construct the actual Stokes chain map or pairing cell.

## Disposition

The previous request for a `Stokes action on affine fillers` was mistyped. The first missing datum is a typed relative-cycle chain model and a source-derived interchange cell with the spectral affine filler. Cutoff refinement then requires a further interchange with both loci.

## Verification

- `research/voevodsky/mellin-stokes-two-locus-interchange-v1.json`
- `research/voevodsky/checkers/check_mellin_stokes_two_locus_interchange.py`
- `research/voevodsky/results/mellin_stokes_two_locus_interchange.json`
