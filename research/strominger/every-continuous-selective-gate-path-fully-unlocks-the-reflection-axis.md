# Every Continuous Selective-Gate Path Fully Unlocks the Reflection Axis

## Continuous order parameter

For a unitary sheet operation (U), define

\[
s(U)=\frac12\operatorname{tr}(U^\dagger XUX),
\]

where (X) exchanges the sheets. In the two-dimensional unitary model this
is a real continuous measure of the overlap between the original reflection
axis and its transported image.

At the identity and selective endpoints,

\[
s(I)=+1,
\qquad
s(Z)=-1.
\]

Therefore every continuous implementation path from (I) to (Z) contains
an intermediate operation (U_*) with

\[
s(U_*)=0.
\]

At this interface, (U_*^\dagger XU_*) is Hilbert-Schmidt orthogonal to (X).
The original reflection axis is not merely perturbed; it is fully unlocked.

## Sharp lossless witness

For the standard phase path

\[
U(t)=\operatorname{diag}(1,e^{i\pi t}),
\]

the midpoint is (U_* = \operatorname{diag}(1,i)). It remains exactly unitary,
while its distance from both the linearly commuting and anticommuting
projective loci is maximal in the plus-or-minus Frobenius test.

Thus the forced interface is not a gap closing, norm loss, or failure of
global reversibility. It is pure symmetry unlocking. This is the magnetic
counterpart of Figueiredo's lossless threshold rotations that preserve global
unitarity while violating the protected reduction.

## Implementation contract

A proposed physical path must therefore declare:

```text
reflection_unlocking_support
maximum_axis_deflection
which source term carries the odd control
how reflection is restored at the endpoint
whether the detector frame co-transports through the unlocked interface
```

Any contract claiming continuous implementation while preserving the original
reflection axis everywhere is rejected. Monitoring only unitarity or spectral
gap cannot detect this failure.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/reflection_axis_midpath_unlocking_checks.py
```
