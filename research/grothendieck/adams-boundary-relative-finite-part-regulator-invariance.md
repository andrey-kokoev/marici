# The Adams-boundary finite part is regulator-independent only relatively

At the doubled critical argument `2s=1+2iT`, the quadratic channel meets the
prime-zeta boundary. At `T=0`, two natural regulator schemes give different
individual constants.

For a sharp prime cutoff,

```
sum_(p<=P) 1/p = log log P + B_1 + o(1),              (1)
```

where `B_1` is the Meissel--Mertens prime constant. For the analytic/Abel
regulator,

```
P(1+epsilon)=sum_p p^(-1-epsilon)
 = log(1/epsilon) + B_1-gamma + o(1).                 (2)
```

The even gamma oscillator with shift `a=1/4` transforms in parallel. Sharp
mode cutoff gives

```
sum_(k<K) 1/(k+a)=log K-psi(a)+o(1),                 (3)
```

whereas exponential/Abel cutoff gives

```
sum_(k>=0) e^(-epsilon(k+a))/(k+a)
 = log(1/epsilon)-psi(a)-gamma+o(1).                 (4)
```

Subtracting gamma from prime gives the same finite constant in both schemes:

```
sharp:  B_1 - [-psi(a)]       = B_1+psi(a),
Abel:   B_1-gamma - [-psi(a)-gamma]
                               = B_1+psi(a).          (5)
```

At `a=1/4`, this is the canonical relative finite part

```
B_1+psi(1/4)
 = B_1-gamma-pi/2-3log 2.                             (6)
```

## Consequence

The finite part at the Adams boundary is not attached to `C_2` alone. It is
a relative prime--gamma quantity. Individual constants depend on regulator,
but the shared logarithmic coordinate makes their difference invariant. This
is exactly the behavior required of a coefficient--Betti relative
determinant.

The result closes only the common `T=0` logarithmic divergence. It does not
construct the full reflection-compatible family at nonzero height or remove
rank-one shell aliasing. Those require the resolved/moment mapping cone.

## Falsifier

A proposal fails if it combines the sharp prime constant `B_1` with the Abel
gamma constant, or vice versa: the uncancelled Euler constant is a regulator
artifact. Prime and gamma legs must use the same cutoff functor before the
relative finite part is taken.

