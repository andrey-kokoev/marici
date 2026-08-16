---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Enhanced Rees and Conductor Lattices Coincide Through a Unimodular Quotient

## Result

The integral gluing left open in Entries 300--301 is fixed by an exact
factorization of the two independently derived source matrices.

Let

\[
\Phi_{\rm exc}
=
\begin{pmatrix}
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix}
\]

be the enhanced-point realization of Entry 301, and let

\[
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix}
\]

be the horizontal primitive-conductor intertwiner of Entry 308. Then

\[
\boxed{\Phi_{\rm exc}=JK}
\]

with

\[
\boxed{
K=
\begin{pmatrix}
0&0&1&-1\\
0&1&0&-1\\
1&-1&-1&1
\end{pmatrix}.
}
\]

The map \(K\) is a unimodular presentation of the augmentation quotient:

\[
\ker K=\mathbb Z(1,1,1,1),
\qquad
\operatorname{coker}K=0.
\]

Thus

\[
\boxed{
\mathbb Z^4/\mathbb Z(1,1,1,1)
\xrightarrow[\sim]{\,K\,}
\mathbb Z\langle
g_{101},g_{110},\widetilde g_{111}
\rangle .
}
\]

The enhanced higher-Rees lattice and the primitive conductor lattice are
therefore not merely abstract lattices with the same Smith type. They are
canonically related by the source occurrence quotient, and their embeddings
into the enhanced character coordinates are literally equal.

## Frozen inputs

No pairing or projector is fitted.

Entry 301 derives \(\Phi_{\rm exc}\) from:

- the four resolved enhanced points \(P_{\epsilon\delta}\);
- the source orientation \(da\wedge db\);
- the source double-pole numerators \((aK_1,bK_1,K_1)\);
- the common physical Leray scalar.

Entry 308 derives \(J\) from:

- the primitive conductor basis
  \(B=(g_{101},g_{110},\widetilde g_{111})\);
- the two occurrence involutions;
- the half-Kummer connection;
- the horizontal identity \(A_{\rm exc}J=JA_B\).

Both matrices use the same enhanced character order

\[
(\delta,\epsilon,\epsilon\delta).
\]

The common invertible kinematic monomials and Leray scalar remain outside
the integral incidence matrix, as frozen in Entry 301.

## Exact factorization

Writing columns in point order \((++,+-,-+,--)\), \(K\) sends

\[
\begin{array}{c|c}
++&(0,0,1)\\
+-&(0,1,-1)\\
-+&(1,0,-1)\\
--&(-1,-1,1)
\end{array}
\]

in the primitive conductor basis. Multiplication by \(J\) gives respectively

\[
(1,1,1),\quad
(-1,1,-1),\quad
(1,-1,-1),\quad
(-1,-1,1),
\]

which are exactly the four columns of \(\Phi_{\rm exc}\).

The four maximal minors of \(K\), ordered by omitted enhanced point, are

\[
\boxed{(1,-1,1,-1).}
\]

Their gcd is one, so \(K\) is surjective over \(\mathbb Z\). Its columns sum
to zero, and its rank is three; hence its kernel is exactly the primitive
diagonal occurrence relation.

## Common image and the two half-sums

Entry 308 proves

\[
\operatorname{im}J
=
\{(u,v,w)\in\mathbb Z^3:
u\equiv v\equiv w\pmod2\}.
\]

Since \(K\) is surjective,

\[
\boxed{
\operatorname{im}\Phi_{\rm exc}
=
\operatorname{im}J.
}
\]

Both cokernels are therefore the same, not just isomorphic:

\[
\mathbb Z^3/\operatorname{im}\Phi_{\rm exc}
=
\mathbb Z^3/\operatorname{im}J
\simeq
(\mathbb Z/2)^2.
\]

The two parity defects are exactly the two pre-existing wall-occurrence
identifications. Passing to the primitive conductor frame by \(J^{-1}\)
uses precisely those two half-sums and leaves the unimodular map \(K\).
There is no residual denominator, third torsion class, or additional gluing
generator.

## Pairing interpretation

The corrected duality type from Entry 306 is logarithmic
residue/Leray-tube duality, not naive contraction of ambient master
coordinates. In the orientation-twisted conductor frame, the residue
connection is horizontal by Entry 308.

After removing the common source-fixed Leray scalar and invertible kinematic
units, the incidence part of the pairing between the enhanced occurrence
quotient and the primitive conductor quotient is therefore \(K\). Because
\(K\) induces an integral isomorphism, this normalized pairing is
unimodular.

This statement identifies the integral occurrence gluing. It does not assert
that the full rank-twelve variation splits: the logarithmic nilpotent image,
the elliptic quotient, and the higher-Rees filtration remain distinct
filtered layers.

## Consequence for the global extension

The rank-three algebraic part of the total-energy logarithmic image,

\[
\left\langle
\Theta_{101}^{\rm fix},
\Theta_{110}^{\rm fix},
\frac{e_6}{8(x+y)}
\right\rangle,
\]

is indexed by the same primitive conductor basis as the enhanced-point
higher-Rees quotient. The four enhanced germs supply its occurrence
presentation; the diagonal sum is the sole relation; \(J\) supplies the
already-derived integral half-Kummer embedding.

Hence the proposed extra extension between these two rank-three algebraic
layers is not an independent class. Its integral gluing is exhausted by

\[
\boxed{
\text{augmentation quotient}
+
\text{the two existing occurrence half-sums}.
}
\]

The elliptic vanishing line remains separate by infinity-Gysin type.

## Classification

| Datum | Classification |
|---|---|
| \(K\) | canonical augmentation-quotient isomorphism |
| \(J\) | horizontal half-Kummer conductor embedding |
| \(\Phi_{\rm exc}=JK\) | enhanced-point realization |
| \((\mathbb Z/2)^2\) | existing two-wall occurrence saturation |
| algebraic log/Rees gluing | exhausted by frozen occurrence data |
| new support divisor | none |
| new carrier datum | none |

## Deutsch--Popperian update M2.55

The hard-to-vary claim

\[
\text{the higher-Rees layer requires an additional integral extension class
beyond the conductor half-sums}
\]

is falsified by the exact factorization \(\Phi_{\rm exc}=JK\) with
unimodular \(K\).

The smaller surviving theorem is

\[
\boxed{
\text{the algebraic logarithmic and enhanced higher-Rees layers have one
common source-occurrence lattice, with no gluing beyond the established
two half-sums.}
}
\]

## Next hostile test

Extend this identification through

\[
xy(x+y)=0
\]

and through intersections with the conductor and elliptic discriminants.
Compute the joint nearby-cycle/Smith data on each corner. A residual
torsion prime, support divisor, or vanishing class not generated by soft
support, the two wall occurrences, and the Legendre node is the next finite
falsifier of the shared-carrier conjecture.
