# Reflection falsifies the global cyclic-resolution conjecture and exposes a five-primary anomaly

## Hostile under test

The Deutschian cyclic-resolution conjecture required the affine comparison to
intertwine physical axis reflection with inversion of cyclic characters.
This is stronger than the oriented-axis theorem and can be tested without
assuming any new source operator.

Let

\[
F_s=\begin{pmatrix}2&n\\3&n\end{pmatrix},
\qquad n=4s-1,
\]

and let row reflection be

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

## Direct descent fails at every spin

Exact calculation gives

\[
F_s^{-1}XF_s
=\begin{pmatrix}
-1&0\\
5/n&1
\end{pmatrix}.
\]

For integer \(s\ge1\), \(n=4s-1\) is at least three and never divides five.
Therefore this matrix is never integral.  Equivalently,

\[
X\operatorname{im}F_s\ne\operatorname{im}F_s.
\]

Row reflection does not descend to \(\operatorname{coker}F_s\).  Hence the
comparison with the \(C_n\) character group cannot intertwine this reflection
with character inversion on one affine chart.

The same failure is visible in the affine coordinate

\[
\ell(x,y)=3x-2y\pmod n.
\]

After row swap,

\[
\ell(X(x,y))=3y-2x,
\]

which is not generally \(-\ell(x,y)\).

Thus the original conjecture is falsified as a global reflection-equivariant
statement, including at spin two.

## Two-chart repair and the hidden five

Retain both chart coordinates

\[
\ell(x,y)=3x-2y,
\qquad
\ell_X(x,y)=3y-2x
\pmod n.
\]

Their joint coefficient matrix is

\[
A=\begin{pmatrix}3&-2\\-2&3\end{pmatrix},
\qquad \det A=5.
\]

The two charts are transverse modulo \(n\) exactly when

\[
\gcd(5,n)=1.
\]

The reflection-stable lattice is

\[
L_s\cap XL_s
=\ker(\ell,\ell_X),
\]

and its index in \(\mathbb Z^2\) is

\[
[\mathbb Z^2:L_s\cap XL_s]
=\frac{n^2}{\gcd(n,5)}.
\]

For spin two, \(n=7\), giving the previously observed 49-class stable packet.
But when

\[
s\equiv4\pmod5,
\]

one has \(5\mid n\), and the stable packet has only \(n^2/5\) classes.
The smallest case is

\[
s=4,qquad n=15,qquad
[\mathbb Z^2:L_s\cap XL_s]=45,
\]

not 225.

This five-primary overlap is invisible in the unary affine cokernel and in
the regular cyclic restriction of \(\mathcal H_{2s-1}\).  It appears only
when reflection forces both charts into the same native binary target.

## Revised theorem

The cyclic-restriction theorem survives only in the oriented sector:

\[
\operatorname{coker}F_s
\cong X^*(SO(2))/nX^*(SO(2)).
\]

It does not extend to an \(O(2)\)-equivariant one-chart theorem.  Full
reflection requires a two-chart local system:

```text
oriented chart +  ---- ell ----> Z/n
       | reflection
       v
oriented chart -  -- ell_X ---> Z/n
       |
       v
joint reflected germ of size n^2/gcd(n,5)
```

At spins with \(5\nmid n\), the two chart characters are jointly faithful.
At spins with \(5\mid n\), their five-primary overlap is a genuine additional
germ and must be retained.

## Disposition of the Deutschian conjecture

- **Falsified:** one affine cyclic residue globally intertwines reflection
  with character inversion.
- **Survives:** an oriented-axis cyclic restriction explains the unary
  discriminant \(4s-1\).
- **New prediction:** spin \(s\equiv4\pmod5\) has a five-primary reflected-chart
  degeneracy, beginning with the 45-class spin-four packet.

The next independent falsifier should construct the spin-four boundary
operator.  If its two reflected affine coordinates remain transverse modulo
15, the generalized affine/local-system model is wrong.  If a fivefold
overlap occurs, the reflection failure has revealed a second structural
prime rather than merely breaking the first conjecture.
