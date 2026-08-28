# Gradewise Fourier saturation isometry

## Exact theorem

Let `J` be the reciprocal Fourier sewing action with `J^4=I`. For any declared
seminorm `q`, define

`q_sat(x) = sum_(j=0)^3 q(J^j x)`.

Then

`q_sat(Jx) = q_sat(x)`.

Applying `J` only cycles the four orbit terms. The argument uses no inner
product and no comparison between grades.

## Grades covered

The same construction applies separately to:

- every primitive weighted Hilbert seminorm;
- the square Hilbert seminorm;
- the connected-tail absolute-summability seminorm;
- every seam or archimedean graph seminorm after its source map is defined.

Thus Fourier sewing has operator bound exactly one in every saturated grade.
This closes the uniform sewing-bound requirement in the corrected pro-Gram
telescope.

## What it does not do

The common bound does not merge the grades. Primitive and square norms remain
nonuniformly inequivalent, and the connected tail remains nonquadratic.

Saturation also does not prove that an unsaturated boundary map is continuous
on its source grade. That must be established before its graph seminorm is
admitted. Nor does this construction create a finite Euler Poisson action.

## Apparatus consequence

At each admitted label/Gram cutoff, acquire the four sewing-orbit copies of a
channel and sum their native readouts. Repeating after one additional sewing
step must give the same total. This is a calibration identity with predicted
gain exactly one for every channel, while preserving each channel's native
detector and units.

The apparatus therefore tests gradewise Fourier isometry without forming a
cross-grade Euclidean stack.

## Remaining frontier

After this result, the completion problem consists of:

1. continuity of each source boundary map on its declared grade;
2. cutoff compatibility in every grade;
3. construction of the common graph domain carrying the dual Green identity.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_gradewise_fourier_saturation_isometry.py
```
