---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Orientation Twist Identifies the Conductor and Enhanced Rees Lattices

> **Type correction (Entries 306--307).** The integral intertwiner \(J\) and
> all representation-theoretic conclusions below are unchanged. References
> to a bulk relative Stokes or Griffiths--Dwork lift are superseded by the
> logarithmic-residue Gauss--Manin connection and Leray-tube pairing.

## Result

The integral conductor quotient of Entry 280 and the enhanced-point
higher-Rees image of Entry 301 are canonically the same occurrence lattice
after tensoring the conductor quotient with the source orientation line.

Let

\[
\mathfrak o_{ab}
=
\mathbb Z_{\epsilon\delta}
\]

be the determinant character supplied by

\[
da\wedge db
\longmapsto
\epsilon\delta\,da\wedge db
\]

on the sign-resolved enhanced charts. Then

\[
\boxed{
\mathfrak o_{ab}\otimes H^1(W;\mathbb Z)
\simeq
\operatorname{im}\Phi_{\rm exc}.
}
\]

This is an integral equivariant isomorphism, not merely an equality of
ranks or Smith groups.

In the conductor basis

\[
(g_{101},g_{110},\widetilde g_{111})
\]

and the enhanced target coordinates

\[
(u,v,w)
=
(\chi_\delta,\chi_\epsilon,\chi_{\epsilon\delta}),
\]

the map is

\[
\boxed{
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix}.
}
\]

Equivalently,

\[
g_{101}\mapsto(2,0,0),
\qquad
g_{110}\mapsto(0,2,0),
\qquad
\widetilde g_{111}\mapsto(1,1,1).
\]

Its image is exactly

\[
\boxed{
\{(u,v,w)\in\mathbb Z^3:
u\equiv v\equiv w\pmod2\},
}
\]

the Smith lattice found independently from the four enhanced points.

## Why an orientation twist is necessary

The two conductor roots on \(W_1\) are labelled by the sign of \(a\), so
their swap is the \(\epsilon\)-character. The two roots on \(W_2\) are
labelled by the sign of \(b\), so their swap is the \(\delta\)-character.
Rationally, Entry 280 gives

\[
H^1(W)_{\mathbb Q}
\simeq
\mathbb Q_\epsilon
\oplus
\mathbb Q_\delta
\oplus
\mathbb Q_1.
\]

Entry 301 gives the enhanced characters

\[
\operatorname{im}\Phi_{\rm exc,\mathbb Q}
\simeq
\mathbb Q_\delta
\oplus
\mathbb Q_\epsilon
\oplus
\mathbb Q_{\epsilon\delta}.
\]

Without a twist these representations are not isomorphic: the conductor
quotient contains a trivial character, while the enhanced image does not.
Tensoring by the source orientation character gives

\[
\epsilon\delta\otimes
(\epsilon,\delta,1)
=
(\delta,\epsilon,\epsilon\delta),
\]

which is exactly the enhanced character list in its source-derived target
order.

Thus the orientation factor in Entry 301 is structural. Omitting it creates
a false representation mismatch.

## Integral half-sum becomes the Smith congruence

The rational invariant conductor lift is

\[
g_{111}^{\rm inv}
=
\widetilde g_{111}
-\frac12(g_{101}+g_{110}).
\]

Write a conductor vector as

\[
a g_{101}+b g_{110}+c\widetilde g_{111}.
\]

In the rational character frame

\[
(g_{101},g_{110},g_{111}^{\rm inv}),
\]

its coordinates are

\[
\left(a+\frac c2,\ b+\frac c2,\ c\right).
\]

Clearing the two forced half-sums gives

\[
(u,v,w)
=
(2a+c,\ 2b+c,\ c).
\]

Hence

\[
u\equiv v\equiv w\pmod2.
\]

Conversely, every triple satisfying these congruences has

\[
c=w,\qquad
a=\frac{u-w}{2},\qquad
b=\frac{v-w}{2}
\]

in \(\mathbb Z\). Therefore \(J\) is a bijection onto the complete enhanced
Smith lattice, not a proper sublattice of it.

The two parity defects

\[
u-w\pmod2,
\qquad
v-w\pmod2
\]

are literally the two conductor half-sum obstructions. This upgrades Entry
301's compatibility statement to a canonical orientation-twisted
identification.

## Equivariance check

Entry 280 gives conductor monodromies

\[
M_1=
\begin{pmatrix}
-1&0&-1\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
M_2=
\begin{pmatrix}
1&0&0\\
0&-1&-1\\
0&0&1
\end{pmatrix}.
\]

The orientation character is \(-1\) under either sign flip, so the twisted
matrices are \(-M_1\) and \(-M_2\).

On enhanced coordinates,

\[
D_\epsilon=\operatorname{diag}(1,-1,-1),
\qquad
D_\delta=\operatorname{diag}(-1,1,-1).
\]

Direct integer multiplication gives

\[
\boxed{
D_\epsilon J=J(-M_1),
\qquad
D_\delta J=J(-M_2).
}
\]

Thus \(J\) intertwines both frozen occurrence actions over \(\mathbb Z\).

## Relation to the moving-wall logarithms

Entry 304 fixes the source-normalized endpoint forms

\[
-\frac{dr}{2xy(r-1)},
\qquad
-\frac{dr}{2xy(r+1)}.
\]

These identify the \(W_1\) and \(W_2\) root occurrences with the two
exceptional endpoints. The present orientation twist then supplies the
Jacobian sign needed to compare their conductor cycles with the enhanced
Leray functionals.

Therefore the lattice-level physical-chain comparison is now fixed. What
remains is the residue Gauss--Manin top extension and its support-sensitive
Leray pairing, not an ambiguity in the integral occurrence lattice.

## Classification

| Datum | Classification |
|---|---|
| \(\mathfrak o_{ab}\) | source orientation coefficient line |
| \(J\) | canonical occurrence-equivariant lattice comparison |
| factors \(2\) in \(J\) | existing conductor half-sum/saturation defect |
| diagonal column \((1,1,1)\) | primitive top lift before rational splitting |
| enhanced Smith congruences | image of the integral conductor extension |
| new carrier datum | none |

## Deutsch--Popperian update M2.48

The hard-to-vary claim

\[
\text{the conductor quotient and enhanced Rees lattice can be compared
without an orientation coefficient}
\]

is falsified by their different rational character multisets.

The smaller surviving theorem is

\[
\boxed{
\text{after the source-forced orientation twist, they are canonically
isomorphic as integral occurrence modules.}
}
\]

This is direct evidence for the current H2 architecture: the carrier and
occurrence calculus are shared, while the comparison includes a
layer-specific coefficient twist already present in the source measure.

## Scope boundary

This entry proves the integral representation/lattice comparison. It does
not compute:

- the primitive top-class residue connection and Leray-tube integrals;
- the rational kinematic scalar matrix multiplying \(J\);
- extension through soft or simultaneous discriminant support;
- cyclic sewing of the three \(q_{\mathcal G_{ij}}\) sectors.

## Next hostile test

Compute the primitive top-class connection in the orientation-twisted frame.
After stripping the two Kummer scalars of Entry 307 and the matrix \(J\), its
Leray-tube pairing must be unimodular and have poles only on the frozen
energy, conductor, Cayley--Menger, soft, and already admitted coefficient
supports. Any residual lattice denominator or new divisor is the next
finite falsifier.
