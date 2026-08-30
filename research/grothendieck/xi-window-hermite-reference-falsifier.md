# Growing Xi windows do not have Hermite global shape

The Hermite-relative entropy is canonical for a closed finite Newman system,
but its use as an infinite-rank Xi reference faces a global-shape falsifier.

Let `N_+(T)` count positive Xi ordinates up to `T`. The leading
Riemann--von Mangoldt law is

```
N_+(T) ~ T log(T)/(2 pi).
```

For the symmetric window `[-T,T]`, its rank `n(T)` and squared radius obey

```
n(T) ~ T log(T)/pi,
R(T)^2 = 2 integral_0^T t^2 dN_+(t)
       ~ T^3 log(T)/(3 pi)
       ~ n(T) T^2/3.                                  (1)
```

More strongly, after scaling ordinates by `T`, the empirical measure tends
weakly to the uniform probability measure on `[-1,1]`: for fixed
`0<a<=1`,

```
N_+(aT)/N_+(T) -> a.                                  (2)
```

By contrast, scaled Hermite roots tend to the semicircle measure. Their
unit-support second moment is `1/4`, whereas the uniform limit has second
moment `1/3`. No affine rescaling can remove this shape difference.

The scale coefficient in the finite Xi window consequently behaves as

```
c(T) = n(T)(n(T)-1)/(2R(T)^2)
     ~ 3 log(T)/(2 pi T),                              (3)
```

but this does not turn the Xi configuration into an asymptotic Hermite
equilibrium. A global Hermite-relative entropy may remain a valid finite
diagnostic, yet it cannot converge to zero as a shape defect for growing
sharp Xi windows.

## Corrected reference geometry

The logarithmic-gas potential whose equilibrium density on `[-1,1]` is
uniform satisfies

```
V_U'(x) = log((1+x)/(1-x)),
V_U(x) = (1+x)log(1+x) + (1-x)log(1-x),                (4)
```

up to an additive constant. Indeed

```
2 PV integral_{-1}^1 [(1/2)/(x-y)] dy
  = log((1+x)/(1-x)).
```

This suggests replacing the Hermite reference by a Weyl-adapted free
energy, or first flattening ordinates by the counting coordinate. Neither
move automatically preserves the Newman heat-flow Lyapunov identity: the
Jacobian and boundary terms must be derived, not assumed.

## Decision

Do not pursue a naïve infinite-rank Hermite entropy. Pursue a
Weyl-renormalized entropy whose reference measure matches (2), while keeping
the exact finite Hermite theorem as a local closed-system control.

