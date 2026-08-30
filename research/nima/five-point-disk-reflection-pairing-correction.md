# Five-Point Disk Reflection Pairing Correction

Entry 891 freezes

\[
0<x=z_2<y=z_3<1
\]

and the Parke--Taylor form \(\operatorname{PT}(12345)\).  Reflecting the
cyclic order to \((15432)\) and returning to the standard gauge gives

\[
X=\frac{y-x}{y},
\qquad
Y=\frac{y-x}{y(1-x)}.
\]

The map sends the bounded chamber to itself in reversed orientation:

\[
0<X<Y<1,
\qquad
\det\frac{\partial(X,Y)}{\partial(x,y)}
=
\frac{x(x-y)}{y^3(1-x)^2}<0.
\]

Direct substitution gives

\[
s^*\operatorname{PT}(15432)
=
-\operatorname{PT}(12345).
\]

The oriented chamber also carries sign \(-1\).  Therefore the fully
transported period pairing has character

\[
\boxed{(-1)\cdot(-1)=+1.}
\]

## Correction

The prior all-arity statement

\[
\chi_n(s)=(-1)^n
\]

is a valid character for the displayed Parke--Taylor/fixed-trivialization
comparison, but it was too broadly called the *physical disk-period
readout*.  A period with cocycle and twisted cycle transported together is
functorially invariant.  At five points the two factor signs are separately
source-derived and cancel.

Thus the five-point string sector supplies a positive example of the paired
mixed-variance architecture:

\[
\text{twisted de Rham class}
\times
\text{oriented twisted chamber}
\longrightarrow
\mathbb C.
\]

This does not yet establish the factor split at all arities; the earlier
factorization ambiguity remains the correct gate for \(n\ne5\).

Artifact:

- `research/nima/check_five_point_disk_reflection_pairing.py`
- `research/nima/results/five-point-disk-reflection-pairing.json`
