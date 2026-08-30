# Elementary real structures do not select the Xi boundary phase

Consider the self-adjoint boundary family for `-i d/du` on `[0,L]`:

```
psi(L)=U psi(0),          |U|=1.                       (1)
```

The Xi counting constant asks for

```
U=exp(i pi/4).                                           (2)
```

Two natural antiunitary real structures fail to derive it.

## Plain conjugation

For `K psi=conj(psi)`, conjugating (1) gives boundary phase `conj(U)`. Domain
invariance requires

```
U=conj(U),
```

so `U=+1` or `U=-1`. Plain conjugation excludes, rather than selects,
`exp(i pi/4)`.

## Reflection plus conjugation

For

```
(J psi)(u)=conj(psi(L-u)),                              (3)
```

one has

```
(J psi)(L)=conj(psi(0)),
(J psi)(0)=conj(psi(L))=conj(U)conj(psi(0)).
```

The same boundary condition for `J psi` becomes

```
conj(psi(0))=U conj(U) conj(psi(0)),
```

which holds for every unit phase. Reflection-conjugation preserves the full
extension family and selects nothing.

## Consequence

The functional-equation-style reflection involution, by itself, cannot
explain the `1/8` phase in this elementary first-order boundary model. A
selection principle needs extra structure, for example a metaplectic lift,
a Maslov index, a corner/orbifold condition, or coupling to the arithmetic
coefficient correspondence.

This narrows the archimedean target: merely stating that the boundary
condition respects conjugation or reflection symmetry is insufficient.

## Falsifier

A proposed derivation fails if its only input is invariance of (1) under
plain conjugation or reflection-conjugation. The former gives only `+-1`;
the latter leaves all `U(1)` phases free.

