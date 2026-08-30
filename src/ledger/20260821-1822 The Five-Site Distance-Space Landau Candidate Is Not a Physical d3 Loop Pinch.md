# 1822 — The Five-Site Distance-Space Landau Candidate Is Not a Physical d3 Loop Pinch

## Defect found

Entries 1786--1790 solved and certified a Landau system in labelled internal
distance/Cayley--Menger variables, then pulled its real points into physical
three-dimensional loop coordinates. The missing gate was differential:
criticality must survive the constrained map

\[
\ell\longmapsto(y_1(\ell),\ldots,y_5(\ell)).
\]

For the proposed pair

\[
G^-_{e_{12}}=0,
\qquad
g_5=0,
\]

physical Landau criticality requires the two loop gradients to be linearly
dependent.

## Exact physical-gradient audit

At each of the two reflected loop points, compute

\[
\nabla_\ell G^-_{e_{12}}
=2\widehat{(\ell-C_0)},
\]

and

\[
\nabla_\ell g_5
=
\widehat{(\ell-C_3)}+\widehat{(\ell-C_4)}.
\]

Exact rational interval propagation over the same isolated algebraic root
certifies

\[
\boxed{
\left\|
\nabla G^-_{e_{12}}\times\nabla g_5
\right\|^2>0
}

on both reflected sheets. Equivalently, the restriction of \(\nabla g_5\)
to the \(G^-_{e_{12}}\)-level tangent plane has strictly positive squared
norm on both sheets.

Therefore

\[
\boxed{
\text{the distance-space Landau candidate is not a critical point of the
physical }d^3\ell\text{ pullback}.}
}

## Correct classification

The algebraic Cayley--Menger/distance-space candidate remains valid as an
unrestricted coefficient-support calculation. It does not define a physical
three-dimensional loop pinch on the frozen current.

This is precisely the type distinction anticipated by Entry 1216: an object
of the unrestricted distance continuation need not have an ordinary physical
\(d=3\) pullback.

## Required retractions and retypings

The following physical conclusions are withdrawn:

- Entry 1790's nonzero physical Picard--Lefschetz discontinuity;
- Entry 1791's physical \(g_5\) divisor;
- Entry 1792's physical logarithmic extension;
- Entries 1793--1798 insofar as they describe specialization of that physical
  extension;
- Entries 1801--1807's instantiated Kummer/pole-log coefficient objects;
- Entries 1811--1815's instantiation of a transverse Morse/Gysin family;
- Entries 1817--1818's physical activation and rank-110 physical object;
- Entry 1821's application of threshold stationarity at Gram rank two.

The following narrower statements survive:

- the exact source-denominator and Cayley--Menger algebra;
- Entries 1808--1810's source cancellation, nonzero algebraic residues, and
  labelled cyclic census, retyped as distance-space/source data;
- Entry 1800's typing warning;
- Entry 1816's frozen-packet gate;
- Entry 1819's standalone coordinate-Jacobian cancellation theorem;
- Entry 1820's universal conditional Rees normal form.

## Architectural consequence

This is not a failure of the shared-carrier hypothesis. It is a failure to
apply the physical pullback functor before assigning a Betti/Morse coefficient
object:

\[
\boxed{
\text{Landau in ambient distance variables}
\not\Rightarrow
\text{Landau on the physical loop current}.
}

The correction removes the apparent five-site physical threshold evidence
but strengthens the requirement that carrier incidence, coefficient support,
and physical-chain criticality be tested as separate typed stages.

## Next falsifier

Return to the complete source-compatible five-site Landau candidate list and
apply the physical \(d^3\ell\) gradient-dependence gate before any Hessian,
residue, or Picard--Lefschetz calculation. Determine whether any labelled wall
pair survives this stricter pullback.

## Evidence

- research/benincasa/checkers/five_site_g5_physical_gradient_obstruction.py
- research/benincasa/results/five-site-g5-physical-gradient-obstruction.json
- Entries 1216 and 1788--1821
- allocator claim: seqclaim-662f38ce244c61a6543a7df9
