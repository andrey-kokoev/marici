# Off-line contractivity reduces to a de Branges--Rovnyak kernel positivity theorem

Let

```
Omega={s:Re(s)>1/2}
```

and let `C(s)` be a holomorphic operator-valued transfer family. Its
right-half-plane de Branges--Rovnyak kernel is

```
K_C(s,w)
 =[I-C(w)*C(s)]/[s+conj(w)-1].                         (1)
```

The operator-valued Schur criterion says:

```
K_C positive definite  iff  ||C(s)||<=1 on Omega.      (2)
```

At the diagonal,

```
I-C(s)*C(s)=2(Re(s)-1/2) K_C(s,s).                     (3)
```

Hence strict positivity of the diagonal kernel gives strict contraction in
the open half-plane. Combined with reflection, this is exactly the off-line
invertibility condition required by the paired gluing determinant.

## Boundary zeros

As `s` approaches `1/2+iT`, the scalar denominator in (3) tends to zero.
The transfer may approach an isometry or acquire a unit singular value on
the boundary without violating open-half-plane contractivity. Thus the
framework naturally separates:

```
open half-plane: strict loss and no determinant zero;
fixed boundary: unit-gain threshold resonances.         (4)
```

## Herglotz/Cayley route

If an operator family `F(s)` has positive real part,

```
Re F(s)>=0,
```

then its Cayley transform

```
C(s)=[F(s)-I][F(s)+I]^(-1)                             (5)
```

is Schur-contracting. In the scalar case,

```
1-|C|^2=4 Re(F)/|F+1|^2.                               (6)
```

This reconnects the transfer lane to the earlier Caratheodory target based
on `xi'/xi`. But proving `Re(xi'/xi)>=0` in the half-plane is itself
RH-equivalent. The gain is not an easier restatement; it is a precise source
kernel whose positivity could potentially be derived from the
coefficient--Betti correspondence.

## New arithmetic target

Construct `C(s)` from the even-oscillator/prime relative correspondence and
prove, for every finite choice of points `s_j` and vectors `v_j`,

```
sum_(i,j) <v_i,K_C(s_i,s_j)v_j> >=0.                   (7)
```

This is the first universal coupled positivity theorem that would directly
imply the required off-line contraction. Finite-rank Gram minors provide
immediate falsifiers.

## Limitation

No Xi transfer family is yet constructed, so (7) cannot currently be tested
arithmetically. Positivity of an invented kernel would be irrelevant unless
its determinant is independently identified with completed `xi`.

