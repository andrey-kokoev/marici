# Two consistent coordinate repairs destroy the frozen spline cancellation

## Repairs tested

The hybrid checker can be repaired in either of two internally consistent ways.

### Preserve the archimedean coordinate

Take `f(x)=profile(x/2)` on both sides. Then prime evaluation is `profile(log(q)/2)`, and compact support extends the prime-power range to approximately `exp(2(4+2a))`, requiring enumeration through about `763000`, not `1024`.

A high-precision direct scout through `800000` gives baseline total approximately

`-14.29680793`.

### Preserve the prime coordinate

Take `f(x)=profile(x)` on both sides. Then prime evaluation and the existing cutoff near `1024` remain compatible, but the archimedean moments must remove the factor-two substitution and `2^-r` jet scaling.

A direct scout gives baseline total approximately

`2.12511464`.

## Consequence

Neither coherent repair retains the frozen near-zero positive value `1.18e-5`. That cancellation was produced by mixing the prime term of the second convention with the archimedean term of the first.

The declared support audit also identifies the likely intended convention: the checker claims complete prime-power enumeration through `1024`, which is compatible with `f(x)=profile(x)` but false for `f(x)=profile(x/2)`. Thus the probable repair is to preserve the prime coordinate and rebuild the archimedean side.

These are non-directed numerical scouts. They establish the scale and support mismatch but do not replace a rational interval regeneration.

## Disposition

Retract the frozen baseline theorem rather than patching one argument locally. Rebuild under `f(x)=profile(x)` unless a source theorem explicitly selects the doubled-support convention; in the latter case expand prime enumeration through the true support endpoint.
