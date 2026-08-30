# The affine seven is a cross-grade discriminant, not a fixed-grade charge index

## Type of the affine frame

The affine frame

\[
F=\begin{pmatrix}2&7\\3&7\end{pmatrix}
\]

was extracted from the family of preferred observation covectors

\[
v_g=(2g+7,3g+7)=F(g,1)^T.
\]

Its two domain axes are therefore:

1. variation of the symbolic operator grade \(g\);
2. the constant affine offset.

They are not two simultaneous source-charge directions.  The order-seven
cokernel of \(F\) is consequently a discriminant of the cross-grade affine
family.

## Fixed-grade boundary map

At one grade, the two nonzero source columns meeting preferred rows
\(R_0,R_1\) are scalar multiples of the same vector \(v_g\).  After the
previously declared ray saturation, the boundary block is

\[
B_g=\begin{pmatrix}
2g+7&2g+7\\
3g+7&3g+7
\end{pmatrix}.
\]

Its Smith form is

\[
\operatorname{diag}(\gcd(g,7),0),
\]

not \(\operatorname{diag}(1,7)\).  Thus a fixed grade sees seven-torsion only
when \(7\mid g\).  On the even chart-divisor family this means
\(14\mid g\).

The physical magnetic incidence operator is grade three.  There

\[
v_3=(13,16),\qquad \gcd(13,16)=1,
\]

so the saturated fixed-grade observation line has no seven-torsion.

## Consequence for quantized helicity

Particle helicity remains a genuine independently quantized source lattice
and remains coupled to spin memory.  But comparing it directly with \(F\)
crosses two type boundaries at once:

- source charge versus observation row;
- fixed physical grade versus symbolic variation across grades.

Even a future common source/observation carrier would not make
\(\operatorname{coker}F\) a physical charge quotient unless it also supplied
a source-authorized grade-changing constructor under which different grades
are jointly composable charge directions.

No such constructor exists in the completed physical source category.  The
general-grade family is a mathematical extension used to classify operators;
it is not a Fock lattice of physical charges.

## Corrected search target

There are now two logically different index-seven routes:

1. **Fixed-grade physical route.** Find a source-derived integral charge-to-
   observation pairing \(P_3\) at physical grade three and calculate
   \(\operatorname{coker}P_3\).  The current preferred block does not provide
   seven.
2. **Cross-grade route.** Construct a physical operation relating charge
   sectors at different grades and prove that its integral comparison matrix
   is \(F\).  Only then may \(|\det F|=7\) be interpreted physically.

The first route preserves the current physical theory but presently has no
index-seven candidate.  The second route explains the existing affine seven
but requires a new grade-changing physical constructor.

## Hostile conclusion

The numerical equality \(|\det F|=7\) cannot be used as the Smith index of the
helicity lattice at grade three.  Doing so treats family parameters as charge
generators.  The smallest rejection code is

```text
cross_grade_parameter_lattice_mistyped_as_fixed_grade_charge_lattice
```
