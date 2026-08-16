---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Reflection--Unipotent Separation at the Finite Lambda Collision

## Result

Entry 282 identifies the finite \(\ell_1=0\) and \(\ell_2=0\)
collisions as \(A_2\) surface singularities whose moving total spaces
have ordinary double points. The physical transverse slice is not the
generic constant-term smoothing of \(A_2\).

For \(\lambda=\ell_1\), direct reduction of the frozen Cayley--Menger
polynomial gives

\[
\boxed{
XY
=
\alpha t^3+\beta\lambda t
+
\text{higher weighted order},
}
\]

with

\[
\alpha=4xy^4(2x-y),
\qquad
\beta=32x^2y(2x-y)(x-y).
\]

At generic nonsoft kinematics, \(\alpha\beta\neq0\). A loop around
\(\lambda=0\) exchanges the square-root pair of roots and fixes the
third root. Therefore the finite \(A_2\) vanishing lattice carries a
single simple reflection:

\[
T_{A_2,s}
\sim
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix},
\qquad
T_{A_2,u}=1,
\qquad
N_{A_2}=0.
\]

At the same divisor, the elliptic boundary has the standard nodal Legendre
degeneration and hence a rank-one unipotent logarithm with \(N^2=0\).
The marked conductor graph itself has identity monodromy on its labeled
off-divisor cycles, although one top cycle specializes to zero.

This separates the unresolved top extension spectrally:

\[
\boxed{
\text{the top conductor line cannot extend rationally into the }
(-1)\text{ reflection line}.
}
\]

Any rational top extension that survives must lie in the \((+1)\)
generalized eigenspace: the invariant \(A_2\) line, the unipotent
elliptic nearby-cycle sector, or algebraic Tate/Kummer classes with
eigenvalue \(+1\).

Thus the finite \(\Lambda\)-collision does not produce an undifferentiated
new extension problem. It reduces to one explicit \((+1)\)-sector
nearby-cycle column.

## Frozen transverse coordinates

Use

\[
\lambda=\ell_1=x-y-z,
\qquad
d=2x-y,
\qquad
r=x-y,
\]

and center the marked collision by

\[
u=a-(x+z),
\qquad
v=b-(y+z).
\]

Resolve the null and transverse directions of the central quadratic form
by

\[
u=yt,
\qquad
v=dt-s.
\]

Then

\[
K_2|_{\lambda=0}=4x^2y^2s^2.
\]

The complete degree-two part in \((t,s,\lambda)\) is

\[
4x^2y^2s^2
+
32x^2ydr\,t\lambda
-
16x^2yr\,s\lambda
+
16x^2r^2\lambda^2.
\]

The last three terms involving only \(s,\lambda\) complete the square:

\[
4x^2y^2
\left(
s-\frac{2r}{y}\lambda
\right)^2.
\]

After the analytic transverse shift

\[
\widehat s=s-\frac{2r}{y}\lambda,
\]

and the standard split change of variables in \((w,\widehat s)\), the
remaining one-variable germ begins with

\[
4xy^4d\,t^3
+
32x^2ydr\,t\lambda.
\]

Neither coefficient is fitted from monodromy; both come from the frozen
Cayley--Menger polynomial.

## Finite braid and reflection

Up to nonzero analytic units, the reduced branch equation is

\[
t^3+c\lambda t+O_{\rm wt}(4).
\]

Its discriminant begins at nonzero order \(\lambda^3\). For small
nonzero \(\lambda\), one root is analytic while the other two have
leading behavior

\[
t_\pm\sim\pm\sqrt{-c\lambda}.
\]

A positive loop in \(\lambda\) performs one transposition of
\(t_+\) and \(t_-\). On the \(A_2\) Milnor lattice this braid is one
Picard--Lefschetz reflection, not the order-three Coxeter element of the
generic constant smoothing.

Consequently its Jordan decomposition is finite semisimple:

\[
T_{A_2}=T_{A_2,s},
\qquad
T_{A_2,u}=1,
\qquad
N_{A_2}=0.
\]

