# Filtered quotient colon/saturation test

## Result

Squared-axis transport is not injective on the full grade-bounded quotients.

Every tested map has an exact nonzero kernel. For both `A12→A14` and `A14→A16`:

- grade six: kernel dimension one for each axis;
- grade seven: dimensions three for `x²` and two for `y²`;
- grade eight: dimensions three for `x²` and two for `y²`.

The twelve checks have total kernel dimension 24. Thus the proposed colon equalities fail at finite degree.

## Consequence

Global quotient injectivity cannot justify all-even persistence of the twelve distinguished classes. Those classes themselves survive every tested path through A16, so the newly detected kernels concern other quotient directions; they do not show that the twelve are killed.

## Claim boundary

This is exact algebraic pole-filtered linear algebra. It neither identifies kernel vectors geometrically nor promotes the filtration to DNC/I-adic structure.

## Disposition

Classify the kernel generators and their relation to the twelve class orbits. A narrower cyclic-submodule injectivity test may still establish persistence even though global saturation fails.

## Verification

- `research/voevodsky/check_cosmology_filtered_quotient_colon_saturation.py` — exit 0
- `research/voevodsky/results/cosmology_filtered_quotient_colon_saturation.json`
