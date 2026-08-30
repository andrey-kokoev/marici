# The Xi constant fixes a boundary phase, but generic boundary phases are tunable

The smooth Xi counting function is

```
N_bar(T)=theta(T)/pi+1,
theta(T)=Im log Gamma(1/4+iT/2)-(T/2)log pi.            (1)
```

Stirling's leading terms give

```
theta(T)
 =T/2 log(T/(2pi))-T/2-pi/8+O(1/T),                   (2)
```

and hence

```
N_bar(T)
 =T/(2pi)log(T/(2pi))-T/(2pi)+7/8+O(1/T).             (3)
```

The `-1/8` correction to the elementary `xp` phase-space constant is
therefore forced by the gamma factor.

## Boundary-phase realization

For the first-order operator `-i d/du` on an interval of length `L`, the
self-adjoint boundary conditions form the family

```
psi(L)=exp(2pi i alpha) psi(0),                         (4)
```

with spectrum

```
(2pi/L)(n+alpha).                                      (5)
```

Its smoothed counting constant shifts by `-alpha`. Thus `alpha=1/8`, or

```
exp(2pi i alpha)=exp(i pi/4),                           (6)
```

supplies exactly the missing `-1/8`.

## Explanatory gate

Equation (6) is not yet an explanation. The family (4) can tune the constant
continuously. Selecting `alpha=1/8` after inspecting Xi merely fits the
answer. A successful archimedean construction must derive the phase from
independent structure, such as:

1. the gamma-factor functional equation and its real structure;
2. a Maslov/metaplectic index;
3. a canonical boundary correspondence; or
4. compatibility with the prime-side adjoint involution.

The phase must also coexist with the fixed-domain and compact-resolvent
requirements; the elementary `xp` cutoff remains energy-dependent.

## Falsifier

An operator model that advertises the `7/8` constant only by choosing an
otherwise free self-adjoint extension parameter has no predictive content.
It must prove why all other phases are forbidden.

