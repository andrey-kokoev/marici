# Two-prime evenization breaks local seam confinement

## Second odd normalization

The co-moving Schur first jet is odd:

`Q_p(z)=2f p^(-1/2)sinh(z log p)`.

Normalize it by the archimedean odd generator `2fz`.  The resulting candidate
even cell is

`H_p(z)=p^(-1/2)sinh(z log p)/z`.

The singularity at `z=0` is removable, with value
`p^(-1/2)log p`.  It also has the positive-kernel representation

`H_p(z)=p^(-1/2) integral_0^(log p) cosh(zu) du`.

Every individual prime cell has only seam zeros:

`z=i n pi/log p`.

Thus odd first jet followed by odd normalization produces an even local
sine-type section with perfect seam confinement.

## Two-prime hostile

Now aggregate the first two prime cells with their positive vacuum weights:

`H_2,3(z)=2^(-1/2)sinh(z log 2)/z`

`          +3^(-1/2)sinh(z log 3)/z`.

This remains even, entire, real on the real axis, and is the cosh transform of
a positive decreasing step kernel.  Nevertheless it has the off-seam zero

`z=0.688255703728031486+7.44004199836615849 i`,

together with the reflected and conjugate partners required by symmetry.

The residual at 60-digit evaluation is below `1e-50`.

## Consequence

Local seam confinement is not compositional under positive prime addition.
The following package is still insufficient:

- affine Green coherence;
- a co-moving odd return incidence;
- exact Schur first-jet reduction;
- division by the canonical odd archimedean generator;
- positivity and monotonicity of the aggregated step kernel.

The failure occurs before infinite completion.  It is already present for the
finite cutoff `{2,3}`.  Therefore a successful theta constructor must contain
a cross-prime incidence that is absent from independent positive addition.
Prime cells cannot be sewn only through a shared scalar output.

## Optical falsifier

Build two normalized unequal-loss segments with lengths `log 2` and `log 3`,
combine their evenized first-jet ports with gains `2^(-1/2)` and `3^(-1/2)`,
and analytically continue the reciprocal parameter through the two-quadrature
emulator.  The combined port must null at the quoted off-seam complex setting
although neither local port does.  A cross-prime coupling proposed as the
repair must move or remove this null without changing either one-prime
calibration.

## Verification

```text
uv run --with sympy --with mpmath python research/aspect/checkers/check_two_prime_evenized_off_seam_zero.py
```
