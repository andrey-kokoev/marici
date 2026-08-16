---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Primitive Two-Wall Extension Requires a Second-Order Rees Gauge

## Result

The primitive two-wall logarithmic class fails to close in a
simple-pole/Fuchsian ansatz. At the exact generic fiber

\[
(x,y)=(2,3),
\qquad
z=E-5,
\]

the relative Griffiths--Dwork system becomes consistent only after allowing
an \(E^{-2}\) coefficient. Its exact-form-gauge-invariant leading term in
the raw source basis is

\[
\boxed{
\operatorname{Lead}^{(-2)}_E(\Theta_{111}^{\rm raw})
=
\frac18 e_6.
}
\]

The class \(e_6\) lies in the already established algebraic kernel
\(\mathcal T_7\) and has zero infinity-Gysin image. Thus the raw
source-normalized lift requires a higher-normal algebraic correction on the
frozen carrier, not a new carrier stratum. This leading term is fixed modulo
the tested exact-form gauge; it is not yet claimed to be invariant under a
meromorphic Rees change of basis.

## Frozen top lift

Retain the two source walls

\[
l_1=b+x-E,
\qquad
l_2=a+y-E.
\]

The primitive same-sheet occurrence class is represented by

\[
\Omega_{111}
=
\frac{da\wedge db}{l_1l_2\sqrt{K_E}}.
\]

Its iterated residues at the two points \(P_\pm\) differ by the sign of
\(w(P_\pm)=\pm\Lambda\). Therefore this lift is fixed by the existing
two-wall incidence geometry; no new cell or support summand is introduced.

Differentiating gives

\[
\partial_E\Omega_{111}
=
\left(
\frac1{l_1^2l_2\sqrt K}
+
\frac1{l_1l_2^2\sqrt K}
-
\frac{\partial_EK}{2l_1l_2K^{3/2}}
\right)da\wedge db.
\]

After clearing \(l_1^2l_2^2K^{3/2}\), the numerator is

\[
(l_1+l_2)K-\frac{l_1l_2}{2}\partial_EK.
\]

## Frozen relative basis and exact calculus

The reduction uses exactly the expected rank-twelve basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9)
\]

and exact one-forms over the four predeclared denominator strata

\[
l_1l_2\sqrt K,
\qquad
l_1\sqrt K,
\qquad
l_2\sqrt K,
\qquad
\sqrt K.
\]

Polynomial vector fields of total degree at most four were used for the
initial reduction and then enlarged to degree five. No additional
cohomology class, carrier cell, or fitted support term was adjoined.

## First-jet falsification

If every connection and exact-form coefficient is restricted to

\[
E^{-1}c_{-1}+c_0+O(E),
\]

the exact cleared system has

\[
148
\]

polynomial equations in \(264\) Laurent-jet variables. Its reduced system
contains a contradictory row:

\[
\boxed{\text{simple-pole system inconsistent}.}
\]

This is a direct finite falsifier of first-jet/Fuchsian closure for the raw
source-normalized top lift.

## Second-order closure

Allow instead

\[
E^{-2}c_{-2}+E^{-1}c_{-1}+c_0+O(E).
\]

The degree-four exact system has

\[
222
\]

polynomial equations in \(396\) variables, rank \(157\), and no
contradictory row. Enlarging to degree five gives 261 equations in 540
variables, rank 194, and again no contradictory row. Every fixed
second-order and first-order coordinate below is unchanged.

At order \(E^{-2}\), the quotient coordinates are forced to vanish:

\[
c_{111}^{(-2)}
=
c_{101}^{(-2)}
=
c_{110}^{(-2)}
=
0.
\]

The fixed absolute coordinates are

\[
\boxed{
e_6^{(-2)}=\frac18,
\qquad
e_7^{(-2)}=e_8^{(-2)}=e_9^{(-2)}=0.
}
\]

The remaining displayed coordinates in the machine certificate vary with
the exact-form gauge and are not promoted to extension invariants.

