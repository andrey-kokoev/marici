# A stable scalar reference can miss anisotropic readout drift

## Orthogonal stability does not calibrate the science direction

Reuse the monotone science contrast `1, 1/2, 1/4`, now carried on the `X`
polarization coordinate. Let the analyzer transfer matrices be diagonal, with
`X` gains `1, 1, 4` and unchanged `Y` and `Z` gains.

A scalar `Z` reference reports `1, 1, 1`: apparently perfect stability. Yet the
raw `X` science record becomes `1, 1/2, 1`, again faking revival. Dividing by the
stable scalar reference changes nothing.

Spanning `X`, `Y`, and `Z` reference probes reconstruct the complete diagonal
transfer matrix at each time. Applying its inverse recovers the monotone science
sequence exactly. The repair succeeds because the science direction lies in the
calibrated reference span and the transfer matrix remains nonsingular.

## Calibration inherits a rank condition

A reference is not adequate merely because it is stable or precise. It must
span every instrument direction on which the scientific contrast depends.
The observation contract therefore needs:

- science contrast subspace;
- reference probe span;
- transfer-matrix singular margins;
- frame alignment and its uncertainty;
- explicit refusal to invert collapsed reference directions.

This is the finite optical form of instrument holonomy: an untracked change in
the measurement frame can appear as evolution of the object.

## Optical instrument

Interleave horizontal/vertical, diagonal/antidiagonal, and circular probe pairs
through the same analyzer as the memory signal. Reconstruct the time-local
Mueller action, compare its singular vectors with the science contrast, and
normalize only on directions whose calibrated lower margin remains admissible.

## Claim boundary

The checker treats exact diagonal transfer matrices and noiseless spanning
references. General rotations, nondepolarizing constraints, source-reference
drift, ill-conditioned inversion, and finite-sample uncertainty remain open.

## Verification

```text
python research/aspect/checkers/check_scalar_reference_blind_to_anisotropic_drift.py
```
