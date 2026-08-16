---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Four Enhanced-Point Rees Classes Have Smith Type 1-2-2

## Result

The four source-generated enhanced points of the total-energy split model
carry a canonical occurrence/deck-orbit higher-Rees lattice

\[
\mathcal H_{\rm exc}
=
\mathbb Z\langle h_{++},h_{+-},h_{-+},h_{--}\rangle.
\]

Their source-normalized leading functionals do not give four independent
directions in the nine-master algebraic kernel. After stripping the common
physical Leray scalar and the invertible kinematic monomials, the realization
map is

\[
\boxed{
\Phi_{\rm exc}
=
\begin{pmatrix}
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},
}
\]

in point order

\[
(++,+-,-+,--)
\]

and target order

\[
(y e_3,\;x e_5,\;e_6).
\]

It has

\[
\boxed{
\ker\Phi_{\rm exc}
=
\mathbb Z(1,1,1,1),
}
\]

and Smith normal form

\[
\boxed{\operatorname{SNF}(\Phi_{\rm exc})=(1,2,2).}
\]

Therefore

\[
\boxed{
\operatorname{rank}\operatorname{im}\Phi_{\rm exc}=3,
\qquad
\operatorname{coker}\Phi_{\rm exc}
\simeq(\mathbb Z/2)^2.
}
\]

The same two occurrence parities already govern the integral conductor
extension of Entry 280. Thus the four enhanced germs add a rank-three
algebraic higher-Rees layer plus the diagonal relation; their only saturation
defect is the existing pair of occurrence-identification factors of two.
No new carrier stratum or new torsion prime appears.

## Frozen sign-resolved germs

Index the four enhanced points by

\[
P_{\epsilon\delta}:
\qquad
(a,b)=(\epsilon y,\delta x),
\qquad
\epsilon,\delta\in\{\pm1\}.
\]

Use the sign-resolved weighted coordinates

\[
E=\tau^2,
\qquad
a=\epsilon\bigl(y+\tau^2r\bigr),
\qquad
b=\delta\bigl(x-\tau^2r+\tau^3n\bigr).
\]

The tangent relation is

\[
\epsilon(a-\epsilon y)+
\delta(b-\delta x)=O(\tau^3).
\]

Because the Cayley--Menger family and the source double-pole numerator depend
on \(a^2\) and \(b^2\), their weighted leading terms are independent of
\((\epsilon,\delta)\):

\[
K
=
\tau^6
\left[
4x^2y^2n^2+
8xy(x+y)(r^2-1)
\right]
+O(\tau^7),
\]

\[
K_1
=
16xy(x+y)\tau^4+O(\tau^5).
\]

No sign-dependent normalization has been introduced.

## Orientation produces the three characters

The global source orientation is \(da\wedge db\). In the displayed chart,

\[
da\wedge db
=
\epsilon\delta\,
\tau^5\,dr\wedge dn.
\]

The three source double-pole masters have numerators proportional to

\[
(aK_1,\;bK_1,\;K_1).
\]

At \(P_{\epsilon\delta}\), multiplication by the Jacobian sign gives

\[
\epsilon\delta(\epsilon y,\delta x,1)
=
(\delta y,\epsilon x,\epsilon\delta).
\]

Entry 226 fixes the common physical Leray coefficient at the positive chart.
Transport through the frozen deck/occurrence action therefore yields

\[
\boxed{
\Lambda_{\epsilon\delta}
=
-\frac{2\pi^2}{xy}
\left(
\delta y\,e_3+
\epsilon x\,e_5+
\epsilon\delta\,e_6
\right),
}
\]

in the equation-(58) de Rham normalization. The overall common wavefunction
prefactor remains outside the source normalization exactly as in Entry 226.

For \((\epsilon,\delta)=(+,+)\), this reduces to

\[
-\frac{2\pi^2}{xy}(y e_3+x e_5+e_6),
\]

the previously computed physical-corner functional.

The three target rows are the nontrivial sign characters

\[
\delta,\qquad\epsilon,\qquad\epsilon\delta.
\]

The trivial character is absent.

## Kernel

Summing all four columns gives zero:

\[
\sum_{\epsilon,\delta}
\delta
=
\sum_{\epsilon,\delta}
\epsilon
=
\sum_{\epsilon,\delta}
\epsilon\delta
=0.
\]

Hence

\[
h_{++}+h_{+-}+h_{-+}+h_{--}
\in\ker\Phi_{\rm exc}.
\]

Any three columns have determinant \(\pm4\), so the matrix has rank three.
The kernel is therefore exactly the primitive diagonal line:

\[
\boxed{
\ker\Phi_{\rm exc}
=
\mathbb Z(h_{++}+h_{+-}+h_{-+}+h_{--}).
}
\]