Hence the double pole is not quotient monodromy. It is a pure absolute
algebraic extension term:

\[
\boxed{
E^{-2}\frac18e_6
\subset
\mathcal T_7.
}
\]

## First-order residue

At order \(E^{-1}\), the fixed quotient coordinates are

\[
\boxed{
c_{111}^{(-1)}=1,
\qquad
c_{101}^{(-1)}=-\frac16,
\qquad
c_{110}^{(-1)}=-\frac14.
}
\]

The fixed final-block tail is

\[
\left(
e_7^{(-1)},
e_8^{(-1)},
e_9^{(-1)}
\right)
=
\left(
-\frac1{288},
\frac1{720},
-\frac1{720}
\right).
\]

At \(x=2,y=3,E=0\), its infinity-Gysin image is

\[
-\frac1{288}
+\frac{9}{2}\frac1{720}
+\frac{4}{2}\left(-\frac1{720}\right)
=0
\]

in the \(\omega_0\) row and

\[
-\frac{4}{2}\frac1{720}
-\frac{4}{2}\left(-\frac1{720}\right)
=0
\]

in the \(\omega_2\) row. The fixed first-order tail is therefore algebraic
as well.

## Relation to the earlier second-Rees warning

Entry 128 established that the algebraic quartic begins at second ordinary
normal order:

\[
\mathcal Q
=
-16p^2-8pE^2+O(E^3).
\]

Entry 287 found that the local surface smoothing at the physical enhanced
point begins only at third order. The present calculation separates these
facts:

- the frozen carrier smoothing is not second order;
- the primitive marked relative connection is second order;
- its first nonzero \(E^{-2}\) term lands in the algebraic coefficient
  kernel.

Thus the required second-order Rees regularization has acquired a candidate
geometric home:

\[
\boxed{
\text{primitive two-wall relative extension inside }\mathcal T_7.
}
\]

The double pole can in principle be removed by a meromorphic basis change
of the form \(\Omega_{111}mapstoOmega_{111}+E^{-1}v\). Therefore it is
not, by itself, the intrinsic second Rees graded class. What is established
is that any such regularization starts with the frozen algebraic
\(e_6\)-line. This does not yet identify \(\mathcal Q\) with the
regularized extension coefficient.

## Classification

| Structure | Geometric home |
|---|---|
| \(g_{111}^{\rm top}\) | existing primitive two-wall occurrence cycle |
| simple-pole failure | higher-normal relative-connection effect |
| raw \(E^{-2}e_6/8\) | algebraic kernel \(\mathcal T_7\); Rees-gauge input |
| fixed \(E^{-1}\) tail | algebraic kernel \(\mathcal T_7\) |
| elliptic modification | none |
| new carrier datum | none |

## Deutsch--Popperian update M2.35

The hard-to-vary claim

\[
\text{the full marked total-energy connection is controlled by logarithmic
nearby cycles plus first normal jets}
\]

is falsified at an exact generic fiber.

The smaller surviving conjecture is

\[
\boxed{
\text{the primitive two-wall occurrence class requires a second-order
algebraic Rees regularization inside the frozen relative coefficient system.}
}
\]

This is the first direct relative-connection evidence matching the earlier
integrated-loop warning that first normal order is insufficient.

## Qualifications

The result is exact but deliberately narrow:

1. it is computed at one generic rational fiber \((x,y)=(2,3)\);
2. degree-four and degree-five exact fields agree on every fixed Laurent
   coordinate;
3. the universal \(\mathbb Q(x,y)\) coefficient remains uncomputed;
4. meromorphic Rees-gauge reduction to a logarithmic connection remains
   uncomputed;
5. the physical period/duality pairing remains unconstructed.

## Next hostile test

Repeat the second-order reduction at independent generic fibers and degree
five. Reconstruct or falsify the universal coefficient of \(e_6^{(-2)}\).
Then perform the canonical meromorphic Rees regularization and test whether
the source quartic \(\mathcal Q\) controls the resulting logarithmic
extension class or neither.
