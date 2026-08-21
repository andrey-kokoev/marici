# The positive leakage determinant is not the native shell determinant

The universal identity

```
det_2(I+J_B)=det(I+B*B)>0
```

is algebraically correct. It remains useful only if the oriented double
`J_B` is supplied by the source construction. The smallest resolved shell
shows that ordinary height compression does not produce it automatically.

Take two equal-weight prime rays with phases `z_1,z_2` and use the normalized
constant and difference vectors. In that basis, height multiplication is

```
U = [ a  b ],       a=(z_1+z_2)/2,
    [ b  a ]        b=(z_1-z_2)/2.                   (1)
```

The retained rank-one determinant is `a`. If `a` is invertible, the exact
kernel Schur complement is

```
a-b^2/a = z_1 z_2/a,                                (2)
```

and the full determinant is

```
a(a-b^2/a)=z_1 z_2.                                 (3)
```

By contrast, the positive leakage correction is

```
1+|b|^2.                                             (4)
```

These are different objects. For the exact hostile phases `z_1=1,z_2=i`,
the native full determinant is `i`, while the positive Gram correction is
`3/2`. The latter cannot replace the shell-kernel determinant.

## Consequence

Hilbert--Schmidt leakage proves that an oriented auxiliary double has a
well-defined positive regularized determinant. It does **not** derive that
double from diagonal prime height evolution. The actual block factorization
retains the kernel diagonal `D` and the generally complex Schur complement
`A-CD^(-1)B`.

Therefore the shell program now has a sharper source gate:

1. either the coefficient--Betti/Mackey construction independently supplies
   the skew pair `B,-B*`, in which case coupled positivity is relevant;
2. or one must use the native unitary block determinant, whose kernel phase
   cannot be erased by Gram positivity.

This falsifies an automatic route from growing-rank shell compression to
positive Xi. It does not falsify the abstract coupled-positivity theorem or
the quarter-shifted covariance correspondence.

