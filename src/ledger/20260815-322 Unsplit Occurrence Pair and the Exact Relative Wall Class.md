---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Unsplit Occurrence Pair and the Exact Relative Wall Class

> Correction: entry 234 supersedes the claimed complete primitive below.
> The displayed exactness applies to the lower-denominator factor before the
> nonconstant Cayley--Menger/master factor is restored. The zero logarithmic
> residue survives, but for the complete-integrand reason proved in entry 234.

## Record

Status: the complete common lower-denominator factors have been restored at
the exceptional corner. The two individual occurrence terms have
hierarchy-dependent simple-pole currents, but their source-defined unsplit
sum has zero simple residue and a canonical exact leading two-form. The
remaining datum is relative wall support, not an absolute delta class.

No denominator, carrier incidence, support summand, regulator hierarchy,
projector, or normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{each lower-denominator occurrence admits an independent canonical
physical boundary lift through the exceptional corner.}
}
\]

The finite falsifier was a hierarchy-dependent individual residue together
with a hierarchy-independent zero residue for the frozen source sum.

## Primary contour theorem

Albayrak--Benincasa--Duaso Pueyo, arXiv:2305.19686v2,
equations (4.14)--(4.18), proves that reduced spurious poles can involve

\[
\alpha\epsilon_{hat b}-\beta\epsilon_{hat a},
\qquad \alpha,\beta>0,
\]

whose sign requires an arbitrary regulator hierarchy. The corresponding
residue of the canonical form is nevertheless zero because the hyperplane is
a spurious boundary rather than a facet.

Entry 231 identifies exactly this sign ambiguity for the two lower
occurrences after the ordered \(q_{\mathcal G_{12}}\) residue. The primary
theorem says not to turn those two triangulation terms into independently
canonical physical currents.

## Complete frozen denominator expansion

At the positive marked corner use

\[
E=\tau^2,
\qquad
X_3=E-x-y,
\]

\[
a=y+\tau^2r,
\qquad
b=x-\tau^2r+\tau^3n.
\]

On the \(q_{\mathcal G_{12}}\)-residue surface, the three denominators
common to both source occurrences are

\[
q_{\mathfrak g_1}
=2x-\tau^2(r+1)+\tau^3n,
\]

\[
q_{\mathfrak g_2}
=2y+\tau^2(r-1),
\]

\[
\boxed{
q_{\mathfrak g_3}
=\tau^2(1+\tau n).
}
\]

The occurrence-specific denominators are

\[
q_{\mathfrak g_{31}}=\tau^2r,
\qquad
q_{\mathfrak g_{23}}=\tau^2(-r+\tau n).
\]

Thus \(q_{\mathfrak g_1}\) and \(q_{\mathfrak g_2}\) are units at
generic nonsoft kinematics, while \(q_{\mathfrak g_3}\) supplies one
additional existing total-normal factor.

## Unsplit cancellation

Each full lower factor

\[
\frac1{
q_{\mathfrak g_1}q_{\mathfrak g_2}q_{\mathfrak g_3}
q_{\mathfrak g_{31}}}
\quad\text{or}\quad
\frac1{
q_{\mathfrak g_1}q_{\mathfrak g_2}q_{\mathfrak g_3}
q_{\mathfrak g_{23}}}
\]

has weight \(-4\) before including the already analyzed
Cayley--Menger/master factor. Their source-defined plus-plus sum satisfies

\[
\frac1{q_{\mathfrak g_{31}}}
+
\frac1{q_{\mathfrak g_{23}}}
=
\tau^{-1}\frac{n}{r(-r+\tau n)}.
\]

It therefore begins at weight \(-3\), not \(-4\), after the common
\(q_{\mathfrak g_3}^{-1}\) factor is restored.

Using

\[
q_{\mathfrak g_1}q_{\mathfrak g_2}
\longrightarrow 4xy,
\]

the leading coefficient two-form is

\[
\boxed{
-\frac{n}{4xy,r^2},dr\wedge dn.
}
\]

It has no simple logarithmic residue at \(r=0\). More strongly,

\[
-\frac{n}{4xy,r^2},dr\wedge dn
=
d\left(
\frac{n}{4xy,r},dn
\right).
\]

Hence the leading unsplit pair is zero in absolute de Rham cohomology on the
punctured exceptional chart. Its primitive has a pole on the already frozen
wall \(r=0\), so a relative boundary class may remain.

## Verdict

The independent-lift conjecture is falsified:

\[
\boxed{
\text{the canonical physical object is the unsplit occurrence pair, not
two independently boundary-valued occurrence currents.}
}
\]

The chamber-dependent delta terms of entry 231 are artifacts of splitting a
spurious reduced pole before applying the canonical-form relation. They are
not physical coefficient classes by themselves.

The unsplit pair still contains a relative wall datum through the singular
primitive \(n,dn/(4xy,r)\). Thus this result does not assert that the full
physical relative period vanishes. It narrows the next problem from an
arbitrary regulator current to a source-defined connecting morphism at the
existing wall.

## Classification

- existing carrier: \(q_{\mathfrak g_3}=0\), the two occurrence divisors,
  their intersection \(r=0\), and the weighted exceptional chart;
- absolute coefficient class: zero at the leading unsplit grade;
- relative coefficient datum: pole of the primitive on \(r=0\);
- regulator-dependent individual currents: noncanonical splitting data;
- elliptic Gauss--Manin data: no new image;
- genuinely new carrier datum: none.

## Exact evidence

- primary source arXiv:2305.19686v2, equations (4.14)--(4.18), pages 21--23;
- `research/benincasa/check_unsplit_occurrence_pair.rs`;
- `research/benincasa/unsplit-occurrence-pair.json`;
- exact weighted denominator tests and exterior-derivative identity;
- warnings-denied optimized Rust compilation and execution.

## Next finite falsifier

Compute the relative connecting morphism for

\[
d\left(
\frac{n}{4xy,r},dn
\right)
\]

in the frozen marked pair. Evaluate it on the source exceptional chain, with
the two occurrence branches retained until after the connecting map.

- A canonical wall class sewing cyclically supports full assembly inside the
  existing relative coefficient object.
- Zero connecting class means the complete exceptional correction disappears
  in the unsplit physical source despite its nonzero projected image.
- Dependence on a splitting or regulator hierarchy falsifies canonical
  occurrence-level assembly but still does not require a new carrier.

## Outcome contract

~~~json
{
  "claim": "Each lower occurrence has an independent canonical physical boundary lift.",
  "status": "falsified",
  "common_total_normal": "q_g3=tau^2(1+tau*n)",
  "individual_weight": -4,
  "unsplit_pair_weight": -3,
  "leading_two_form": "-n/(4*x*y*r^2) dr wedge dn",
  "absolute_class": "exact",
  "relative_wall_datum": "primitive n/(4*x*y*r) dn",
  "individual_delta_currents": "noncanonical splitting artifacts",
  "new_carrier_incidence": false,
  "next_experiment": "Compute the relative connecting morphism on the source exceptional chain before occurrence forgetting."
}
~~~
