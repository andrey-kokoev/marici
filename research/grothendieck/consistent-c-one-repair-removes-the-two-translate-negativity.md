# The consistent c=1 repair removes the two-translate negativity

## Repair selected for reconnaissance

Take the stored spline profile itself as the canonical logarithmic test:

`f(x)=profile(x)`.

This is the `c=1` member of the dilation family. It has three implementation advantages already encoded by the original construction:

- prime samples are `profile(log q)`;
- the support-derived prime-power cutoff lies below `1024`;
- with `a=2 log 2`, the double pole-annihilator remains at the centered pole characters.

Only the archimedean moments and jets must be rebuilt without the erroneous `x/2` substitution.

## Independent scout

Direct high-precision quadrature of

`-(gamma+log pi)f(0)`

`+integral_0^infinity [f(0)e^-x-f(x)e^(-x/4)]/(1-e^-x) dx`

combined with complete prime-power enumeration through `1024` gives:

- baseline energy approximately `2.12511463965`;
- symmetric cross energy approximately `-0.846660221734`.

The two-translate matrix then has

- determinant approximately `3.79927870059`;
- coherent eigenvalue approximately `1.27845441792`;
- disagreement eigenvalue approximately `2.97177486138`.

Thus both two-translate directions are positive under this coherent repair. The prior negative determinant is eliminated rather than weakened.

## Claim boundary

These are high-precision numerical scouts, not directed interval certificates and not source-authorized Weil values. They show that the negative result is unstable under repair in exactly the way predicted by the mixed-coordinate defect.

## Disposition

The first regeneration target should be a rational interval implementation of the `c=1` archimedean moments, with direct quadrature as a regression fixture. If certified, the baseline margin is order one rather than `1e-5`, and the first Gram minor is positive.
