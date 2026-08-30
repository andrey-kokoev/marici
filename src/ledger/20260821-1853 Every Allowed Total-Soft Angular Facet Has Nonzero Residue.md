# 1853 — Every Allowed Total-Soft Angular Facet Has Nonzero Residue

> **Correction (Entry 1854).**  The twelve residues computed here belong to
> the ambient rational lift.  After restriction to
> (g_{123}=g_{125}=0), two labelled facets coincide and cancel.  The claim
> that all twelve are physical poles is withdrawn.

## Exact rational reduction

Entry 1852 bounded the representative angular pole support by twelve frozen
OFPT facets.  The ten source terms were now summed exactly over

\[
\mathbb Q(t,y_1,\ldots,y_5)
\]

using Symbolica.  For each candidate linear facet (L=0), the checker formed

\[
\left.L\,C_{\rm angular}\right|_{L=0}
\]

after exact common-denominator reduction and cancellation.

## Residue census

Every candidate residue is nonzero:

\[
\begin{gathered}
G,\quad G_{-e_{34}},\quad G_{-e_{45}},\\
g_1,g_2,g_3,g_4,g_5,\\
g_{12},g_{1234},g_{1235},g_{1245}.
\end{gathered}
\]

Thus the representative has exactly twelve genuine simple angular poles.
No pole allowed by Entry 1852's support bound cancels in the ten-term OFPT
sum.

## Cyclic consequence

The ordered residue orientation and source expression are cyclically
covariant.  Therefore the five occurrence charts assemble these twelve
representative poles into all twenty-one residual facets of Entry 1852:

\[
\boxed{
\operatorname{Pole}(C_{\rm angular}^{C_5})
=
\mathcal A_{21}^{\rm residual}.
}
\]

The remaining five source facets are precisely the active three-site wall
orbit on which the double residue has already been taken.

## Architectural conclusion

The all-soft angular coefficient uses the complete frozen complement of the
active wall orbit.  Its complexity is arrangement-theoretic but not smaller
than the allowed carrier support:

\[
\boxed{
26
=
21\ \text{genuine coefficient poles}
+
5\ \text{active residue walls}.
}
\]

This strengthens H2.  The coefficient is nontrivial on every available frozen
facet, yet requires no new incidence generator.

## Scope

Nonzero simple residues establish the polar divisor, not the dimension or
extension structure of the logarithmic cohomology class.  Higher intersections
and Orlik--Solomon relations remain to be reduced.

## Next falsifier

Construct the residue vector on the twenty-one-facet projective arrangement
and apply the frozen Orlik--Solomon circuit relations.  Test whether the
ten-term class closes in the existing logarithmic complex or leaves a derived
coefficient extension at higher intersections.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_region_pair_total_soft_angular_residues.rs`
- `research/benincasa/results/five-site-region-pair-total-soft-angular-residues.json`
- Entries 1851--1852
- allocator claim: `seqclaim-3c800d6363142a0e0b5e138a`
