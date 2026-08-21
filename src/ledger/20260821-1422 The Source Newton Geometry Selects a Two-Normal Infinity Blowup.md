# 1422 — The Source Newton Geometry Selects a Two-Normal Infinity Blowup

## Status

Exact source-denominator Rees construction for the two infinity normals of Entry 1421.

## Normals

Set

\[
x=z^{-1},
\qquad
w=R^{-1},
\]

where (z) is the total-energy scale and (R) is the loop-radial scale.

Write the leading edge radii as

\[
y_e=R\,r_e=w^{-1}r_e.
\]

## Cleared source walls

Every connected-region wall has the form

\[
q_A
=
\frac{|A|w+x(r_e+r_f)}{xw},
\]

where (e,f\in\partial A).

The deleted-edge walls are

\[
q_{G\setminus e}
=
\frac{5w+2xr_e}{xw},
\]

and total energy is

\[
q_G
=
\frac{5w}{xw}
=
\frac5x.
\]

Thus every cleared numerator is linear in ((x,w)).

## Forced blowup

The common Newton ideal is

\[
(x,w).
\]

Therefore the source walls select the ordinary blowup

\[
\boxed{
\operatorname{Bl}_{(x,w)},
}
\]

not a fitted weighted blowup.

On the chart

\[
w=x\tau,
\]

the exceptional coordinate is

\[
\tau=\frac zR,
\qquad
\tau^{-1}=\frac Rz.
\]

For example,

\[
q_A
=
x^{-1}\frac{|A|\tau+r_e+r_f}{\tau}.
\]

Every generic marked denominator has order (x^{-1}) along the exceptional divisor.

## Complete packet audit

The checker verifies:

- all (26) frozen walls have Newton order one;
- every one of the (180) OFPT terms has exactly ten denominators;
- every strict-transform wall is a labelled linear section on the exceptional ratio chart.

Hence each source term contributes (x^{10}) after denominator inversion. The physical measure contributes

\[
d^3\ell=x^{-3}d^3k.
\]

Therefore the complete physical form has generic order

\[
\boxed{x^{10-3}=x^7,}
\]

recovering Entry 1310’s (z^{-7}) asymptotic from the two-normal geometry.

## Architectural consequence

The physical total-energy and loop-radial limits are not identical associated grades, but they are boundary charts of one source-derived compactification. Their comparison variable is the exceptional ratio (R/z).

No new carrier incidence is required:

\[
\boxed{
\text{existing energy and loop-radial normals}
+
\operatorname{Bl}_{(x,w)}
+
\text{sector coefficient forms}.
}
\]

## Next finite falsifier

Restrict the full Kummer-resolved coefficient form to the exceptional divisor. Determine its singular sections in (\tau), including deck-sign cancellations, and test whether the physical (z^{-7}) coefficient and the auxiliary Cut-defect class occupy the same exceptional cohomology object or disjoint support sectors.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_two_normal_rees.rs`
- `research/benincasa/results/five-site-two-normal-rees.json`

Allocator claim: `seqclaim-5e77273a72d3b87e6042b4d5`.
