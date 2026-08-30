# Global-unit dark-port correlation instrument

## Why local units can still produce a zero

Let the direct global arm have nonzero amplitude `A` and the reciprocal arm
have nonzero amplitude `B`.  Suppose each local comparison is invertible and
write its ratio as `u_v`.  At finite cutoff,

`B/A=U=product_v u_v`.

The antisymmetric output of a balanced coherent combiner is

`D=A-B=A(1-U)`.

Thus `D` can vanish while every local factor and both global arms remain
nonzero.  The zero is a global correlation condition `U=1`, not local rank
loss.

On the critical seam, reciprocal reality makes every admitted local ratio a
unit phase.  The cancellation condition becomes closure of the accumulated
phase around the entire place packet.

## Exact extinction bound

Write `r=|U|`.  Permit a phase scan in one arm but keep its magnitude fixed.
The smallest dark-port intensity is

`I_min=|A|^2(1-r)^2`.

Relative to the corresponding bright-port maximum, the minimum extinction
ratio is

`eta_min=((1-r)/(1+r))^2`.

Therefore perfect extinction requires `r=1`.  Local invertibility is not
enough.  The modulus of the complete reciprocal transport is the radial
witness, while its total phase locates the dark fringe.

## Optical architecture

Use a coherent two-arm interferometer:

- direct arm: ordered finite-place Tate transitions followed by the
  archimedean dilation cell;
- reciprocal arm: the reflected transitions in reverse sewing order;
- reference ports: the unit finite-place minors and the calibrated
  archimedean area;
- output ports: symmetric and antisymmetric coherent sums.

For each spectral sample, record both arm amplitudes before recombination and
the complex dark-port field after recombination.  This prevents a local loss
from masquerading as destructive interference.

## Falsifiers

1. Block either arm.  A declared zero that remains is local loss, not global
   correlation.
2. Randomize one local phase.  The dark fringe must move by the same phase;
   if it does not, that channel was not part of the global section.
3. Introduce calibrated amplitude imbalance `r`.  The observed minimum must
   obey `eta_min=((1-r)/(1+r))^2`.
4. Permute two noncommuting source channels.  A change measures ordered
   cross-place transport; no change supports a factorized scalar product.

## What this contributes

The instrument makes the new frontier operational.  It distinguishes three
mechanisms that a scalar zero alone conflates:

- a vanishing local transition;
- incoherent attenuation of one global arm;
- coherent cancellation of two nonvanishing globally assembled arms.

The completed theta source must still prove which two arm amplitudes its
distinguished scalar section combines.  Once that map is supplied, the
extinction bound is a direct falsifier of the proposed reciprocal
aggregation law.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_global_unit_dark_port.py
```