This monodromy statement is directly computed from the physical
one-parameter unfolding, using the standard Picard--Lefschetz action of a
single root transposition.

## Simultaneous elliptic monodromy

Because

\[
A=\ell_1\ell_2,
\]

the same loop reaches the Legendre component \(A=0\). The elliptic
boundary undergoes a standard nodal degeneration. On its rank-two
variation,

\[
T_{\rm ell}=\exp N_{\rm ell},
\qquad
\operatorname{rank}N_{\rm ell}=1,
\qquad
N_{\rm ell}^2=0.
\]

This part is inferred from the standard nodal Legendre degeneration already
identified from the source family. It is not newly derived from the finite
surface Taylor expansion.

The absolute nearby-cycle system therefore contains both:

- a finite semisimple reflection sector from the affine \(A_2\) point;
- a unipotent sector from the elliptic boundary.

They must not be conflated.

## Monodromy of the conductor graph quotient

Off the divisor, the same-sheet intersections are the analytic marked
sections

\[
P_\pm:
\qquad
w=\pm\Lambda.
\]

A loop in \(\lambda\) returns each labeled section to itself. The other
wall roots remain simple on the frozen generic locus and likewise admit
analytic labels. Hence the rank-three graph quotient has identity
monodromy around this loop:

\[
T_{H^1(W)}=1.
\]

At \(\lambda=0\), its specialization rank nevertheless drops by one,
as entry 282 computes. Identity monodromy of the punctured local system
does not imply that the specialization or variation map vanishes.

## Spectral consequence for the relative extension

Consider the marked localization extension

\[
0\to H^2(S_E)
\to H^2(S_E\setminus W)
\to H^1(W)(-1)
\to0.
\]

Let \(g_{111}\) denote the top conductor line. Since

\[
T(g_{111})=g_{111},
\]

an extension column from \(g_{111}\) into the \((-1)\)-eigenline
\(V_-\) of the \(A_2\) reflection is removable over any coefficient
field in which \(2\) is invertible. Equivalently,

\[
\operatorname{Ext}^1_{\rm loc}
(\mathbf 1,V_-)=0
\qquad
\text{over }\mathbb Q.
\]

The only unresolved rational target is

\[
H^2(S_E)_{(+1),\rm gen}.
\]

It contains the invariant \(A_2\) direction and the generalized
\(+1\)-eigenspace of the elliptic and algebraic sectors. The broad
top-column problem has therefore been reduced to this single spectral
block.

An integral mod-two gluing can remain and is not excluded by this rational
projector.

## Classification

| Datum | Classification |
|---|---|
| \(\ell_1=0\) | existing signed-energy carrier |
| \(A_2\) reflection line | finite Cayley--Menger coefficient support |
| invariant \(A_2\) line | finite Cayley--Menger coefficient support |
| nodal elliptic \(N\) | Legendre/Gauss--Manin coefficient data |
| disappearing top graph cycle | frozen marked-relative coefficient data |
| possible mod-two gluing | integral occurrence data |
| new carrier stratum | none found |

## Deutsch--Popperian conjecture M2.26

On a generic \(\ell_1=0\) or \(\ell_2=0\) slice, the only nonzero
rational extension of the disappearing top conductor class is generated
inside the generalized \((+1)\)-eigenspace by the canonical nearby-cycle
maps of the frozen pair \((S_E,W)\). No component of the extension lands
in the finite reflection line, and no new carrier stratum is required.

The finite falsifier is the \((+1)\)-block specialization matrix. A
nonzero target outside the invariant \(A_2\), elliptic nearby-cycle, and
algebraic Tate/Kummer pieces falsifies the conjecture.

## Next hostile test

Construct the local semistable model of the pair on \(\ell_1=0\) and
compute only the surviving \((+1)\) block:

1. the specialization and variation maps of the top conductor class;
2. the joint nilpotent operator on the relative cohomology;
3. the projection to the invariant \(A_2\) and elliptic weight-graded
   pieces;
4. the integral mod-two residue after rational splitting.

Then repeat by symmetry on \(\ell_2=0\). The non-isolated
\(E=0\) split degeneration remains a separate global calculation.
