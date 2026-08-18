---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Unique Elliptic Top Class Has a Canonical Residue Boundary

> **Correction (Entry 574).**  The canonical geometric Cousin face vector is
> \((1,-1,1)\), as already proved in Entry 341.  The vector \((1,-1,0)\)
> below incorrectly substitutes the zero proper Möbius grade for the existing
> lower-pair stratum.  Retain the transverse-intersection and
> Cayley--Menger identities; disregard the claimed proper-grade boundary.

## Record

Entry 340 found one proper support class for the frozen homogeneous family

\[
\{q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathcal G_{12}}\}
\]

but left its deletion arrows unconstructed.  This entry computes the local
Cartier/Cousin boundary from the source denominators themselves.  No splitting
of the rank cube and no new carrier cell is introduced.

Use fiber coordinates

\[
(c,a,b)=(y_{12},y_{23},y_{31})
\]

and source hyperplanes

\[
q_{\mathfrak g_1}=X_1+c+b,
\qquad
q_{\mathfrak g_2}=X_2+c+a,
\qquad
q_{\mathcal G_{12}}=E+c.
\]

## Clean triple section

Their unique intersection is

\[
\boxed{
c=-E,
\qquad
a=X_1+X_3,
\qquad
b=X_2+X_3.
}
\]

In the ordered normal coordinates
\((q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathcal G_{12}})\),

\[
\det
\frac{\partial(q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathcal G_{12}})}
{\partial(c,a,b)}=-1.
\]

Thus the three marked divisors meet transversely with unit normal Jacobian.

## Cayley--Menger restriction

Exact symbolic substitution into the source-normalized Cayley--Menger
polynomial gives

\[
\boxed{
K\big|_{q_{\mathfrak g_1}=q_{\mathfrak g_2}=q_{\mathcal G_{12}}=0}
=
E^2
(X_2+X_3-X_1)^2
(X_1+X_3-X_2)^2.
}
\]

Hence the twist is a unit along the generic triple section away from three
already frozen energy letters.  The top class does not require a new branch
or incidence divisor.

## Oriented proper-support boundary

The Boolean support ranks from Entry 340 are

\[
m_{111}=1,
\qquad
(m_{110},m_{101},m_{011})=(1,1,0).
\]

Purity at the clean triple section identifies the unique top associated
grade with its iterated logarithmic residue.  With denominator order

\[
(q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathcal G_{12}}),
\]

the Cousin sign convention gives the proper-grade boundary

\[
\boxed{
\partial_{111}^{\rm geom}=(1,-1,1):
\operatorname{gr}_{111}\mathcal M
\longrightarrow
\operatorname{gr}_{110}\mathcal M
\oplus
\operatorname{gr}_{101}\mathcal M
\oplus
\operatorname{gr}_{011}\mathcal M.
}
\]

All three components are geometric residues.  The lower-pair stratum remains
present even though its proper Möbius grade is zero.  There is no canonical
projection of the geometric Cousin boundary to the list of proper grades.

## Classification

- triple section: existing denominator-incidence carrier;
- normal orientation: ordinary Cartier/Cousin datum;
- restricted Cayley--Menger twist: square of existing energy letters;
- unique top class: sector-specific relative coefficient class;
- deletion arrows: source-derived residue/Gysin maps;
- new cosmology-specific carrier datum: none.

This closes the first arrow requested in Entry 340 at associated-grade level
and strengthens H2:

\[
\boxed{
\text{shared carrier and support calculus}
+
\text{sector-specific filtered coefficient objects}.
}
\]

It does not prove that the full rank-21 module splits by support.

## Next falsifier

Construct the extension one step below the associated grade: lift the two
unit mixed-face residues through the deletion-closed modules of ranks 18 and
then compare their common image in the rank-16
\(q_{\mathcal G_{12}}\)-closed module.  The required test is the Cousin
identity on actual twisted de Rham representatives, not only on support
ranks.  Failure of that identity would localize the missing datum in the
coefficient extension; it would justify a new carrier object only if the
frozen denominator intersections cannot supply the required homotopy.

## Evidence

- `research/benincasa/marici-gm/src/bin/top_sector_residue_boundary.rs`;
- `research/benincasa/top-sector-residue-boundary.json`;
- Entry 340 and its exact two-prime deletion cube.

## Outcome contract

~~~json
{
  "claim": "The unique proper three-denominator class lacks a source-derived deletion boundary.",
  "status": "falsified_at_associated_grade",
  "triple_normal_jacobian": -1,
  "K_at_triple": "E^2 (X2+X3-X1)^2 (X1+X3-X2)^2",
  "geometric_boundary": [1, -1, 1],
  "new_carrier_datum": false,
  "remaining_problem": "Lift the residue boundary through the rank-18 mixed modules and verify the Cousin homotopy in the rank-16 q-closed module."
}
~~~