This is an occurrence-orbit relation. It does not assert that four
independent physical integration chains are present; the frozen physical
Leray germ selects one chamber, while the other points are its
occurrence/deck companions.

## Smith calculation

The gcd of all entries is \(1\). The gcd of all \(2\times2\) minors is
\(2\). The four maximal minors are

\[
(4,-4,4,-4),
\]

so their gcd is \(4\). Consequently the invariant factors are

\[
d_1=1,
\qquad
d_1d_2=2,
\qquad
d_1d_2d_3=4,
\]

and therefore

\[
\boxed{(d_1,d_2,d_3)=(1,2,2).}
\]

Equivalently, if the target coordinates are \((u,v,w)\), then

\[
\operatorname{im}\Phi_{\rm exc}
=
\{(u,v,w)\in\mathbb Z^3:
u\equiv v\equiv w\pmod2\}.
\]

The two quotient parities may be represented by

\[
u-w\pmod2,
\qquad
v-w\pmod2.
\]

They are precisely the two independent occurrence axes inherited from the
two frozen walls.

## Relation to conductor gluing

Entry 280 found

\[
0\to
\mathcal K_{\Delta_{W_1}}\oplus
\mathcal K_{\Delta_{W_2}}
\to H^1(W)
\to\mathbb Z_{\rm top}
\to0
\]

with extension class

\[
(1,1)\in(\mathbb Z/2)^2.
\]

The present Smith cokernel is not a new torsion group that merely happens to
have the same order. Its two parity coordinates are induced by the same two
sign flips \(\epsilon\) and \(\delta\). The top half-sum defect is nonzero
on both parity axes, reproducing the \((1,1)\) pattern.

What is established is compatibility of the two integral occurrence
lattices. A canonical identification of the full conductor extension with
the higher-Rees realization still requires the physical relative-chain
pairing; it is not inferred solely from isomorphic cokernels.

## Nearby-cycle type

Each local exceptional class has, by Entry 226,

\[
T_{\rm exc}=1,
\qquad
N_{\rm exc}=0.
\]

Thus

\[
\mathcal H_{\rm exc}/\ker\Phi_{\rm exc}
\]

is a rank-three algebraic Tate higher-Rees grade. It is distinct from the
rank-four logarithmic nilpotent image of Entry 300.

The current filtered picture at generic nonsoft total energy is therefore:

\[
\begin{array}{c|c|c}
\text{layer}&\text{rank}&\text{type}\\
\hline
\operatorname{im}N_E^{(12)}&4&
1\text{ elliptic}+3\text{ algebraic logarithmic}\\
\operatorname{im}\Phi_{\rm exc}&3&
\text{algebraic higher-Rees/Cut--nearby}\\
\ker\Phi_{\rm exc}&1&
\text{diagonal occurrence relation}\\
\operatorname{coker}\Phi_{\rm exc}&(\mathbb Z/2)^2&
\text{occurrence saturation defect}
\end{array}
\]

No splitting between the logarithmic and higher-Rees layers is claimed.

## Classification

| Datum | Classification |
|---|---|
| four enhanced points | frozen occurrence-resolved coefficient support |
| \(\mathcal H_{\rm exc}\) | higher-Rees local Tate lattice |
| sign matrix | source orientation and double-pole numerator realization |
| rank-three image | algebraic Tate/Kummer coefficient data |
| diagonal kernel | global occurrence-orbit relation |
| \((\mathbb Z/2)^2\) cokernel | existing conductor/occurrence saturation |
| new carrier datum | none |

## Deutsch--Popperian update M2.44

The hard-to-vary claim

\[
\text{the four enhanced germs require four independent coefficient
directions or a new global gluing generator}
\]

is falsified.

The smaller surviving theorem is

\[
\boxed{
\text{the four germs realize the augmentation-zero three-character lattice,
with Smith type }(1,2,2)\text{ and no new carrier datum.}
}
\]

## Scope boundary

This result does not yet compute:

1. the extension class between the higher-Rees image and the logarithmic
   nearby-cycle filtration;
2. the pairing with the global physical relative chain;
3. extension through soft support or collisions of enhanced points;
4. cyclic sewing among the three \(q_{\mathcal G_{ij}}\) residue sectors;
5. a global integral basis of the complete rank-twelve variation.

## Next hostile test

Construct the source intersection/duality pairing between

\[
\operatorname{im}\Phi_{\rm exc}
\quad\text{and}\quad
\langle
\Theta_{101}^{\rm fix},
\Theta_{110}^{\rm fix},
e_6/[8s]
\rangle.
\]

Determine whether its integral matrix is unimodular after adjoining exactly
the two already forced half-sum corrections. A residual denominator, kernel,
or support divisor not generated by the frozen walls and occurrence
identifications is the next finite falsifier of global assembly.
