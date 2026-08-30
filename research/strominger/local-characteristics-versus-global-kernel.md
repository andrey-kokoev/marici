# Local characteristic ridge waves do not enlarge the global physical kernel

## 1. Two symbols must not be conflated

In a real local dyad, put

\[
 p=\frac{\xi_x-i\xi_y}{2},\qquad
 q=\frac{\xi_x+i\xi_y}{2}.
\]

The paired covariant grade-three operator has branch symbols proportional to

\[
 p^3q,qquad q^3p.
\]

For a nonzero real covector, `q=conjugate(p)` and `pq=|xi|^2/4>0`. The paired
symbol determinant is

\[
 (p^3q)(q^3p)=(pq)^4>0.
\]

Hence the paired operator is elliptic. Any distribution in its kernel is
smooth by microlocal elliptic regularity, in agreement with the harmonic
classification.

By contrast, identifying the two spin frames and taking a raw coordinate
magnetic difference gives

\[
 p^4-q^4=-\frac{i}{2}\xi_x\xi_y
 (\xi_x-\xi_y)(\xi_x+\xi_y).
\]

This scalar presentation is nonelliptic and depends on the selected dyad.

## 2. Local ridge solutions

The constant-coefficient projected equation is

\[
 \partial_x\partial_y(\partial_x^2-\partial_y^2)u=0.
\]

It admits the four ridge families

\[
 u=f(x),\qquad g(y),\qquad h(x+y),\qquad k(x-y),
\]

and their distributional analogues. In Fourier space their support lies on
the four characteristic lines. These demonstrate algebraic describability,
but not localization, global spin-bundle gluing, antipodal parity, or source
constructibility.

## 3. Localization obstruction

There is no nonzero compactly supported distribution on a flat patch solving
the homogeneous projected equation. Indeed, its Fourier transform is entire;
outside the characteristic lines the nonzero polynomial multiplier forces it
to vanish on an open set, and analyticity forces it to vanish everywhere.

Likewise, an `L2(R2)` solution is zero: its Fourier transform is an `L2`
function supported on a measure-zero union of lines. Nonzero ridge solutions
are necessarily extended/nonlocalized or lie in larger distribution classes.
Multiplying one by a compact cutoff creates boundary source terms and destroys
the homogeneous equation.

## 4. Globalization obstruction

The raw scalar projected equation is not the transition law of a global spin
bundle section. To globalize, one must retain the paired spin-four output and
impose the antipodal/helicity relation. The paired elliptic equation then
forces smoothness, while the exact harmonic multiplier forces all `l>=5`
coefficients to vanish.

Therefore

\[
 \boxed{
 \text{global physical kernel}
 =\text{smooth }l=2,3,4\text{ parity modes},}
\]

with no singular characteristic addition. The characteristic ridge waves are
solutions of a presentation-level scalar equation, not sections of the
source-derived global kernel.

## 5. Wavefront taxonomy

| object | wavefront/support | physical status |
|---|---|---|
| paired-kernel distribution | empty wavefront | smooth low modes |
| projected ridge wave | characteristic conormal directions | nonlocalized presentation solution |
| cutoff ridge wave | new boundary wavefront and nonzero source | forced/inhomogeneous |
| point jet | full cotangent fiber at a point | admitted, but detected |
| curve source | conormal to curve | requires independent matter authority |

The local characteristic locus therefore supplies a falsifier of overly broad
scalar formulations, not a new finite-energy localized kernel class.

## Evidence

`checkers/local_characteristics_global_kernel_checks.py` verifies paired
ellipticity, scalar factorization, the four ridge families, cutoff failure,
the measure-zero Fourier support criterion, and agreement with the exact
global harmonic kernel.
